package lownoise.dev.ejercicio1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

// Proceso padre
public class Ejecuta_Ejercicio1 {
    public static final int longitudArrays = 10;
    public static void main(String[] args){
        int[] arrayA = generarArrayAleatorio(longitudArrays);
        int[] arrayB = generarArrayAleatorio(longitudArrays);

        mostrarArray(arrayA, "Array A");
        mostrarArray(arrayB, "Array B");

        List<String> listaArgumentosProceso1 = crearListaArgumentos(arrayA, arrayB, 0, longitudArrays / 2);
        List<String> listaArgumentosProceso2 = crearListaArgumentos(arrayA, arrayB, longitudArrays / 2, longitudArrays);

        try {
            Process proceso1 = ejecutarProceso(listaArgumentosProceso1);
            Process proceso2 = ejecutarProceso(listaArgumentosProceso2);

            int[] numerosObtenidosProceso1 = leerResultados(proceso1, longitudArrays / 2);
            int[] numerosObtenidosProceso2 = leerResultados(proceso2, longitudArrays / 2);

            int codigoEstadoProceso1 = proceso1.waitFor();
            int codigoEstadoProceso2 = proceso2.waitFor();

            if (codigoEstadoProceso1 == 0 && codigoEstadoProceso2 == 0) {
                int[] todosLosNumeros = combinarArrays(numerosObtenidosProceso1, numerosObtenidosProceso2);

                if(verificarResultados(arrayA, arrayB, todosLosNumeros)){
                    mostrarArray(todosLosNumeros, "Array Combinado");
                }else{
                    System.err.println("[ERROR]: hubo un fallo matematico");
                }
            }
        } catch (Exception e) {
            System.err.println("[ERROR]: error al leer los resultados de los procesos");
        }
    }

    private static boolean verificarResultados(int[] array1, int[] array2, int[] arrayResultados){
        for (int i = 0; i < arrayResultados.length; i ++){
            if(array1[i] * array2[i] != arrayResultados[i]){
                return false;
            }
        }
        return true;
    }

    private static void mostrarArray(int[] array, String msg){
        System.out.println("------- " + msg + " -------");
        for (int i = 0; i < array.length; i ++){
            System.out.println(array[i]);
        }
        System.out.println("---------------------");
    }

    private static int[] combinarArrays(int[] array1, int[] array2) {
        int[] arrayCombinado = new int[array1.length + array2.length];
        for (int i = 0; i < arrayCombinado.length; i ++){
            if (i < array1.length) {
                arrayCombinado[i] = array1[i];
            }else{
                arrayCombinado[i] = array2[i - array1.length];
            }
        }

        return arrayCombinado;
    }

    private static int[] leerResultados(Process proceso, int cantidadResutados) throws IOException {
        int[] resultados = new int[cantidadResutados];

        try (BufferedReader br = new BufferedReader(new InputStreamReader(proceso.getInputStream()))){

            for (int i = 0; i < cantidadResutados; i++) {
                String cadena = br.readLine();
                if(cadena == null){
                    System.err.println("[ERROR]: la linea que se intenta leer es nula");
                    throw new IOException();
                }else {
                    try {
                        int dato = Integer.parseInt(cadena);
                        resultados[i] = dato;
                    } catch (NumberFormatException e) {
                        System.err.println("[ERROR]: El dato convertido no es un numero entero");
                        throw new NumberFormatException();
                    }
                }
            }
        }

        return resultados;
    }

    private static Process ejecutarProceso(List<String> argumentos) {
        try {
            ProcessBuilder pb = new ProcessBuilder(argumentos);
            Process procesoHijo = pb.start();
            return procesoHijo;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static List<String> crearListaArgumentos(int[] arrayA, int[] arrayB, int posInicio, int posFinal){
        // Argumentos base SIN incluir los elementos del array
        List<String> listaArgumentos = new ArrayList<>();
        listaArgumentos.add("java");
        listaArgumentos.add("-cp");
        listaArgumentos.add(System.getProperty("java.class.path"));
        listaArgumentos.add("lownoise.dev.ejercicio1.Ejercicio1");

        // Agregamos el conjunto de argumentos del arrayA desde el inicio hasta el final
        // (proceso1 -> desde 0 hasta la mitad de la longitud final
        // (proceso2 -> desde la mitad de la longitud hasta la longitud final
        for (int i = posInicio; i < posFinal; i++){
            listaArgumentos.add(String.valueOf(arrayA[i]));
        }

        // Agregamos el conjunto de argumentos del arrayB desde el inicio hasta el final
        // (proceso1 -> desde 0 hasta la mitad de la longitud final
        // (proceso2 -> desde la mitad de la longitud hasta la longitud final
        for (int i = posInicio; i < posFinal; i++){
            listaArgumentos.add(String.valueOf(arrayB[i]));
        }

        return listaArgumentos;
    }

    private static int[] generarArrayAleatorio(int longitudArray){
        int min = 1, max = 100;
        int [] array = new int[longitudArray];
        for (int i = 0; i < array.length; i++){
            array[i] = (int) (Math.random() * max) + min;
        }
        return array;
    }
}
