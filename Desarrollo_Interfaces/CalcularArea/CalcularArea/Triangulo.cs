using System;
using System.Collections.Generic;
using System.Text;

namespace CalcularArea
{
    internal class Triangulo : IFigura
    {
        public float CalcularArea()
        {
            Console.WriteLine("Introduce la base del triangulo: ");
            float baseTriangulo = float.Parse(Console.ReadLine());
            Console.WriteLine("Introduce la altura del triangulo: ");
            float alturaTriangulo = float.Parse(Console.ReadLine());
            return (baseTriangulo * alturaTriangulo) / 2;
        }
    }
}
