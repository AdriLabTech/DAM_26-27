package modulo1.ejerciciosFileStream;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Ejercicio7 {
    public static void main(String[] args) {
        String file1 = "archivo1.dat";
        String file2 = "archivo2.dat";

        // Escribir datos en ambos archivos
        try (FileOutputStream fos1 = new FileOutputStream(file1);
             FileOutputStream fos2 = new FileOutputStream(file2)) {
            fos1.write(new byte[]{10, 20, 30, 40, 50});
            fos2.write(new byte[]{10, 20, 30, 40, 50});  // Los mismos datos
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Comparar los archivos
        try (FileInputStream fis1 = new FileInputStream(file1);
             FileInputStream fis2 = new FileInputStream(file2)) {
            boolean iguales = true;
            int byte1, byte2;

            while ((byte1 = fis1.read()) != -1 && (byte2 = fis2.read()) != -1) {
                if (byte1 != byte2) {
                    iguales = false;
                    break;
                }
            }

            if (iguales && fis1.read() == -1 && fis2.read() == -1) {
                System.out.println("Los archivos son idénticos.");
            } else {
                System.out.println("Los archivos son diferentes.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

