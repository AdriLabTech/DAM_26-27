// Ejercicio 09: Vehiculo y Autobus
/* Clase base Vehiculo con Velocidad y clase hija Autobus
 * con Capacidad. Se instancia un Autobus y se accede a
 * los miembros heredados y a los propios.
 */

using System;

class Vehiculo
{
  public int Velocidad { get; set; }
}

class Autobus : Vehiculo
{
  public int Capacidad { get; set; }
}

class Principal
{
  static void Main()
  {
    Autobus bus = new Autobus();
    bus.Velocidad = 90;   // miembro heredado de Vehiculo
    bus.Capacidad = 55;   // miembro propio de Autobus

    Console.WriteLine($"{bus.Velocidad}km/h, {bus.Capacidad}p");
  }
}
