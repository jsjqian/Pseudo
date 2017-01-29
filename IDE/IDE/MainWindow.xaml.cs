using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Windows;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System.Windows.Controls;

namespace IDE
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
           
            InitializeComponent();
            initialize();
            
        }

        public void initialize()
        {
            editor.FontFamily = new FontFamily("Consolas"); // the Media namespace
            editor.SelectAll();
            editor.FontSize = 16;
            editor.Width = System.Windows.SystemParameters.PrimaryScreenWidth / 2;
            editor.Height = System.Windows.SystemParameters.PrimaryScreenHeight - 50;
            Paragraph p = editor.Document.Blocks.FirstBlock as Paragraph;
            p.LineHeight = 0.5;
            python.FontSize = 16;
            python.FontFamily = new FontFamily("Consolas"); // the Media namespace
            python.Width = System.Windows.SystemParameters.PrimaryScreenWidth / 2;
            python.Height = System.Windows.SystemParameters.PrimaryScreenHeight - 50;
            Paragraph par = python.Document.Blocks.FirstBlock as Paragraph;
            par.LineHeight = 0.5;
            python.FontSize = 16;
        }

        private void File_Click(object sender, RoutedEventArgs e) { }

        private void Run_Click(object sender, RoutedEventArgs e) { }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            string sMessageBoxText = "Are You Sure You Want To Exit";
            string sCaption = "Exit?";

            MessageBoxButton btnMessageBox = MessageBoxButton.YesNo;
            MessageBoxImage icnMessageBox = MessageBoxImage.Question;

            MessageBoxResult rsltMessageBox = MessageBox.Show(sMessageBoxText, sCaption, btnMessageBox, icnMessageBox);

            switch (rsltMessageBox)
            {
                case MessageBoxResult.Yes:
                    this.Close();
                    break;
                case MessageBoxResult.No:
                    break;
            }
        }

        private void Open_Click(object sender, RoutedEventArgs e)
        {
            Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
            dlg.FileName = "Document"; // Default file name
            dlg.DefaultExt = ".psu"; // Default file extension
            dlg.Filter = "Pseudo Files (.psu)|*.psu"; // Filter files by extension
            dlg.Title = "Open File";
            // Show open file dialog box
            Nullable<bool> result = dlg.ShowDialog();

            // Process open file dialog box results
            if (result == true)
            {

                using (System.IO.StreamReader sr = new System.IO.StreamReader(dlg.FileName))
                {
                    Add_Tab(sender, e, dlg.SafeFileName);
                    // Read the stream to a string, and write the string to the console.
                    String line = sr.ReadToEnd();
                    editor.Document.Blocks.Clear();
                    editor.Document.Blocks.Add(new Paragraph(new Run(line)));
                }
                initialize();
                CheckKeyword(editor.Document);
            }

        }

        private void Save_Click(object sender, System.EventArgs e)
        {
            Microsoft.Win32.SaveFileDialog saveFileDialog = new Microsoft.Win32.SaveFileDialog();
            saveFileDialog.Filter = "Pseudo Files (.psu)|*.psu";
            saveFileDialog.Title = "Save a Pseudo File";
            saveFileDialog.ShowDialog();
            saveFileDialog.RestoreDirectory = true;
            saveFileDialog.DefaultExt = "psu";

            // If the file name is not an empty string open it for saving.
            if (saveFileDialog.FileName != "")
            {
                string lines = new TextRange(editor.Document.ContentStart, editor.Document.ContentEnd).Text;
                // WriteAllLines creates a file, writes a collection of strings to the file,
                // and then closes the file.  You do NOT need to call Flush() or Close().
                System.IO.File.WriteAllText(@saveFileDialog.FileName, lines);
            }
        }

        void editorKeyPress(object sender, KeyEventArgs e)
        {

            editor.Foreground = new SolidColorBrush(Colors.White);
            
            IEnumerable<TextRange> wordRanges = CheckKeyword(editor.Document);
            foreach (TextRange wordRange in wordRanges)
            {
                if (wordRange.Text == "while" || wordRange.Text == "for" || wordRange.Text == "if" || wordRange.Text == "else")
                {
                    wordRange.ApplyPropertyValue(TextElement.ForegroundProperty, Brushes.Purple);
                }
                else if (wordRange.Text == "variable")
                {
                    wordRange.ApplyPropertyValue(TextElement.ForegroundProperty, Brushes.LawnGreen);
                }
                else if (wordRange.Text == "set")
                {
                    wordRange.ApplyPropertyValue(TextElement.ForegroundProperty, Brushes.Firebrick);
                }
                else
                {
                    wordRange.ApplyPropertyValue(TextElement.ForegroundProperty, Brushes.White);
                }
                wordRange.ApplyPropertyValue(TextElement.FontWeightProperty, FontWeights.Bold);
            }

        }
        
        public static IEnumerable<TextRange> CheckKeyword(FlowDocument document)
        {
                string pattern = @"(while|for|if|else|variable|set)";
                TextPointer pointer = document.ContentStart;
                while (pointer != null)
                {
                    if (pointer.GetPointerContext(LogicalDirection.Forward) == TextPointerContext.Text)
                    {
                        string textRun = pointer.GetTextInRun(LogicalDirection.Forward);
                        System.Text.RegularExpressions.MatchCollection matches = System.Text.RegularExpressions.Regex.Matches(textRun, pattern);
                        foreach (System.Text.RegularExpressions.Match match in matches)
                        {
                            int startIndex = match.Index;
                            int length = match.Length;
                            TextPointer start = pointer.GetPositionAtOffset(startIndex);
                            TextPointer end = start.GetPositionAtOffset(length);
                            yield return new TextRange(start, end);
                        }
                    }

                    pointer = pointer.GetNextContextPosition(LogicalDirection.Forward);
                }
        }

        private void Code_Click_Editor(object sender, RoutedEventArgs e)
        {

        }

        private void Code_Click_File(object sender, RoutedEventArgs e)
        {
            string lines = new TextRange(editor.Document.ContentStart, editor.Document.ContentEnd).Text;
            Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
            dlg.FileName = "Document"; // Default file name
            dlg.DefaultExt = ".psu"; // Default file extension
            dlg.Filter = "Pseudo Files (.psu)|*.psu"; // Filter files by extension
            dlg.Title = "Open File";
            // Show open file dialog box
            Nullable<bool> result = dlg.ShowDialog();

            // Process open file dialog box results
            if (result == true)
            {

                using (System.IO.StreamReader sr = new System.IO.StreamReader(dlg.FileName))
                {
                    // Read the stream to a string, and write the string to the console.
                    String line = sr.ReadToEnd();
                    editor.Document.Blocks.Clear();
                    editor.Document.Blocks.Add(new Paragraph(new Run(line)));
                    run_python(@dlg.FileName);
                }
                initialize();

            }

        }

        private void run_python(string param)
        {
            char[] delimiterChars = {'\\'};
            string[] tokens = param.Split(delimiterChars);
            string path = "\"" + param + "\"";
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = "C:\\Python27\\python.exe";
            start.Arguments = string.Format("{0} {1}", "pseudo.py", path);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    python.Document.Blocks.Clear();
                    python.Document.Blocks.Add(new Paragraph(new Run(result)));
                }
            }
        }

        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {

        }

        void Add_Tab(object sender, EventArgs e, string title)
        {
            int idx = Tabs.Items.Count;
            Tabs.SelectedIndex = idx - 1;
            TabItem ti = new TabItem();
            ti.Header = title;
            Tabs.Items.Insert(Tabs.Items.Count, ti);
            ti.IsSelected = true;
        }

    }
}
