using MathGame.Enums;

namespace MathGame.Operaciones
{
    // Resta el segundo numero al primero.
    internal sealed class Resta : Operacion
    {
        // Crea una resta a partir de sus dos operandos.
        public Resta(int primerOperando, int segundoOperando)
            : base(primerOperando, segundoOperando, ETipoOperacion.RESTA)
        {
            Signo = '-';
        }

        // Devuelve el resultado de la resta.
        public override int Calcular()
        {
            return ResultadoEsperado;
        }
    }
}
