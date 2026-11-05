using System.Windows;

namespace AgendaAmpliada;

// Cambiar el tema es un detalle de la vista: el ViewModel solo pide «alterna»
public interface ITemaService
{
    bool EsOscuro { get; }
    void Alternar();
}

public class TemaService : ITemaService
{
    public bool EsOscuro => Application.Current.ThemeMode == ThemeMode.Dark;

    public void Alternar() =>
        Application.Current.ThemeMode = EsOscuro ? ThemeMode.Light : ThemeMode.Dark;
}
