using System.Windows;

namespace CambioVentana;

public partial class MainWindow : Window
{
    public MainWindow(string usuario)
    {
        InitializeComponent();
        lbusuario.Content = "Bienvenido, " + usuario;
    }
}
