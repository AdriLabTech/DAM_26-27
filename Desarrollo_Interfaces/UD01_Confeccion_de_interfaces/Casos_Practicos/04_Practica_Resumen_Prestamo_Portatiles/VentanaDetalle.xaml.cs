using System.Windows;
using PrestamosGC.Datos;

namespace PrestamosGC;

/// <summary>
/// Detalle de un préstamo. Todos los datos salen de Binding (el préstamo es el DataContext).
/// </summary>
public partial class VentanaDetalle : Window
{
    private readonly Prestamo prestamo;

    public VentanaDetalle(Prestamo prestamo)
    {
        InitializeComponent();
        this.prestamo = prestamo;
        DataContext = prestamo;
    }

    private void Devolucion_Click(object sender, RoutedEventArgs e)
    {
        MessageBoxResult respuesta = MessageBox.Show(
            "¿Registrar la devolución del portátil " + prestamo.Portatil + "?",
            "Confirmar devolución", MessageBoxButton.YesNo, MessageBoxImage.Question);

        if (respuesta != MessageBoxResult.Yes) return;

        try
        {
            App.Prestamos.RegistrarDevolucion(prestamo.Id);
        }
        catch (InvalidOperationException ex)
        {
            MessageBox.Show(ex.Message, "No se pudo registrar la devolución",
                MessageBoxButton.OK, MessageBoxImage.Warning);
            return;
        }

        DialogResult = true;
    }
}
