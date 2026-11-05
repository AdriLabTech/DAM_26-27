// Ejercicio 02: Ficha de Datos Personales
/* Crea variables para nombre, edad, altura y estado de
 * matricula usando inferencia de tipos (var).
 * Imprime la ficha con separadores y verifica los tipos.
 */

using System;

class Principal
{
  static void Main()
  {
    var nombre = "Lucia";
    var edad = 22;
    var altura = 1.68;
    var esMatriculado = true;

    string separador = new string('=', 32);

    Console.WriteLine(separador);
    Console.WriteLine("        FICHA DE DATOS PERSONALES");
    Console.WriteLine(separador);
    Console.WriteLine($"Nombre      : {nombre}");
    Console.WriteLine($"Edad        : {edad} anios");
    Console.WriteLine($"Altura      : {altura} m");
    Console.WriteLine($"Matriculado : {esMatriculado}");
    Console.WriteLine(new string('-', 32));

    // Verificacion de tipos: var infiere el tipo en compilacion
    Console.WriteLine("Tipos inferidos:");
    Console.WriteLine($"  nombre        -> {nombre.GetType().Name}");
    Console.WriteLine($"  edad          -> {edad.GetType().Name}");
    Console.WriteLine($"  altura        -> {altura.GetType().Name}");
    Console.WriteLine($"  esMatriculado -> {esMatriculado.GetType().Name}");
    Console.WriteLine(separador);
  }
}
