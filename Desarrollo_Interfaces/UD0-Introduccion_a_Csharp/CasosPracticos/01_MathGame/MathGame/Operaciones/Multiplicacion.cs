using MathGame.Enums;

namespace MathGame.Operaciones
{
    // Multiplica dos numeros enteros.
    internal sealed class Multiplicacion : Operacion
    {
        // Crea una multiplicacion a partir de sus dos operandos.
        public Multiplicacion(int primerOperando, int segundoOperando)
            : base(primerOperando, segundoOperando, ETipoOperacion.MULTIPLICACION)
        {
            Signo = '*';
        }

        // Devuelve el resultado de la multiplicacion.
        public override int Calcular()
        {
            return ResultadoEsperado;
        }
    }
}
