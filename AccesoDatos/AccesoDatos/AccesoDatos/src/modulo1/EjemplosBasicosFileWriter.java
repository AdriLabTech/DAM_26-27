package modulo1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class EjemplosBasicosFileWriter {

	
	  public static void main(String[] args) {
		    String filePathTexto = "src/data/ejemplosBasicos.txt";
	        
	        escribirFileWriter(filePathTexto);
	        leerFileWriter(filePathTexto);

	        escribirFileWriterBuffered(filePathTexto);
	        leerFileWriterBuffered(filePathTexto);
	  }
	  
	  public static void escribirFileWriter(String filePath) {
		  
		  // Usar FileWriter dentro de un bloque try-with-resources para asegurar el cierre automático
	        try (FileWriter writer = new FileWriter(filePath)) {
	            // Escribir una línea en el archivo
	            writer.write("¡Hola, mundo!\n");
	            // Escribir otra línea
	            writer.write("Este es un archivo de ejemplo.\n");
	            System.out.println("Archivo FILEWRITER creado con éxito");
	        } catch (IOException e) {
	            // Manejar posibles excepciones
	            e.printStackTrace();
	        }
		    
		  
	  }
	  
  public static void escribirFileWriterBuffered(String filePath) {
	  
		/*
		 * 
		 * FileWriter: Escribe directamente en el archivo. Cada llamada al método write
		 * puede implicar una operación de escritura en disco, lo que puede ser lento si
		 * se escriben muchas líneas. BufferedWriter: Utiliza un buffer (memoria
		 * temporal) para almacenar datos antes de escribirlos en el archivo. Esto
		 * reduce el número de operaciones de escritura en disco, lo que mejora el
		 * rendimiento.
		 */

	  // Usar BufferedWriter dentro de un bloque try-with-resources
      try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true))) {
          // Escribir una línea en el archivo
          writer.write("¡Hola, mundo!\n");
          // Escribir otra línea
          writer.write("Este es un archivo de ejemplo utilizando BufferedWriter.\n");
          System.out.println("Archivo BUFEREDWRITER creado con éxito");

      } catch (IOException e) {
          // Manejar posibles excepciones
          e.printStackTrace();
      }
		    
		  
 }
  public static void leerFileWriterBuffered(String filePath) {
	  
	  
      System.out.println("\nLectura con Buffered");

	  // Usar BufferedReader dentro de un bloque try-with-resources
      try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
          String linea;
          // Leer línea por línea
          while ((linea = reader.readLine()) != null) {
              // Imprimir cada línea en la consola
              System.out.println(linea);
          }
      } catch (IOException e) {
          // Manejar posibles excepciones
          e.printStackTrace();
      }
	    
	  
	  
  }
  
  public static void leerFileWriter(String filePath) {
	  
      System.out.println("\nLectura con Writter");

	  
	  /*
	   * Ten en cuenta que FileReader se utiliza para leer bytes de un archivo, 
	   * mientras que BufferedReader está optimizado para leer texto.
	   */
	  
	  try (FileReader reader = new FileReader(filePath)) {
          int caracter;
          // Leer carácter por carácter
          while ((caracter = reader.read()) != -1) {
              // Imprimir cada carácter en la consola
              System.out.print((char) caracter);
          }
      } catch (IOException e) {
          // Manejar posibles excepciones
          e.printStackTrace();
      }
  }
  
  
	  
	
}
