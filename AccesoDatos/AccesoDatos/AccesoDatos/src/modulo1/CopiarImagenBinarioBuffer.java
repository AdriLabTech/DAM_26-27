package modulo1;

import java.io.*;

public class CopiarImagenBinarioBuffer {
	
	public static void main(String[] args) {
//        // Obtenemos la ruta del proyecto
//        String rutaProyecto = System.getProperty("user.dir");
//
//       System.out.println(rutaProyecto);
//        
//        // Ruta de la imagen original dentro de la carpeta 'src'
//        String rutaImagenOriginal = rutaProyecto + "/src/data/grancapitan.jpg";
//
//        // Ruta donde se guardará la copia de la imagen
//        String rutaImagenCopia = rutaProyecto + "/src/data/copiaImagenBinario.jpg";
//
//        // Llamamos al método para copiar la imagen en binario
//        copiarImagenBinario(rutaImagenOriginal, rutaImagenCopia);
//        copiarImagenBinarioSinBuffer(rutaImagenOriginal,rutaImagenCopia);
//        
//        
            try (FileInputStream fis = new FileInputStream("src/data/grancapitan.jpg"); // Ponemos la ruta de la imagen
                FileOutputStream fos = new FileOutputStream("src/data/duplicate.jpg")) { // Ponemos la ruta final del archivo

                int i; // Variable para leer el archivo
                while((i = fis.read()) != -1) { // Leemos el archivo
                    fos.write(i); // Escribimos el archivo
                }

                
                
                byte[] datos = new byte[fis.available()]; // Almacenamos el tamaño del archivo
                fis.read(datos);
                fos.write(datos);

                System.out.print("Se ha copiado el archivo");

            } catch (IOException e) { // Si hay un error lo imprimimos.
                e.printStackTrace();
            }
        
    }

    private static void copiarImagenBinarioSinBuffer(String rutaOriginal, String rutaCopia) {
    	
    	long inicio = System.currentTimeMillis(); // Inicio del tiempo
        
        try (
            FileInputStream fis = new FileInputStream(rutaOriginal);
            FileOutputStream fos = new FileOutputStream(rutaCopia)
        ) {
            int byteLeido;
            
            while ((byteLeido = fis.read()) != -1) {
                fos.write(byteLeido); // Escribir byte a byte
            }
            
            System.out.println("Copia realizada sin buffer.");
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        long fin = System.currentTimeMillis(); // Fin del tiempo
        System.out.println("Tiempo tomado sin buffer: " + (fin - inicio) + " ms");
    		
	}

	public static void copiarImagenBinario(String rutaOriginal, String rutaCopia) {
        File archivoOriginal = new File(rutaOriginal);
        File archivoCopia = new File(rutaCopia);
        
        long inicio = System.currentTimeMillis(); // Inicio del tiempo


        try (FileInputStream fis = new FileInputStream(archivoOriginal);
             FileOutputStream fos = new FileOutputStream(archivoCopia)) {
        	

                byte[] bytes = new byte[(int) rutaOriginal.length()]; // Crea un arreglo de bytes
                fis.read(bytes); // Lee los bytes del archivo
                
                // Imprime cada byte en formato binario
                for (byte b : bytes) {
                    // Convierte el byte a binario y lo imprime
                    System.out.print(String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0') + " ");
                }
           

            // Creamos un buffer para leer los datos en bloques
            byte[] buffer = new byte[1024];  // 1 KB de buffer
            int bytesLeidos;

            // Leer y escribir el archivo en bloques
            while ((bytesLeidos = fis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesLeidos);
            }

            System.out.println("Imagen copiada correctamente en formato binario: " + archivoCopia.getAbsolutePath());
            long fin = System.currentTimeMillis(); // Fin del tiempo
            System.out.println("Tiempo tomado con buffer: " + (fin - inicio) + " ms");
      

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
