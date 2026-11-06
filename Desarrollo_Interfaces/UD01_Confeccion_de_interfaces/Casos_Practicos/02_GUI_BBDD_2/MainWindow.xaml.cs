using System;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Input;
using gui_bbdd.Data;
using gui_bbdd.Models;

namespace gui_bbdd
{
    public partial class MainWindow : Window
    {
        private HabitoRepositorio _repositorio;
        private ObservableCollection<Habito> _habitos;
        private ICollectionView _vista;

        public MainWindow()
        {
            InitializeComponent();

            _repositorio = new HabitoRepositorio(HabitoRepositorio.RutaPorDefecto());
            _habitos = new ObservableCollection<Habito>(_repositorio.Cargar());

            _vista = CollectionViewSource.GetDefaultView(_habitos);
            _vista.Filter = new Predicate<object>(FiltrarHabito);
            dgHabitos.ItemsSource = _vista;
            ActualizarEstado();
        }

        // Solo se muestran los hábitos cuyo nombre contiene el texto del buscador.
        private bool FiltrarHabito(object objeto)
        {
            Habito habito = (Habito)objeto;
            return habito.Nombre.IndexOf(txtBuscar.Text, StringComparison.CurrentCultureIgnoreCase) >= 0;
        }

        private void txtNombre_TextChanged(object sender, TextChangedEventArgs e)
        {
            btnAnadir.IsEnabled = txtNombre.Text.Trim().Length > 0;
        }

        private void txtBuscar_TextChanged(object sender, TextChangedEventArgs e)
        {
            _vista.Refresh();
        }

        private void dgHabitos_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            bool haySeleccion = dgHabitos.SelectedItem != null;
            btnHechoHoy.IsEnabled = haySeleccion;
            btnEliminar.IsEnabled = haySeleccion;
        }

        private void btnAnadir_Click(object sender, RoutedEventArgs e)
        {
            Habito habito = _repositorio.Insertar(txtNombre.Text.Trim(), txtDescripcion.Text.Trim());
            _habitos.Add(habito);
            dgHabitos.SelectedItem = habito;
            txtNombre.Text = "";
            txtDescripcion.Text = "";
            ActualizarEstado();
        }

        private void btnHechoHoy_Click(object sender, RoutedEventArgs e)
        {
            Habito habito = (Habito)dgHabitos.SelectedItem;
            _repositorio.AlternarHoy(habito);
            _vista.Refresh();
            ActualizarEstado();
        }

        private void btnEliminar_Click(object sender, RoutedEventArgs e)
        {
            Habito habito = (Habito)dgHabitos.SelectedItem;
            _repositorio.Eliminar(habito.Id);
            _habitos.Remove(habito);
            ActualizarEstado();
        }

        private void Fila_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            DataGridRow fila = (DataGridRow)sender;
            Habito habito = fila.Item as Habito;
            if (habito == null)
            {
                return;
            }

            DetalleWindow ventana = new DetalleWindow(habito, _repositorio.Historial(habito.Id));
            ventana.Owner = this;
            ventana.ShowDialog();
            e.Handled = true;
        }

        private void ActualizarEstado()
        {
            int completados = 0;
            foreach (Habito habito in _habitos)
            {
                if (habito.HechoHoy)
                {
                    completados++;
                }
            }

            lblEstado.Content = string.Format("{0} hábitos · {1} completados hoy", _habitos.Count, completados);
        }
    }
}
