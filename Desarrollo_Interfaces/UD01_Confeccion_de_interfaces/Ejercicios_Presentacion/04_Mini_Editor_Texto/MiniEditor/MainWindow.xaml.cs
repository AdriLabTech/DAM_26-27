using System.Windows;

namespace MiniEditor;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    private void Nuevo_Click(object sender, RoutedEventArgs e)
    {
        editor.Clear();
        editor.Focus();
    }

    private void Salir_Click(object sender, RoutedEventArgs e)
    {
        Close();
    }
}
