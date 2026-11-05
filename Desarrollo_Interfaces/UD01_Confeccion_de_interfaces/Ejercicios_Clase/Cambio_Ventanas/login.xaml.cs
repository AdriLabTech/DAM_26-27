using System.Windows;

namespace CambioVentana;

public partial class login : Window
{
    public login()
    {
        InitializeComponent();
    }

    public void Enviar_Form(object sender, RoutedEventArgs e)
    {
        string usuario = txtUsuario.Text.Trim();

        if (usuario.Length == 0)
        {
            MessageBox.Show("Escribe tu usuario", "Aviso", MessageBoxButton.OK, MessageBoxImage.Error);
            txtUsuario.Focus();
            return;
        }

        var principal = new MainWindow(usuario);
        // Al cerrar la ventana principal termina la aplicación (el login queda oculto).
        principal.Closed += (_, _) => Application.Current.Shutdown();
        Application.Current.MainWindow = principal;
        principal.Show();

        // En LibreWPF (Linux), cerrar la primera ventana nativa arrastra a las demás: se oculta en vez de cerrarse.
        Hide();
    }
}
