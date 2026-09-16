package ejercicios.model;

public class Asignatura {
    private String nombre;
    private int nota;

    public Asignatura(){}

    public Asignatura(String nombre, int nota){
        this.nombre = nombre;
        this.nota = nota;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getNota() {
        return nota;
    }

    public void setNota(int nota) {
        this.nota = nota;
    }

    @Override
    public String toString() {
        return "Asignatura{" +
                "nombre='" + nombre + '\'' +
                ", nota=" + nota +
                '}';
    }
}
