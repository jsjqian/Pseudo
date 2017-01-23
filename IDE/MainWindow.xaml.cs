using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

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
            editor.SelectAll();
            editor.Document.FontFamily = new FontFamily("./Resources/Fonts/#overpass-mono");
            editor.FontSize = 16;
            editor.Width = System.Windows.SystemParameters.PrimaryScreenWidth;
            editor.Height = System.Windows.SystemParameters.PrimaryScreenHeight - 50;
            Paragraph p = editor.Document.Blocks.FirstBlock as Paragraph;
            p.LineHeight = 0.5;
        }

        private void File_Click(object sender, RoutedEventArgs e) { }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
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
                    // Read the stream to a string, and write the string to the console.
                    String line = sr.ReadToEnd();
                    editor.Document.Blocks.Clear();
                    editor.Document.Blocks.Add(new Paragraph(new Run(line)));
                }
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
                string lines = new TextRange(editor.Document.ContentStart, editor.Document.ContentEnd).Text; ;
                // WriteAllLines creates a file, writes a collection of strings to the file,
                // and then closes the file.  You do NOT need to call Flush() or Close().
                System.IO.File.WriteAllText(@saveFileDialog.FileName, lines);
            }
        }

        void editorKeyPress(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Space || e.Key == Key.Back)
            {
                editor.Foreground = Brushes.White;
            }
                IEnumerable<TextRange> wordRanges = CheckKeyword(editor.Document);
                foreach (TextRange wordRange in wordRanges)
                {
                    if (wordRange.Text == "while" || wordRange.Text == "for" || wordRange.Text == "if" || wordRange.Text == "else")
                    {
                        wordRange.ApplyPropertyValue(TextElement.ForegroundProperty, Brushes.Purple);
                    }
                    if (wordRange.Text == "variable")
                    {
                        wordRange.ApplyPropertyValue(TextElement.ForegroundProperty, Brushes.LawnGreen);
                    }
                    if (wordRange.Text == "set")
                    {
                        wordRange.ApplyPropertyValue(TextElement.ForegroundProperty, Brushes.Firebrick);
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



    }
}
