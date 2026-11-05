using System.IO;
using System.Text.Json;

namespace AgendaAmpliada;

// Guarda y carga los contactos en un fichero JSON. El ViewModel no sabe cómo se guardan.
public class ContactoRepositorio
{
    private static readonly JsonSerializerOptions Opciones = new() { WriteIndented = true };

    private readonly string _carpeta;
    private readonly string _ruta;

    public ContactoRepositorio(string? carpeta = null)
    {
        _carpeta = carpeta ?? Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "AgendaAmpliada");
        _ruta = Path.Combine(_carpeta, "contactos.json");
    }

    public void Guardar(IEnumerable<Contacto> contactos)
    {
        Directory.CreateDirectory(_carpeta);
        var datos = contactos.Select(c => new ContactoDto(c.Nombre, c.Email, c.Telefono, c.Ciudad));
        File.WriteAllText(_ruta, JsonSerializer.Serialize(datos, Opciones));
    }

    public List<Contacto> Cargar()
    {
        if (!File.Exists(_ruta)) return [];

        var datos = JsonSerializer.Deserialize<List<ContactoDto>>(File.ReadAllText(_ruta)) ?? [];
        return datos
            .Select(d => new Contacto { Nombre = d.Nombre, Email = d.Email, Telefono = d.Telefono, Ciudad = d.Ciudad })
            .ToList();
    }
}
