using System.Collections.ObjectModel;
using System.ComponentModel;
using System.IO;
using System.Text;
using System.Windows.Data;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace AgendaAmpliada;

public partial class MainViewModel : ObservableObject
{
    private readonly ContactoRepositorio _repositorio;
    private readonly IDialogoService _dialogos;
    private readonly ITemaService _tema;

    // Estado: todos los datos, la vista filtrada y la fila elegida
    public ObservableCollection<Contacto> Contactos { get; }
    public ICollectionView Vista { get; }

    [ObservableProperty]
    private string _filtro = "";

    [ObservableProperty]
    [NotifyCanExecuteChangedFor(nameof(EditarCommand), nameof(EliminarCommand))]
    private Contacto? _seleccionado;

    [ObservableProperty]
    private string _estado = "";

    public string TextoTema => _tema.EsOscuro ? "Tema claro" : "Tema oscuro";

    public MainViewModel(ContactoRepositorio repositorio, IDialogoService dialogos, ITemaService tema)
    {
        _repositorio = repositorio;
        _dialogos = dialogos;
        _tema = tema;

        Contactos = new ObservableCollection<Contacto>(_repositorio.Cargar());
        Vista = CollectionViewSource.GetDefaultView(Contactos);
        Vista.Filter = Coincide;
        Vista.SortDescriptions.Add(new SortDescription(nameof(Contacto.Nombre), ListSortDirection.Ascending));

        ActualizarEstado();
    }

    // Buscar mientras se escribe: al cambiar el filtro se refresca la vista
    partial void OnFiltroChanged(string value)
    {
        Vista.Refresh();
        ActualizarEstado();
    }

    private bool Coincide(object o) =>
        o is Contacto c &&
        (c.Nombre.Contains(Filtro, StringComparison.CurrentCultureIgnoreCase) ||
         c.Ciudad.Contains(Filtro, StringComparison.CurrentCultureIgnoreCase));

    [RelayCommand]
    private void Nuevo()
    {
        var nuevo = new Contacto();
        if (_dialogos.Editar(nuevo) == true)
        {
            Contactos.Add(nuevo);
            Guardar();
        }
    }

    [RelayCommand(CanExecute = nameof(HaySeleccion))]
    private void Editar()
    {
        // Se edita una copia: si se cancela, el contacto original no cambia
        var copia = new Contacto();
        copia.CopiarDesde(Seleccionado!);

        if (_dialogos.Editar(copia) == true)
        {
            Seleccionado!.CopiarDesde(copia);
            Vista.Refresh();
            Guardar();
        }
    }

    // Actividad 2.9 (3): confirma antes de eliminar, mediante el servicio de diálogos
    [RelayCommand(CanExecute = nameof(HaySeleccion))]
    private void Eliminar()
    {
        if (!_dialogos.Confirmar($"¿Eliminar a {Seleccionado!.Nombre}?", "Eliminar contacto")) return;

        Contactos.Remove(Seleccionado!);
        Guardar();
    }

    // Actividad 2.9 (2): exportar a CSV con comando + SaveFileDialog (a través del servicio)
    [RelayCommand(CanExecute = nameof(HayContactos))]
    private void ExportarCsv()
    {
        var ruta = _dialogos.PedirRutaCsv("contactos.csv");
        if (ruta is null) return;

        File.WriteAllText(ruta, ContactoCsv.Generar(Contactos), new UTF8Encoding(encoderShouldEmitUTF8Identifier: true));
        Estado = $"Exportados {Contactos.Count} contactos a {Path.GetFileName(ruta)}";
    }

    // Actividad 2.9 (4): alternar entre tema claro y oscuro
    [RelayCommand]
    private void CambiarTema()
    {
        _tema.Alternar();
        OnPropertyChanged(nameof(TextoTema));
    }

    private bool HaySeleccion() => Seleccionado is not null;
    private bool HayContactos() => Contactos.Count > 0;

    private void Guardar()
    {
        _repositorio.Guardar(Contactos);
        ExportarCsvCommand.NotifyCanExecuteChanged();
        ActualizarEstado();
    }

    private void ActualizarEstado()
    {
        int visibles = Vista.Cast<object>().Count();
        Estado = string.IsNullOrEmpty(Filtro)
            ? $"{Contactos.Count} contactos"
            : $"{visibles} de {Contactos.Count} contactos";
        ExportarCsvCommand.NotifyCanExecuteChanged();
    }
}
