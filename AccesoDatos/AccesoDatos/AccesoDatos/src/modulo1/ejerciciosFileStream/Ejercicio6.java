	package modulo1.ejerciciosFileStream;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class Ejercicio6 {
    public static void main(String[] args) {
        String filePath = "datosMixtos.dat";
        int entero1 = 100;
        char caracter1 = 'A';
        int entero2 = 200;
        char caracter2 = 'B';

        // Escribir datos mixtos
        try (FileOutputStream fos = new FileOutputStream(filePath)) {
            fos.write(entero1);  // Escribe el entero
            fos.write(caracter1);  // Escribe el carácter
            fos.write(entero2);  // Escribe el entero
            fos.write(caracter2);  // Escribe el carácter
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Leer datos mixtos
        try (FileInputStream fis = new FileInputStream(filePath)) {
            int byteLeido;
            System.out.println("Datos leídos del archivo:");
            while ((byteLeido = fis.read()) != -1) {
                System.out.println("Dato: " + byteLeido);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
