/* Solicitar el nombre del usuario y su ciclo
 * formativo por consola.
 * Imprimir un mensaje de bienvenida
 * usando interpolacion de cadenas.
 * Guardar el archivo como `Ejercicio01.cs`
 */
using System;

class Principal
{
  public static void Main(string[] args)
  {
    Console.WriteLine("Introduce tu nombre: ");
    string nombre = Console.ReadLine();

    Console.WriteLine("Introduce tu cuiclo: ");
    string ciclo = Console.ReadLine();

    Console.WriteLine($"Bienvenido al ciclo de {ciclo}, {nombre}");
  }
}
