using System.Text;

namespace AgendaAmpliada;

// Exportación a CSV (separador «;» para que Excel en español lo abra por columnas)
public static class ContactoCsv
{
    public const char Separador = ';';

    public static string Generar(IEnumerable<Contacto> contactos)
    {
        var sb = new StringBuilder();
        sb.AppendLine(string.Join(Separador, "Nombre", "Email", "Telefono", "Ciudad"));

        foreach (var c in contactos)
            sb.AppendLine(string.Join(Separador, Escapar(c.Nombre), Escapar(c.Email), Escapar(c.Telefono), Escapar(c.Ciudad)));

        return sb.ToString();
    }

    // Si el valor contiene separador, comillas o saltos de línea se entrecomilla y se duplican las comillas
    public static string Escapar(string valor)
    {
        if (valor.IndexOfAny([Separador, '"', '\n', '\r']) < 0) return valor;
        return "\"" + valor.Replace("\"", "\"\"") + "\"";
    }
}
