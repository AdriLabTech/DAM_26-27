package modulo1.ejerciciosRandomAccessFile;
import java.io.IOException;
import java.io.RandomAccessFile;

public class Ejercicio1 {
    public static void main(String[] args) {
        try {
            RandomAccessFile archivo = new RandomAccessFile("numeros.dat", "rw");

            // Escritura de 5 números enteros
            archivo.writeInt(10);
            archivo.writeInt(20);
            archivo.writeInt(30);
            archivo.writeInt(40);
            archivo.writeInt(50);

            // Posicionarse al inicio para leer
            archivo.seek(0);

            // Lectura de los números
            for (int i = 0; i < 5; i++) {
                int numero = archivo.readInt();
                System.out.println("Número " + (i + 1) + ": " + numero);
            }

            archivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
