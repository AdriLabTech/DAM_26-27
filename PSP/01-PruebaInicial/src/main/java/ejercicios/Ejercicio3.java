package ejercicios;

import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

/** Juego del ahorcado con selección aleatoria de palabra. */
public class Ejercicio3 {
    private static final Set<Character> LETRAS_DISPONIBLES = new HashSet<>(List.of(
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'));
    private static final List<String> PALABRAS = List.of("pez", "loco", "prueba");
    private static final Scanner SCANNER = new Scanner(System.in);

    public static void main(String[] args) {
        StringBuilder palabraParaAdivinar = new StringBuilder(seleccionarPalabraAleatoria());
        StringBuilder reconstruccionPalabra = new StringBuilder("_".repeat(palabraParaAdivinar.length()));

        System.out.println("Palabra a Adivinar: ");
        System.out.println(reconstruccionPalabra);

        boolean palabraAcertada = false;
        int intentos = 0;

        // El límite original permite siete intentos fallidos, no seis.
        while (!palabraAcertada && intentos <= 6) {
            char letra = pedirLetraUsuario();

            for (int i = 0; i < palabraParaAdivinar.length(); i++) {
                char letraPalabra = palabraParaAdivinar.charAt(i);
                if (letraPalabra == letra) {
                    System.out.println("Letra correcta!!!");
                    reconstruccionPalabra.setCharAt(i, letra);
                }
            }

            if (reconstruccionPalabra.compareTo(palabraParaAdivinar) == 0) {
                palabraAcertada = true;
            } else {
                System.out.println("Resultado actual: " + reconstruccionPalabra);
            }

            if (!palabraAcertada) {
                intentos++;
            }
        }

        if (palabraAcertada) {
            System.out.println("Palabra correcta!!!");
        } else {
            System.out.println("La palabra no ha sido acertada...");
        }
    }

    private static char pedirLetraUsuario() {
        char letra;
        boolean letraDisponible;

        do {
            System.out.println("Introduce una letra: ");
            String entradaUsuario = SCANNER.next();
            letra = entradaUsuario.charAt(0);
            letraDisponible = LETRAS_DISPONIBLES.remove(letra);

            if (!letraDisponible) {
                System.out.println("Letra ya introducida anteriormente o caracter no valido...");
            }
        } while (!letraDisponible);

        return letra;
    }

    private static String seleccionarPalabraAleatoria() {
        int indiceAleatorio = (int) Math.round(Math.random() * (PALABRAS.size() - 1));
        return PALABRAS.get(indiceAleatorio);
    }
}
