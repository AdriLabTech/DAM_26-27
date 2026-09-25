using MathGame.Operaciones;

namespace MathGame.Modelos
{
    // Conserva la operacion, la solucion y la respuesta introducida.
    internal sealed class AlmacenamientoResultados
    {
        // Consulta la solucion de la operacion almacenada.
        public int ResultadoEsperado => Operacion.ResultadoEsperado;

        // Respuesta introducida por el usuario.
        public int ResultadoUsuario { get; }

        // Operacion evaluada durante la pregunta.
        public Operacion Operacion { get; }

        // Indica si la respuesta coincide con la solucion.
        public bool EsCorrecto => ResultadoUsuario == ResultadoEsperado;

        // Crea un registro con la operacion evaluada y la respuesta del usuario.
        public AlmacenamientoResultados(Operacion operacionEjecutada, int resultadoUsuario)
        {
            ArgumentNullException.ThrowIfNull(operacionEjecutada);
            Operacion = operacionEjecutada;
            ResultadoUsuario = resultadoUsuario;
        }
    }
}
