using MathGame.Enums;
using MathGame.Modelos;
using MathGame.Operaciones;

namespace MathGame.Utilidades
{
    // Reune la entrada de consola, la generacion aleatoria y las consultas auxiliares.
    internal static class Utils
    {
        private const int MINIMO_OPERANDO = 0;
        private const int MAXIMO_OPERANDO = 100;
        private const int MINIMO_DIVISOR = 1;

        private static readonly ETipoOperacion[] TiposOperacion = Enum.GetValues<ETipoOperacion>();

        // Genera un entero en el intervalo semiabierto [minimo, maximo).
        public static int GenerarNumeroAleatorio(
            int minimo = MINIMO_OPERANDO,
            int maximo = MAXIMO_OPERANDO)
        {
            if (minimo >= maximo)
            {
                throw new ArgumentOutOfRangeException(nameof(maximo), "El maximo debe ser mayor que el minimo.");
            }

            return Random.Shared.Next(minimo, maximo);
        }

        // Elige al azar uno de los tipos disponibles.
        public static ETipoOperacion GenerarTipoOperacion()
        {
            return TiposOperacion[Random.Shared.Next(TiposOperacion.Length)];
        }

        // Genera una operacion valida, incluyendo divisiones con cociente entero exacto.
        public static Operacion GenerarOperacion()
        {
            ETipoOperacion tipoOperacion = GenerarTipoOperacion();

            if (tipoOperacion == ETipoOperacion.DIVISION)
            {
                // El cociente se elige primero para que el dividendo sea siempre multiplo del divisor.
                int divisor = GenerarNumeroAleatorio(MINIMO_DIVISOR, MAXIMO_OPERANDO);
                int cociente = GenerarNumeroAleatorio(MINIMO_OPERANDO, MAXIMO_OPERANDO);
                return new Division(divisor * cociente, divisor);
            }

            int operando1 = GenerarNumeroAleatorio();
            int operando2 = GenerarNumeroAleatorio();

            // La expresion switch crea la subclase concreta segun el tipo elegido.
            return tipoOperacion switch
            {
                ETipoOperacion.SUMA => new Suma(operando1, operando2),
                ETipoOperacion.RESTA => new Resta(operando1, operando2),
                ETipoOperacion.MULTIPLICACION => new Multiplicacion(operando1, operando2),
                _ => throw new ArgumentOutOfRangeException(nameof(tipoOperacion), tipoOperacion, "Tipo de operacion no valido.")
            };
        }

        // Lee un entero, repite la peticion ante texto invalido y devuelve null en EOF.
        public static int? PedirEntero(string mensaje)
        {
            while (true)
            {
                Console.Write(mensaje);
                string? entrada = Console.ReadLine();

                // EOF no es un cero: el cero sigue siendo una respuesta valida.
                if (entrada is null)
                {
                    return null;
                }

                if (int.TryParse(entrada, out int numero))
                {
                    return numero;
                }

                Console.WriteLine("Introduzca un numero entero valido.");
            }
        }

        // Escribe las opciones disponibles del menu principal.
        public static void MostrarOpciones()
        {
            Console.WriteLine("\n0. Salir");
            Console.WriteLine("1. Comenzar partida de 5 preguntas");
            Console.WriteLine("2. Mostrar historial de partidas");
            Console.WriteLine("3. Mostrar historial de operaciones");
            Console.WriteLine("4. Mostrar estadisticas");
        }

        // Obtiene las respuestas incorrectas de una partida.
        public static List<AlmacenamientoResultados> ObtenerPreguntasFalladas(Partida partida)
        {
            ArgumentNullException.ThrowIfNull(partida);

            // La lambda conserva solo los resultados que no coinciden con la solucion.
            return partida.Resultados.Values.Where(resultado => !resultado.EsCorrecto).ToList();
        }
    }
}
