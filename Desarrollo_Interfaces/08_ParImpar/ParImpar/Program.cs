/* Numero Par o Impar
 * Solicita un numero entero por consola
 * Evalua si es par o impar
 * Muestra el resultado por pantalla
 */
using System;

class Principal
{
  public static void Main(string[] args)
  {
    Console.WriteLine("Introduce un número: ");
    int num = int.Parse(Console.ReadLine());

    Console.WriteLine(num % 2 == 0 ? "El número es Par" : "El número es Impar");
  }
}
