using System;
using System.Collections.Generic;
using System.Windows;
using gui_bbdd.Models;

namespace gui_bbdd
{
    public partial class DetalleWindow : Window
    {
        public DetalleWindow(Habito habito, List<DateTime> fechas)
        {
            InitializeComponent();

            Title = "Detalle: " + habito.Nombre;
            txtId.Text = habito.Id.ToString();
            txtNombre.Text = habito.Nombre;
            txtDescripcion.Text = habito.Descripcion;
            chkHechoHoy.IsChecked = habito.HechoHoy;
            txtRacha.Text = habito.Racha + " días seguidos";
            txtTotal.Text = habito.Total + " registros";

            foreach (DateTime fecha in fechas)
            {
                lstHistorial.Items.Add(fecha.ToString("dddd, d 'de' MMMM 'de' yyyy"));
            }

            if (fechas.Count == 0)
            {
                txtResumen.Text = "Todavía no hay registros de este hábito.";
            }
            else
            {
                txtResumen.Text = "Último registro: " + lstHistorial.Items[0];
            }
        }
    }
}
