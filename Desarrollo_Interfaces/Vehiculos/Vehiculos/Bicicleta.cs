using System;
using System.Collections.Generic;
using System.Text;

namespace Vehiculos
{
    internal class Bicicleta : Vehiculo
    {

        public override void Mover()
        {
            Console.WriteLine("La bicicleta se está moviendo... (Metodo Sobreescrito)");
        }
    }
}
