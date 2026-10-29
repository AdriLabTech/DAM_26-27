namespace HabitLoggerTui;

/// <summary>
/// Guarda las operaciones del usuario en un fichero .log. Se crea un fichero por dia
/// dentro de la carpeta "logs" (ej. logs/06_10_2026.log).
/// Es static para poder usarla desde cualquier clase sin crear un objeto
/// </summary>
internal static class LogOperaciones
{
    private static readonly string CarpetaLogs = Path.Combine(AppContext.BaseDirectory, "logs");

    public static void Escribir(string mensaje)
    {
        try
        {
            // Si la carpeta ya existe no hace nada, asi que se puede llamar siempre
            Directory.CreateDirectory(CarpetaLogs);

            // El nombre del fichero es la fecha de hoy: cada dia empieza un fichero nuevo.
            // AppendAllText crea el fichero si no existe y, si existe, anade la linea al final
            string nombreFichero = DateTime.Now.ToString("dd_MM_yyyy") + ".log";
            string linea = DateTime.Now.ToString("HH:mm:ss") + " - " + mensaje + Environment.NewLine;
            File.AppendAllText(Path.Combine(CarpetaLogs, nombreFichero), linea);
        }
        catch (Exception)
        {
            // Si el log falla no pasa nada: no podemos escribir en consola porque estropearia la pantalla de la TUI
        }
    }
}
