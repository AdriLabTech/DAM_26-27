// Ejercicio 12 (1/3): Interfaz y clase EmailNotificador
/* Sistema de notificaciones polimorfico con interfaces.
 * Paso 1: interfaz INotificable (Destinatario y Enviar())
 * e implementacion EmailNotificador.
 */

using System;

public interface INotificable
{
  string Destinatario { get; set; }
  void Enviar(string mensaje);
}

public class EmailNotificador : INotificable
{
  public string Destinatario { get; set; } = "";

  public void Enviar(string msj) =>
    Console.WriteLine($"Email a {Destinatario}: {msj}");
}
