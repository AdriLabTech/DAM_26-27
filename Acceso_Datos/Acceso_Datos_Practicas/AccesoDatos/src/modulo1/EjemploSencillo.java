package modulo1;

import java.io.*;

public class EjemploSencillo {

	public static void main(String[] args) {

		System.out.println("Ejemplo de guardar y leer en archivo");
		
		try (FileOutputStream fos = new FileOutputStream ("src/data/miArchivo.bin")){
		
			char letra = 'a';
			char letra2 = 'b';
			int entero = 2;
			
			String frase = "hola";
			
			
		    System.out.print(frase.getBytes());
			
			fos.write(letra);
			fos.write(letra2);
			fos.write(entero);
			fos.write(frase.getBytes());
		
			
			 File file = new File("src/data/miArchivo.bin");
		    
			 long fileSize = file.length();  // Obtener el tamaño del archivo en bytes
		     System.out.println("\nEl tamaño del archivo es: " + fileSize + " bytes.");
		
		
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		System.out.println("Ejemplo guardado");

		try {
			
			String rutaOriginal = "src/data/miArchivo.bin";
			FileInputStream fis = new FileInputStream(rutaOriginal);
			
			
			 int cadena;
			
			 File file = new File(rutaOriginal);
			    
			 long fileSize = file.length();  // Obtener el tamaño del archivo en bytes
		     System.out.println("LECTURA: El tamaño del archivo es: " + fileSize + " bytes."); 
			
			//System.out.println("Archivo antes de leer: " + rutaOriginal.length());
			
			
			//byte[] bytes = new byte[(int) fileSize]; // Crea un arreglo de bytes
           // fis.read(bytes); // Lee los bytes del archivo
            
//            for (byte b : bytes) {
//                // Convierte el byte a binario y lo imprime
//                System.out.println("Primera lectura: " + b);
//            }
            
            //LECTURA 2
            
			while ((cadena = fis.read()) != -1) {
				
				System.out.println("Numero: " + (char) cadena);
                System.out.println("Byte leído: " + cadena + " (en binario: " + String.format("%8s", Integer.toBinaryString(cadena)).replace(' ', '0') + ")");

			}
		
			fis.close();
		
		
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}

}
