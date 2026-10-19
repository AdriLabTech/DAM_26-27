package lownoise.dev.ejercicio1;

// Proceso hijo
public class Ejercicio1 {
    // main recibe argumentos de esta forma: ["2", "3", "4", "5"]
    public static void main(String[] args){
        // Comprobamos que la cantidad de argumentos sea 10
        if(args.length != Ejecuta_Ejercicio1.longitudArrays){
            System.err.println("[ERROR]: La cantidad de argumentos debe ser 10");
            // En vez de hacer un return, devolvemos un status 1, que indica fallo
            System.exit(1);
        }
        // Declaramos cada uno de los arrays (5 del Array1 del padre y 5 del Array2 del padre)
        int[] arrayA = new int[args.length / 2];
        int[] arrayB = new int[args.length / 2];
        // Recorremos un bucle desde el 0 hasta el 4º argumento para el arrayA
        for (int i = 0; i < arrayA.length; i++){
            try {
                // Como los argumentos del main son cadenas de texto, necesitamos parsearlas
                arrayA[i] = Integer.parseInt(args[i]);
            } catch (NumberFormatException e) {
                System.err.println("[ERROR]: Alguno de los argumentos no es un numero entero");
                System.exit(1);
            }
        }

        // Recorremos un bucle desde el 5 hasta el 10º argumento para el arrayB
        for (int i = 0; i < arrayB.length; i++){
            try {
                // Como los argumentos del main son cadenas de texto, necesitamos parsearlas
                arrayB[i] = Integer.parseInt(args[i + arrayA.length]);
            } catch (NumberFormatException e) {
                System.err.println("[ERROR]: Alguno de los argumentos no es un numero entero");
                System.exit(1);
            } catch (IndexOutOfBoundsException ioobe){
                System.err.println("[ERROR]: la cantidad de argumentos es impar");
                System.exit(1);
            }
        }

        // Calcular la multiplicacion de los dos elementos
        for (int i = 0; i < arrayA.length; i++){
            int resultado = arrayA[i] * arrayB[i];
            System.out.println(resultado);
        }
    }
}
