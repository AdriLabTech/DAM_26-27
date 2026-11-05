// Ejercicio 15: Lectura Segura de Numeros
/* Funcion LeerEntero() protegida con try-catch: pide un
 * numero repetidamente hasta que se introduce un entero
 * valido.
 */

using System;

class Principal
{
  static int LeerEntero()
  {
    while (true)
    {
      try
      {
        return int.Parse(Console.ReadLine());
      }
      catch (Exception)
      {
        Console.Write("Reintenta: ");
      }
    }
  }

  static void Main()
  {
    Console.Write("Introduce un numero entero: ");
    int numero = LeerEntero();

    Console.WriteLine($"Has introducido: {numero}");
  }
}
