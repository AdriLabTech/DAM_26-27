using System.Windows;
using gui_bbdd.Data;
using gui_bbdd.ViewModels;

namespace gui_bbdd;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        DataContext = new MainViewModel(new HabitoRepositorio(HabitoRepositorio.RutaPorDefecto()));
    }
}
