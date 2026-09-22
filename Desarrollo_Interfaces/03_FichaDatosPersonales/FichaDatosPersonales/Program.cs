/* Crea variables de distintos tipos:
 * Nombre, Edad, Altura, EsEstudiante.
 * Muestra la ficha formateada en consola con separadores.
 * Comprueba la inferencia con `var`
 */

class Principal
{
  public static void Main(string[] args)
  {
    Console.WriteLine("Introduce tu nombre: ");
    string nombre = Console.ReadLine();

    Console.WriteLine("Introduce tu edad: ");
    int edad = int.Parse(Console.ReadLine());

    Console.WriteLine("Introduce tu altura (en metros): ");
    float altura = float.Parse(Console.ReadLine());

    Console.WriteLine("¿Eres Estudiante? (s/n): ");
    string entradaEstudiante = Console.ReadLine();

    bool esEstudiante = entradaEstudiante == "s";

    Console.WriteLine($"--- Ficha de {nombre} ---");
    Console.WriteLine($"Edad: {edad}");
    Console.WriteLine($"Altura: {altura}");
    Console.WriteLine(esEstudiante ? "Es Estudiante" : "No es estudiante");
  }
}
