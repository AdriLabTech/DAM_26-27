package dev.lownoise.cadenas;

/**
 * Genera N cadenas alfabéticas de longitud aleatoria (1..20) y las escribe
 * en la salida estándar, una por línea. N se recibe como argumento.
 * Termina con código 0 si todo va bien y con 1 si el argumento no es válido.
 */
public class Cadenas {

    static final int LONGITUD_MAXIMA = 20;
    static final String ALFABETO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Uso: Cadenas <numeroDeCadenas>");
            System.exit(1);
        }

        int cantidad = 0;
        try {
            cantidad = Integer.parseInt(args[0].trim());
        } catch (NumberFormatException e) {
            System.err.println("Error: '" + args[0] + "' no es un número entero válido.");
            System.exit(1);
        }
        if (cantidad < 1) {
            System.err.println("Error: el número de cadenas debe ser al menos 1.");
            System.exit(1);
        }

        for (int i = 0; i < cantidad; i++) {
            System.out.println(generarCadena());
        }
    }

    /** Devuelve una cadena de letras con longitud aleatoria entre 1 y LONGITUD_MAXIMA. */
    static String generarCadena() {
        int longitud = 1 + (int) (Math.random() * LONGITUD_MAXIMA);
        String cadena = "";
        for (int i = 0; i < longitud; i++) {
            cadena += ALFABETO.charAt((int) (Math.random() * ALFABETO.length()));
        }
        return cadena;
    }
}
