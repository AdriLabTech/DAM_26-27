/* Variables y Tipos de Datos (I, II)
 * 
 * Variables y Tipos de Datos (I)
 * -------------------------------
 * - Espacios en Memoria: Direccion
 *   etiquetada con nombre y tipo estatico
 * - Tipos Primitivos: int, double, bool,
 *   char, string
 * - Fuerte Tipado: C# no permite
 *   asignaciones incompatibles sin conversion
 */

using System;

class Principal
{
  public static void Main(string [] args)
  {
    int edad = 20;
    double precio = 19.99;
    bool activo = true;
    char letra = 'A';
    string modulo = "C# y .NET";

    /// Para mostrarlo por pantalla usamos Console.WriteLine();
    Console.WriteLine("Edad: " + edad);
    Console.WriteLine("Precio: " + precio);
    Console.WriteLine("Activo: " + activo);
    Console.WriteLine("Letra: " + letra);
    Console.WriteLine("Modulo: " + modulo);

    /* Variables y Tipos de Datos (II)
     * -------------------------------
     * - Stack (Pila): Memoria rapida para tipos
     *   por valor (int, struct)
     * - Heap: Memoria dinamica para objetos y referencias
     * - Copia de Datos: Asignar un tipo por valor duplica
     *   el dato original
     */

    int a = 10;
    int b = a; // -> Copia del valor
    b = 20;
    Console.WriteLine(a); // -> 10
    Console.WriteLine(b); // -> 20

    /* Declaracion e Inicializacion de Variables
     * Inferencia e Inmutabilidad
     * ----------------------------
     * - var: Inferencia de tipos implicita en
     *   tiempo de compilacion
     * - const: Variables inmutables con valor
     *   fijo en compilacion
     * - Convencion: usar `camelCase` para
     *   variables y `PascalCase` para constantes
     */

    var total = 150.50;
    const double Iva = 0.21;
    var final = total * (1 + Iva);

    Console.WriteLine($"Total: {final:C}");

    /* Tipos Anulables (Nullable Reference Types)
     * Seguridad frente a Nulos
     * --------------------------
     * - String?: Permite valores nulos implicitos
     * - Operator?: Navegacion segura frente a referencias nulas
     * - Operador??: Asigna un valor por defecto si el objeto es null
     */

    string nombre = "Fernando";
    int edad = 22;
    double altura = 1.78;
    bool esEstudiante = true;
    Console.WriteLine($"Ficha: {nombre},{edad}a, {altura}m, Est: {esEstudiante}");

  }
}
