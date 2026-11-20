using System.Net.Mail;
using System.Windows;
using System.Windows.Controls;
using PrestamosGC.Datos;

namespace PrestamosGC;

/// <summary>
/// Formulario para registrar un préstamo nuevo. Si se guarda, deja el préstamo en PrestamoCreado.
/// </summary>
public partial class VentanaPrestamo : Window
{
    private const string DominioCentro = "@g.educaand.es";

    // Los manejadores de eventos saltan ya durante InitializeComponent (por ejemplo, al marcar
    // el CheckBox inicial); este indicador evita tocar controles que todavía no existen.
    private readonly bool inicializado;

    /// <summary>Préstamo guardado, o null si se ha cancelado.</summary>
    public Prestamo? PrestamoCreado { get; private set; }

    public VentanaPrestamo()
    {
        InitializeComponent();

        // Portátiles libres y fecha de préstamo (hoy, sin poder elegir días anteriores)
        cmbPortatil.ItemsSource = App.Prestamos.PortatilesDisponibles();
        dpPrestamo.DisplayDateStart = DateTime.Today;
        dpPrestamo.SelectedDate = DateTime.Today;

        inicializado = true;
        LimitarFechaDevolucion();
    }

    private void Window_Loaded(object sender, RoutedEventArgs e)
    {
        txtNombre.Focus();
    }

    // ---------------------------------------------------------------- Eventos de los controles

    private void dpPrestamo_SelectedDateChanged(object? sender, SelectionChangedEventArgs e)
    {
        if (!inicializado) return;
        LimitarFechaDevolucion();
        txtErrorPrestamo.Visibility = Visibility.Collapsed;
    }

    /// <summary>La devolución solo puede ser entre el día siguiente y 14 días después del préstamo.</summary>
    private void LimitarFechaDevolucion()
    {
        DateTime? prestamo = dpPrestamo.SelectedDate;
        if (prestamo == null)
        {
            dpDevolucion.DisplayDateStart = null;
            dpDevolucion.DisplayDateEnd = null;
            return;
        }

        DateTime minima = prestamo.Value.AddDays(1);
        DateTime maxima = prestamo.Value.AddDays(14);
        dpDevolucion.DisplayDateStart = minima;
        dpDevolucion.DisplayDateEnd = maxima;

        DateTime? elegida = dpDevolucion.SelectedDate;
        if (elegida != null && (elegida.Value.Date < minima.Date || elegida.Value.Date > maxima.Date))
        {
            dpDevolucion.SelectedDate = null;
        }
    }

    private void dpDevolucion_SelectedDateChanged(object? sender, SelectionChangedEventArgs e)
    {
        if (!inicializado) return;
        txtErrorDevolucion.Visibility = Visibility.Collapsed;
    }

    private void txtObservaciones_TextChanged(object sender, TextChangedEventArgs e)
    {
        if (!inicializado) return;
        txtContador.Text = txtObservaciones.Text.Length + "/200";
        txtErrorObservaciones.Visibility = Visibility.Collapsed;
    }

    private void Motivo_Checked(object sender, RoutedEventArgs e)
    {
        if (!inicializado) return;
        lblObservaciones.Text = rbOtro.IsChecked == true ? "Observaciones (obligatorias)" : "Observaciones";
        txtErrorMotivo.Visibility = Visibility.Collapsed;
        txtErrorObservaciones.Visibility = Visibility.Collapsed;
    }

    // Un único manejador por tipo de control para que el error desaparezca al corregir el campo

    private void Texto_Changed(object sender, TextChangedEventArgs e)
    {
        if (!inicializado) return;
        if (sender == txtNombre) txtErrorNombre.Visibility = Visibility.Collapsed;
        else if (sender == txtApellidos) txtErrorApellidos.Visibility = Visibility.Collapsed;
        else if (sender == txtCorreo) txtErrorCorreo.Visibility = Visibility.Collapsed;
    }

