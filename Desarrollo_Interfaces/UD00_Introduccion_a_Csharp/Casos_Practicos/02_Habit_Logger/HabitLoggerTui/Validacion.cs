using System.Globalization;

namespace HabitLoggerTui;

/// <summary>
/// Comprueba lo que escribe el usuario. Si el valor no es valido devuelve false
/// y en "error" deja el motivo para mostrarlo en pantalla.
/// Los parametros "out" son valores que el metodo devuelve ademas del bool: el resultado
/// ya convertido (fecha, cantidad) y el mensaje de error. Hay que asignarlos en todos los caminos
/// </summary>
internal static class Validacion
{
    public const string FormatoFecha = "dd/MM/yyyy";

    /// <summary>
    /// Comprueba una fecha en formato dd/MM/yyyy. Si el usuario escribe "hoy" se usa la fecha de hoy
    /// </summary>
    public static bool EsFechaValida(string texto, out DateTime fecha, out string error)
    {
        error = "";
        fecha = DateTime.Today;

        // Atajo: "hoy" ya deja la fecha de hoy en "fecha" (se asigno arriba)
        if (texto.ToLower() == "hoy")
        {
            return true;
        }

        // TryParseExact solo acepta el formato exacto dd/MM/yyyy. InvariantCulture hace que
        // funcione igual en cualquier PC, sea cual sea su configuracion regional
        if (!DateTime.TryParseExact(texto, FormatoFecha, CultureInfo.InvariantCulture, DateTimeStyles.None, out fecha))
        {
            error = "Fecha no valida. Usa el formato " + FormatoFecha + " o escribe 'hoy'.";
            return false;
        }

        if (fecha > DateTime.Today)
        {
            error = "La fecha no puede ser futura.";
            return false;
        }

        return true;
    }

    /// <summary>
    /// Comprueba que la cantidad es un numero entero mayor o igual que 1
    /// </summary>
    public static bool EsCantidadValida(string texto, out int cantidad, out string error)
    {
        error = "";

        // TryParse intenta convertir el texto a numero sin lanzar excepcion: devuelve false si no puede
        if (!int.TryParse(texto, out cantidad))
        {
            error = "Debes escribir un numero entero.";
            return false;
        }

        if (cantidad < 1)
        {
            error = "El numero debe ser mayor o igual que 1.";
            return false;
        }

        return true;
    }
}
