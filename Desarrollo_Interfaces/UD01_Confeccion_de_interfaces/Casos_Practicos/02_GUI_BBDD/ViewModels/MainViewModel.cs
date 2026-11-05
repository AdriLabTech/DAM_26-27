using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Windows.Data;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using gui_bbdd.Data;
using gui_bbdd.Models;

namespace gui_bbdd.ViewModels;

public class MainViewModel : ObservableObject
{
    private readonly HabitoRepositorio _repositorio;

    private string _nuevoNombre = "";
    private string _nuevaDescripcion = "";
    private string _filtro = "";
    private Habito? _seleccionado;
    private string _estado = "";

    public ObservableCollection<Habito> Habitos { get; }

    public ICollectionView Vista { get; }

    public IRelayCommand AnadirCommand { get; }
    public IRelayCommand AlternarHoyCommand { get; }
    public IRelayCommand EliminarCommand { get; }

    public string NuevoNombre
    {
        get => _nuevoNombre;
        set
        {
            if (SetProperty(ref _nuevoNombre, value))
                AnadirCommand.NotifyCanExecuteChanged();
        }
    }

    public string NuevaDescripcion
    {
        get => _nuevaDescripcion;
        set => SetProperty(ref _nuevaDescripcion, value);
    }

    public string Filtro
    {
        get => _filtro;
        set
        {
            if (SetProperty(ref _filtro, value))
                Vista.Refresh();
        }
    }

    public Habito? Seleccionado
    {
        get => _seleccionado;
        set
        {
            if (!SetProperty(ref _seleccionado, value))
                return;

            AlternarHoyCommand.NotifyCanExecuteChanged();
            EliminarCommand.NotifyCanExecuteChanged();
        }
    }

    public string Estado
    {
        get => _estado;
        set => SetProperty(ref _estado, value);
    }

    public MainViewModel(HabitoRepositorio repositorio)
    {
        _repositorio = repositorio;

        AnadirCommand = new RelayCommand(Anadir, PuedeAnadir);
        AlternarHoyCommand = new RelayCommand(AlternarHoy, HaySeleccion);
        EliminarCommand = new RelayCommand(Eliminar, HaySeleccion);

        Habitos = new ObservableCollection<Habito>(repositorio.Cargar());
        Vista = CollectionViewSource.GetDefaultView(Habitos);
        Vista.Filter = o => o is Habito h &&
            h.Nombre.Contains(Filtro, StringComparison.CurrentCultureIgnoreCase);
        ActualizarEstado();
    }

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

    private void AlternarHoy()
    {
        _repositorio.AlternarHoy(Seleccionado!);
        ActualizarEstado();
    }

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
