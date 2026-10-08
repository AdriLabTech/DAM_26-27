package modulo1;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class EjemploDataInputStream {
    public static void main(String[] args) {
       
    	 try {
             // Crear flujo de salida para escribir en un archivo
             FileOutputStream fileOut = new FileOutputStream("src/data/datosData.bin");
             DataOutputStream dataOut = new DataOutputStream(fileOut);

             // Escribir datos primitivos en el archivo
             dataOut.writeInt(123);          // Escribir un entero
             dataOut.writeDouble(45.67);     // Escribir un doble
             dataOut.writeBoolean(true);     // Escribir un booleano

             // Cerrar el flujo
             dataOut.close();
             System.out.println("Datos escritos en el archivo correctamente.");
         } catch (IOException e) {
             e.printStackTrace();
         }
    	
    	
    	try {
            FileInputStream fileIn = new FileInputStream("src/data/datosData.bin");
            DataInputStream dataIn = new DataInputStream(fileIn);

            // Leer datos primitivos en el orden correcto
            int numero = dataIn.readInt();           // Leer un entero
            double precio = dataIn.readDouble();     // Leer un double
            boolean disponible = dataIn.readBoolean(); // Leer un booleano

            System.out.println("Entero: " + numero);
            System.out.println("Double: " + precio);
            System.out.println("Boolean: " + disponible);

            dataIn.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
