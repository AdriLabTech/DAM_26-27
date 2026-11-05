using System.ComponentModel.DataAnnotations;
using CommunityToolkit.Mvvm.ComponentModel;

namespace AgendaAmpliada;

// Modelo: guarda los datos de un contacto. ObservableValidator avisa de cambios y de errores;
// las reglas se escriben como atributos.
public partial class Contacto : ObservableValidator
{
    [ObservableProperty]
    [NotifyDataErrorInfo]
    [Required(ErrorMessage = "El nombre es obligatorio")]
    private string _nombre = "";

    [ObservableProperty]
    [NotifyDataErrorInfo]
    [EmailAddress(ErrorMessage = "Correo no válido")]
    private string _email = "";

    [ObservableProperty]
    private string _telefono = "";

    // Campo añadido en la actividad 2.9
    [ObservableProperty]
    private string _ciudad = "";

    // Mensajes de error para mostrarlos bajo cada campo (validación visible)
    public string ErrorNombre => PrimerError(nameof(Nombre));
    public string ErrorEmail => PrimerError(nameof(Email));

    public Contacto()
    {
        ErrorsChanged += (_, _) =>
        {
            OnPropertyChanged(nameof(ErrorNombre));
            OnPropertyChanged(nameof(ErrorEmail));
        };
    }

    private string PrimerError(string propiedad) =>
        GetErrors(propiedad).FirstOrDefault()?.ErrorMessage ?? "";

    // Valida todas las reglas a la vez (el diálogo lo usa al pulsar Aceptar)
    public bool Validar()
    {
        ValidateAllProperties();
        return !HasErrors;
    }

    // Copia los datos de otro contacto (para editar sobre una copia y poder cancelar)
    public void CopiarDesde(Contacto otro)
    {
        Nombre = otro.Nombre;
        Email = otro.Email;
        Telefono = otro.Telefono;
        Ciudad = otro.Ciudad;
    }
}

// Forma en que se guarda en disco (sin lógica de validación)
public record ContactoDto(string Nombre, string Email, string Telefono, string Ciudad = "");
