namespace AgendaAmpliada;

// El ViewModel pide «edita esto» o «confirma esto» sin conocer ninguna ventana.
// Así se puede probar sin abrir diálogos.
public interface IDialogoService
{
    // Abre el diálogo de edición; true si el usuario acepta
    bool? Editar(Contacto contacto);

    // Pregunta sí/no antes de una acción destructiva
    bool Confirmar(string mensaje, string titulo);

    // Pide dónde guardar el CSV; null si se cancela
    string? PedirRutaCsv(string nombreSugerido);
}
