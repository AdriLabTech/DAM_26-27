using System.Windows;
using System.Windows.Controls;

namespace Ficha_de_Usuario;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    // Guardar muestra un resumen de la ficha en el TextBlock «resumen».
    // El botón solo está habilitado si la casilla de condiciones está marcada (ver XAML).
    private void Guardar_Click(object sender, RoutedEventArgs e)
    {
        string ciudadElegida = (ciudad.SelectedItem as ComboBoxItem)?.Content?.ToString() ?? "";
        string fecha = fechaSeleccionada.SelectedDate?.ToString("dd/MM/yyyy") ?? "sin fecha";

        resumen.Text =
            $"Nombre: {nombre.Text}\n" +
            $"Correo: {correo.Text}\n" +
            $"Ciudad: {ciudadElegida}\n" +
            $"Fecha: {fecha}";
    }
}
