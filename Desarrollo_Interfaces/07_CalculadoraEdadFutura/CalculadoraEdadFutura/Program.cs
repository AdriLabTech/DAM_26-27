/* Calculadora de Edad Futura
 *
 * Pide al usuario su edad actual con consola
 * Convierte el dato en un entero
 * Muestra la edad que tendra dentro de 10 años
 */
using System;
class Principal
{
  public static void Main(string[] args)
  {
    Console.WriteLine("Introduce tu edad: ");
    int edad = int.Parse(Console.ReadLine());

    Console.WriteLine($"Tu edad dentro de 5 años será: {edad + 5}");
  }
}
