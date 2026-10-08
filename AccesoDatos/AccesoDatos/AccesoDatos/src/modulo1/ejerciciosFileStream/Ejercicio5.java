package modulo1.ejerciciosFileStream;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Ejercicio5 {
    public static void main(String[] args) {
        String archivoOriginal = "archivo_origen.txt";
        String archivoCopia = "archivo_copia.txt";

        // Escribir algo en el archivo original
        try (FileOutputStream fos = new FileOutputStream(archivoOriginal)) {
            String contenido = "Este es el contenido del archivo original.";
            fos.write(contenido.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Copiar el contenido del archivo original a otro archivo
        try (FileInputStream fis = new FileInputStream(archivoOriginal);
             FileOutputStream fos = new FileOutputStream(archivoCopia)) {
            int byteLeido;
            while ((byteLeido = fis.read()) != -1) {
                fos.write(byteLeido);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("El contenido del archivo original ha sido copiado al archivo copia.");
    }
}
