namespace EstiloFormulario;

// Elemento de la lista de la actividad 2.7 (conversión anotada)
public record Anotacion(double Celsius, double Fahrenheit)
{
    public string Resumen => $"{Celsius:0.##} °C = {Fahrenheit:0.##} °F";
}
