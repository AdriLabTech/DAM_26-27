// Ejercicio 03: Calculadora de Edad Futura
/* Solicita la edad actual por consola, la convierte
 * a entero con int.Parse() e imprime la edad que
 * tendra dentro de 10 anios.
 */

using System;

class Principal
{
  static void Main()
  {
    Console.Write("Tu edad actual: ");
    int edad = int.Parse(Console.ReadLine());

    int futura = edad + 10;

    Console.WriteLine($"En 10 anios tendras {futura}");
  }
}
