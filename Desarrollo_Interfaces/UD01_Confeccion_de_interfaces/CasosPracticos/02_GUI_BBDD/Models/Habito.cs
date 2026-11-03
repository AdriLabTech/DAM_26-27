using CommunityToolkit.Mvvm.ComponentModel;

namespace gui_bbdd.Models;

public class Habito : ObservableObject
{
    private bool _hechoHoy;
    private int _racha;
    private int _total;

    public int Id { get; init; }

    public string Nombre { get; init; } = "";

    public string Descripcion { get; init; } = "";

    public bool HechoHoy
    {
        get => _hechoHoy;
        set => SetProperty(ref _hechoHoy, value);
    }

    public int Racha
    {
        get => _racha;
        set => SetProperty(ref _racha, value);
    }

    public int Total
    {
        get => _total;
        set => SetProperty(ref _total, value);
    }
}
