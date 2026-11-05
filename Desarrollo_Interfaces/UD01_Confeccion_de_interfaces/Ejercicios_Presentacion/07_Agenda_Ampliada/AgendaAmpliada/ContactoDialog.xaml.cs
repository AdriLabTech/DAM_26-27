using System.Windows;

namespace AgendaAmpliada;

// Diálogo modal de edición. El DataContext es el propio Contacto (ObservableValidator).
public partial class ContactoDialog : Window
{
    public ContactoDialog() => InitializeComponent();

    // Detalle visual: solo se cierra con éxito si todas las reglas se cumplen
    private void Aceptar_Click(object sender, RoutedEventArgs e)
    {
        if (DataContext is Contacto contacto && contacto.Validar())
            DialogResult = true;
    }
}
