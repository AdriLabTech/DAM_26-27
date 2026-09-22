using System;
using System.Collections.Generic;
using System.Text;

namespace HolaMundo
{
    internal class Transporte
    {
        private string capacidad;
        private string ruta;

        public Transporte() { }

        public Transporte(string capacidad, string ruta)
        {
            this.capacidad = capacidad;
            this.ruta = ruta;
        }

        public string Capacidad
        {
            get { return this.capacidad; }
            set { this.capacidad = value; }
        }

        public string Ruta
        {
            get { return this.ruta; }
            set { this.ruta = value; }
        }


        public void AbrirPuertas()
        {
            Console.WriteLine("Abriendo puertas...");
        }

        public void CerrarPuertas()
        {
            Console.WriteLine("Cerrando puertas...");
        }

    }
}
