// Ejercicio 12 (2/3): Clases SmsNotificador y PushNotificador
/* Paso 2: mas implementaciones del contrato INotificable.
 * Cada clase adapta el envio a su canal.
 */

using System;

public class SmsNotificador : INotificable
{
  public string Destinatario { get; set; } = "";

  public void Enviar(string msj) =>
    Console.WriteLine($"SMS a {Destinatario}: {msj}");
}

public class PushNotificador : INotificable
{
  public string Destinatario { get; set; } = "";

  public void Enviar(string msj) =>
    Console.WriteLine($"Push a {Destinatario}: {msj}");
}
