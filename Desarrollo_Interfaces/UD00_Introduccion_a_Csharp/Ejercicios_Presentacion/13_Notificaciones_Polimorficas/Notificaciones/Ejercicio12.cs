// Ejercicio 12 (3/3): Uso polimorfico en Main()
/* Paso 3: una List<INotificable> con Email, SMS y Push se
 * recorre enviando la misma alerta. Main no conoce la
 * clase concreta de cada elemento (desacoplamiento).
 */

using System;
using System.Collections.Generic;

class Principal
{
  static void Main()
  {
    var lista = new List<INotificable>
    {
      new EmailNotificador { Destinatario = "a@a.com" },
      new SmsNotificador { Destinatario = "600112233" },
      new PushNotificador { Destinatario = "Usr_99" }
    };

    foreach (var n in lista)
      n.Enviar("Alerta!");
  }
}
