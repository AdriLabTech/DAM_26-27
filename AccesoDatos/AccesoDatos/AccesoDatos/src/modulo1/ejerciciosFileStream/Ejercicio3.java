package modulo1.ejerciciosFileStream;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Ejercicio3 {
    public static void main(String[] args) {
        String filePath = "caracteres_especiales.txt";
        String mensaje = "¡Hola, ¿cómo estás?";

        // Escribir la cadena en el archivo (UTF-8)
        try (FileOutputStream fos = new FileOutputStream(filePath)) {
            fos.write(mensaje.getBytes(StandardCharsets.UTF_8));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Leer el archivo y mostrar los caracteres especiales
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
