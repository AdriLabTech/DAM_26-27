package ejercicios;

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args){
        // Varificador de Palindromos
        Scanner s = new Scanner(System.in);
        System.out.println("Introduce una frase: ");
        String entrada = s.nextLine();
        //Expresion regular para obtener todos los caracteres especiales y eliminarlos
        String frase = entrada.replace(" ", "").toLowerCase().replaceAll("\\p{P}", "");

        boolean isPalindromo = verificarPalindromo(frase);
        System.out.println(isPalindromo ? "La cadena es palindroma" : "La cadena NO es palindroma");
    }

    private static boolean verificarPalindromo(String frase){
        String cadenaInvertida = new StringBuilder(frase).reverse().toString();

        return frase.equals(cadenaInvertida);
    }
}
