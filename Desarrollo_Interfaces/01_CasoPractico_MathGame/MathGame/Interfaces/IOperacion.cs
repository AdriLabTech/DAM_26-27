namespace MathGame.Interfaces
{
    // Define el comportamiento comun de una expresion aritmetica.
    internal interface IOperacion
    {
        // Obtiene el resultado numerico de la operacion.
        int Calcular();

        // Muestra por consola el resultado de la operacion.
        void ImprimirResultado();
    }
}
