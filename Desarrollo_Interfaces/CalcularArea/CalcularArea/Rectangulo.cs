using System;
using System.Collections.Generic;
using System.Text;

namespace CalcularArea
{
    internal class Rectangulo : IFigura
    {
        public float CalcularArea()
        {
            Console.WriteLine("Introduce la base del rectángulo: ");
            float base_cuadrado = float.Parse(Console.ReadLine());
            Console.WriteLine("Introduce la altura del rectángulo: ");
            float altura = float.Parse(Console.ReadLine());
            return base_cuadrado * altura;
        }
    }
}
