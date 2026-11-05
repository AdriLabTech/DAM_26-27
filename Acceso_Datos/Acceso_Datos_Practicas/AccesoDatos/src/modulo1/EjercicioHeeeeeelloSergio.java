package modulo1;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class EjercicioHeeeeeelloSergio {

	public static void main(String[] args) {

		jaime();
		sergio();

	}

	private static void sergio() {
		// Sergio Martínez del Castillo
		
		
		String filePath = "src/data/archivo_mitad.txt";

		
		File f = new File (filePath);
		
		if( f.exists())
			f.delete();

		try {
			// Crear un archivo de acceso aleatorio en modo "rw" (lectura/escritura)
			RandomAccessFile raf = new RandomAccessFile(filePath, "rw");
			
			
			
			// Escribir un mensaje inicial en el archivo
			raf.seek(0);
			raf.writeUTF("Hola");
			
			// Obtener la longitud del archivo (restamos 2 para que la longitud de
			raf.seek(0);
			long fileLength = raf.length();
			System.out.println("Longitud del archivo antes de escribir: " + fileLength + " bytes.");
			
			
			// Mover el puntero a la mitad del archivo (restamos los bytes de la
			// codificación y los sumamos
			// más tarde para que se ponga justo antes de la mitad)
			long midPosition = ((fileLength - 2) / 2) + 2;
			raf.seek(midPosition);
			
			
			
			String textoTemporal = "";
			for (int i = (int) midPosition; i < fileLength; i++) {
				char caracter = (char) raf.read();
				textoTemporal += caracter;
			}
			
			// Cambiar el tamaño de la cadena que indica la codificación UTF con
			// .setLength()
			
			String cadenaNueva = "ooo";
			int bytesNuevaCadena = cadenaNueva.length();
			System.out.println("Tamaño bytes nueva cadena: " + bytesNuevaCadena);
			
			
			// Ponemos el cursor en la posicion que indica el tamaño de la cadena en UTF
			// e insertamos el nuevo tamaño de la cadena (antigua+nueva)
			raf.seek(1);
			short cantidadFinal = (short) ((fileLength - 2) + bytesNuevaCadena);
			raf.write(cantidadFinal);
			raf.setLength(cantidadFinal);
			System.out.println("Peso del texto antiguo y el nuevo sumados: " + (fileLength + bytesNuevaCadena));
			System.out.println("Texto temporal: " + textoTemporal);
			// Escribimos un nuevo mensaje a partir de la mitad del archivo
			raf.seek(midPosition);
			raf.write(cadenaNueva.getBytes());
			raf.write(textoTemporal.getBytes());
			// Leer toda la cadena desde el principio
			raf.seek(0);
			String textoDesdePosicion = raf.readUTF();
			// Mostrar lo que se leyó
			System.out.println("Texto con nueva cadena insertada: " + textoDesdePosicion);
			// Mostrar la nueva longitud del archivo
			System.out.println("Longitud del archivo después de escribir: " + raf.length() + " bytes.");
			// Cerrar el archivo
			raf.close();
		} catch (IOException e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}

	private static void jaime() {
		String nombreArchivo = "src/data/archivoparaalterar.txt";
		try {
		
			RandomAccessFile raf = new RandomAccessFile(nombreArchivo, "rw");
			raf.writeUTF("Hola");

			raf.seek(0);
			String contenidoOriginal = raf.readUTF();
			System.out.println("Contenido original del archivo: " + contenidoOriginal);

			raf.seek(0);
			String original = raf.readUTF();

			String parteAntesL = original.substring(0, 2);
			String parteDespuesL = original.substring(2);

			raf.seek(0);
			raf.write(parteAntesL.getBytes());
			raf.writeBytes("ooooo");
			raf.writeBytes(parteDespuesL);

			raf.seek(0); // Cambio de readUTF a readLine
			String contenidoModificado = raf.readUTF();
			System.out.println("Contenido alterado: " + contenidoModificado);

			raf.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
