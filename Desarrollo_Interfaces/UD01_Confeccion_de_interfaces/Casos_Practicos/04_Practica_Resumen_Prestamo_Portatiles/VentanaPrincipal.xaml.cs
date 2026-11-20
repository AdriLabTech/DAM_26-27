using System.ComponentModel;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using PrestamosGC.Datos;

namespace PrestamosGC;

/// <summary>
/// Ventana principal: lista de préstamos con filtro y acceso al formulario y al detalle.
/// </summary>
public partial class VentanaPrincipal : Window
{
    public VentanaPrincipal()
    {
        InitializeComponent();
        CargarLista();
    }

    /// <summary>
    /// Rellena la lista con los préstamos del filtro marcado y actualiza la barra de estado.
    /// </summary>
    private void CargarLista()
    {
        // Durante InitializeComponent se marca "Todos" y salta Checked antes de que exista la lista
        if (lstPrestamos == null || txtEstado == null) return;

        List<Prestamo> todos = App.Prestamos.ObtenerPrestamos();
        List<Prestamo> visibles = new List<Prestamo>();

        foreach (Prestamo p in todos)
        {
            bool mostrar = true;
            if (rbActivos.IsChecked == true) mostrar = p.Estado == "En préstamo";
            else if (rbVencidos.IsChecked == true) mostrar = p.EstaVencido;
            else if (rbDevueltos.IsChecked == true) mostrar = p.EstaDevuelto;

            if (mostrar) visibles.Add(p);
        }

        lstPrestamos.ItemsSource = visibles;

        int enPrestamo = todos.Count(p => p.Estado == "En préstamo");
        int vencidos = todos.Count(p => p.EstaVencido);
        int disponibles = App.Prestamos.PortatilesDisponibles().Count;

        string textoVencidos = vencidos == 1 ? "1 vencido" : vencidos + " vencidos";
        txtEstado.Text = enPrestamo + " en préstamo · " + textoVencidos + " · " +
                         disponibles + " portátiles disponibles de " + App.Prestamos.TotalPortatiles;
    }

    private void Filtro_Checked(object sender, RoutedEventArgs e)
    {
        CargarLista();
    }

    private void lstPrestamos_SelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        btnDetalle.IsEnabled = lstPrestamos.SelectedItem != null;
    }

    private void btnNuevo_Click(object sender, RoutedEventArgs e)
    {
        VentanaPrestamo ventana = new VentanaPrestamo();
        ventana.Owner = this;

        if (ventana.ShowDialog() == true)
        {
            rbTodos.IsChecked = true;
            CargarLista();

            // Se selecciona el préstamo nuevo buscándolo por su Id
            Prestamo? nuevo = ventana.PrestamoCreado;
            if (nuevo != null)
            {
                foreach (Prestamo p in lstPrestamos.Items)
                {
                    if (p.Id == nuevo.Id)
                    {
                        lstPrestamos.SelectedItem = p;
                        lstPrestamos.ScrollIntoView(p);
                        break;
                    }
                }
            }
        }
    }

    private void btnDetalle_Click(object sender, RoutedEventArgs e)
    {
        AbrirDetalle();
    }

    private void lstPrestamos_MouseDoubleClick(object sender, MouseButtonEventArgs e)
    {
        AbrirDetalle();
    }

    private void AbrirDetalle()
    {
        if (lstPrestamos.SelectedItem is not Prestamo seleccionado) return;

        VentanaDetalle ventana = new VentanaDetalle(seleccionado);
        ventana.Owner = this;

        if (ventana.ShowDialog() == true)
        {
            CargarLista();
        }
    }

    private void Window_Closing(object? sender, CancelEventArgs e)
    {
        int vencidos = App.Prestamos.ObtenerPrestamos().Count(p => p.EstaVencido);
        if (vencidos == 0) return;

        string texto = vencidos == 1
            ? "Hay 1 préstamo vencido. ¿Quieres salir de todos modos?"
            : "Hay " + vencidos + " préstamos vencidos. ¿Quieres salir de todos modos?";

        MessageBoxResult respuesta = MessageBox.Show(texto, "Salir", MessageBoxButton.YesNo, MessageBoxImage.Question);
        if (respuesta == MessageBoxResult.No)
        {
            e.Cancel = true;
        }
    }
}
