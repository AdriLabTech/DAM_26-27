package modulo1;

import java.io.*;

public class CopiarArchivoBinario {

	public static void main(String[] args) {

	//FILE INPUT/OUTPUT STREAM	
			
		crearArchivo();
		leerArchivo();
		copiarArchivo();
		leerArchivoBrutalidad();
		compararArchivos();
		
		
	}

	private static void compararArchivos() {

		try {
			
			File archivo1 = new File ("src/data/dataAlumno.bin");
			File archivo2 = new File ("src/data/archivo.bin");

			boolean isCopy = true;
			
			if (archivo1.length() != archivo2.length()) 
			{				
				System.out.println("No son iguales. Lo siento. No son igual tamaño");
			}else {
		
					FileInputStream fis = new FileInputStream("src/data/dataAlumnoCopiaBrutalidad.bin");
					FileInputStream fisCopia = new FileInputStream("src/data/dataAlumno.bin");
			
						 
								
					while ( fis.available() > 0 && isCopy)
					{
						if (fis.read() != fisCopia.read())
						{
							isCopy = false;
						}
					}
				
			if(isCopy) {
				System.out.println("Son iguales");
			}else System.out.println("No son iguales. Lo siento");

					
		}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void leerArchivoBrutalidad() {
		try {
			
			FileInputStream fis = new FileInputStream("src/data/dataAlumnoCopiaBrutalidad.bin");

			while ( fis.available() > 0)
			{
				System.out.println("Brutalidad " + fis.read());
			}
			
			fis.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}			
	}

	private static void copiarArchivo() {

	try {
			
			FileInputStream fis = new FileInputStream("src/data/dataAlumno.bin");
			FileOutputStream fos = new FileOutputStream("src/data/dataAlumnoCopiaBrutalidad.bin");

			
			while ( fis.available() > 0)
			{
				fos.write(fis.read());
			}
			
			fis.close();
			fos.close();

		
			
		} catch (IOException e) {
			e.printStackTrace();
		}	
	}

	
	private static void crearArchivo() {
		
		try {
			
			FileOutputStream fos = new FileOutputStream("src/data/dataAlumno.bin");
			fos.write(7);
			fos.write(2);
			fos.write(3);
			fos.close();

		
			
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}

private static void leerArchivo() {
		
		try {
			
			FileInputStream fis = new FileInputStream("src/data/dataAlumno.bin");

			while ( fis.available() > 0)
			{
				System.out.println(fis.read());
			}
			
			fis.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}		
	}
	
}
