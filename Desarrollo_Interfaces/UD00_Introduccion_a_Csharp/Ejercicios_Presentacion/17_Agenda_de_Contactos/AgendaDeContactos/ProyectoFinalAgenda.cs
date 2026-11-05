// Proyecto Integrador: Agenda de Contactos
/* Gestor de contactos en consola con Dictionary<string, string>.
 * Menu: 1. Anadir contacto, 2. Buscar por nombre
 * (TryGetValue), 3. Listar todos, 4. Salir.
 */

using System;
using System.Collections.Generic;

class Principal
{
  static void Main()
  {
    var agenda = new Dictionary<string, string>();
    string opcion;

    do
    {
      Console.WriteLine();
      Console.WriteLine("=== AGENDA DE CONTACTOS ===");
      Console.WriteLine("1. Anadir contacto");
      Console.WriteLine("2. Buscar por nombre");
      Console.WriteLine("3. Listar todos");
      Console.WriteLine("4. Salir");
      Console.Write("Opcion: ");
      opcion = Console.ReadLine();

      switch (opcion)
      {
        case "1":
          Anadir(agenda);
          break;
        case "2":
          Buscar(agenda);
          break;
        case "3":
          Listar(agenda);
          break;
        case "4":
          Console.WriteLine("Hasta pronto!");
          break;
        default:
          Console.WriteLine("Opcion no valida.");
          break;
      }
    } while (opcion != "4");
  }

  static void Anadir(Dictionary<string, string> agenda)
  {
    Console.Write("Nombre: ");
    string nombre = Console.ReadLine().Trim();
    if (nombre == "")
    {
      Console.WriteLine("El nombre no puede estar vacio.");
      return;
    }

    Console.Write("Telefono: ");
    string telefono = Console.ReadLine().Trim();

    // Si ya existia se actualiza el telefono
    bool existia = agenda.ContainsKey(nombre);
    agenda[nombre] = telefono;
    Console.WriteLine(existia ? "Contacto actualizado." : "Contacto anadido.");
  }

  static void Buscar(Dictionary<string, string> agenda)
  {
    Console.Write("Nombre a buscar: ");
    string nombre = Console.ReadLine().Trim();

    if (agenda.TryGetValue(nombre, out string telefono))
      Console.WriteLine($"Telefono: {telefono}");
    else
      Console.WriteLine("Contacto no encontrado.");
  }

  static void Listar(Dictionary<string, string> agenda)
  {
    if (agenda.Count == 0)
    {
      Console.WriteLine("La agenda esta vacia.");
      return;
    }

    foreach (var contacto in agenda)
      Console.WriteLine($"{contacto.Key}: {contacto.Value}");
  }
}
