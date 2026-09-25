package ejercicios;

import java.util.Scanner;

/** Comprueba si una frase es un palíndromo después de limpiar algunos caracteres. */
public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduce una frase: ");
        String entrada = scanner.nextLine();

        // La limpieza conserva el tratamiento original de espacios y signos de puntuación.
        String frase = entrada.replace(" ", "").toLowerCase().replaceAll("\\p{P}", "");

        boolean esPalindromo = verificarPalindromo(frase);
        System.out.println(esPalindromo ? "La cadena es palindroma" : "La cadena NO es palindroma");
    }

    private static boolean verificarPalindromo(String frase) {
        int indiceIzquierdo = 0;
        int indiceDerecho = frase.length() - 1;

        // Dos índices evitan crear una copia invertida de la frase.
        while (indiceIzquierdo < indiceDerecho) {
            if (frase.charAt(indiceIzquierdo) != frase.charAt(indiceDerecho)) {
                return false;
            }

            indiceIzquierdo++;
            indiceDerecho--;
        }

        return true;
    }
}
