package ejercicios;

import java.util.Scanner;

public class Ejercicio1 {
    private static Scanner s = new Scanner(System.in);
    //Calculadora Basica
    public static void main(String[] args){
        System.out.println("Operacion a realizar: (s/r/m/d): ");
        String operacion = s.next();

        float numero1 = pedirNumeroUsuario();
        float numero2 = pedirNumeroUsuario();

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

    public static float sumaNumeros(float numero1, float numero2){
        return numero1 + numero2;
    }

    public static float restaNumeros(float numero1, float numero2){
        return numero1 - numero2;
    }

    public static float multiplicacionNumeros(float numero1, float numero2){
        int resultado = 0;
        for(int i = 0; i < numero2; i++){
            resultado += numero1;
        }
        return resultado;
    }

    public static float divisionNumeros(float numero1, float numero2){
        float cociente = 0;
        try{
            while (numero1 >= numero2) {
                numero1 -= numero2;
                cociente++;
            }

            return cociente;
        } catch (Exception e){
            System.out.println("No se puede dividir entre 0!!!");
        }

        return cociente;

    }

    public static float pedirNumeroUsuario(){
        System.out.println("Introduce un numero: ");
        return s.nextFloat();
    }
}
