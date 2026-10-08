package modulo1.ejerciciosRandomAccessFile;

import java.io.IOException;
import java.io.RandomAccessFile;

public class Ejercicio4 {
    public static void main(String[] args) {
        try {
            RandomAccessFile archivo = new RandomAccessFile("numeros.dat", "rw");

            // Escritura de 10 números enteros
            for (int i = 1; i <= 10; i++) {
                archivo.writeInt(i * 10);
            }

            // Leer los números en orden inverso
            System.out.println("Números en orden inverso:");
            for (int i = 9; i >= 0; i--) {
                archivo.seek(i * 4); // Cada entero ocupa 4 bytes
                System.out.println("Número: " + archivo.readInt());
            }

            archivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
