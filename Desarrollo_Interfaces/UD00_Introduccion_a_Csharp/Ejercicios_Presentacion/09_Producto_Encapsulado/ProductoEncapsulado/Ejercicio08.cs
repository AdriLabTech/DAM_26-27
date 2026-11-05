// Ejercicio 08: Clase Producto Encapsulada
/* Clase Producto con el atributo precio privado y un
 * metodo de acceso (SetPrecio) que valida que el valor
 * no sea negativo antes de asignarlo.
 */

using System;

class Producto
{
  private decimal precio;

  // Solo asigna si el valor es valido (>= 0); devuelve si lo ha hecho
  public bool SetPrecio(decimal p)
  {
    if (p >= 0)
    {
      precio = p;
      return true;
    }
    return false;
  }

  public decimal GetPrecio()
  {
    return precio;
  }
}

class Principal
{
  static void Main()
  {
    Producto producto = new Producto();

    Console.WriteLine($"SetPrecio(25,50) -> {producto.SetPrecio(25.50m)}");
    Console.WriteLine($"Precio actual: {producto.GetPrecio():C}");

    Console.WriteLine($"SetPrecio(-5) -> {producto.SetPrecio(-5m)}");
    Console.WriteLine($"Precio actual (sin cambios): {producto.GetPrecio():C}");
  }
}
