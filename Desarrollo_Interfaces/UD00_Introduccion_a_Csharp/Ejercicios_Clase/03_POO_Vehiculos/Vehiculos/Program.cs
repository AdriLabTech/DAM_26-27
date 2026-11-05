using System;
using Vehiculos;

class MainClass
{
    static void Main(string[] args)
    {
        Vehiculo bicicleta = new Bicicleta();

        bicicleta.Mover();
        bicicleta.Frenar();
    }
}
