using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Windows.Data;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using gui_bbdd.Data;
using gui_bbdd.Models;

namespace gui_bbdd.ViewModels;

public partial class MainViewModel : ObservableObject
{
    private readonly HabitoRepositorio _repositorio;

    public ObservableCollection<Habito> Habitos { get; }

    public ICollectionView Vista { get; }

    [ObservableProperty]
    [NotifyCanExecuteChangedFor(nameof(AnadirCommand))]
    private string _nuevoNombre = "";

    [ObservableProperty]
    private string _nuevaDescripcion = "";

    [ObservableProperty]
    private string _filtro = "";

    [ObservableProperty]
    [NotifyCanExecuteChangedFor(nameof(AlternarHoyCommand))]
    [NotifyCanExecuteChangedFor(nameof(EliminarCommand))]
    private Habito? _seleccionado;

    [ObservableProperty]
    private string _estado = "";

    public MainViewModel(HabitoRepositorio repositorio)
    {
        _repositorio = repositorio;
        Habitos = new ObservableCollection<Habito>(repositorio.Cargar());
        Vista = CollectionViewSource.GetDefaultView(Habitos);
        Vista.Filter = Coincide;
        ActualizarEstado();
    }

    partial void OnFiltroChanged(string value) => Vista.Refresh();

    private bool Coincide(object o) =>
        o is Habito h && h.Nombre.Contains(Filtro, StringComparison.CurrentCultureIgnoreCase);

    [RelayCommand(CanExecute = nameof(PuedeAnadir))]
    private void Anadir()
    {
        var habito = _repositorio.Insertar(NuevoNombre.Trim(), NuevaDescripcion.Trim());
        Habitos.Add(habito);
        Seleccionado = habito;
        NuevoNombre = "";
        NuevaDescripcion = "";
        ActualizarEstado();
    }

    private bool PuedeAnadir() => !string.IsNullOrWhiteSpace(NuevoNombre);

    [RelayCommand(CanExecute = nameof(HaySeleccion))]
    private void AlternarHoy()
    {
        _repositorio.AlternarHoy(Seleccionado!);
        ActualizarEstado();
    }

    [RelayCommand(CanExecute = nameof(HaySeleccion))]
    private void Eliminar()
    {
        var habito = Seleccionado!;
        _repositorio.Eliminar(habito.Id);
        Habitos.Remove(habito);
        ActualizarEstado();
    }

    private bool HaySeleccion() => Seleccionado is not null;

    private void ActualizarEstado() =>
        Estado = $"{Habitos.Count} hábitos · {Habitos.Count(h => h.HechoHoy)} completados hoy";
}
