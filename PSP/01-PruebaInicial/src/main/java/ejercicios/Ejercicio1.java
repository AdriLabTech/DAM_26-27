package ejercicios;

import java.util.Scanner;

public class Ejercicio1 {
    private static Scanner s = new Scanner(System.in);
    //Calculadora Basica
    public static void main(String[] args){
        System.out.println("Operacion a realizar: (s/r/m/d): ");
        String operacion = s.next();

        int numero1 = pedirNumeroUsuario();
        int numero2 = pedirNumeroUsuario();

        switch (operacion){
            case "s", "suma" -> {
                System.out.println(sumaNumeros(numero1, numero2));
            }
            case "r", "resta" -> {
                System.out.println(restaNumeros(numero1, numero2));
            }
            case "m", "nultiplicacion" -> {
                System.out.println(multiplicacionNumeros(numero1, numero2));
            }
            case "d", "division" -> {
                System.out.println(divisionNumeros(numero1, numero2));
            }
        }

    }

    public static int sumaNumeros(int numero1, int numero2){
        return numero1 + numero2;
    }

    public static int restaNumeros(int numero1, int numero2){
        return numero1 - numero2;
    }

    public static int multiplicacionNumeros(int numero1, int numero2){
        int resultado = 0;
        for(int i = 0; i < numero2; i++){
            resultado += numero1;
        }
        return resultado;
    }

    public static int divisionNumeros(int numero1, int numero2){
        int cociente = 0;
        while (numero1 >= numero2) {
            numero1 -= numero2;
            cociente++;
        }

        return cociente;
    }

    public static int pedirNumeroUsuario(){
        System.out.println("Introduce un numero: ");
        return s.nextInt();
    }
}
