package modulo1;
import java.io.FileInputStream;
import java.io.IOException;

public class CompararArchivosBinarios {
    public static void main(String[] args) {
        String rutaArchivo1 = "src/data/archivo.txt";
        String rutaArchivo2 = "src/data/archivo_mitad.txt";

        try (FileInputStream fis1 = new FileInputStream(rutaArchivo1);
             FileInputStream fis2 = new FileInputStream(rutaArchivo2)) {

            int byteArchivo1, byteArchivo2;
            boolean sonIguales = true;

            // Comparar ambos archivos byte a byte
            while ((byteArchivo1 = fis1.read()) != -1 && (byteArchivo2 = fis2.read()) != -1) {
                if (byteArchivo1 != byteArchivo2) {
                    sonIguales = false;
                    break;
                }
            }

            // Verificar si ambos archivos tienen la misma longitud
            if (fis1.read() != -1 || fis2.read() != -1) {
                sonIguales = false;
            }

            if (sonIguales) {
                System.out.println("Los archivos son idénticos.");
            } else {
                System.out.println("Los archivos son diferentes.");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}