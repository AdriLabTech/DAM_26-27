// Ejercicio 01: Mensaje Personalizado
/* Solicita el nombre del usuario y su ciclo
 * formativo por consola.
 * Imprime un mensaje de Bienvenida 
 * usando interpolacion de cadenas.
 */

using System;

class Principal
{
  static void Main()
  {
    Console.WriteLine("Introduce tu nombre: ");
    string nombre = Console.ReadLine();

    Console.WriteLine("Introduce tu ciclo formativo: ");
    string ciclo = Console.ReadLine();

    Console.WriteLine($"Bienvenido/a {nombre} a {ciclo}!!!");
  }
}
