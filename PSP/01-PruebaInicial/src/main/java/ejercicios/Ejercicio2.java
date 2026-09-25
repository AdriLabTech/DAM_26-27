package ejercicios;

import ejercicios.model.Alumno;
import ejercicios.model.Asignatura;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/** Menú de consola para gestionar alumnos y sus notas. */
public class Ejercicio2 {
    private static final Scanner SCANNER = new Scanner(System.in);

    public static void main(String[] args) {
        List<Alumno> listaAlumnos = new ArrayList<>();
        int opcionUsuario;

        do {
            mostrarOpciones();
            opcionUsuario = pedirNumeroUsuario();

            switch (opcionUsuario) {
                case 1 -> agregarAlumno(listaAlumnos);
                case 2 -> eliminarAlumno(listaAlumnos);
                case 3 -> mostrarAlumnos(listaAlumnos);
                case 4 -> mostrarPromedio(listaAlumnos);
                default -> {
                    System.out.println("Saliendo...");
                    opcionUsuario = 0;
                }
            }
        } while (opcionUsuario != 0);
    }

    public static int pedirNumeroUsuario() {
        System.out.println("Introduce el numero de la opcion: ");
        return SCANNER.nextInt();
    }

    public static void mostrarOpciones() {
        System.out.println("1.- Agregar Alumno");
        System.out.println("2.- Borrar Alumno");
        System.out.println("3.- Mostrar todos los Alumnos");
        System.out.println("4.- Calcular promedio de Alumno");
        System.out.println("0.- Salir");
    }

    private static void agregarAlumno(List<Alumno> listaAlumnos) {
        List<Asignatura> notasAlumno = new ArrayList<>();

        System.out.println("Introduce el Nombre del Alumno: ");
        String nombreAlumno = SCANNER.next();

        System.out.println("Introduce la edad del Alumno: ");
        int edadAlumno = SCANNER.nextInt();

        Alumno alumno = new Alumno(nombreAlumno, edadAlumno);

        System.out.println("Cuantas notas quieres agregar?");
        int cantidadNotas = SCANNER.nextInt();

        for (int i = 0; i < cantidadNotas; i++) {
            System.out.println("Introduce el nombre de la Asignatura: ");
            String nombreAsignatura = SCANNER.next();

            System.out.println("Que nota ha sacada en " + nombreAsignatura + "?: ");
            float notaAsignatura = SCANNER.nextFloat();

            notasAlumno.add(new Asignatura(nombreAsignatura, notaAsignatura));
        }

        alumno.setNotas(notasAlumno);
        listaAlumnos.add(alumno);
    }

    private static void eliminarAlumno(List<Alumno> listaAlumnos) {
        System.out.println("Inserta el nombre del Alumno que quieras borrar: ");
        String nombreAlumnoABorrar = SCANNER.next();
        String nombreNormalizado = nombreAlumnoABorrar.toLowerCase();
        int longitudListaSinModificar = listaAlumnos.size();

        for (Alumno alumno : listaAlumnos) {
            if (coincideNombre(alumno.getNombre(), nombreNormalizado)) {
                System.out.println("Alumno borrado!!!");
                listaAlumnos.remove(alumno);
                break;
            }
        }

        int longitudListaModificada = listaAlumnos.size();
        if (longitudListaModificada == longitudListaSinModificar) {
            System.out.println("No se ha encontrado ningun alumno con ese nombre");
        }
    }

    private static void mostrarAlumnos(List<Alumno> listaAlumnos) {
        for (Alumno alumno : listaAlumnos) {
            System.out.println(alumno.toString());
        }
    }

    private static void mostrarPromedio(List<Alumno> listaAlumnos) {
        System.out.println("Introduce el nombre del Alumno que quieras calcular su promedio: ");
        String nombreAlumnoABuscar = SCANNER.next();
        String nombreNormalizado = nombreAlumnoABuscar.toLowerCase();

        for (Alumno alumno : listaAlumnos) {
            if (coincideNombre(alumno.getNombre(), nombreNormalizado)) {
                System.out.println("Alumno encontrado: ");
                System.out.println(alumno.toString());
                System.out.println("Promedio del Alumno " + alumno.getNombre() + ": " + alumno.calcularPromedio());
                break;
            }
        }

        // El mensaje final forma parte del comportamiento original del ejercicio.
        System.out.println("Alumno no encontrado...");
    }

    private static boolean coincideNombre(String nombreAlumno, String nombreNormalizado) {
        return nombreAlumno.toLowerCase().equals(nombreNormalizado);
    }
}
