package ejercicios.model;

import java.util.ArrayList;
import java.util.List;

public class Alumno {
    private String nombre;
    private int edad;
    private List<Asignatura> notas = new ArrayList<>();

    public Alumno(){}

    public Alumno(String nombre, int edad, List<Asignatura> listaNotas){
        this.edad = edad;
        this.nombre = nombre;
        this.notas = notas;
    }

    public Alumno(String nombre){
        this.nombre = nombre;
    }

    public List<Asignatura> getNotas() {
        return notas;
    }

    public void setNotas(List<Asignatura> notas) {
        this.notas = notas;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Alumno{" +
                "nombre='" + nombre + '\'' +
                ", edad=" + edad +
                ", notas=" + notas +
                '}';
    }

    public float calcularPromedio(){
        float sumaNotas = 0;
        for(Asignatura a : notas){
            sumaNotas += a.getNota();
        }

        return sumaNotas / notas.size();
    }
}
