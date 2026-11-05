using System;
using System.Collections.Generic;
using System.Text;

namespace CalcularArea
{
    internal class Circulo : IFigura
    {
        public float CalcularArea()
        {
            Console.WriteLine("Introduce el radio del circulo: ");
            float radio = float.Parse(Console.ReadLine());
            const float pi = 3.14159f;
            return pi * (radio * radio);
        }
    }
}
