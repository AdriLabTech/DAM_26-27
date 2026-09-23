/* Validacion de Contraseña
 * Solicitar una clave secreta al usuario
 * Repetir la solicitud con do-while hasta acertar(1234)
 * Mostrar Mensaje de exito
 */
using System;

class Principal
{
  public static void Main(string[] args)
  {
    string entradaContrasenia;
    do{
      Console.WriteLine("Introduzca la contraseña secreta: ");
      entradaContrasenia = Console.ReadLine();
    }while(entradaContrasenia != "1234");
    Console.WriteLine("Acceso al Sistema!");
  }
}
