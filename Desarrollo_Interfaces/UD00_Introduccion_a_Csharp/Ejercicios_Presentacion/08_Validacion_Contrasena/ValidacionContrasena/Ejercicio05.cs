// Ejercicio 05: Validacion de Contrasena
/* Pide una clave por teclado con un bucle do-while,
 * repitiendo la peticion hasta que se acierte ("1234").
 */

using System;

class Principal
{
  static void Main()
  {
    string clave;

    do
    {
      Console.Write("Clave: ");
      clave = Console.ReadLine();
    } while (clave != "1234");

    Console.WriteLine("Acceso Concedido!");
  }
}
