using MathGame.Modelos;
using MathGame.Operaciones;
using MathGame.Utilidades;

// Coordina el menu, las partidas y el historial de la sesion.
internal static class Principal
{
    // Centraliza las reglas del menu y el numero de preguntas.
    private const int NUMERO_PREGUNTAS = 5;
    private const int OPCION_SALIR = 0;
    private const int OPCION_NUEVA_PARTIDA = 1;
    private const int OPCION_HISTORIAL_PARTIDAS = 2;
    private const int OPCION_HISTORIAL_OPERACIONES = 3;
    private const int OPCION_ESTADISTICAS = 4;

    // Mantiene el menu activo hasta que el usuario sale o se cierra la entrada.
    private static void Main()
    {
        // El historial se mantiene en memoria durante esta ejecucion.
        List<Partida> historialPartidas = new();

        while (true)
        {
            Utils.MostrarOpciones();
            int? opcion = Utils.PedirEntero("Introduce una Opcion: ");

            // EOF se trata como una salida controlada del programa.
            if (opcion is null)
            {
                Console.WriteLine("Saliendo...");
                return;
            }

            switch (opcion.Value)
            {
                case OPCION_SALIR:
                    Console.WriteLine("Saliendo...");
                    return;

                case OPCION_NUEVA_PARTIDA:
                    Partida? partida = JugarPartida(historialPartidas.Count + 1);

                    if (partida is null)
                    {
                        Console.WriteLine("Partida cancelada porque se cerro la entrada.");
                        return;
                    }

                    historialPartidas.Add(partida);
                    MostrarResumenPartida(partida);
                    break;

                case OPCION_HISTORIAL_PARTIDAS:
                    MostrarHistorialPartidas(historialPartidas);
                    break;

                case OPCION_HISTORIAL_OPERACIONES:
                    MostrarHistorialOperaciones(historialPartidas);
                    break;

                case OPCION_ESTADISTICAS:
                    MostrarEstadisticas(historialPartidas);
                    break;

                default:
                    // Una opcion desconocida no debe terminar la aplicacion con una excepcion.
                    Console.WriteLine("Opcion no valida. Elige una opcion del menu.");
                    break;
            }
        }
    }

    // Ejecuta cinco preguntas y devuelve la partida solo cuando el usuario responde todas.
    private static Partida? JugarPartida(int numeroPartida)
    {
        Partida partida = new(numeroPartida);

        Console.WriteLine($"Nueva partida de {NUMERO_PREGUNTAS} preguntas:");

        for (int numeroPregunta = 1; numeroPregunta <= NUMERO_PREGUNTAS; numeroPregunta++)
        {
            Console.WriteLine($"\nPregunta {numeroPregunta}/{NUMERO_PREGUNTAS}");

            Operacion operacion = Utils.GenerarOperacion();
            Console.WriteLine($"{operacion.Operando1} {operacion.Signo} {operacion.Operando2} = ?");

            int? resultadoUsuario = Utils.PedirEntero("Introduzca una respuesta: ");

            // Sin entrada no se crea una respuesta incompleta ni se guarda una partida a medias.
            if (resultadoUsuario is null)
            {
                return null;
            }

            AlmacenamientoResultados resultado = new(operacion, resultadoUsuario.Value);
            partida.AgregarResultado(numeroPregunta, resultado);

            Console.WriteLine(resultado.EsCorrecto
                ? "Resultado correcto."
                : $"Resultado incorrecto. La solucion era {resultado.ResultadoEsperado}.");
        }

        return partida;
    }

    // Muestra la puntuacion y el detalle de las preguntas falladas.
    private static void MostrarResumenPartida(Partida partida)
    {
        Console.WriteLine("\nPartida finalizada.");
        Console.WriteLine($"Puntuacion: {partida.Puntuacion}/{NUMERO_PREGUNTAS}");

        List<AlmacenamientoResultados> preguntasFalladas = Utils.ObtenerPreguntasFalladas(partida);

        if (preguntasFalladas.Count == 0)
        {
            return;
        }

        Console.WriteLine("Preguntas falladas:");

        foreach (AlmacenamientoResultados resultado in preguntasFalladas)
        {
            Operacion operacion = resultado.Operacion;
            Console.WriteLine($"{operacion.Operando1} {operacion.Signo} {operacion.Operando2} = {operacion.ResultadoEsperado}");
            Console.WriteLine($"Tu respuesta: {resultado.ResultadoUsuario}");
        }
    }

