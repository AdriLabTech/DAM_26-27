package lownoise.dev.ejercicio2;

import java.io.File;
import java.io.IOException;

// Proceso padre
public class Ejecuta_Ejercicio2 {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Uso: java Ejecuta_Ejercicio2 <fichero1> [fichero2 ...]");
            System.out.println("Debes indicar al menos un fichero de entrada. Fin del programa.");
            return;
        }

        int ejecuciones = 0;
        for (String nombre : args) {
            File entrada = new File(nombre);
            if (!entrada.isFile()) {
                System.out.println("El fichero '" + nombre + "' no existe. Se omite.");
                continue;
            }
            try {
                ejecutar(entrada);
                ejecuciones++;
            } catch (IOException | InterruptedException e) {
                System.out.println("Error al ejecutar Ejercicio2 con '" + nombre + "': " + e.getMessage());
                if (e instanceof InterruptedException) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        }

        System.out.println("Ejercicio2 se ha ejecutado " + ejecuciones + " vez/veces.");
        System.out.println("Fin del proceso.");
    }

    private static void ejecutar(File entrada) throws IOException, InterruptedException {
        File carpeta = entrada.getAbsoluteFile().getParentFile();
        File salida = new File(carpeta, "S" + entrada.getName());
        File error = new File(carpeta, "E" + entrada.getName());

        String java = System.getProperty("java.home") + "/bin/java";
        String classpath = System.getProperty("java.class.path");
        ProcessBuilder pb = new ProcessBuilder(java, "-cp", classpath, "Ejercicio2");
        pb.redirectInput(entrada);
        pb.redirectOutput(salida);
        pb.redirectError(error);

        int codigo = pb.start().waitFor();
        System.out.println("'" + entrada.getName() + "' -> " + salida.getName() + ", " + error.getName()
                + " (código de salida " + codigo + ")");
    }
}
