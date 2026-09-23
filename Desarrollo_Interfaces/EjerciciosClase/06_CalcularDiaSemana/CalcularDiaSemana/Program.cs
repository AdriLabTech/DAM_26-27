using System;

static class Program
{
    static void Main(string[] args)
    {
       string [] diasSemana = { "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo" };

        Console.WriteLine("Ingrese un número del 1 al 7 para obtener el día de la semana correspondiente:");
        int numeroDia = int.Parse(Console.ReadLine());

        if (numeroDia >= 1 && numeroDia <= 7)
        {
            Console.WriteLine($"El día de la semana es: {diasSemana[numeroDia - 1]}");
        }
        else
        {
            Console.WriteLine("Número inválido. Por favor, ingrese un número del 1 al 7.");
        }
    }
}
