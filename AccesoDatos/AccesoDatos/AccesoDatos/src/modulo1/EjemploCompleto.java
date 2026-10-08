package modulo1;

import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;

public class EjemploCompleto {

	public static void main(String[] args) {
		
		escritura();
		//lecturaFile();
	}
	
	public static void lecturaFile(){
		
		 // Obtenemos la ruta del proyecto
        String rutaProyecto = System.getProperty("user.dir");
        
        // Especificamos la ruta relativa hacia la carpeta 'src'
        String rutaArchivo = rutaProyecto + "/src/data/archivo.bin";

        // Creamos el archivo utilizando la clase File
        File fichero = new File(rutaArchivo);

        // Llamamos al método para leer el archivo
        leerArchivo(fichero);
    }

    public static void leerArchivo(File fichero) {
        
    	// Usamos BufferedReader para leer el archivo
        try (BufferedReader reader = new BufferedReader(new FileReader(fichero))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    
	
	}
	

	
	public static void escritura(){
		 // Obtenemos la ruta del proyecto
        String rutaProyecto = System.getProperty("user.dir");
        
        //System.out.println(rutaProyecto);
        
        // Especificamos la ruta relativa hacia la carpeta 'src'
        String rutaArchivo = rutaProyecto + "/src/data/archivo.bin";
				
		File f = new File(rutaArchivo);

		
		if (f.exists()) {
			System.out.println("Fichero " + rutaArchivo + " ya existe.");
			//return;
		}
		
		
		try {
			BufferedWriter bfw = new BufferedWriter(new FileWriter(f)); //Añadir el Append
			bfw.write(" Este es un fichero de texto. ");
			bfw.newLine();
			bfw.write(" quizá no está del todo bien.");
			bfw.newLine();
			
			bfw.close();
		
			bfw = new BufferedWriter(new FileWriter(f, true));
			bfw.write(" Pero se puede arreglar.");
			bfw.newLine();
            System.out.println("Archivo guardado correctamente en: " + f.getAbsolutePath());

			bfw.close();
			
			/*
			 * 
			 *Hacemos lo mismo pero aplicando FileOuStream
			 *
			 * Explicación:
				FileOutputStream escribe datos en formato 
				binario (en este caso, el texto es convertido en bytes usando getBytes()).
				Aunque estamos escribiendo texto, este es tratado como una secuencia de bytes.
				Si abres el archivo, el contenido será el mismo que el generado por BufferedWriter, 
				pero FileOutputStream es más apropiado para trabajar con datos binarios, mientras que 
				BufferedWriter es para trabajar con caracteres.
			 *
			 */
			
			
			//ESCRITURA
			
	        String texto = "Hola, este es un ejemplo con FileOutputStream.\nEscribiendo texto como bytes.";

	        FileOutputStream fos = new FileOutputStream(rutaArchivo); 
	           
	        // Convertir el texto a bytes y escribirlo en el archivo
        	System.out.println("Texto:" + texto.getBytes());
        	
        	   // Imprimir el contenido del arreglo de bytes
            System.out.println("Contenido del arreglo de bytes:");
            for (byte b : texto.getBytes()) {
                System.out.print(b + " "); // Mostrar cada byte individualmente
                
                
                /*
                 * Explicación:
				b & 0xFF: El operador & (AND bit a bit) con 0xFF es para asegurarnos de que el valor del byte 
				sea tratado como un entero positivo de 8 bits, ya que en Java los bytes pueden ser negativos (entre -128 y 127). 
				Con 0xFF lo convertimos a un valor entre 0 y 255.
				
				Integer.toBinaryString(): Este método convierte el valor entero del byte en su representación binaria, 
				pero el resultado no siempre tiene 8 dígitos (por ejemplo, el número 5 en binario es 101 en vez de 00000101).
				
				String.format("%8s", ...): Usamos String.format para asegurarnos de que la representación binaria tenga exactamente 8 bits, 
				rellenando con ceros a la izquierda si es necesario.
				
				.replace(' ', '0'): Rellenamos los espacios generados por el String.format con ceros (0), para que los números binarios tengan 8 bits siempre.
                 */
                String binario = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
                System.out.println(binario);
                
            }
            System.out.println(); // Salto de línea final
        	
            fos.write(texto.getBytes());
            
            
            System.out.println("Texto escrito correctamente en el archivo como bytes.");
	      
	    
	        //LECTURA

        	FileInputStream fis = new FileInputStream(rutaArchivo);
            int byteLeido;

            // Leer cada byte del archivo hasta llegar al final (cuando devuelve -1)
            while ((byteLeido = fis.read()) != -1) {
                // Mostrar el byte leído en formato numérico
                char caracter = (char) byteLeido;

                System.out.println(byteLeido + " = " + caracter);
                

            }
	            
	
			
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
}


