using System.Net.Mail;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using FichaUsuario_BBDD.Data;
using FichaUsuario_BBDD.Models;
using Microsoft.Data.Sqlite;

namespace FichaUsuario_BBDD;

public partial class MainWindow : Window
{
    private readonly UsuarioRepositorio? _repositorio;
    private bool _baseDatosLista;

    public MainWindow()
    {
        InitializeComponent();

        try
        {
            _repositorio = new UsuarioRepositorio(UsuarioRepositorio.RutaPorDefecto());
            CargarCiudades();
            _baseDatosLista = true;
        }
        catch (Exception ex)
        {
            MostrarError($"No se pudo abrir la base de datos: {ex.Message}");
            btnGuardar.IsEnabled = false;
        }
    }

    private void CargarCiudades()
    {
        var ciudades = _repositorio!.ObtenerCiudades();
        cbCuidad.ItemsSource = ciudades;
        cbCuidad.DisplayMemberPath = nameof(Ciudad.Nombre);
        cbCuidad.SelectedIndex = ciudades.Count > 0 ? 0 : -1;
    }

    private void CambioAceptacion(object sender, RoutedEventArgs e)
    {
        if (btnGuardar is not null)
            btnGuardar.IsEnabled = _baseDatosLista && cbAceptarCondiciones.IsChecked == true;
    }

    public void VerificarDatos(object sender, RoutedEventArgs e)
    {
        var nombre = tbNombre.Text.Trim();
        var correo = tbCorreo.Text.Trim();

        if (string.IsNullOrWhiteSpace(nombre))
        {
            MostrarError("Escribe el nombre del usuario.");
            tbNombre.Focus();
            return;
        }

        if (!EsCorreoValido(correo))
        {
            MostrarError("El correo no tiene un formato válido (ejemplo: nombre@dominio.com)");
            tbCorreo.Focus();
            return;
        }

        if (cbCuidad.SelectedItem is not Ciudad ciudad)
        {
            MostrarError("Selecciona una ciudad.");
            cbCuidad.Focus();
            return;
        }

        if (dpFecha.SelectedDate is not DateTime fecha)
        {
            MostrarError("Selecciona una fecha.");
            dpFecha.Focus();
            return;
        }

        if (cbAceptarCondiciones.IsChecked != true)
        {
            MostrarError("Debes aceptar las condiciones para continuar.");
            cbAceptarCondiciones.Focus();
            return;
        }

        if (_repositorio is null || !_baseDatosLista)
        {
            MostrarError("La base de datos no está disponible.");
            return;
        }

        try
        {
            if (_repositorio.ExisteCorreo(correo))
            {
                MostrarError($"Ya existe un usuario con el correo {correo}.");
                tbCorreo.Focus();
                return;
            }

            _repositorio.Insertar(nombre, correo, ciudad.Id, DateOnly.FromDateTime(fecha));
        }
        catch (SqliteException ex) when (ex.SqliteErrorCode == 19)
        {
            MostrarError($"Ya existe un usuario con el correo {correo}.");
            tbCorreo.Focus();
            return;
        }
        catch (Exception ex)
        {
            MostrarError($"No se pudo guardar el usuario: {ex.Message}");
            return;
        }

        MostrarMensaje(
            $"Usuario'{nombre}' guardado correctamente ({correo}, {ciudad.Nombre}, {fecha:dd/MM/yyyy}).",
            esError: false);

        LimpiarFormulario();
    }

    private void LimpiarFormulario()
    {
        tbNombre.Clear();
        tbCorreo.Clear();
        cbCuidad.SelectedIndex = 0;
        dpFecha.SelectedDate = DateTime.Today;
        cbAceptarCondiciones.IsChecked = false;
        tbNombre.Focus();
    }

    private static bool EsCorreoValido(string correo)
    {
        if (string.IsNullOrWhiteSpace(correo))
            return false;

        if (!MailAddress.TryCreate(correo, out var direccion))
            return false;

        // Evita formatos como "Nombre <correo@dominio.com>" y exige un dominio real.
        return string.Equals(direccion.Address, correo, StringComparison.OrdinalIgnoreCase)
            && direccion.Host.Contains('.')
            && !direccion.Host.StartsWith('.')
            && !direccion.Host.EndsWith('.');
    }

    private void MostrarError(string mensaje) => MostrarMensaje(mensaje, esError: true);

    private void MostrarMensaje(string mensaje, bool esError)
    {
        tbResumen.Text = mensaje;
        tbResumen.Foreground = esError ? Brushes.Firebrick : Brushes.Green;
    }
}
