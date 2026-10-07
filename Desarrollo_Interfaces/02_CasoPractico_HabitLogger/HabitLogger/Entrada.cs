using System.Globalization;

namespace HabitLogger;

/// <summary>
/// Metodos para pedir datos al usuario. Si el dato no es valido se avisa
/// y se vuelve a pedir hasta que sea correcto
/// </summary>
internal static class Entrada
{
    public const string FormatoFecha = "dd/MM/yyyy";

    public static string PedirTexto(string mensaje)
    {
        Console.Write(mensaje);
        string? texto = Console.ReadLine();

        // ReadLine devuelve null si se cierra la entrada (ej. Ctrl+Z): se avisa en vez de seguir sin datos
        if (texto == null)
        {
            throw new EndOfStreamException("La entrada de la consola se ha cerrado.");
        }
        return texto.Trim();
    }

    /// <summary>
    /// Pide un numero entero entre min y max (ambos incluidos)
    /// </summary>
    public static int PedirNumero(string mensaje, int min, int max)
    {
        // Patron de bucle: cada comprobacion o bien devuelve el valor (si es correcto) o bien
        // rellena "error". Si se llega al final del bucle se muestra el error y se vuelve a preguntar
        while (true)
        {
            string texto = PedirTexto(mensaje);
            string error;

            // TryParse intenta convertir el texto a numero sin lanzar excepcion: devuelve false si no puede
            if (!int.TryParse(texto, out int numero))
            {
                error = "Debes escribir un numero entero.";
            }
            else if (numero < min || numero > max)
            {
                error = "El numero debe estar entre " + min + " y " + max + ".";
            }
            else
            {
                return numero;
            }

            Console.WriteLine(error);
            LogOperaciones.Escribir("Entrada no valida '" + texto + "': " + error);
        }
    }

    /// <summary>
    /// Pide una fecha en formato dd/MM/yyyy. Si el usuario escribe "hoy" se usa la fecha de hoy
    /// </summary>
    public static DateTime PedirFecha(string mensaje)
    {
        while (true)
        {
            string texto = PedirTexto(mensaje);
            string error;

            if (texto.ToLower() == "hoy")
            {
                return DateTime.Today;
            }
            // TryParseExact solo acepta el formato exacto dd/MM/yyyy. InvariantCulture hace que
            // funcione igual en cualquier PC, sea cual sea su configuracion regional
            else if (!DateTime.TryParseExact(texto, FormatoFecha, CultureInfo.InvariantCulture, DateTimeStyles.None, out DateTime fecha))
            {
                error = "Fecha no valida. Usa el formato " + FormatoFecha + " o escribe 'hoy'.";
            }
            else if (fecha > DateTime.Today)
            {
                error = "La fecha no puede ser futura.";
            }
            else
            {
                return fecha;
            }

            Console.WriteLine(error);
            LogOperaciones.Escribir("Entrada no valida '" + texto + "': " + error);
        }
    }
}
