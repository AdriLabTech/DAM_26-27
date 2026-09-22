using System;
using System.Collections.Generic;
using System.Text;

namespace HolaMundo
{
    internal class Coche
    {
        private string marca;
        private string modelo;

        private int velocidad;


        public Coche() { }

        public Coche(string marca, string modelo)
        {
            this.marca = marca;
            this.modelo = modelo;
            this.velocidad = 0;
        }

        public string Modelo{
            get { return this.modelo; }
            set { this.modelo = value; }
        }

        public string Marca
        {
            get { return this.marca; }
            set { this.marca = value; }
        }

        public int Velocidad
        {
            get { return this.velocidad; }
            set { this.velocidad = value; }
        }

        public void Acelerar(int incremento)
        {
            velocidad += incremento;
            Console.WriteLine($"El coche {marca} {modelo} ha acelerado a {velocidad} km/h.");
        }

        public void Frenar(int decremento)
        {
            velocidad -= decremento;
            if (velocidad < 0) velocidad = 0;
            Console.WriteLine($"El coche {marca} {modelo} ha frenado a {velocidad} km/h.");
        }

        public void MostrarVelocidad()
        {
            Console.WriteLine($"La velocidad actual del coche es: {velocidad} km/h");
        }
    }
}