    // Presenta cada partida y el resultado de sus preguntas.
    private static void MostrarHistorialPartidas(IReadOnlyList<Partida> historialPartidas)
    {
        Console.WriteLine("\nHistorial de partidas:");

        if (historialPartidas.Count == 0)
        {
            Console.WriteLine("Todavia no hay partidas completadas.");
            return;
        }

        foreach (Partida partida in historialPartidas)
        {
            Console.WriteLine($"\nPartida {partida.NumeroPartida}: {partida.Puntuacion}/{NUMERO_PREGUNTAS} correctas.");

            // La lambda ordena por clave para conservar el orden de las preguntas.
            foreach (KeyValuePair<int, AlmacenamientoResultados> pregunta in partida.Resultados.OrderBy(resultado => resultado.Key))
            {
                string estado = pregunta.Value.EsCorrecto ? "correcta" : "incorrecta";
                Console.WriteLine($"  Pregunta {pregunta.Key}: {estado} ({pregunta.Value.ResultadoUsuario}/{pregunta.Value.ResultadoEsperado}).");
            }
        }
    }

    // Muestra cada operacion jugada con su solucion y la respuesta del usuario.
    private static void MostrarHistorialOperaciones(IReadOnlyList<Partida> historialPartidas)
    {
        Console.WriteLine("\nHistorial de operaciones:");

        if (historialPartidas.Count == 0)
        {
            Console.WriteLine("Todavia no hay operaciones jugadas.");
            return;
        }

        foreach (Partida partida in historialPartidas)
        {
            Console.WriteLine($"\nPartida {partida.NumeroPartida}:");

            // La lambda mantiene las operaciones en el orden en que se respondieron.
            foreach (KeyValuePair<int, AlmacenamientoResultados> pregunta in partida.Resultados.OrderBy(resultado => resultado.Key))
            {
                Operacion operacion = pregunta.Value.Operacion;
                string estado = pregunta.Value.EsCorrecto ? "correcta" : "incorrecta";
                Console.WriteLine(
                    $"  Pregunta {pregunta.Key}: {operacion.Operando1} {operacion.Signo} {operacion.Operando2} = {operacion.ResultadoEsperado}; " +
                    $"respuesta: {pregunta.Value.ResultadoUsuario} ({estado}).");
            }
        }
    }

    // Calcula los totales de la sesion sin modificar las partidas guardadas.
    private static void MostrarEstadisticas(IReadOnlyList<Partida> historialPartidas)
    {
        Console.WriteLine("\nEstadisticas:");

        if (historialPartidas.Count == 0)
        {
            Console.WriteLine("Todavia no hay estadisticas disponibles.");
            return;
        }

        // Las lambdas recorren las partidas y resumen sus resultados.
        int totalPreguntas = historialPartidas.Sum(partida => partida.Resultados.Count);
        int totalAciertos = historialPartidas.Sum(partida => partida.Puntuacion);
        int totalFallos = totalPreguntas - totalAciertos;
        int mejorPuntuacion = historialPartidas.Max(partida => partida.Puntuacion);
        decimal porcentajeAciertos = totalPreguntas == 0
            ? 0
            : totalAciertos * 100m / totalPreguntas;

        Console.WriteLine($"Partidas jugadas: {historialPartidas.Count}");
        Console.WriteLine($"Preguntas respondidas: {totalPreguntas}");
        Console.WriteLine($"Aciertos: {totalAciertos}");
        Console.WriteLine($"Fallos: {totalFallos}");
        Console.WriteLine($"Porcentaje de aciertos: {porcentajeAciertos:F1}%");
        Console.WriteLine($"Mejor puntuacion: {mejorPuntuacion}/{NUMERO_PREGUNTAS}");
    }
}
