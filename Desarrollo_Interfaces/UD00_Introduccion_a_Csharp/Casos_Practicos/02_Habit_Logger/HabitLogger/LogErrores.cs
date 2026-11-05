using Microsoft.Data.Sqlite;

namespace HabitLogger;

/// <summary>
/// Guarda los errores del sistema en la tabla "Errores" de la base de datos
/// </summary>
internal class LogErrores
{
    private readonly DataBaseConnector.DataBaseConnector _conector;

    public LogErrores(DataBaseConnector.DataBaseConnector conector)
    {
        _conector = conector;
    }

    public void CrearTabla()
    {
        using SqliteCommand comando = _conector.CrearComando(
            "CREATE TABLE IF NOT EXISTS Errores (" +
            "Id INTEGER PRIMARY KEY AUTOINCREMENT, " +
            "FechaHora TEXT NOT NULL, " +
            "Origen TEXT NOT NULL, " +
            "Mensaje TEXT NOT NULL)");
        comando.ExecuteNonQuery();
    }

    /// <summary>
    /// Guarda un error. "origen" indica donde ha ocurrido (ej. la opcion del menu)
    /// </summary>
    public void Guardar(string origen, Exception error)
    {
        // Este metodo se llama desde un catch, asi que NO puede lanzar otro error: si lo hiciera,
        // el programa se caeria justo al intentar gestionar un fallo. Por eso va en su propio try/catch
        try
        {
            using SqliteCommand comando = _conector.CrearComando(
                "INSERT INTO Errores (FechaHora, Origen, Mensaje) VALUES ($fechaHora, $origen, $mensaje)");
            comando.Parameters.AddWithValue("$fechaHora", DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
            comando.Parameters.AddWithValue("$origen", origen);
            comando.Parameters.AddWithValue("$mensaje", error.Message);
            comando.ExecuteNonQuery();
        }
        catch (Exception errorBD)
        {
            // Si la BD tampoco funciona, dejamos el error en el .log para no perderlo
            LogOperaciones.Escribir("ERROR (no se pudo guardar en la BD: " + errorBD.Message + "): " + origen + " - " + error.Message);
        }
    }
}
