using System.Collections.ObjectModel;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace EstiloFormulario;

public partial class FormularioViewModel : ObservableObject
{
    public IReadOnlyList<string> Ciudades { get; } =
        ["Córdoba", "Sevilla", "Málaga", "Granada", "Cádiz", "Huelva", "Almería", "Jaén"];

    [ObservableProperty]
    private string _nombre = "";

    [ObservableProperty]
    private string _correo = "";

    [ObservableProperty]
    private string _ciudad = "Córdoba";

    [ObservableProperty]
    [NotifyCanExecuteChangedFor(nameof(GuardarCommand))]
    private bool _aceptado;

    [ObservableProperty]
    private string _resumen = "";

    // Lista de la actividad 2.7, mostrada con un DataTemplate
    public ObservableCollection<Anotacion> Anotaciones { get; } =
    [
        new(0, 32),
        new(21.5, 70.7),
        new(100, 212),
        new(-40, -40),
    ];

    [RelayCommand(CanExecute = nameof(PuedeGuardar))]
    private void Guardar()
    {
        Resumen = $"{Nombre} ({Correo}) · {Ciudad}";
    }

    private bool PuedeGuardar() => Aceptado;
}
