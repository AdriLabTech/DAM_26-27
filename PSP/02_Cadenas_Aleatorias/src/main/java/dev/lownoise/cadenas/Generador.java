package dev.lownoise.cadenas;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * Lanza varias instancias (mínimo 10) de Cadenas como procesos hijos con
 * ProcessBuilder, lee la salida de cada una con getInputStream() y la muestra
 * prefijada con el número de instancia. Al final espera a todas con waitFor() y
 * comprueba su código de terminación.
 */
public class Generador {

    private static final int instanciasMinimas = 10;

    public static void main(String[] args) {
        try {
            BufferedReader lectorDatos = new BufferedReader(new InputStreamReader(System.in));
            int numeroInstancias = leerEntero(lectorDatos, "Número de instancias (mínimo " + instanciasMinimas + "): ", instanciasMinimas);
            int numeroCadenas = leerEntero(lectorDatos, "Cadenas por instancia (mínimo 1): ", 1);

            // Se lanzan todos los procesos primero, para que se ejecuten de forma concurrente.
            List<Process> procesos = new ArrayList<>();
            for (int i = 0; i < numeroInstancias; i++) {
                procesos.add(lanzarCadenas(numeroCadenas));
            }

            // Después se recoge la salida de cada uno y se espera a que termine.
            int fallos = 0;
            for (int i = 0; i < procesos.size(); i++) {
                Process proceso = procesos.get(i);
                mostrarSalida(proceso, "[Instancia " + (i + 1) + "] ");
                int codigo = proceso.waitFor();
                if (codigo != 0) {
                    fallos++;
                    System.out.println("La instancia " + (i + 1) + " terminó con código " + codigo);
                }
            }
            System.out.println("Finalizado: " + (numeroInstancias - fallos) + "/" + numeroInstancias + " instancias correctas.");
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    // Pide un entero por escaner hasta que sea válido y no menor que minimo
    private static int leerEntero(BufferedReader escaner, String mensaje, int minimo) throws IOException {
        while (true) {
            System.out.print(mensaje);
            String linea = escaner.readLine();
            if (linea == null) {
                throw new IOException("no hay más entrada disponible");
            }
            try {
                int valor = Integer.parseInt(linea.trim());
                if (valor >= minimo) {
                    return valor;
                }
                System.out.println("Error: el valor debe ser como mínimo " + minimo + ".");
            } catch (NumberFormatException e) {
                System.out.println("Error: '" + linea + "' no es un número entero válido.");
            }
        }
    }

    // Arranca un proceso hijo que ejecuta Cadenas con el classpath actual
    private static Process lanzarCadenas(int cadenas) throws IOException {
        String classpath = System.getProperty("java.class.path");
        // Ejecutamos un proceso llamando a la Clase Cadenas junto al argumento (numero de cadenas, un numero entero)
        ProcessBuilder pb = new ProcessBuilder("java", "-cp", classpath, "dev.lownoise.cadenas.Cadenas", String.valueOf(cadenas));
        pb.redirectErrorStream(true);
        return pb.start();
    }

    // Lee línea a línea la salida del proceso hijo y la imprime con un prefijo
    private static void mostrarSalida(Process proceso, String prefijo) throws IOException {
        BufferedReader salida = new BufferedReader(new InputStreamReader(proceso.getInputStream()));
        String linea;
        System.out.println(prefijo);
        System.out.println("-".repeat(21));
        while ((linea = salida.readLine()) != null) {
            System.out.println(linea);
        }
        System.out.println("-".repeat(21));
        salida.close();
    }
}
