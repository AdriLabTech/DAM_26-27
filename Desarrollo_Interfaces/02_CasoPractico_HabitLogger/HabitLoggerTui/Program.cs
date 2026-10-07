using System;
using System.Text;

namespace HabitLoggerTui;

public class Principal
{
    public static void Main(string[] args)
    {
        // La TUI necesita una consola interactiva: no funciona si la entrada o la salida estan redirigidas
        if (Console.IsInputRedirected || Console.IsOutputRedirected)
        {
            Console.WriteLine("Esta aplicacion necesita ejecutarse en una consola interactiva.");
            return;
        }

        // Necesario para que los bordes y los caracteres especiales se vean bien
        Console.OutputEncoding = Encoding.UTF8;

        DataBaseConnector.DataBaseConnector conector = new DataBaseConnector.DataBaseConnector(AppContext.BaseDirectory + "mi_bbdd.bd");
        GestorHabitos gestor = new GestorHabitos(conector);
        LogErrores logErrores = new LogErrores(conector);

        LogOperaciones.Escribir("Aplicacion iniciada");

        try
        {
            // Al abrir la conexion se crea el archivo de la BD si no existia
            conector.AbrirConexionBBDD();
            LogOperaciones.Escribir("Conexion con la BD abierta");
            gestor.CrearTabla();
            logErrores.CrearTabla();

            // Ejecutar() no termina hasta que el usuario sale de la TUI; despues se pasa al finally
            new Aplicacion(gestor, logErrores).Ejecutar();
        }
        catch (Exception ex)
        {
            // Errores graves (ej. no se puede abrir la BD o no se puede iniciar la TUI): avisamos y cerramos sin crash.
            // Llegados aqui la TUI ya se ha cerrado, asi que se puede escribir en consola
            LogOperaciones.Escribir("ERROR GRAVE: " + ex.Message);
            Console.WriteLine("Ha ocurrido un error grave y la aplicacion se cerrara. Mira la carpeta de logs.");
            Console.WriteLine("Detalle: " + ex.Message);
        }
        finally
        {
            conector.CerrarConexionBBDD();
            LogOperaciones.Escribir("Aplicacion finalizada");
        }
    }
}
