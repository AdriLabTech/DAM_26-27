// Ejercicio 14: Lista de la Compra
/* List<string> con 3 productos: se elimina uno por nombre
 * y se recorre la lista resultante.
 */

using System;
using System.Collections.Generic;

class Principal
{
  static void Main()
  {
    List<string> compra = new List<string>();

    compra.Add("Pan");
    compra.Add("Leche");
    compra.Add("Cafe");

    // Remove devuelve true si lo encontro y lo elimino
    bool eliminado = compra.Remove("Leche");
    Console.WriteLine($"Leche eliminada: {eliminado}");

    Console.WriteLine("Lista final:");
    foreach (var producto in compra)
      Console.WriteLine($"- {producto}");
  }
}
