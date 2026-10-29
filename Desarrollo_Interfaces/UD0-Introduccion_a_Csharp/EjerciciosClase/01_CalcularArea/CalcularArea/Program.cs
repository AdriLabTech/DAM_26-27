using System;
using CalcularArea;

namespace MiPrograma
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Ingrese el tipo de figura (rectangulo, triangulo, circulo):");
            string figura = Console.ReadLine().ToLower();

            switch (figura)
            {
                case "rectangulo":
                    Rectangulo rectangulo = new Rectangulo();
                    Console.WriteLine("El area del Rectangulo es: " + rectangulo.CalcularArea());
                    break;
                case "triangulo":
                    Triangulo triangulo = new Triangulo();
                    Console.WriteLine("El area del Triángulo es: " + triangulo.CalcularArea());
                    break;

                case "circulo":
                    Circulo circulo = new Circulo();
                    Console.WriteLine("El area del Círculo es: " + circulo.CalcularArea());
                    break;

                default:
                    Console.WriteLine("Figura no reconocida.");
                    break;
            }
        }
    }
}
