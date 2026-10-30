using System.Windows;

namespace Ficha_de_Usuario;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    private void BotonSaludar_Click(
        object sender,
        RoutedEventArgs e)
    {
        MessageBox.Show("¡LibreWPF funciona en Ryoku!");
    }
}