using System.Windows;
using System.Windows.Input;
using System.Windows.Controls;

namespace EventosRaton;

public partial class MainWindow : Window
{

    private int tamanio = 20;
    public MainWindow()
    {
        InitializeComponent();
    }

    private void Lienzo_MouseMove(object sender, MouseEventArgs e)
    {
        Point puntero = e.GetPosition(lienzo);

        Canvas.SetLeft(punto, puntero.X - tamanio / 2);
        Canvas.SetTop(punto, puntero.Y - tamanio / 2);
        txtEstado.Text = $"{puntero.X:0}, {puntero.Y:0}";
    }

    private void Lienzo_MouseDown(object sender, MouseButtonEventArgs e)
    {
        
        if (e.ClickCount == 2)
        {
            txtEstado.Text = "Click Izquierdo";
        } else if (e.ChangedButton == MouseButton.Left)
        {
            txtEstado.Text = "DobleClick";
        }
    }

    private void Lienzo_MouseWheel(object sender, MouseWheelEventArgs e)
    {
        
    }

    private void Window_KeyDown(object sender, KeyEventArgs e)
    {
        if (e.Key == Key.W)
        {
            Canvas.SetLeft(punto, punto.ActualHeight * 2);
            Canvas.SetTop(punto, punto.ActualWidth * 2);
            txtEstado.Text = "W pulsada";
        }
    }

}