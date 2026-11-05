using System;

namespace Vehiculos
{
    abstract class Vehiculo
    {
        public abstract void Mover();

        public void Frenar()
        {
            Console.WriteLine("El vehículo está frenando... (Metodo concreto)");
        }
    }
}
