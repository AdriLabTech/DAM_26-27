using gui_bbdd.Models;
using Microsoft.Data.Sqlite;

namespace gui_bbdd.Data;

public class HabitoRepositorio
{
    private static DateOnly Hoy => DateOnly.FromDateTime(DateTime.Today);

    private readonly string _cadenaConexion;

    public HabitoRepositorio(string ruta)
    {
        var carpeta = Path.GetDirectoryName(ruta);
        if (!string.IsNullOrEmpty(carpeta))
            Directory.CreateDirectory(carpeta);

        _cadenaConexion = new SqliteConnectionStringBuilder
        {
            DataSource = ruta,
            ForeignKeys = true,
        }.ToString();

        CrearTablas();
    }

    public static string RutaPorDefecto() =>
        Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
            "gui_bbdd",
            "habitos.db");

    public List<Habito> Cargar()
    {
        using var conexion = Abrir();

        var fechasPorHabito = new Dictionary<int, HashSet<DateOnly>>();
        using (var cmd = conexion.CreateCommand())
        {
            cmd.CommandText = "SELECT habito_id, fecha FROM registros";
            using var lector = cmd.ExecuteReader();
            while (lector.Read())
            {
                var id = lector.GetInt32(0);
                if (!fechasPorHabito.TryGetValue(id, out var fechas))
                    fechasPorHabito[id] = fechas = [];
                fechas.Add(lector.GetFieldValue<DateOnly>(1));
            }
        }

        var habitos = new List<Habito>();
        using (var cmd = conexion.CreateCommand())
        {
            cmd.CommandText = "SELECT id, nombre, descripcion FROM habitos ORDER BY nombre COLLATE NOCASE";
            using var lector = cmd.ExecuteReader();
            while (lector.Read())
            {
                var habito = new Habito
                {
                    Id = lector.GetInt32(0),
                    Nombre = lector.GetString(1),
                    Descripcion = lector.GetString(2),
                };
                Recalcular(habito, fechasPorHabito.GetValueOrDefault(habito.Id) ?? []);
                habitos.Add(habito);
            }
        }
        return habitos;
    }

    public Habito Insertar(string nombre, string descripcion)
    {
        using var conexion = Abrir();
        using var cmd = conexion.CreateCommand();
        cmd.CommandText = "INSERT INTO habitos (nombre, descripcion) VALUES ($nombre, $descripcion) RETURNING id";
        cmd.Parameters.AddWithValue("$nombre", nombre);
        cmd.Parameters.AddWithValue("$descripcion", descripcion);
        var id = Convert.ToInt32(cmd.ExecuteScalar());
        return new Habito { Id = id, Nombre = nombre, Descripcion = descripcion };
    }

    public void Eliminar(int id)
    {
        using var conexion = Abrir();
        using var cmd = conexion.CreateCommand();
        cmd.CommandText = "DELETE FROM habitos WHERE id = $id";
        cmd.Parameters.AddWithValue("$id", id);
        cmd.ExecuteNonQuery();
    }

    /// <summary>Marca o desmarca el hábito para hoy y actualiza sus contadores.</summary>
    public void AlternarHoy(Habito habito)
    {
        using var conexion = Abrir();

        using (var cmd = conexion.CreateCommand())
        {
            cmd.CommandText = habito.HechoHoy
                ? "DELETE FROM registros WHERE habito_id = $id AND fecha = $fecha"
                : "INSERT OR IGNORE INTO registros (habito_id, fecha) VALUES ($id, $fecha)";
            cmd.Parameters.AddWithValue("$id", habito.Id);
            cmd.Parameters.AddWithValue("$fecha", Hoy);
            cmd.ExecuteNonQuery();
        }

        Recalcular(habito, LeerFechas(conexion, habito.Id));
    }

    private static HashSet<DateOnly> LeerFechas(SqliteConnection conexion, int habitoId)
    {
        var fechas = new HashSet<DateOnly>();
        using var cmd = conexion.CreateCommand();
        cmd.CommandText = "SELECT fecha FROM registros WHERE habito_id = $id";
        cmd.Parameters.AddWithValue("$id", habitoId);
        using var lector = cmd.ExecuteReader();
        while (lector.Read())
            fechas.Add(lector.GetFieldValue<DateOnly>(0));
        return fechas;
    }

    private static void Recalcular(Habito habito, HashSet<DateOnly> fechas)
    {
        var hoy = Hoy;
        habito.HechoHoy = fechas.Contains(hoy);
        habito.Total = fechas.Count;

        // Racha: días seguidos hasta hoy; si hoy aún no está hecho, cuenta desde ayer.
        var dia = habito.HechoHoy ? hoy : hoy.AddDays(-1);
        var racha = 0;
        while (fechas.Contains(dia))
        {
            racha++;
            dia = dia.AddDays(-1);
        }
        habito.Racha = racha;
    }

    private SqliteConnection Abrir()
    {
        var conexion = new SqliteConnection(_cadenaConexion);
        conexion.Open();
        return conexion;
    }

    private void CrearTablas()
    {
        using var conexion = Abrir();
        using var cmd = conexion.CreateCommand();
        cmd.CommandText = """
            CREATE TABLE IF NOT EXISTS habitos (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre      TEXT NOT NULL,
                descripcion TEXT NOT NULL DEFAULT ''
            );
            CREATE TABLE IF NOT EXISTS registros (
                habito_id INTEGER NOT NULL REFERENCES habitos(id) ON DELETE CASCADE,
                fecha     TEXT    NOT NULL,
                PRIMARY KEY (habito_id, fecha)
            );
            """;
        cmd.ExecuteNonQuery();
    }
}
