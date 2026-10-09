package dev.lownoise.cadenas;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * Lanza varias instancias (mínimo 10) de {@link Cadenas} como procesos hijos con
 * ProcessBuilder, lee la salida de cada una con getInputStream() y la muestra
 * prefijada con el número de instancia. Al final espera a todas con waitFor() y
 * comprueba su código de terminación.
 */
public class Generador {

    private static final int MIN_INSTANCIAS = 10;

    public static void main(String[] args) {
        try {
            BufferedReader teclado = new BufferedReader(new InputStreamReader(System.in));
            int instancias = leerEntero(teclado, "Número de instancias (mínimo " + MIN_INSTANCIAS + "): ", MIN_INSTANCIAS);
            int cadenas = leerEntero(teclado, "Cadenas por instancia (mínimo 1): ", 1);

            // Se lanzan todos los procesos primero, para que se ejecuten de forma concurrente.
            List<Process> procesos = new ArrayList<>();
            for (int i = 0; i < instancias; i++) {
                procesos.add(lanzarCadenas(cadenas));
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
            System.out.println("Finalizado: " + (instancias - fallos) + "/" + instancias + " instancias correctas.");
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    /** Pide un entero por teclado hasta que sea válido y no menor que minimo. */
    private static int leerEntero(BufferedReader teclado, String mensaje, int minimo) throws IOException {
        while (true) {
            System.out.print(mensaje);
            String linea = teclado.readLine();
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

    /** Arranca un proceso hijo que ejecuta Cadenas con el classpath actual. */
    private static Process lanzarCadenas(int cadenas) throws IOException {
        String classpath = System.getProperty("java.class.path");
        ProcessBuilder pb = new ProcessBuilder("java", "-cp", classpath, "dev.lownoise.cadenas.Cadenas", String.valueOf(cadenas));
        pb.redirectErrorStream(true); // stderr llega junto a stdout por getInputStream()
        return pb.start();
    }

    /** Lee línea a línea la salida del proceso hijo y la imprime con un prefijo. */
    private static void mostrarSalida(Process proceso, String prefijo) throws IOException {
        BufferedReader salida = new BufferedReader(new InputStreamReader(proceso.getInputStream()));
        String linea;
        while ((linea = salida.readLine()) != null) {
            System.out.println(prefijo + linea);
        }
        salida.close();
    }
}
