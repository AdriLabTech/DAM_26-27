using System.Globalization;

namespace HabitLoggerTui;

/// <summary>
/// Una ocurrencia del habito: el dia en que sucedio y la cantidad
/// </summary>
internal class Habito
{
    public int Id { get; set; }
    public DateTime Fecha { get; set; }
    public int Cantidad { get; set; }

    // La fecha tal como la ve y la escribe el usuario (dd/MM/yyyy)
    public string FechaTexto
    {
        get { return Fecha.ToString(Validacion.FormatoFecha, CultureInfo.InvariantCulture); }
    }

    // Texto que se muestra al concatenar el objeto con un string: lo usa la pantalla de confirmacion
    public override string ToString()
    {
        return "Id=" + Id + " Fecha=" + FechaTexto + " Cantidad=" + Cantidad;
    }
}
