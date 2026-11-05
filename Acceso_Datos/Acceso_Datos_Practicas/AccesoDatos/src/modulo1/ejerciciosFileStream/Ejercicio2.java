package modulo1.ejerciciosFileStream;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class Ejercicio2 {
    public static void main(String[] args) {
        String filePath = "numeros.dat";
        int[] numeros = {1, 2, 3, 4, 5};

        // Escribir números en el archivo
        try (FileOutputStream fos = new FileOutputStream(filePath)) {
            for (int numero : numeros) {
                fos.write(numero);  // Escribe los números como bytes
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Leer los números del archivo
        try (FileInputStream fis = new FileInputStream(filePath)) {
            int byteLeido;
            System.out.println("Números leídos del archivo:");
            while ((byteLeido = fis.read()) != -1) {
                System.out.print(byteLeido + " ");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

