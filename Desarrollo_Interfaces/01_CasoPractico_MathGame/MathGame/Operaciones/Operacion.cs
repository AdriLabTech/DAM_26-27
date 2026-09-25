using MathGame.Enums;
using MathGame.Interfaces;

namespace MathGame.Operaciones
{
    // Agrupa los datos comunes de una operacion y calcula su resultado una sola vez.
    internal abstract class Operacion : IOperacion
    {
        // Primer operando de la expresion.
        public int Operando1 { get; }

        // Segundo operando de la expresion.
        public int Operando2 { get; }

        // Resultado calculado al construir la operacion.
        public int ResultadoEsperado { get; }

        // Simbolo que se muestra en la interfaz.
        public char Signo { get; protected init; }

        // Valida los operandos y prepara el resultado de la operacion indicada.
        protected Operacion(int primerOperando, int segundoOperando, ETipoOperacion tipoOperacion)
        {
            if (tipoOperacion == ETipoOperacion.DIVISION)
            {
                // La division se valida antes de calcular para evitar cero y resultados truncados.
                if (segundoOperando == 0)
                {
                    throw new DivideByZeroException("El divisor de una division no puede ser cero.");
                }

                if (primerOperando % segundoOperando != 0)
                {
                    throw new ArgumentException("La division debe tener un resultado entero exacto.", nameof(segundoOperando));
                }
            }

            Operando1 = primerOperando;
            Operando2 = segundoOperando;
            ResultadoEsperado = CalcularResultado(tipoOperacion);
        }

        // Resuelve la operacion y usa checked para detectar desbordamientos.
        private int CalcularResultado(ETipoOperacion tipoOperacion)
        {
            // El switch evita repetir la formula en el flujo principal.
            return tipoOperacion switch
            {
                ETipoOperacion.SUMA => checked(Operando1 + Operando2),
                ETipoOperacion.RESTA => checked(Operando1 - Operando2),
                ETipoOperacion.MULTIPLICACION => checked(Operando1 * Operando2),
                ETipoOperacion.DIVISION => checked(Operando1 / Operando2),
                _ => throw new ArgumentOutOfRangeException(nameof(tipoOperacion), tipoOperacion, "Tipo de operacion no compatible.")
            };
        }

        // Devuelve el resultado numerico de la operacion.
        public abstract int Calcular();

        // Muestra la expresion y su resultado esperado.
        public virtual void ImprimirResultado()
        {
            Console.WriteLine($"{Operando1} {Signo} {Operando2} = {ResultadoEsperado}");
        }
    }
}
