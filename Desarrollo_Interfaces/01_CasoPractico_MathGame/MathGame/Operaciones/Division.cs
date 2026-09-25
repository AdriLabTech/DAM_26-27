using MathGame.Enums;

namespace MathGame.Operaciones
{
    // Representa una division entera exacta entre dos numeros.
    internal sealed class Division : Operacion
    {
        // Crea una division exacta con un divisor distinto de cero.
        public Division(int dividendo, int divisor)
            : base(dividendo, divisor, ETipoOperacion.DIVISION)
        {
            Signo = '/';
        }

        // Devuelve el cociente entero de la division.
        public override int Calcular()
        {
            return ResultadoEsperado;
        }
    }
}
