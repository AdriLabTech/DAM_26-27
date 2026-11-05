using System.Windows;

namespace AgendaAmpliada;

public partial class MainWindow : Window
{
    // Une las piezas: crea el repositorio, los servicios y el ViewModel y los asigna como DataContext.
    // Desde aquí todo funciona con Binding (en proyectos grandes se usaría inyección de dependencias).
    public MainWindow()
    {
        InitializeComponent();
        DataContext = new MainViewModel(
            new ContactoRepositorio(),
            new DialogoService(),
            new TemaService());
    }
}
