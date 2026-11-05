// Ejercicio 04: Numero Par o Impar
/* Solicita un numero entero por teclado, calcula el
 * resto de dividirlo entre 2 con el operador % e
 * informa de si es PAR o IMPAR.
 */

using System;

class Principal
{
  static void Main()
  {
    Console.Write("Numero: ");
    int num = int.Parse(Console.ReadLine());

    // El resto de dividir entre 2 es 0 en los pares
    if (num % 2 == 0)
      Console.WriteLine("PAR");
    else
      Console.WriteLine("IMPAR");
  }
}
