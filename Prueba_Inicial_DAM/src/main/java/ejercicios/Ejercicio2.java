package ejercicios;

import ejercicios.model.Alumno;
import ejercicios.model.Asignatura;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Ejercicio2 {
    private static Scanner s = new Scanner(System.in);

    public static void main (String[] args){
        //Gestion de Estudiantes
        List<Alumno> listaAlumnos = new ArrayList<>();
        mostrarOpciones();
        int opcionUsuario = pedirNumeroUsuario();
        while (opcionUsuario != 0){
            switch (opcionUsuario){
                case 1 -> {
                    //Agregar Alumno
                    System.out.println("Introduce el Nombre del Alumno: ");
                    String nombreAlunmno = s.next();
                    System.out.println("Introduce la edad del Alumno: ");
                    int edadAlumno = s.nextInt();
                    System.out.println("Cuantas notas quieres agregat?");
                    int cantidadNotas = s.nextInt();
                    List<Asignatura> notasAlumno = List.of();
                    for(int i = 0;i < cantidadNotas; i++){
                        System.out.println("Introduce el nombre de la Asignatura: ");
                        String nombreAsig = s.next();
                        System.out.println("Que nota ha sacada en " + nombreAsig + "?: ");
                        int notaAsig = s.nextInt();
                        notasAlumno.add(new Asignatura(nombreAsig, notaAsig));
                    }
                    listaAlumnos.add(new Alumno(nombreAlunmno, edadAlumno, notasAlumno));
                }

                case 2 -> {
                    //Eliminar Alumno
                    System.out.println("Inserta el nombre del Alumno que quieras borrar: ");
                    String alumnoABorrar = s.next();
                    int longitudListaSinModificar = listaAlumnos.size();
                    for(Alumno a : listaAlumnos){
                        if (a.getNombre().toLowerCase().equals(alumnoABorrar.toLowerCase())){
                            System.out.println("Alumno encontrado!!!");
                            listaAlumnos.remove(a);
                        }
                    }
                    int longitudListaModificada = listaAlumnos.size();
                    if(longitudListaModificada == longitudListaSinModificar){
                        System.out.println("No se ha encontrado ningun alumno con ese nombre");
                    }
                }

                case 3 -> {
                    //Mostrar todos los Alumnos
                    for(Alumno a : listaAlumnos){
                        System.out.println(a.toString());
                    }
                }
            }
        }
    }

    public static int pedirNumeroUsuario(){
        System.out.println("Introduce el numero de la opcion: ");
        return s.nextInt();
    }

    public static void mostrarOpciones(){
        System.out.println("1.- Agregar Alumno");
        System.out.println("2.- Borrar Alumno");
        System.out.println("3.- Mostrar todos los Alumnos");
        System.out.println("4.- Calcular promedio de Alumno");
        System.out.println("0.- Salir");
    }
}
