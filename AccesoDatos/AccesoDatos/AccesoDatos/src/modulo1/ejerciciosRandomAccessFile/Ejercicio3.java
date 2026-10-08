package modulo1.ejerciciosRandomAccessFile;

import java.io.IOException;
import java.io.RandomAccessFile;

public class Ejercicio3 {
    public static void main(String[] args) {
        try {
            RandomAccessFile archivo = new RandomAccessFile("cadenas.dat", "rw");

            // Escribir dos cadenas
            archivo.writeUTF("PrimeraCadena");
            archivo.writeUTF("SegundaCadena");

            // Guardar la posición de la segunda cadena
            long posicionSegunda = archivo.getFilePointer();

            // Insertar nueva cadena entre las dos
            archivo.seek(0); // Volver al inicio
            archivo.readUTF(); // Leer la primera cadena para posicionar al final
            archivo.writeUTF("NuevaCadena");

            // Mover la segunda cadena al final
            archivo.seek(posicionSegunda); // Mover el puntero a la segunda cadena
            String segundaCadena = archivo.readUTF(); // Leer la segunda cadena

            // Volver a la posición después de la nueva cadena
            archivo.seek(archivo.getFilePointer());
            archivo.writeUTF(segundaCadena); // Escribir la segunda cadena de nuevo

            // Mostrar el contenido del archivo
            archivo.seek(0); // Volver al inicio para leer
            System.out.println("Contenido del archivo:");
            System.out.println(archivo.readUTF());
            System.out.println(archivo.readUTF());
            System.out.println(archivo.readUTF());

            archivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

