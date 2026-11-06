namespace gui_bbdd.Models
{
    public class Habito
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public string Descripcion { get; set; }
        public bool HechoHoy { get; set; }
        public int Racha { get; set; }
        public int Total { get; set; }

        public Habito(int id, string nombre, string descripcion)
        {
            Id = id;
            Nombre = nombre;
            Descripcion = descripcion;
        }
    }
}