    private void Combo_SelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        if (!inicializado) return;
        if (sender == cmbGrupo) txtErrorGrupo.Visibility = Visibility.Collapsed;
        else if (sender == cmbPortatil) txtErrorPortatil.Visibility = Visibility.Collapsed;
    }

    private void Normas_Changed(object sender, RoutedEventArgs e)
    {
        if (!inicializado) return;
        txtErrorNormas.Visibility = Visibility.Collapsed;
    }

    // ---------------------------------------------------------------- Validación y guardado

    private void Registrar_Click(object sender, RoutedEventArgs e)
    {
        txtErrorGeneral.Visibility = Visibility.Collapsed;
        Control? primero = null; // primer campo incorrecto, para llevarle el foco

        // Nombre y apellidos
        if (string.IsNullOrWhiteSpace(txtNombre.Text))
            MostrarError(txtErrorNombre, "Campo obligatorio.", txtNombre, ref primero);
        if (string.IsNullOrWhiteSpace(txtApellidos.Text))
            MostrarError(txtErrorApellidos, "Campo obligatorio.", txtApellidos, ref primero);

        // Grupo: sus opciones son ComboBoxItem escritos en el XAML, así que se lee su Content
        string grupo = "";
        if (cmbGrupo.SelectedItem is ComboBoxItem itemGrupo)
            grupo = itemGrupo.Content?.ToString() ?? "";
        if (grupo == "")
            MostrarError(txtErrorGrupo, "Elige un grupo.", cmbGrupo, ref primero);

        // Correo del centro
        string correo = txtCorreo.Text.Trim();
        if (!CorreoValido(correo))
            MostrarError(txtErrorCorreo, "Usa el correo del centro (" + DominioCentro + ").", txtCorreo, ref primero);

        // Portátil: este ComboBox se rellenó con cadenas, así que SelectedItem ya es un string
        string portatil = cmbPortatil.SelectedItem as string ?? "";
        if (portatil == "")
            MostrarError(txtErrorPortatil, "Elige un portátil.", cmbPortatil, ref primero);

        // Motivo
        string motivo = "";
        if (rbProyecto.IsChecked == true) motivo = "Proyecto";
        else if (rbPracticas.IsChecked == true) motivo = "Prácticas";
        else if (rbOtro.IsChecked == true) motivo = "Otro";
        if (motivo == "")
            MostrarError(txtErrorMotivo, "Elige un motivo.", rbProyecto, ref primero);

        // Fechas
        DateTime? fechaPrestamo = dpPrestamo.SelectedDate;
        if (fechaPrestamo == null || fechaPrestamo.Value.Date < DateTime.Today)
            MostrarError(txtErrorPrestamo, "La fecha no puede ser anterior a hoy.", dpPrestamo, ref primero);

        DateTime? fechaDevolucion = dpDevolucion.SelectedDate;
        bool devolucionValida = fechaDevolucion != null;
        if (devolucionValida && fechaPrestamo != null)
        {
            int dias = (fechaDevolucion!.Value.Date - fechaPrestamo.Value.Date).Days;
            devolucionValida = dias >= 1 && dias <= 14;
        }
        if (!devolucionValida)
            MostrarError(txtErrorDevolucion, "El préstamo dura entre 1 y 14 días.", dpDevolucion, ref primero);

        // Observaciones: obligatorias si el motivo es «Otro»
        string observaciones = txtObservaciones.Text.Trim();
        if (motivo == "Otro" && observaciones == "")
            MostrarError(txtErrorObservaciones, "Explica el motivo del préstamo.", txtObservaciones, ref primero);

        // Normas de uso
        if (chkNormas.IsChecked != true)
            MostrarError(txtErrorNormas, "El alumno debe aceptar las normas.", chkNormas, ref primero);

        if (primero != null)
        {
            primero.Focus();
            return;
        }

        Prestamo nuevo = new Prestamo
        {
            Nombre = txtNombre.Text.Trim(),
            Apellidos = txtApellidos.Text.Trim(),
            Grupo = grupo,
            Correo = correo,
            Portatil = portatil,
            Motivo = motivo,
            IncluyeCargador = chkCargador.IsChecked == true,
            Observaciones = observaciones,
            FechaPrestamo = fechaPrestamo!.Value.Date,
            FechaDevolucionPrevista = fechaDevolucion!.Value.Date
        };

        try
        {
            App.Prestamos.InsertarPrestamo(nuevo);
        }
        catch (InvalidOperationException ex)
        {
            // Portátil ya prestado o alumno con otro portátil sin devolver
            txtErrorGeneral.Text = ex.Message;
            txtErrorGeneral.Visibility = Visibility.Visible;
            return;
        }

        PrestamoCreado = nuevo;
        DialogResult = true;
    }

    private static void MostrarError(TextBlock mensaje, string texto, Control campo, ref Control? primero)
    {
        mensaje.Text = texto;
        mensaje.Visibility = Visibility.Visible;
        if (primero == null) primero = campo;
    }

    private static bool CorreoValido(string correo)
    {
        if (!MailAddress.TryCreate(correo, out MailAddress? direccion)) return false;
        // TryCreate acepta cosas como «Nombre <a@b.c>»: se exige que la dirección sea justo lo escrito
        return direccion.Address.Equals(correo, StringComparison.OrdinalIgnoreCase)
            && correo.EndsWith(DominioCentro, StringComparison.OrdinalIgnoreCase)
            && correo.Length > DominioCentro.Length;
    }
}
