using System;


namespace HabitLogger;

public class Principal
{
    /// <summary>
    /// Punto de entrada. Prepara la BD y repite el menu hasta que el usuario elige salir (0).
    /// Hay dos niveles de try/catch: uno por cada opcion del menu (el programa sigue) y uno
    /// general (el programa se cierra de forma controlada). El finally siempre cierra la BD
    /// </summary>
    public static void Main(string[] args)
    {
        // La BD y los logs se guardan junto al ejecutable. Todas las clases comparten el mismo conector
        DataBaseConnector.DataBaseConnector conector = new DataBaseConnector.DataBaseConnector(AppContext.BaseDirectory + "mi_bbdd.bd");
        GestorHabitos gestor = new GestorHabitos(conector);
        LogErrores logErrores = new LogErrores(conector);

        LogOperaciones.Escribir("Aplicacion iniciada");

        try
        {
            // Al abrir la conexion se crea el archivo de la BD si no existia
            conector.AbrirConexionBBDD();
            LogOperaciones.Escribir("Conexion con la BD abierta");
            // Las tablas se crean solo si no existian (CREATE TABLE IF NOT EXISTS)
            gestor.CrearTabla();
            logErrores.CrearTabla();

            // Bucle principal: -1 es un valor inicial para que entre la primera vez
            int opcion = -1;
            while (opcion != 0)
            {
                MostrarMenu();
                opcion = Entrada.PedirNumero("Elige una opcion: ", 0, 6);

                // Este try/catch evita que un error en una opcion cierre la aplicacion
                try
                {
                    // Cada opcion pide el nombre del habito y se lo pasa al gestor, que hace el trabajo.
                    // La opcion 0 no entra en ningun if: el while termina y el programa se cierra
                    if (opcion == 1)
                    {
                        gestor.CrearHabito(Entrada.PedirTexto("Introduce el nombre del nuevo hábito: "));
                    }
                    else if (opcion == 2)
                    {
                        gestor.Ver(Entrada.PedirTexto("Introduce el habito que quieras ver: "));
                    }
                    else if (opcion == 3)
                    {
                        gestor.Insertar(Entrada.PedirTexto("Introduce el habito que quieras registrar: "));
                    }
                    else if (opcion == 4)
                    {
                        gestor.Actualizar(Entrada.PedirTexto("Introduce el habito que quieres actualizar: "));
                    }
                    else if (opcion == 5)
                    {
                        gestor.Eliminar(Entrada.PedirTexto("Introduce el habito que quieras borrar: "));
                    }
                    else if (opcion == 6)
                    {
                        gestor.MostrarHabitos();
                    }
                }
                catch (Exception ex)
                {
                    // El error se guarda en la tabla Errores y se vuelve al menu
                    logErrores.Guardar("Opcion " + opcion + " del menu", ex);
                    LogOperaciones.Escribir("ERROR en la opcion " + opcion + " del menu");
                    Console.WriteLine("Ha ocurrido un error y la operacion no se ha completado. El error se ha guardado.");
                }
            }
        }
        catch (Exception ex)
        {
            // Errores graves (ej. no se puede abrir la BD): avisamos y cerramos sin crash
            LogOperaciones.Escribir("ERROR GRAVE: " + ex.Message);
            Console.WriteLine("Ha ocurrido un error grave y la aplicacion se cerrara. Mira la carpeta de logs.");
        }
        finally
        {
            conector.CerrarConexionBBDD();
            LogOperaciones.Escribir("Aplicacion finalizada");
        }
    }

    private static void MostrarMenu()
    {
        Console.WriteLine();
        Console.WriteLine("=== REGISTRO DE HABITOS ===");
        Console.WriteLine("1. Crear un Hábito");
        Console.WriteLine("2. Ver registros");
        Console.WriteLine("3. Insertar registro");
        Console.WriteLine("4. Actualizar registro");
        Console.WriteLine("5. Eliminar registro");
        Console.WriteLine("6. Mostrar todos los hábitos");
        Console.WriteLine("0. Salir");
    }
}
