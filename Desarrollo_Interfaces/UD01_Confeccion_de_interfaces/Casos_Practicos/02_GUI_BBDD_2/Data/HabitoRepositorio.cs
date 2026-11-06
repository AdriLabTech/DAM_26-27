using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using gui_bbdd.Models;
using Microsoft.Data.Sqlite;

namespace gui_bbdd.Data
{
    public class HabitoRepositorio
    {
        private const string FormatoFecha = "yyyy-MM-dd";

        private string _cadenaConexion;

        public HabitoRepositorio(string ruta)
        {
            string carpeta = Path.GetDirectoryName(ruta);
            if (!string.IsNullOrEmpty(carpeta))
            {
                Directory.CreateDirectory(carpeta);
            }

            SqliteConnectionStringBuilder constructor = new SqliteConnectionStringBuilder();
            constructor.DataSource = ruta;
            constructor.ForeignKeys = true;
            _cadenaConexion = constructor.ToString();

            CrearTablas();
        }

        public static string RutaPorDefecto()
        {
            string carpeta = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
            return Path.Combine(carpeta, "gui_bbdd", "habitos.db");
        }

        public List<Habito> Cargar()
        {
            List<Habito> habitos = new List<Habito>();

            using (SqliteConnection conexion = Abrir())
            {
                using (SqliteCommand cmd = conexion.CreateCommand())
                {
                    cmd.CommandText = "SELECT id, nombre, descripcion FROM habitos ORDER BY nombre COLLATE NOCASE";
                    using (SqliteDataReader lector = cmd.ExecuteReader())
                    {
                        while (lector.Read())
                        {
                            habitos.Add(new Habito(lector.GetInt32(0), lector.GetString(1), lector.GetString(2)));
                        }
                    }
                }

                foreach (Habito habito in habitos)
                {
                    Recalcular(habito, LeerFechas(conexion, habito.Id));
                }
            }

            return habitos;
        }

        public Habito Insertar(string nombre, string descripcion)
        {
            using (SqliteConnection conexion = Abrir())
            {
                using (SqliteCommand cmd = conexion.CreateCommand())
                {
                    cmd.CommandText = "INSERT INTO habitos (nombre, descripcion) VALUES ($nombre, $descripcion) RETURNING id";
                    cmd.Parameters.AddWithValue("$nombre", nombre);
                    cmd.Parameters.AddWithValue("$descripcion", descripcion);
                    int id = Convert.ToInt32(cmd.ExecuteScalar());
                    return new Habito(id, nombre, descripcion);
                }
            }
        }

        public void Eliminar(int id)
        {
            using (SqliteConnection conexion = Abrir())
            {
                using (SqliteCommand cmd = conexion.CreateCommand())
                {
                    cmd.CommandText = "DELETE FROM habitos WHERE id = $id";
                    cmd.Parameters.AddWithValue("$id", id);
                    cmd.ExecuteNonQuery();
                }
            }
        }

        // Marca o desmarca el hábito para hoy y actualiza sus contadores.
        public void AlternarHoy(Habito habito)
        {
            using (SqliteConnection conexion = Abrir())
            {
                using (SqliteCommand cmd = conexion.CreateCommand())
                {
                    if (habito.HechoHoy)
                    {
                        cmd.CommandText = "DELETE FROM registros WHERE habito_id = $id AND fecha = $fecha";
                    }
                    else
                    {
                        cmd.CommandText = "INSERT OR IGNORE INTO registros (habito_id, fecha) VALUES ($id, $fecha)";
                    }
                    cmd.Parameters.AddWithValue("$id", habito.Id);
                    cmd.Parameters.AddWithValue("$fecha", DateTime.Today.ToString(FormatoFecha, CultureInfo.InvariantCulture));
                    cmd.ExecuteNonQuery();
                }

                Recalcular(habito, LeerFechas(conexion, habito.Id));
            }
        }

        // Fechas en las que se completó el hábito, de la más reciente a la más antigua.
        public List<DateTime> Historial(int habitoId)
        {
            using (SqliteConnection conexion = Abrir())
            {
                List<DateTime> fechas = LeerFechas(conexion, habitoId);
                fechas.Sort();
                fechas.Reverse();
                return fechas;
            }
        }

        private static List<DateTime> LeerFechas(SqliteConnection conexion, int habitoId)
        {
            List<DateTime> fechas = new List<DateTime>();

            using (SqliteCommand cmd = conexion.CreateCommand())
            {
                cmd.CommandText = "SELECT fecha FROM registros WHERE habito_id = $id";
                cmd.Parameters.AddWithValue("$id", habitoId);
                using (SqliteDataReader lector = cmd.ExecuteReader())
                {
                    while (lector.Read())
                    {
                        fechas.Add(DateTime.Parse(lector.GetString(0), CultureInfo.InvariantCulture).Date);
                    }
                }
            }

            return fechas;
        }

        private static void Recalcular(Habito habito, List<DateTime> fechas)
        {
            DateTime hoy = DateTime.Today;
            habito.HechoHoy = fechas.Contains(hoy);
            habito.Total = fechas.Count;

            // Racha: días seguidos hasta hoy; si hoy aún no está hecho, cuenta desde ayer.
            DateTime dia = hoy.AddDays(-1);
            if (habito.HechoHoy)
            {
                dia = hoy;
            }

            int racha = 0;
            while (fechas.Contains(dia))
            {
                racha++;
                dia = dia.AddDays(-1);
            }
            habito.Racha = racha;
        }

        private SqliteConnection Abrir()
        {
            SqliteConnection conexion = new SqliteConnection(_cadenaConexion);
            conexion.Open();
            return conexion;
        }

        private void CrearTablas()
        {
            using (SqliteConnection conexion = Abrir())
            {
                using (SqliteCommand cmd = conexion.CreateCommand())
                {
                    cmd.CommandText =
                        "CREATE TABLE IF NOT EXISTS habitos (" +
                        "    id          INTEGER PRIMARY KEY AUTOINCREMENT," +
                        "    nombre      TEXT NOT NULL," +
                        "    descripcion TEXT NOT NULL DEFAULT ''" +
                        ");" +
                        "CREATE TABLE IF NOT EXISTS registros (" +
                        "    habito_id INTEGER NOT NULL REFERENCES habitos(id) ON DELETE CASCADE," +
                        "    fecha     TEXT    NOT NULL," +
                        "    PRIMARY KEY (habito_id, fecha)" +
                        ");";
                    cmd.ExecuteNonQuery();
                }
            }
        }
    }
}
