using System.Windows;
using System.Windows.Controls;

namespace Pedido;

public partial class MainWindow : Window
{
    // Por debajo de este ancho (en píxeles) el resumen pasa debajo de los datos
    private const double AnchoMinimoDosColumnas = 520;

    public MainWindow()
    {
        InitializeComponent();
    }

    private void Ventana_SizeChanged(object sender, SizeChangedEventArgs e)
    {
        Reorganizar();
    }

    // Cambia la disposición según el ancho de la ventana
    private void Reorganizar()
    {
        bool estrecho = ActualWidth < AnchoMinimoDosColumnas;

        Grid.SetColumn(grpResumen, estrecho ? 0 : 1);
        Grid.SetRow(grpResumen, estrecho ? 1 : 0);

        // En modo estrecho el Resumen ocupa todo el ancho: se ajustan los márgenes
        grpDatos.Margin = estrecho ? new Thickness(0, 0, 0, 8) : new Thickness(0, 0, 8, 8);
        grpResumen.Margin = estrecho ? new Thickness(0, 0, 0, 8) : new Thickness(8, 0, 0, 8);
        Grid.SetColumnSpan(grpDatos, estrecho ? 2 : 1);
        Grid.SetColumnSpan(grpResumen, estrecho ? 2 : 1);
    }
}
