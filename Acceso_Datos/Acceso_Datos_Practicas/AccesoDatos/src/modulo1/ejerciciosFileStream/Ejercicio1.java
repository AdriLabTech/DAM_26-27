package modulo1.ejerciciosFileStream;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class Ejercicio1 {
    public static void main(String[] args) {
        String filePath = "cadena.txt";
        String mensaje = "Hola Mundo";

        // Escribir en el archivo
        try (FileOutputStream fos = new FileOutputStream(filePath)) {
            fos.write(mensaje.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Leer el archivo
        try (FileInputStream fis = new FileInputStream(filePath)) {
            int byteLeido;
            System.out.println("Contenido del archivo:");
            while ((byteLeido = fis.read()) != -1) {
                System.out.print((char) byteLeido);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
