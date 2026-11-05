using System.Collections.ObjectModel;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace ConversorTemperaturas;

// ViewModel: no conoce ningún control de la vista
public partial class ConversorViewModel : ObservableObject
{
    // Genera la propiedad pública Celsius. NotifyPropertyChangedFor avisa de que
    // Fahrenheit también cambia cada vez que cambia Celsius.
    [ObservableProperty]
    [NotifyPropertyChangedFor(nameof(Fahrenheit))]
    private double _celsius;

    // Propiedad calculada: °F = °C × 9/5 + 32
    public double Fahrenheit => Celsius * 9 / 5 + 32;

    // Valores anotados con el comando Anotar
    public ObservableCollection<string> Anotaciones { get; } = [];

    // Genera AnotarCommand: guarda el valor actual en la colección
    [RelayCommand]
    private void Anotar()
    {
        Anotaciones.Add($"{Celsius:0.##} °C = {Fahrenheit:0.##} °F");
    }
}
