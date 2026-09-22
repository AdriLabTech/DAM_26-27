using HolaMundo;
using System;
class HolaNombre
{
    static void Main(string[] args)
    {

        //Ejercicio1();

        //Ejercicio2();

        //Ejercicio3();

        //Ejercicio4();

        //TestingLoop("Hola Mundo!");

        Console.WriteLine("Introduce el primer numero: ");
        int numero1 = int.Parse(Console.ReadLine());
        Console.WriteLine("Introduce el segundo numero: ");
        int numero2 = int.Parse(Console.ReadLine());

        int resultado = Suma(numero1, numero2);
        Console.WriteLine("El resultado de la suma es: " + resultado);

        Coche coche1 = new Coche("Toyota", "Corolla");
        coche1.Acelerar(20);

        coche1.MostrarVelocidad();
    }

    static int Suma(int num1, int num2)
    {
        return num1 + num2;
    }

    static void TestingLoop(string cadena)
    {
        foreach (char c in cadena)
        {
            Console.Write(c);
            Thread.Sleep(200);
        }
    }

    static void Ejercicio4()
    {
        Console.WriteLine("Introduce un numero: ");
        int numero = int.Parse(Console.ReadLine());

        Console.WriteLine(numero % 2 == 0 ? "El numero es par" : "El numero es impar");
    }

    static void Ejercicio3()
    {
        Console.WriteLine("Introduce tu edad: ");
        int edad = int.Parse(Console.ReadLine());

        if(edad >= 18)
        {
            Console.WriteLine("Eres mayor de edad");
        }
        else
        {
            Console.WriteLine("Eres menor de edad");
        }

    }

    static void Ejercicio2()
    {
        Console.WriteLine("Introduce tu edad; ");
        int edad = int.Parse(Console.ReadLine());
        Console.WriteLine("Tu edad dentro de 15 años sera: " + (edad + 15));
    }

    static void Ejercicio1()
    {
        Console.Write("Ingresa tu nombre: ");
        string nombre = Console.ReadLine();

        Console.Write("Ingresa tu edad: ");

        int edad = int.Parse(Console.ReadLine());

        Console.Write("Ingresa tu estatura: ");

        double altura = double.Parse(Console.ReadLine());

        Console.WriteLine("Nombre de Usuario: " + nombre);
        Console.WriteLine("Edad de Usuario: " + edad);
        Console.WriteLine("Estatura de Usuario: " + altura);
    }
}
