// Ejercicio 10: Area de Figuras
/* Clase CalculadoraArea con el metodo Calcular()
 * sobrecargado: area de un cuadrado (double lado) y de
 * un rectangulo (double b, double h).
 */

using System;

class CalculadoraArea
{
  // Cuadrado
  public double Calcular(double lado)
  {
    return lado * lado;
  }

  // Rectangulo
  public double Calcular(double b, double h)
  {
    return b * h;
  }
}

class Principal
{
  static void Main()
  {
    CalculadoraArea c = new CalculadoraArea();

    Console.WriteLine(c.Calcular(5));     // Cuadrado
    Console.WriteLine(c.Calcular(4, 6));  // Rectangulo
  }
}
