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
            editor.FontFamily = new FontFamily("./Resources/Fonts/#overpass-mono");
            editor.FontSize = 16;
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
                    editor.AppendText(line);
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

    }
}
