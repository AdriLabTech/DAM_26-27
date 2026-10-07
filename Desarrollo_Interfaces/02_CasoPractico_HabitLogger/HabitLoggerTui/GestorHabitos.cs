using System.Globalization;
using Microsoft.Data.Sqlite;

namespace HabitLoggerTui;

/// <summary>
/// Operaciones sobre la tabla "Habitos": ver, insertar, actualizar y eliminar.
/// No escribe nada en pantalla: devuelve los datos y la TUI se encarga de mostrarlos
/// </summary>
internal class GestorHabitos
{
    // Asi se guarda la fecha en SQLite (de esta forma se ordena bien por fecha)
    private const string FormatoFechaBD = "yyyy-MM-dd";

    private readonly DataBaseConnector.DataBaseConnector _conector;

    public GestorHabitos(DataBaseConnector.DataBaseConnector conector)
    {
        _conector = conector;
    }

    public void CrearTabla()
    {
        using SqliteCommand comando = _conector.CrearComando(
            "CREATE TABLE IF NOT EXISTS Habitos (" +
            "Id INTEGER PRIMARY KEY AUTOINCREMENT, " +
            "Fecha TEXT NOT NULL, " +
            "Cantidad INTEGER NOT NULL)");
        comando.ExecuteNonQuery();
    }

    // Lee todos los registros y los convierte en objetos Habito para que la TUI los dibuje.
    // ORDER BY Fecha, Id: primero por fecha y, si coinciden, por orden de creacion
    public List<Habito> ObtenerTodos()
    {
        List<Habito> habitos = new List<Habito>();

        using SqliteCommand comando = _conector.CrearComando("SELECT Id, Fecha, Cantidad FROM Habitos ORDER BY Fecha, Id");
        using SqliteDataReader lector = comando.ExecuteReader();

        // Read() avanza a la siguiente fila y devuelve false cuando ya no quedan.
        // GetInt32(0), GetString(1)... leen cada columna por su posicion en el SELECT
        while (lector.Read())
        {
            Habito habito = new Habito();
            habito.Id = lector.GetInt32(0);

            // En la BD la fecha es un texto yyyy-MM-dd; aqui se convierte de vuelta a DateTime
            habito.Fecha = DateTime.ParseExact(lector.GetString(1), FormatoFechaBD, CultureInfo.InvariantCulture);
            habito.Cantidad = lector.GetInt32(2);
            habitos.Add(habito);
        }
        return habitos;
    }

    // Los valores ($fecha, $cantidad) van como parametros y no pegados al texto SQL: asi nunca se
    // interpretan como SQL. Las fechas se guardan como yyyy-MM-dd para que ordenen bien.
    // Insertar, Actualizar y Eliminar solo escriben en la BD: la validacion ya la hizo Validacion
    public void Insertar(DateTime fecha, int cantidad)
    {
        using SqliteCommand comando = _conector.CrearComando("INSERT INTO Habitos (Fecha, Cantidad) VALUES ($fecha, $cantidad)");
        comando.Parameters.AddWithValue("$fecha", fecha.ToString(FormatoFechaBD, CultureInfo.InvariantCulture));
        comando.Parameters.AddWithValue("$cantidad", cantidad);
        comando.ExecuteNonQuery();

        LogOperaciones.Escribir("INSERTAR: Fecha=" + fecha.ToString(Validacion.FormatoFecha, CultureInfo.InvariantCulture) + " Cantidad=" + cantidad);
    }

    public void Actualizar(int id, DateTime fecha, int cantidad)
    {
        using SqliteCommand comando = _conector.CrearComando("UPDATE Habitos SET Fecha = $fecha, Cantidad = $cantidad WHERE Id = $id");
        comando.Parameters.AddWithValue("$fecha", fecha.ToString(FormatoFechaBD, CultureInfo.InvariantCulture));
        comando.Parameters.AddWithValue("$cantidad", cantidad);
        comando.Parameters.AddWithValue("$id", id);
        comando.ExecuteNonQuery();

        LogOperaciones.Escribir("ACTUALIZAR: Id=" + id + " Fecha=" + fecha.ToString(Validacion.FormatoFecha, CultureInfo.InvariantCulture) + " Cantidad=" + cantidad);
    }

    public void Eliminar(int id)
    {
        using SqliteCommand comando = _conector.CrearComando("DELETE FROM Habitos WHERE Id = $id");
        comando.Parameters.AddWithValue("$id", id);
        comando.ExecuteNonQuery();

        LogOperaciones.Escribir("ELIMINAR: Id=" + id);
    }
}
