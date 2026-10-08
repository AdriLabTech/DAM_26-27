package modulo1;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;

public class EjemploListarDir {

	public static void main(String[] args) {
		
		
		
        listarDirectorios();
		//escritura();
		//lectura();
		
		
    }
	
	public static void listarDirectorios() {
		// Especifica el directorio que deseas analizar
        String path = "src"; // Cambia esto por la ruta de tu directorio
        File directory = new File(path);
        
        // Verificar si el archivo es un directorio
        if (directory.isDirectory()) {
            System.out.println("Contenido del directorio: " + directory.getAbsolutePath());
            
            listDirectories(directory, 0); // Llamada a la función recursiva
            
            // Listar archivos y subdirectorios
            File[] files = directory.listFiles();
            if (files != null) {
                for (File file : files) {
                    // Mostrar información del archivo/directorio
                    System.out.println("Nombre: " + file.getName());
                    System.out.println("Ruta: " + file.getAbsolutePath());
                    System.out.println("¿Es un directorio?: " + file.isDirectory());
                    System.out.println("Tamaño: " + (file.isFile() ? file.length() + " bytes" : "N/A"));
                    System.out.println("Última modificación: " + file.lastModified());
                    System.out.println("----------------------------------");
                }
            } else {
                System.out.println("El directorio está vacío o no se puede acceder a él.");
            }
        } else {
            System.out.println("La ruta especificada no es un directorio.");
        }
	}
	
	 // Función recursiva para listar directorios
    private static void listDirectories(File dir, int level) {
        File[] files = dir.listFiles(); // Obtener los archivos y subdirectorios
        if (files != null) {
            for (File file : files) {
                // Indentar para mostrar la profundidad
                for (int i = 0; i < level; i++) {
                    System.out.print("    "); // Indentación
                }
                // Mostrar información del directorio o archivo
                System.out.println("Nombre: " + file.getName());
                if (file.isDirectory()) {
                    // Llamada recursiva para directorios
                    listDirectories(file, level + 1);
                }
            }
        } else {
            System.out.println("No se puede acceder al contenido del directorio: " + dir.getAbsolutePath());
        }
    }
	
	public static void escritura() {
		
			String rutaArchivo = "src/data/numeros.dat"; // Ruta del archivo
	
			int number = 5; // El número 5
	        
	        // Crear un arreglo de 4 bytes
	        byte[] byteArray = new byte[4];
	        byteArray[0] = (byte) (number >> 24); // byte más significativo  // 
	        byteArray[1] = (byte) (number >> 16);
	        byteArray[2] = (byte) (number >> 8);
	        byteArray[3] = (byte) number; // byte menos significativo
	        
	        /*
	         *  byte[] buffer = new byte[4];
		        buffer[0] = 0; // byte más significativo
		        buffer[1] = 0;
		        buffer[2] = 0;
		        buffer[3] = 5; // byte menos significativo
			 * 
	         */
	        
	        // Imprimir el valor en el arreglo
	        System.out.print("El número 5 en 4 bytes es: ");
	        for (byte b : byteArray) {
	            System.out.print(b + " ");
	        }

	        try (FileOutputStream fos = new FileOutputStream(rutaArchivo)) {
	       
            fos.write(byteArray);
	            
	            System.out.println("Números escritos en el archivo binario.");
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
		
	}
	
	public static void lectura() {
		
		String rutaArchivo = "src/data/numeros.dat"; // Ruta del archivo

	    try (FileInputStream fis = new FileInputStream(rutaArchivo)) {
           
	    	byte[] buffer = new byte[4]; // Buffer para leer 4 bytes (un entero)

            
            /*
             * Cuando utilizas un InputStream (como FileInputStream) para leer datos, 
             * el método read() devuelve el siguiente byte del flujo. Cuando el flujo ha llegado al 
             * final del archivo y no hay más datos para leer, read() retorna -1. Esto es una señal para que el 
             * programa sepa que ya no hay más datos disponibles y, generalmente, indica que se debe salir del bucle de lectura.
             */
            
            
            System.out.println("Números leídos del archivo binario:");
            while (fis.read(buffer) != -1) {
                // Convierte los bytes leídos a un entero
                int numero = ByteBuffer.wrap(buffer).getInt();
                System.out.println(numero);
                
            //Si quisieramos que fuera una cadena
            //System.out.print((char) byteLeido); // Imprime cada byte como un carácter

                
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
		
	}	
	
}
