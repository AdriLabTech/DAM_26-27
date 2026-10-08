package modulo1;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

/*
 * Resumen:
 *Las clases como FileOutputStream y FileInputStream 
 *se utilizan en situaciones en las que es necesario manejar datos binarios directamente. Esto incluye:
 *Guardar el estado de una aplicación (serialización)
 *Intercambio eficiente de datos a través de la red
 *Manejo de grandes volúmenes de datos binarios
 *Desarrollo de sistemas que requieren alta eficiencia en la lectura/escritura
 *Estas clases son clave para el desarrollo de aplicaciones que 
 *necesiten trabajar directamente con archivos o datos binarios en general.
 */

public class EjemplosBasicosStream {

	public static void main(String[] args) {

		escribirNumeros();
		leerNumeros();
		mezclaAmbos();

	}

	public static void escribirNumeros() {

		// Definimos un array de enteros
		int[] numeros = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

		try (FileOutputStream fos = new FileOutputStream("src/data/numeros.dat")) {
			// Recorremos el array de números y los escribimos en el archivo
			for (int numero : numeros) {
				fos.write(numero); // Escribe el número como byte
			}
			System.out.println("Números escritos en el archivo correctamente.");
		} catch (IOException e) {
			System.out.println("Ocurrió un error al escribir en el archivo.");
			e.printStackTrace();
		}
	}

	public static void leerNumeros() {

		try (FileInputStream fis = new FileInputStream("src/data/numeros.dat")) {
			int numero;

			// Leer cada byte del archivo hasta que no queden más (-1 indica el final del
			// archivo)
			while ((numero = fis.read()) != -1) {
				System.out.println("Número leído: " + numero);
			}

		} catch (IOException e) {
			System.out.println("Ocurrió un error al leer el archivo.");
			e.printStackTrace();
		}
	}

	public static void mezclaAmbos() {
		// Datos que vamos a escribir
		int[] numeros = { 10, 20, 30 };
		String[] cadenas = { "Hola", "Mundo", "Java" };

		try (FileOutputStream fos = new FileOutputStream("src/data/mezcla.dat")) {
			// Escribir números en el archivo
			for (int numero : numeros) {
				fos.write(numero); // Escribimos el número como byte
			}

			// Escribir cadenas en el archivo
			for (String cadena : cadenas) {
				byte[] cadenaBytes = cadena.getBytes(StandardCharsets.UTF_8);
				fos.write(cadenaBytes); // Escribimos la cadena como bytes
				fos.write('\n'); // Añadimos un salto de línea entre cadenas
			}

			System.out.println("Números y cadenas escritos en el archivo correctamente.");

			try (FileInputStream fis = new FileInputStream("src/data/mezcla.dat")) {

				// Leer los primeros 3 números
				System.out.println("Números:");
				for (int i = 0; i < 3; i++) {
					int numero = fis.read();
					System.out.println("Número leído: " + numero);
				}

				// Leer las cadenas de texto
				System.out.println("\nCadenas:");
				int valor;
				StringBuilder sb = new StringBuilder();

				while ((valor = fis.read()) != -1) {
					if (valor == '\n') {
						System.out.println("Cadena leída: " + sb.toString());
						sb.setLength(0); // Limpiar el StringBuilder
					} else {
						sb.append((char) valor);
					}
				}

				// Si queda algo por imprimir (si no hay un salto de línea al final)
				if (sb.length() > 0) {
					System.out.println("Cadena leída: " + sb.toString());
				}

			} catch (IOException e) {
				System.out.println("Ocurrió un error al leer el archivo.");
				e.printStackTrace();
			}

		} catch (IOException e) {
			System.out.println("Ocurrió un error al escribir en el archivo.");
			e.printStackTrace();
		}

	}

}
