using System;
using System.Collections.Generic;
using System.Text;
using System.Data;
using Microsoft.Data.Sqlite;

namespace HabitLoggerTui.DataBaseConnector
{
    /// <summary>
    /// Se encarga de la conexion con la BD SQLite. Toda la aplicacion comparte una unica conexion,
    /// que se abre solo una vez y se reutiliza para todos los comandos
    /// </summary>
    internal class DataBaseConnector : IDisposable
    {
        private readonly string _cadenaConexion;
        private SqliteConnection? _conexion;


        // Definimos el constructor principal
        public DataBaseConnector(string rutaDelArchivo)
        {
            _cadenaConexion = new SqliteConnectionStringBuilder
            {
                DataSource = rutaDelArchivo,
                Mode = SqliteOpenMode.ReadWriteCreate // El modo permite crear una base de datos en caso de que no exista previamente (si ya existe, no se crea una nueva)
            }.ToString();
        }

        /// <summary>
        /// Metodo para abrir una conexion a una BD
        /// Creamos una conexon usando la cadena definida en el constructor y abrimos la conexion
        /// (SOLAMENTE CUANDO ESTE CERRADA). Si la conexion ya estaba abierta en otro punto del programa,
        /// no abriremos otra conexion
        /// </summary>
        public void AbrirConexionBBDD()
        {
            // "??=" significa: si _conexion todavia es null, crea el objeto (si ya existe, lo deja como esta)
            _conexion ??= new SqliteConnection(_cadenaConexion);

            if (_conexion.State == ConnectionState.Closed)
            {
                _conexion.Open();
            }
        }


        public void CerrarConexionBBDD()
        {
            if (_conexion != null && _conexion.State != ConnectionState.Closed)
            {
                _conexion.Close();
            }
        }


        /// <summary>
        /// Crea un comando SQL listo para usar (abre la conexion si hacia falta).
        /// Asi el resto de clases no repiten este codigo
        /// </summary>
        public SqliteCommand CrearComando(string sql)
        {
            AbrirConexionBBDD();

            // El "!" le dice al compilador que _conexion no es null aqui: la linea de arriba acaba de crearla
            SqliteCommand comando = _conexion!.CreateCommand();
            comando.CommandText = sql;
            return comando;
        }


        // Al implementar IDisposable, la clase se puede usar dentro de un "using" y la conexion se cierra sola
        public void Dispose()
        {
            CerrarConexionBBDD();
        }
    }
}
