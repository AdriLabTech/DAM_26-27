package lownoise.dev.ejercicio2;

import java.util.Scanner;

// Proceso hijo
public class Ejercicio2 {

    private static final String fin = "*";
    private static final int edadMin = 1;
    private static final int edadMax = 99;

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int leidos = 0;
        String nombreMayor = null;
        String nombreMenor = null;
        int edadMayor = Integer.MIN_VALUE;
        int edadMenor = Integer.MAX_VALUE;

        boolean entradaAgotada = false;
        while (true) {
            System.out.println((leidos + 1) + "- Introduce datos de alumnos:");
            System.out.println();

            String[] alumno = leerAlumno(s);
            if (alumno == null) { // fin de la entrada sin "*"
                entradaAgotada = true;
                break;
            }
            if (alumno[0].equals(fin)) {
                break;
            }

            String nombre = alumno[0];
            int edad = Integer.parseInt(alumno[1]);
            System.out.println("Datos introducidos: " + nombre + ", " + edad);
            System.out.println();

            leidos++;
            if (edad > edadMayor) {
                edadMayor = edad;
                nombreMayor = nombre;
            }
            if (edad < edadMenor) {
                edadMenor = edad;
                nombreMenor = nombre;
            }
        }

        if (entradaAgotada) {
            System.err.println("Error: la entrada terminó sin el carácter '" + fin + "'.");
        }
        System.out.println("Fin del proceso de lectura...");
        System.out.println();
        System.out.println("Datos leídos: " + leidos);
        System.out.println();
        if (leidos > 0) {
            System.out.println("Alumno con más edad: " + nombreMayor);
            System.out.println();
            System.out.println("Alumno con menos edad: " + nombreMenor);
        } else {
            System.out.println("No se ha leído ningún alumno.");
        }
    }

    /**
     * Lee un alumno completo. Devuelve {nombre, edad}, {"*", null} si se
     * introdujo el centinela, o null si la entrada se agotó.
     */
    private static String[] leerAlumno(Scanner s) {
        while (true) {
            System.out.println("Escribe un nombre:");
            if (!s.hasNextLine()) {
                return null;
            }
            String linea = s.nextLine().trim();
            System.out.println(linea);

            if (linea.isEmpty()) {
                System.out.println();
                System.out.println("Incorrecto, escríbelo de nuevo:");
                System.out.println();
                continue;
            }
            if (linea.equals(fin)) {
                return new String[] {fin, null};
            }

            // Formato de fichero: "NOMBRE EDAD" en una sola línea.
            int ultimoEspacio = linea.lastIndexOf(' ');
            if (ultimoEspacio > 0 && esEntero(linea.substring(ultimoEspacio + 1))) {
                String nombre = linea.substring(0, ultimoEspacio).trim();
                String edad = linea.substring(ultimoEspacio + 1);
                if (edadValida(edad)) {
                    return new String[] {nombre, edad};
                }
                // Registro de una línea con edad fuera de rango: se descarta entero.
                System.out.println();
                System.out.println("Incorrecto, debe estar entre " + edadMin + " y " + edadMax
                        + ". Se descarta el registro.");
                System.out.println();
                continue;
            }

            String edad = leerEdad(s);
            if (edad == null) {
                return null;
            }
            return new String[] {linea, edad};
        }
    }

    /** Pide la edad hasta que sea un entero entre 1 y 99. Devuelve null si la entrada se agota. */
    private static String leerEdad(Scanner s) {
        while (true) {
            System.out.println();
            System.out.println("Introduce la edad entre " + edadMin + " y " + edadMax + ":");
            if (!s.hasNextLine()) {
                return null;
            }
            String texto = s.nextLine().trim();
            System.out.println(texto);
            System.out.println();

            if (!esEntero(texto)) {
                System.out.println("Incorrecto, debe ser un número entero");
            } else if (!edadValida(texto)) {
                System.out.println("Incorrecto, debe estar entre " + edadMin + " y " + edadMax);
            } else {
                return texto;
            }
        }
    }

    private static boolean esEntero(String texto) {
        try {
            Integer.parseInt(texto);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private static boolean edadValida(String texto) {
        int edad = Integer.parseInt(texto);
        return edad >= edadMin && edad <= edadMax;
    }
}
