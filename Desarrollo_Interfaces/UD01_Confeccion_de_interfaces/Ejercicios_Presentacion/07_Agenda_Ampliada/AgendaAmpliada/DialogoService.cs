using System.Windows;
using Microsoft.Win32;

namespace AgendaAmpliada;

public class DialogoService : IDialogoService
{
    private static Window? Principal => Application.Current?.MainWindow;

    public bool? Editar(Contacto contacto)
    {
        var dialogo = new ContactoDialog
        {
            DataContext = contacto,
            Owner = Principal
        };
        return dialogo.ShowDialog();
    }

    public bool Confirmar(string mensaje, string titulo) =>
        MessageBox.Show(Principal!, mensaje, titulo, MessageBoxButton.YesNo, MessageBoxImage.Question)
            == MessageBoxResult.Yes;

    public string? PedirRutaCsv(string nombreSugerido)
    {
        var dialogo = new SaveFileDialog
        {
            Title = "Exportar contactos",
            FileName = nombreSugerido,
            DefaultExt = ".csv",
            Filter = "CSV (*.csv)|*.csv|Todos los archivos (*.*)|*.*"
        };
        return dialogo.ShowDialog(Principal) == true ? dialogo.FileName : null;
    }
}
