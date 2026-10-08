package modulo1;

import java.io.IOException;
import java.io.RandomAccessFile;

public class EjemploRandomAccessPointer {
    public static void main(String[] args) {
        String nombreArchivo = "src/data/archivo_ejemplo_clase.txt";

        //ejemploClase(nombreArchivo);
        ejemploHooooola(nombreArchivo);
        
    }

	private static void ejemploHooooola(String nombreArchivo) {
		
		try {
            // Abrir archivo en modo lectura/escritura
            RandomAccessFile raf = new RandomAccessFile(nombreArchivo, "rw");

            // Escribir algunos datos en el archivo
            raf.writeUTF("Hola");
           

            // Mostrar la posición del puntero después de escribir
            System.out.println("Posición del puntero después de escribir 'Hola': " + raf.getFilePointer());

            // Mover el puntero al inicio del archivo
            raf.seek(0);
            System.out.println("Posición del puntero después de seek(0): " + raf.readUTF());

            raf.seek(4);
            
            System.out.println("El puntero es: "+ raf.getFilePointer());

            raf.setLength(2);
            String extra = raf.readUTF();
            System.out.println("El extra es: "+ extra);
            
            
            raf.writeUTF("AA");
            
            // Leer el contenido del archivo
            
            raf.seek(0);
            String contenido = raf.readUTF();
            System.out.println("Contenido leído: " + contenido);

            // Mostrar la posición del puntero después de leer
            System.out.println("Posición del puntero después de leer: " + raf.getFilePointer());

         
            // Cerrar el archivo
            raf.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
	}

	private static void ejemploClase(String nombreArchivo) {
		  
			try {
	            // Abrir archivo en modo lectura/escritura
	            RandomAccessFile raf = new RandomAccessFile(nombreArchivo, "rw");

	            // Escribir algunos datos en el archivo
	            raf.writeUTF("");
	           

	            // Mostrar la posición del puntero después de escribir
	            System.out.println("Posición del puntero después de escribir 'B': " + raf.getFilePointer());

	            // Mover el puntero al inicio del archivo
	            raf.seek(0);
	            System.out.println("Posición del puntero después de seek(0): " + raf.getFilePointer());

	            // Leer el contenido del archivo
	            String contenido = raf.readUTF();
	            System.out.println("Contenido leído: " + contenido);

	            // Mostrar la posición del puntero después de leer
	            System.out.println("Posición del puntero después de leer: " + raf.getFilePointer());

	            // Escribir más datos al final del archivo
	            raf.writeUTF("¡Adiós Mundo!");
	            System.out.println("Posición del puntero después de escribir '¡Adiós Mundo!': " + raf.getFilePointer());

	            // Cerrar el archivo
	            raf.close();

	        } catch (IOException e) {
	            e.printStackTrace();
	        }
		
		
	}
}
