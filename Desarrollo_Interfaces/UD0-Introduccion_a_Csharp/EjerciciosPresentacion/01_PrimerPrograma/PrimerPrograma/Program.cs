// Primer Programa: Hola Nombre
/* Conceptos Clave:
 * - Main(): Punto de entrada de ejecuccion
 *   del Programa
 * - Console.WriteLine(): Metodo de salida
 *   estandar por pantalla
 * - Identificadores: Nombre de clases y
 *   mwetodos en C#
 */

using System;

class HolaNombre
{
  static void Main(){
    Console.Write("Tu nombre: "); // Cuando imprime el texto pasado entre parentesis NO hace ningun salto de linea
    string nombre = Console.ReadLine(); // Sirve para captura la entrada del usuario (y guardarlo en una variable)

    Console.WriteLine($"Hola, {nombre}"); // -> El $ sirve para insertar directamente alguna variable entre {}
  }
}
