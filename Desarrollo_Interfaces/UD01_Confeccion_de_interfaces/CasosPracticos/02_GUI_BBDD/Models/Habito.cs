using CommunityToolkit.Mvvm.ComponentModel;

namespace gui_bbdd.Models;

public partial class Habito : ObservableObject
{
    public int Id { get; init; }

    public string Nombre { get; init; } = "";

    public string Descripcion { get; init; } = "";

    [ObservableProperty]
    private bool _hechoHoy;

    [ObservableProperty]
    private int _racha;

    [ObservableProperty]
    private int _total;
}
