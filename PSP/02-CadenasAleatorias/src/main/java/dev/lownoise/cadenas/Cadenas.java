package dev.lownoise.cadenas;

/**
 * Genera N cadenas alfabéticas de longitud aleatoria (1..20) y las escribe
 * en la salida estándar, una por línea. N se recibe como argumento.
 * Termina con código 0 si todo va bien y con 1 si el argumento no es válido.
 */
public class Cadenas {

    static final int longitudMaxima = 20;
    static final String alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static void main(String[] args) {
        // En caso de que la cantidad de argumentos no sea 1, se cierra la ejecuccion
        if (args.length != 1) {
            System.err.println("Error. Usa: Cadenas <numeroDeCadenas>");
            System.exit(1);
        }

        int cantidad = 0;
        try {
            // Verificamos que el argumento pasado sea un numero (y nos salimos)
            cantidad = Integer.parseInt(args[0].trim());
        } catch (NumberFormatException e) {
            System.err.println("Error: '" + args[0] + "' no es un número entero válido.");
            System.exit(1);
        }
        // Verificamos que la cantidad de cadenas sea minimo 1
        if (cantidad < 1) {
            System.err.println("Error: el número de cadenas debe ser al menos 1.");
            System.exit(1);
        }

        for (int i = 0; i < cantidad; i++) {
            System.out.println(generarCadena());
        }
    }

    // Devuelve una cadena de letras con longitud aleatoria entre 1 y 20
    static String generarCadena() {
        int longitud = 1 + (int) (Math.random() * longitudMaxima);
        String cadena = "";
        for (int i = 0; i < longitud; i++) {
            cadena += alfabeto.charAt((int) (Math.random() * alfabeto.length()));
        }
        return cadena;
    }
}
