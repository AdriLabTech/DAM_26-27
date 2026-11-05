using System.Globalization;
using FichaUsuario_BBDD.Models;
using Microsoft.Data.Sqlite;

namespace FichaUsuario_BBDD.Data;

public class UsuarioRepositorio
{
    private const string Esquema = """
        CREATE TABLE IF NOT EXISTS Ciudad (
            Id     INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS Usuario (
            Id        INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre    TEXT NOT NULL,
            Correo    TEXT NOT NULL UNIQUE,
            CiudadId  INTEGER NOT NULL REFERENCES Ciudad(Id),
            Fecha     TEXT NOT NULL,
            Acepta    INTEGER NOT NULL CHECK (Acepta = 1),
            FechaAlta TEXT NOT NULL DEFAULT (datetime('now','localtime'))
        );

        INSERT OR IGNORE INTO Ciudad (Nombre) VALUES
            ('Almería'), ('Cádiz'), ('Córdoba'), ('Granada'),
            ('Huelva'), ('Jaén'), ('Málaga'), ('Sevilla');
        """;

    private readonly string _cadenaConexion;

    public UsuarioRepositorio(string ruta)
    {
        var carpeta = Path.GetDirectoryName(ruta);
        if (!string.IsNullOrEmpty(carpeta))
            Directory.CreateDirectory(carpeta);

        _cadenaConexion = new SqliteConnectionStringBuilder
        {
            DataSource = ruta,
            ForeignKeys = true,
        }.ToString();

        CrearBaseDatos();
    }

    public static string RutaPorDefecto() =>
        Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
            "FichaUsuario_BBDD",
            "fichausuarios.db");

    public List<Ciudad> ObtenerCiudades()
    {
        using var conexion = Abrir();
        using var comando = conexion.CreateCommand();
        comando.CommandText = "SELECT Id, Nombre FROM Ciudad ORDER BY Id";

        var ciudades = new List<Ciudad>();
        using var lector = comando.ExecuteReader();
        while (lector.Read())
        {
            ciudades.Add(new Ciudad
            {
                Id = lector.GetInt32(0),
                Nombre = lector.GetString(1),
            });
        }
        return ciudades;
    }

    // Comprueba el correo sin distinguir mayúsculas y minúsculas
    public bool ExisteCorreo(string correo)
    {
        using var conexion = Abrir();
        using var comando = conexion.CreateCommand();
        comando.CommandText = "SELECT EXISTS(SELECT 1 FROM Usuario WHERE Correo = $correo COLLATE NOCASE)";
        comando.Parameters.AddWithValue("$correo", correo);
        return Convert.ToInt32(comando.ExecuteScalar()) == 1;
    }

    public void Insertar(string nombre, string correo, int ciudadId, DateOnly fecha)
    {
        using var conexion = Abrir();
        using var comando = conexion.CreateCommand();
        comando.CommandText = """
            INSERT INTO Usuario (Nombre, Correo, CiudadId, Fecha, Acepta)
            VALUES ($nombre, $correo, $ciudadId, $fecha, 1)
            """;
        comando.Parameters.AddWithValue("$nombre", nombre);
        comando.Parameters.AddWithValue("$correo", correo);
        comando.Parameters.AddWithValue("$ciudadId", ciudadId);
        comando.Parameters.AddWithValue("$fecha", fecha.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture));
        comando.ExecuteNonQuery();
    }

    private SqliteConnection Abrir()
    {
        var conexion = new SqliteConnection(_cadenaConexion);
        conexion.Open();
        return conexion;
    }

    private void CrearBaseDatos()
    {
        using var conexion = Abrir();
        using var comando = conexion.CreateCommand();
        comando.CommandText = Esquema;
        comando.ExecuteNonQuery();
    }
}
