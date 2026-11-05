// Ejercicio 13: Promedio de Calificaciones
/* Declara un array con 5 calificaciones double, lo recorre
 * sumando las notas e imprime el promedio con 2 decimales.
 */

using System;

class Principal
{
  static void Main()
  {
    double[] notas = { 6.5, 8.0, 9.2, 5.0, 7.5 };

    double suma = 0;
    foreach (double n in notas)
      suma += n;

    Console.WriteLine($"Media: {suma / notas.Length:F2}");
  }
}
