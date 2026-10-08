package modulo1.ejerciciosRandomAccessFile;

import java.io.IOException;
import java.io.RandomAccessFile;

public class Ejercicio5 {
    public static void main(String[] args) {
        try {
            RandomAccessFile archivo = new RandomAccessFile("estudiantes.dat", "rw");

            // Escritura de 5 estudiantes (nombre y nota)
            escribirEstudiante(archivo, "Juan", 85);
            escribirEstudiante(archivo, "Ana", 90);
            escribirEstudiante(archivo, "Carlos", 75);
            escribirEstudiante(archivo, "Lucía", 95);
            escribirEstudiante(archivo, "Miguel", 80);

            // Buscar el tercer estudiante (índice 2)
            archivo.seek(2 * (20 + 4)); // Nombre (20 bytes) + Nota (4 bytes)
            String nombre = leerNombre(archivo);
            int nota = archivo.readInt();
            System.out.println("Estudiante encontrado: " + nombre + " con nota: " + nota);

            // Actualizar la nota de "Carlos" a 85
            archivo.seek(2 * (20 + 4)); // Volver a la posición del tercer estudiante
            archivo.skipBytes(20); // Saltar el nombre
            archivo.writeInt(85); // Actualizar la nota

            // Mostrar la lista completa de estudiantes
            archivo.seek(0); // Volver al inicio para leer
            System.out.println("Lista actualizada de estudiantes:");
            for (int i = 0; i < 5; i++) {
                nombre = leerNombre(archivo);
                nota = archivo.readInt();
                System.out.println(nombre + " - Nota: " + nota);
            }

            archivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Método para escribir un estudiante (nombre y nota)
    public static void escribirEstudiante(RandomAccessFile archivo, String nombre, int nota) throws IOException {
        archivo.writeUTF(String.format("%-20s", nombre)); // Nombre con longitud fija (20 caracteres)
        archivo.writeInt(nota); // Nota
    }

    // Método para leer el nombre del estudiante
    public static String leerNombre(RandomAccessFile archivo) throws IOException {
        return archivo.readUTF().trim(); // Leer el nombre y quitar espacios
    }
}
