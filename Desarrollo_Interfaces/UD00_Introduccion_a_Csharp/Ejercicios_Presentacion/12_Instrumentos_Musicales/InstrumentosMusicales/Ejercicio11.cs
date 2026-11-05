// Ejercicio 11: Instrumentos Musicales
/* Clase base Instrumento con el metodo virtual Tocar() y
 * subclases Guitarra y Piano que lo sobrescriben. Se
 * ejecutan mediante referencias de la clase base
 * (polimorfismo).
 */

using System;

class Instrumento
{
  public virtual void Tocar()
  {
    Console.WriteLine("Suena un instrumento");
  }
}

class Guitarra : Instrumento
{
  public override void Tocar()
  {
    Console.WriteLine("Suena la guitarra");
  }
}

class Piano : Instrumento
{
  public override void Tocar()
  {
    Console.WriteLine("Suena el piano");
  }
}

class Principal
{
  static void Main()
  {
    Instrumento i1 = new Guitarra();
    Instrumento i2 = new Piano();

    i1.Tocar();
    i2.Tocar();
  }
}
