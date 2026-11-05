package modulo1.ejerciciosFileStream;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class Ejercicio4 {
    public static void main(String[] args) {
        String filePath = "cadena_inversa.txt";
        String mensaje = "Hola, mundo";

        // Escribir la cadena en el archivo
        try (FileOutputStream fos = new FileOutputStream(filePath)) {
            fos.write(mensaje.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Leer el archivo y mostrar su contenido de manera inversa
        try (FileInputStream fis = new FileInputStream(filePath)) {
            byte[] contenido = fis.readAllBytes();  // Leer todo el contenido del archivo en un array de bytes
            System.out.println("Contenido del archivo en orden inverso:");
            for (int i = contenido.length - 1; i >= 0; i--) {
                System.out.print((char) contenido[i]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
