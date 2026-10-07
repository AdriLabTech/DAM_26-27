using System.Globalization;
using Microsoft.Data.Sqlite;

namespace HabitLogger;

/// <summary>
/// Cada habito es una tabla de la BD con sus registros. Operaciones: crear, ver, insertar, actualizar y eliminar.
/// Idea clave: el nombre del habito es el nombre de su tabla (ej. habito "agua" = tabla "agua" con
/// las columnas Id, Fecha y Cantidad). Por eso todos los metodos empiezan comprobando que el nombre
/// es valido y que el habito existe
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

    // Tablas de la BD que no son habitos (no se pueden usar como nombre de habito)
    private static readonly string[] TablasReservadas = { "habitos", "errores" };

    public void MostrarHabitos()
    {
        // sqlite_master es una tabla interna de SQLite que lista todo lo que hay en la BD.
        // Pedimos solo las tablas (type = 'table') y quitamos las internas (sqlite_...) y las
        // dos que no son habitos (Habitos y Errores): lo que queda son los habitos creados
        using SqliteCommand comando = _conector.CrearComando(
            "SELECT name FROM sqlite_master " +
            "WHERE type = 'table' AND name NOT LIKE 'sqlite_%' AND name NOT IN ('Habitos', 'Errores') " +
            "ORDER BY name");
        using SqliteDataReader lector = comando.ExecuteReader();

        if (!lector.HasRows)
        {
            Console.WriteLine("No hay habitos creados.");
        }
        else
        {
            Console.WriteLine();
            Console.WriteLine("Habitos:");
            while (lector.Read())
            {
                Console.WriteLine("- " + lector.GetString(0));
            }
        }
        LogOperaciones.Escribir("MOSTRAR habitos");
    }

    // Se llama al arrancar. IF NOT EXISTS hace que solo se cree si todavia no existe.
    // Los registros de cada habito van en su propia tabla (ver CrearHabito), no en esta
    public void CrearTabla()
    {
        using SqliteCommand comando = _conector.CrearComando(
            "CREATE TABLE IF NOT EXISTS Habitos (" +
            "Id INTEGER PRIMARY KEY AUTOINCREMENT, " +
            "NombreHabito TEXT NOT NULL)");
        comando.ExecuteNonQuery();
    }

    // Crear un habito = crear una tabla nueva con su nombre. Se guarda en minusculas porque SQLite
    // no distingue mayusculas en los nombres de tabla ("Agua" y "agua" serian el mismo habito)
    public void CrearHabito(string nombreHabito)
    {
        if (!NombreValido(nombreHabito))
        {
            return;
        }

        if (ExisteTabla(nombreHabito))
        {
            Console.WriteLine("Ya existe un habito con ese nombre.");
            LogOperaciones.Escribir("CREAR HABITO cancelado: ya existe " + nombreHabito);
            return;
        }

        // Aqui el nombre se une al SQL con "+" (no se puede usar un parametro para un nombre de tabla).
        // Es seguro porque NombreValido ya ha comprobado que solo tiene letras, numeros y _
        using SqliteCommand comando = _conector.CrearComando(
            "CREATE TABLE " + nombreHabito.ToLower() + " (" +
            "Id INTEGER PRIMARY KEY AUTOINCREMENT, " +
            "Fecha TEXT NOT NULL, " +
            "Cantidad INTEGER NOT NULL)");
        comando.ExecuteNonQuery();

        Console.WriteLine("Habito creado.");
        LogOperaciones.Escribir("HABITO CREADO: " + nombreHabito);
    }

    public void Ver(string nombreHabito)
    {
        if (!ExisteHabito(nombreHabito))
        {
            return;
        }

        MostrarRegistros(nombreHabito);
        LogOperaciones.Escribir("VER registros de " + nombreHabito);
    }

    public void Insertar(string nombreHabito)
    {
        if (!ExisteHabito(nombreHabito))
        {
            return;
        }

        // Entrada ya repite la pregunta hasta que el dato sea valido, aqui llegan datos correctos
        DateTime fecha = Entrada.PedirFecha("Fecha (" + Entrada.FormatoFecha + ", o escribe 'hoy'): ");
        int cantidad = Entrada.PedirNumero("Cantidad: ", 1, int.MaxValue);

        // Los valores ($fecha, $cantidad) van como parametros y no pegados al texto: asi nunca se
        // interpretan como SQL. La fecha se guarda como yyyy-MM-dd para que ordene bien
        using SqliteCommand comando = _conector.CrearComando("INSERT INTO " + nombreHabito.ToLower() + " (Fecha, Cantidad) VALUES ($fecha, $cantidad)");
        comando.Parameters.AddWithValue("$fecha", fecha.ToString(FormatoFechaBD, CultureInfo.InvariantCulture));
        comando.Parameters.AddWithValue("$cantidad", cantidad);
        comando.ExecuteNonQuery();

        Console.WriteLine("Registro insertado.");
        LogOperaciones.Escribir("INSERTAR en " + nombreHabito + ": Fecha=" + fecha.ToString(Entrada.FormatoFecha) + " Cantidad=" + cantidad);
    }

    public void Actualizar(string nombreHabito)
    {
        if (!ExisteHabito(nombreHabito))
        {
            return;
        }

        // PedirIdExistente devuelve 0 si no hay registros o el Id no existe (los Id empiezan en 1)
        int id = PedirIdExistente(nombreHabito, "actualizar");
        if (id == 0)
        {
            return;
        }

        DateTime fecha = Entrada.PedirFecha("Nueva fecha (" + Entrada.FormatoFecha + ", o escribe 'hoy'): ");
        int cantidad = Entrada.PedirNumero("Nueva cantidad: ", 1, int.MaxValue);

        using SqliteCommand comando = _conector.CrearComando("UPDATE " + nombreHabito.ToLower() + " SET Fecha = $fecha, Cantidad = $cantidad WHERE Id = $id");
        comando.Parameters.AddWithValue("$fecha", fecha.ToString(FormatoFechaBD, CultureInfo.InvariantCulture));
        comando.Parameters.AddWithValue("$cantidad", cantidad);
        comando.Parameters.AddWithValue("$id", id);
        comando.ExecuteNonQuery();

        Console.WriteLine("Registro actualizado.");
        LogOperaciones.Escribir("ACTUALIZAR en " + nombreHabito + ": Id=" + id + " Fecha=" + fecha.ToString(Entrada.FormatoFecha) + " Cantidad=" + cantidad);
    }

    public void Eliminar(string nombreHabito)
    {
        if (!ExisteHabito(nombreHabito))
        {
            return;
        }

        int id = PedirIdExistente(nombreHabito, "eliminar");
        if (id == 0)
        {
            return;
        }

        // Borrar no se puede deshacer, asi que se pide confirmacion: cualquier respuesta distinta de "s" cancela
        string respuesta = Entrada.PedirTexto("Seguro que quieres eliminar el registro " + id + "? (s/n): ");
        if (respuesta.ToLower() != "s")
        {
            Console.WriteLine("Operacion cancelada.");
            LogOperaciones.Escribir("ELIMINAR cancelado en " + nombreHabito + ": Id=" + id);
            return;
        }

        using SqliteCommand comando = _conector.CrearComando("DELETE FROM " + nombreHabito.ToLower() + " WHERE Id = $id");
        comando.Parameters.AddWithValue("$id", id);
        comando.ExecuteNonQuery();

        Console.WriteLine("Registro eliminado.");
        LogOperaciones.Escribir("ELIMINAR en " + nombreHabito + ": Id=" + id);
    }

    // El nombre del habito se usa como nombre de tabla (SQLite no permite parametros ahi), asi que
    // solo se aceptan letras, numeros y _, sin empezar por numero. Si no es valido avisa y devuelve false
    private bool NombreValido(string nombreHabito)
    {
        // Cada comprobacion es un "else if": solo se mira la siguiente si la anterior estaba bien,
        // asi que se muestra siempre el primer fallo. Si "error" sigue vacio al final, el nombre es valido
        string error = "";

        if (nombreHabito == "")
        {
            error = "El nombre del habito no puede estar vacio.";
        }
        else if (char.IsDigit(nombreHabito[0]))
        {
            error = "El nombre del habito no puede empezar por un numero.";
        }
        else if (TablasReservadas.Contains(nombreHabito.ToLower()) || nombreHabito.ToLower().StartsWith("sqlite_"))
        {
            error = "Ese nombre esta reservado, elige otro.";
        }
        else
        {
            // Se revisa letra a letra: solo se permiten letras, numeros y el guion bajo
            foreach (char letra in nombreHabito)
            {
                if (!char.IsLetterOrDigit(letra) && letra != '_')
                {
                    error = "El nombre solo puede tener letras, numeros y _ (sin espacios ni simbolos).";
                    break;
                }
            }
        }

        if (error != "")
        {
            Console.WriteLine(error);
            LogOperaciones.Escribir("Nombre de habito no valido '" + nombreHabito + "': " + error);
            return false;
        }
        return true;
    }

    // Pregunta a SQLite (en sqlite_master) cuantas tablas hay con ese nombre: 0 = no existe, 1 = existe.
    // ExecuteScalar devuelve la primera celda del resultado (aqui el COUNT) y Convert la pasa a int
    private bool ExisteTabla(string nombreHabito)
    {
        using SqliteCommand comando = _conector.CrearComando("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = $nombre");
        comando.Parameters.AddWithValue("$nombre", nombreHabito.ToLower());
        return Convert.ToInt32(comando.ExecuteScalar()) > 0;
    }

    // Comun a ver, insertar, actualizar y eliminar: comprueba que el nombre es valido y que el habito esta creado
    private bool ExisteHabito(string nombreHabito)
    {
        if (!NombreValido(nombreHabito))
        {
            return false;
        }

        if (!ExisteTabla(nombreHabito))
        {
            Console.WriteLine("No existe el habito '" + nombreHabito + "'. Crealo primero con la opcion 1.");
            LogOperaciones.Escribir("Habito inexistente: " + nombreHabito);
            return false;
        }
        return true;
    }

    // Muestra todos los registros. Devuelve false si no hay ninguno.
    // En la BD la fecha esta como yyyy-MM-dd (para ordenar bien) y strftime la convierte a dd/MM/yyyy
    // para el usuario. ORDER BY Fecha, Id: primero por fecha y, si coinciden, por orden de creacion
    private bool MostrarRegistros(string nombreHabito)
    {
        using SqliteCommand comando = _conector.CrearComando(
            "SELECT Id, strftime('%d/%m/%Y', Fecha), Cantidad FROM " + nombreHabito.ToLower() + " ORDER BY Fecha, Id");
        using SqliteDataReader lector = comando.ExecuteReader();

        if (!lector.HasRows)
        {
            Console.WriteLine("No hay registros.");
            return false;
        }

        Console.WriteLine();
        Console.WriteLine("Id\tFecha\t\tCantidad");

        // Read() avanza a la siguiente fila y devuelve false cuando ya no quedan.
        // GetInt32(0), GetString(1)... leen cada columna por su posicion en el SELECT
        while (lector.Read())
        {
            Console.WriteLine(lector.GetInt32(0) + "\t" + lector.GetString(1) + "\t" + lector.GetInt32(2));
        }
        return true;
    }

    // Comun a actualizar y eliminar: muestra los registros, pide un Id y comprueba que existe.
    // Devuelve 0 si no hay registros o el Id no existe
    private int PedirIdExistente(string nombreHabito,string accion)
    {
        if (!MostrarRegistros(nombreHabito.ToLower()))
        {
            LogOperaciones.Escribir(accion.ToUpper() + " cancelado: no hay registros");
            return 0;
        }

        int id = Entrada.PedirNumero("Id del registro a " + accion + ": ", 1, int.MaxValue);

        // El usuario puede escribir cualquier numero, asi que se cuenta si hay un registro con ese Id
        using SqliteCommand comando = _conector.CrearComando("SELECT COUNT(*) FROM " + nombreHabito.ToLower() + " WHERE Id = $id");
        comando.Parameters.AddWithValue("$id", id);
        int total = Convert.ToInt32(comando.ExecuteScalar());

        if (total == 0)
        {
            Console.WriteLine("No existe ningun registro con el Id " + id + ".");
            LogOperaciones.Escribir(accion.ToUpper() + " cancelado: no existe el Id " + id);
            return 0;
        }
        return id;
    }
}
