package modulo1;

import java.io.*;

public class RandomAccessFileWriteMidExample {
    public static void main(String[] args) {
    	
    	/*
		 * 
		 * 
		 * 
		 * Resumen:
		 * 
		 * seek(long pos) mueve el puntero del archivo a una posición específica en
		 * bytes desde el inicio del archivo.
		 * 
		 * Los datos se almacenan en archivos como bytes (8 bits), y puedes
		 * interpretarlos o manipularlos a nivel binario si es necesario.
		 * 
		 * La posición de seek debe calcularse en función del tamaño en bytes de los
		 * tipos de datos que estás manejando (por ejemplo, 4 bytes para un int, 8 bytes
		 * para un double).
		 * 
		 * Aunque RandomAccessFile opera a nivel de bytes, puedes convertir los bytes
		 * leídos a su representación binaria para trabajar a nivel de bits si es
		 * necesario.
		 * 
		 */
    	
    	// ejemploByte();
    	 ejemploMitad();
    	 //ejemploMitadArchivosTemporales();
    	// ejemploBIN();
    	
    	
    }
    
    private static void ejemploMitadArchivosTemporales() {
    	try {
            // Crear el archivo con la palabra "Hola"
            RandomAccessFile archivo = new RandomAccessFile("src/data/archivo.txt", "rw");
            archivo.write("Hola".getBytes());
            
            // Determinar la mitad del archivo
            long longitud = archivo.length();
            long mitad = longitud / 2;
            
            // Crear un archivo temporal para reescribir el contenido
            RandomAccessFile archivoTemporal = new RandomAccessFile("src/data/archivoTemporal.txt", "rw");
            
            // Mover el puntero a la mitad
            archivo.seek(mitad);
            
            // Escribir el contenido hasta la mitad en el archivo temporal
            archivo.seek(0);  // Volver al principio
            for (int i = 0; i < mitad; i++) {
                archivoTemporal.write(archivo.read());  // Copiar byte a byte hasta la mitad
            }
            
            // Escribir "ooooo" en el archivo temporal
            archivoTemporal.write("ooooo".getBytes());
            
            // Escribir el resto del archivo original después de la mitad
            while (archivo.getFilePointer() < longitud) {
                archivoTemporal.write(archivo.read());
            }
            
            // Cerrar ambos archivos
            archivo.close();
            archivoTemporal.close();
            
            // Renombrar el archivo temporal al nombre original (opcionalmente puedes borrar el archivo original antes)
            RandomAccessFile nuevoArchivo = new RandomAccessFile("src/data/archivo.txt", "rw");
            RandomAccessFile temporalLectura = new RandomAccessFile("src/data/archivoTemporal.txt", "r");
            
            // Sobrescribir el archivo original con el contenido del temporal
            int byteLeido;
            while ((byteLeido = temporalLectura.read()) != -1) {
                nuevoArchivo.write(byteLeido);
            }
            
            // Cerrar los archivos y borrar el archivo temporal
            nuevoArchivo.close();
            temporalLectura.close();
            
            // Borrar el archivo temporal
            new java.io.File("src/data/archivoTemporal.txt").delete();
            
            System.out.println("Archivo modificado exitosamente.");
        } catch (IOException e) {
            e.printStackTrace();
        }		
	}

	public static void ejemploByte() {
    	 String filePath = "src/data/archivo_byte.txt";

         try {
             // Crear un archivo de acceso aleatorio en modo lectura/escritura
             RandomAccessFile raf = new RandomAccessFile(filePath, "rw");

             // Escribir datos en el archivo en formato de bytes
             raf.write(new byte[]{10, 20, 30, 40, 50});  // Escribimos 5 bytes

             // Mover el puntero a la posición del byte 2 (tercer byte)
             raf.seek(3);

             // Leer el byte en esa posición
             int byteLeido = raf.read();  // Lee un byte y lo devuelve como entero

             // Mostrar el byte leído
             System.out.println("Byte leído: " + byteLeido); // Debería mostrar 30

             // Cerrar el archivo
             raf.close();

         } catch (IOException e) {
             e.printStackTrace();
         }
    }
    
    public static void ejemploMitad() {
    	String filePath = "src/data/archivo_mitad_clase_completo.txt";

        try {
            // Crear un archivo de acceso aleatorio en modo "rw" (lectura/escritura)
            RandomAccessFile raf = new RandomAccessFile(filePath, "rw");

            raf.seek(0);
            // Escribir un mensaje inicial en el archivo
            raf.writeUTF("Hola");
            
            // Obtener la longitud del archivo
            long fileLength = raf.length();
            System.out.println("Longitud del archivo antes de escribir: " + fileLength + " bytes." );

            // Mover el puntero a la mitad del archivo
            long midPosition = fileLength / 2;
            
            System.out.println("mitad: " + midPosition);
            raf.seek(2);
         
            // Leer el resto del archivo y guardarlo en un buffer
            byte[] resto = new byte[(int) (fileLength - midPosition)];
            raf.readFully(resto);  // Leer el resto del archivo desde la mitad
            
            // Volver a la mitad y escribir "ooooo"
            raf.write("ooooo".getBytes());
            
            // Escribir el resto del archivo que habíamos guardado
            raf.write(resto);
            
            
            // Mostrar la nueva longitud del archivo
            System.out.println("\nLongitud del archivo después de escribir: " + raf.length() + " bytes.");
          
            raf.seek(0);
            System.out.println("Contenido del archivo:");
            for (int i = 0; i < raf.length(); i++) {
                byte byteLeido = raf.readByte();
                System.out.print((char) byteLeido);  // Convertir el byte leído a carácter
            }

            // Cerrar el archivo
            raf.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void ejemploBIN() {

    	        String filePath = "src/data/archivo_binario.txt";

    	        try {
    	            // Crear un archivo de acceso aleatorio en modo lectura/escritura
    	            RandomAccessFile raf = new RandomAccessFile(filePath, "rw");

    	            // Escribir algunos bytes en el archivo
    	            raf.write(new byte[]{(byte) 0b00101101, (byte) 0b11001100, (byte) 0b10101010});  // Escribimos 3 bytes en binario

    	            // Mover el puntero al primer byte
    	            raf.seek(2);
    	            byte byteTemporal = (byte) raf.read(); 
    	            
    	            //Retrocedo el puntero ya que con read, avanza una posición 
    	            raf.seek(2);
    	            raf.write((byte) 0b00000011);
    	            
    	            raf.seek(3);
    	            raf.write(byteTemporal);
    	            
    	            
    	            raf.seek(0);
    	            // Leer los bytes y mostrarlos en binario
    	            for (int i = 0; i < raf.length(); i++) {
    	                int byteLeido = raf.read();  // Leer un byte
    	                String binario = String.format("%8s", Integer.toBinaryString(byteLeido & 0xFF)).replace(' ', '0');
    	                System.out.println("Byte " + i + " en binario: " + binario);
    	            }

    	            // Cerrar el archivo
    	            raf.close();

    	        } catch (IOException e) {
    	            e.printStackTrace();
    	        }
    	    }
    	

}

