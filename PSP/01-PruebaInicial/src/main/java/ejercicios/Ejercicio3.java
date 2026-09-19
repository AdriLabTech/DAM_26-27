package ejercicios;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ejercicio3 {
    private static List<Character> letras = List.of('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
    private static List<Character> letrasSinUtilizar = new ArrayList<>(letras);
    private static Scanner s = new Scanner(System.in);
    public static void main (String[] args){

        // Juego del ahoracado
        StringBuilder palabraParaAdivinar = new StringBuilder(seleccionarPalabraAleatoria());
        StringBuilder reconstruccionPalabra = new StringBuilder("_".repeat(palabraParaAdivinar.length()));
        // Imprimir las letras censuradas
        System.out.println("Palabra a Adivinar: ");
        System.out.println(reconstruccionPalabra);
        boolean palabraAcertada = false;
        int intentos = 0;

        while(!palabraAcertada && intentos <= 6){
            char letra = pedirLetraUsuario();
            for(int i = 0; i < palabraParaAdivinar.length(); i ++){
                char caracterPalabraAdivinarIdx = palabraParaAdivinar.charAt(i);
                if(caracterPalabraAdivinarIdx == letra){
                    System.out.println("Letra correcta!!!");
                    reconstruccionPalabra.setCharAt(i, letra);
                }
            }

            if(reconstruccionPalabra.compareTo(palabraParaAdivinar) == 0){
                palabraAcertada = true;
            }else {
                System.out.println("Resultado actual: " + reconstruccionPalabra);
            }

            if(!palabraAcertada){
                intentos ++;
            }

        }

        if(palabraAcertada){
            System.out.println("Palabra correcta!!!");
        }else{
            System.out.println("La palabra no ha sido acertada...");
        }
    }

    private static char pedirLetraUsuario(){
        char caracter = ' ';
        boolean letraYaUsada = true;

        while(letraYaUsada) {
            System.out.println("Introduce una letra: ");
            String entradaUsuario = s.next();
            caracter = entradaUsuario.charAt(0);
            for (Character c : letrasSinUtilizar) {
                if (c == caracter) {
                    letrasSinUtilizar.remove(c);
                    letraYaUsada = false;
                    break;
                }
            }

            if (letraYaUsada) {
                System.out.println("Letra ya introducida anteriormente o caracter no valido...");
            }
        }
        return caracter;
    }

    private static String seleccionarPalabraAleatoria(){
        String [] palabras = {"pez", "loco", "prueba"};
        int randomIdx = (int) Math.round(Math.random()* ((palabras.length - 1)));
        return palabras[randomIdx];
    }
}
