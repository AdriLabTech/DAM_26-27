package modulo1.ejerciciosRandomAccessFile;
import java.io.IOException;
import java.io.RandomAccessFile;

public class Ejercicio2 {
    public static void main(String[] args) {
        try {
            RandomAccessFile archivo = new RandomAccessFile("numeros.dat", "rw");

            // Escritura de 5 números enteros
            archivo.writeInt(10);
            archivo.writeInt(20);
            archivo.writeInt(30);
            archivo.writeInt(40);
            archivo.writeInt(50);

            // Posicionarse en el tercer número (índice 2, desplazamiento: 2 * 4 bytes)
            archivo.seek(2 * 4);
            archivo.writeInt(35);  // Modificar el valor de 30 a 35

            // Volver al inicio para leer todos los números
            archivo.seek(0);
            for (int i = 0; i < 5; i++) {
                System.out.println("Número " + (i + 1) + ": " + archivo.readInt());
            }

            archivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
