package ejercicios;

import ejercicios.model.Alumno;
import ejercicios.model.Asignatura;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ejercicio2 {
    private static Scanner s = new Scanner(System.in);

    public static void main (String[] args){
        //Gestion de Estudiantes
        List<Alumno> listaAlumnos = new ArrayList<>();
        List<Asignatura> notasAlumno;
        int opcionUsuario = 1;
        while (opcionUsuario != 0){
            mostrarOpciones();
            opcionUsuario = pedirNumeroUsuario();
            switch (opcionUsuario){
                case 1 -> {
                    //Borrar el Alumno
                    notasAlumno = new ArrayList<>();

                    //Agregar Alumno
                    System.out.println("Introduce el Nombre del Alumno: ");
                    String nombreAlunmno = s.next();
                    System.out.println("Introduce la edad del Alumno: ");
                    int edadAlumno = s.nextInt();
                    Alumno alumno = new Alumno(nombreAlunmno, edadAlumno);

                    System.out.println("Cuantas notas quieres agregar?");
                    int cantidadNotas = s.nextInt();
                    for(int i = 0;i < cantidadNotas; i++){
                        System.out.println("Introduce el nombre de la Asignatura: ");
                        String nombreAsig = s.next();
                        System.out.println("Que nota ha sacada en " + nombreAsig + "?: ");
                        float notaAsig = s.nextFloat();
                        notasAlumno.add(new Asignatura(nombreAsig, notaAsig));
                    }
                    alumno.setNotas(notasAlumno);

                    listaAlumnos.add(alumno);
                }

                case 2 -> {
                    //Eliminar Alumno
                    System.out.println("Inserta el nombre del Alumno que quieras borrar: ");
                    String alumnoABorrar = s.next();
                    int longitudListaSinModificar = listaAlumnos.size();
                    for(Alumno a : listaAlumnos){
                        if (a.getNombre().toLowerCase().equals(alumnoABorrar.toLowerCase())){
                            System.out.println("Alumno borrado!!!");
                            listaAlumnos.remove(a);
                            break;
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

                case 4 -> {
                    System.out.println("Introduce el nombre del Alumno que quieras calcular su promedio: ");
                    String nombreAlumnoABuscar = s.next();
                    for(Alumno a : listaAlumnos){
                        if(a.getNombre().toLowerCase().equals(nombreAlumnoABuscar.toLowerCase())){
                            System.out.println("Alumno encontrado: ");
                            System.out.println(a.toString());
                            System.out.println("Promedio del Alumno " + a.getNombre() + ": "+ a.calcularPromedio());
                            break;
                        }
                    }
                    System.out.println("Alumno no encontrado...");
                }

                default -> {
                    System.out.println("Saliendo...");
                    opcionUsuario = 0;
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
