using System.Windows;
using System.Windows.Controls;
using System.Text.RegularExpressions;

namespace Calculadora;

public partial class MainWindow : Window
{

    private bool seHaModificado = false;
    public MainWindow()
    {
        InitializeComponent();
    }
    private void AgregarContenido(int numero)
    {
        if (seHaModificado)
        {
            ResultadoFinal.Text += numero.ToString();
        }
        else
        {
            ResultadoFinal.Text = "";
            ResultadoFinal.Text += numero.ToString();
            seHaModificado = true;
        }
    }

    private void AgregarNumero(object sender, RoutedEventArgs e)
    {
        if (sender is Button b)
        {
            AgregarContenido(int.Parse(b.Content.ToString()));
        }
    }

    private void LimpiarPantalla(object sender, RoutedEventArgs e)
    {
        ResultadoFinal.Text = "0";
        seHaModificado = false;
    }

    private void CalcularResultado(object sender, RoutedEventArgs e)
    {
        bool algunError = false;
        string operacionCompleta = ResultadoFinal.Text;

        string[] elementos = Regex.Split(operacionCompleta, @"([+\-*/])"); // pares son numeros e impares signos
        var lista_numeros = new System.Collections.Generic.List<int>();
        var lista_signos = new System.Collections.Generic.List<string>();

        for (int j = 0; j < elementos.Length; j++)
        {
            string elemento = elementos[j].Trim();

            if (j % 2 == 0) // Numeros
            {
                if (!int.TryParse(elemento, out int valor))
                {
                    algunError = true;
                    break;
                }
                lista_numeros.Add(valor);
            }
            else // Signos
            {
                lista_signos.Add(elemento);
            }
        }

        int[] numeros = lista_numeros.ToArray();
        string[] signos = lista_signos.ToArray();
        string resultado = "0";

        algunError = algunError || signos.Length != numeros.Length - 1;

        int i = 0;
        while( i < signos.Length && !algunError)
        {
            int numero1 = numeros[i];
            int numero2 = numeros[i + 1];
            switch (signos[i])
            {
                case "+":
                    numeros[i + 1] = numero1 + numero2;
                    break;
                case "-":
                    numeros[i + 1] = numero1 - numero2;
                    break;
                case "*":
                    numeros[i + 1] = numero1 * numero2;
                    break;
                case "/":
                    if(numero2 != 0)
                    {
                        numeros[i + 1] = numero1 / numero2;
                    }
                    else
                    {
                        algunError = true;
                    }
                    break;
            }
            resultado = numeros[i + 1].ToString();
            i++;
        }
        
        if (!algunError)
        {
            ResultadoFinal.Text = resultado;
        }
        else
        {
            ResultadoFinal.FontSize = 60;
            ResultadoFinal.Text = "SINTAX ERROR";
        }


    }

    private void AgregarSigno(object sender, RoutedEventArgs e)
    {
        if(sender is Button b)
        {
            ResultadoFinal.Text += b.Content.ToString();
        }
    }
}