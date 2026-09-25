using MathGame.Enums;

namespace MathGame.Operaciones
{
    // Representa una suma entre dos numeros enteros.
    internal sealed class Suma : Operacion
    {
        // Crea una suma a partir de sus dos operandos.
        public Suma(int primerOperando, int segundoOperando)
            : base(primerOperando, segundoOperando, ETipoOperacion.SUMA)
        {
            Signo = '+';
        }

        // Devuelve el resultado de la suma.
        public override int Calcular()
        {
            return ResultadoEsperado;
        }
    }
}
