class Program
{
    static void Main(string[] args)
    {

        Ejercicio_Hola_C();

        Ejercicio_Datos_Personales();


    }

    static void Ejercicio_Datos_Personales()
    {
        Console.WriteLine("Como te llamas?: ");
        string nombre = Console.ReadLine();
        Console.WriteLine("Cual es tu edad?: ");
        int edad = int.Parse(Console.ReadLine());
        Console.WriteLine("Cuanto mides?: ");
        double altura = double.Parse(Console.ReadLine());
        Console.WriteLine("Eres estudiante? (s/n): ");
        bool esEstudiante = Console.ReadLine().ToLower() == "s";

        string statusEstudante = esEstudiante ? "soy estudiante" : "no soy estudiante";

        Console.WriteLine($"Me llamo {nombre}, tengo {edad} años, mido {altura}m  y {statusEstudante}");
    }

    static void Ejercicio_Hola_C()
    {
        string nombreMostrar = "Carlos";

        Console.WriteLine($"Hola, soy {nombreMostrar}");
        Console.WriteLine("Estoy aprendiendo C#");
    }
}