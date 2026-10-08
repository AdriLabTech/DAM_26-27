package modulo1.ejercicios;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class EjerciciosResueltos {

	public static void main(String[] args) {

		ejercicio1();
//		ejercicio2();
//		ejercicio3();
//		ejercicio4();
//		ejercicio5();
//		ejercicio6();
//		ejercicio7();
//		ejercicio8();
//		ejercicio9();
//		ejercicio10();

	}

	public static void ejercicio1() {

		String rutaArchivo = "/src/data/notas.txt";

		try (BufferedWriter writer = new BufferedWriter(new FileWriter(rutaArchivo))) {
			writer.write("Matemáticas: 95\n");
			writer.write("Ciencias: 88\n");
			writer.write("Historia: 76\n");
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void ejercicio2() {
		String rutaArchivo = "/src/data/notas.txt";

		try (BufferedReader reader = new BufferedReader(new FileReader(rutaArchivo))) {
			String linea;
			while ((linea = reader.readLine()) != null) {
				System.out.println(linea);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void ejercicio3() {
		String rutaArchivo = "/src/data/notas.txt";

		try (BufferedWriter writer = new BufferedWriter(new FileWriter(rutaArchivo, true))) {
			writer.write("Inglés: 90\n");
			writer.write("Arte: 85\n");
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void ejercicio4() {
		String rutaArchivo = "/src/data/notas.txt";
		int contadorLineas = 0;

		try (BufferedReader reader = new BufferedReader(new FileReader(rutaArchivo))) {
			while (reader.readLine() != null) {
				contadorLineas++;
			}
			System.out.println("Número total de líneas: " + contadorLineas);
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void ejercicio5() {
		String rutaArchivo = "/src/data/notas.txt";

		try (BufferedWriter writer = new BufferedWriter(new FileWriter(rutaArchivo))) {
			writer.write("Archivo limpio\n");
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void ejercicio6() {
		String rutaArchivo = "/src/data/nombres.txt";
		Scanner scanner = new Scanner(System.in);

		try (BufferedWriter writer = new BufferedWriter(new FileWriter(rutaArchivo))) {
			for (int i = 0; i < 5; i++) {
				System.out.print("Introduce un nombre: ");
				String nombre = scanner.nextLine();
				writer.write(nombre + "\n");
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			scanner.close();
		}
	}

	public static void ejercicio7() {
		String rutaArchivo = "/src/data/nombres.txt";

		try (BufferedReader reader = new BufferedReader(new FileReader(rutaArchivo))) {
			String nombre;
			while ((nombre = reader.readLine()) != null) {
				System.out.println(nombre);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	public static void ejercicio8() {
		String rutaArchivo = "/src/data/nombres.txt";

		Scanner scanner = new Scanner(System.in);
		System.out.print("Introduce el nombre a buscar: ");
		String nombreBuscado = scanner.nextLine();
		boolean encontrado = false;

		try (BufferedReader reader = new BufferedReader(new FileReader(rutaArchivo))) {
			String nombre;
			while ((nombre = reader.readLine()) != null) {
				if (nombre.equalsIgnoreCase(nombreBuscado)) {
					encontrado = true;
					break;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		if (encontrado) {
			System.out.println("El nombre fue encontrado.");
		} else {
			System.out.println("El nombre no fue encontrado.");
		}
		scanner.close();

	}

	public static void ejercicio9() {
		String archivoOrigen = "/src/data/nombres.txt";
        String archivoDestino = "/src/data/nombres_copia.txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(archivoOrigen));
             BufferedWriter writer = new BufferedWriter(new FileWriter(archivoDestino))) {
             
            String linea;
            while ((linea = reader.readLine()) != null) {
                writer.write(linea + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

	}

	public static void ejercicio10() {
		
		 String rutaArchivo = "/src/data/nombres.txt";
	        Scanner scanner = new Scanner(System.in);
	        String actividad;

	        try (BufferedWriter writer = new BufferedWriter(new FileWriter(rutaArchivo, true))) {
	            while (true) {
	                System.out.print("Introduce una actividad (o escribe 'salir' para terminar): ");
	                actividad = scanner.nextLine();
	                if (actividad.equalsIgnoreCase("salir")) {
	                    break;
	                }
	                writer.write(actividad + "\n");
	            }
	        } catch (IOException e) {
	            e.printStackTrace();
	        } finally {
	            scanner.close();
	        }

	}

}
