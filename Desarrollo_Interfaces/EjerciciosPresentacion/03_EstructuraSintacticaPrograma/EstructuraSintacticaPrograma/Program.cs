// EStructura Sintáctica de un Programa C#
/* Elementos principales
 * - Namespaces: Organizacion logica de
 *   clases y librerias
 * - Clase: Contenedor principal de datos y
 *   comportamiento
 * - Bloques {}: Delimitan el alcance de
 *   código
 */

using System.Text.RegularExpressions;
using System;
namespace MiApp
{
    class Estructura
    {
      static void Main()
      {
        Console.WriteLine("Estructura C#");

        /* Sentencias de Nivel Superior (Top-Level)
         * Desde C# 9, podemso eliminar explicitamente
         * la necesidad de `class Program`, ideal para
         * scripts por su codigo mas limpio e intuitivo.
         *
         * El compilador crea un punto Main internamente
         */


        /* Formateo Avanzado de Cadenas
         * Interpolacion y Verbatim
         * --------------------------
         * - Interpolacion ($): Insercion directa de
         *   variables entre {}
         * - Cadenas Verbatim (@): Ignora caracteres
         *   de escape
         * - Raw String Literals("""...): Permite multilinea
         *   y caracteres especiales
         */

        string ruta = @"C:\Datos\archivo.txt";
        string nombre = "Adrian";
        string msj = $"Usuario: {nombre}";
        string json = """
          { "id": 1}
        """;

        /* Expreisones Regulares
         * Validacion y Busqueda
         * -----------------------
         * - Regex.IsMatch(): Comprueva si una
         *   cadena cumple un patrón
         * - Regex.Match(): Extrae coincidencias
         *   especificas de un texto
         */

        string email = "usuario@dominio.com";
        string patron = @"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$";
        bool ok = Regex.IsMatch(email, patron);
        Console.WriteLine(ok ? "Email Válido" : "Email Invalido");
      }
    }
}
