package modulo1;

import java.io.*;
import java.util.Scanner;

public class RandomAccessEditorBinarioSencillo {
	 public static void main(String[] args) {
	      
		 String filePath = "src/data/numeros.bin";
	        Scanner scanner = new Scanner(System.in);

	        try {
	            // Crear o abrir el archivo en modo lectura/escritura
	            RandomAccessFile raf = new RandomAccessFile(filePath, "rw");

	            // Escribir 10 números enteros en el archivo
	            if (raf.length() == 0) { // Solo escribir si el archivo está vacío
	                for (int i = 1; i <= 10; i++) {
	                    raf.writeInt(i * 10); // Escribir los números 10, 20, 30, ..., 100
	                }
	            }

	            // Mostrar los números en el archivo antes de la modificación
	            System.out.println("Contenido del archivo antes de la modificación:");
	            raf.seek(0); // Mover el puntero al inicio del archivo
	            for (int i = 1; i <= 10; i++) {
	                int numero = raf.readInt();
	                System.out.println("Posición " + i + ": " + numero);
	            }

	            // Solicitar al usuario la posición y el nuevo valor
	            System.out.print("Elige la posición del número que quieres modificar (1-10): ");
	            int posicion = scanner.nextInt();

	            System.out.print("Introduce el nuevo valor: ");
	            int nuevoValor = scanner.nextInt();

	            // Calcular la posición en bytes del número a modificar
	            long posicionByte = (posicion - 1) * 4; // Cada int ocupa 4 bytes
	            raf.seek(posicionByte); // Mover el puntero a la posición calculada

	            // Sobrescribir el número en la posición elegida
	            raf.writeInt(nuevoValor);

	            // Mostrar los números en el archivo después de la modificación
	            System.out.println("\nContenido del archivo después de la modificación:");
	            raf.seek(0); // Mover el puntero al inicio del archivo
	            for (int i = 1; i <= 10; i++) {
	                int numero = raf.readInt();
	                System.out.println("Posición " + i + ": " + numero);
	            }
	            
	            //añado al final del archivo una cadena de texto de 6 bytes
	            
	            System.out.println("Tamaño antes de meter la cadena" + raf.length());
	           
	            raf.writeUTF("Hola");  // 6 bytes: 2 bytes de longitud + 4 bytes de caracteres
	           	            
		        System.out.println("Tamaño después de meter la cadena" + raf.length());

		        
		        System.out.println("Contenido del fichero: ");
		        
		        
		    
	            
	            // Cerrar el archivo
	            raf.close();
	        } catch (IOException e) {
	            e.printStackTrace();
	        } finally {
	            scanner.close();
	        }
	    }
}
