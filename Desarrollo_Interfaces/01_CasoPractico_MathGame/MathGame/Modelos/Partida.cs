namespace MathGame.Modelos
{
    // Agrupa las respuestas de una partida y calcula su puntuacion.
    internal class Partida
    {
        private readonly Dictionary<int, AlmacenamientoResultados> resultados = new();

        // Numero correlativo de la partida dentro de la sesion.
        public int NumeroPartida { get; }

        // Expone las respuestas mediante una vista de solo lectura.
        public IReadOnlyDictionary<int, AlmacenamientoResultados> Resultados => resultados;

        // La lambda cuenta solo las respuestas marcadas como correctas.
        public int Puntuacion => resultados.Values.Count(resultado => resultado.EsCorrecto);

        // Crea una partida vacia con el numero indicado.
        public Partida(int numeroPartida)
        {
            ArgumentOutOfRangeException.ThrowIfNegativeOrZero(numeroPartida);
            NumeroPartida = numeroPartida;
        }

        // Registra la respuesta de una pregunta en la partida.
        public void AgregarResultado(int numeroPregunta, AlmacenamientoResultados resultado)
        {
            ArgumentOutOfRangeException.ThrowIfNegativeOrZero(numeroPregunta);
            ArgumentNullException.ThrowIfNull(resultado);
            resultados.Add(numeroPregunta, resultado);
        }
    }
}
