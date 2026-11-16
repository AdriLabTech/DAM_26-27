package utils;

import java.util.Scanner;

public class Utils {
    private static final Scanner sc = new Scanner(System.in);

    public static int mostrarOpciones(){
        System.out.println("0.- Salir");
        System.out.println("1.- Mostrar Todos los Buses");
        System.out.println("2.- Buscar Bus (id)");
        System.out.println("3.- Añadir Bus");
        System.out.println("4.- Editar Bus");

        return sc.nextInt();
    }

    public static String pedirCadenaAlUsuario(String msg){
        System.out.println(msg);
        return sc.next();
    }
}
