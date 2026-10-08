package modulo5OODB.ejemploSerializacion;


import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class Principal {
	

	    public static void main(String[] args) {
	        
	    	//guardarProgreso();
	    	//guardarProgreso2();

	    	cargarProgreso();
	    	
	    	
	    }

		private static void cargarProgreso() {
			 try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("jugador.ser"))) {
		            Jugador jugador = (Jugador) in.readObject();
		            System.out.println("Progreso cargado: " + jugador);
		        } catch (IOException | ClassNotFoundException e) {
		            e.printStackTrace();
		        }			
		}

		private static void guardarProgreso() {
			Jugador jugador = new Jugador("Carlos", 5, 1200);

	        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("jugador.ser"))) {
	            out.writeObject(jugador);
	            
	            
	            System.out.println("Progreso guardado exitosamente.");
	        } catch (IOException e) {
	            e.printStackTrace();
	        }			
		}
		private static void guardarProgreso2() {
			Jugador jugador = new Jugador("Juan", 10, 1200);

	        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("jugador.ser"))) {
	            out.writeObject(jugador);
	            System.out.println("Progreso guardado exitosamente.");
	        } catch (IOException e) {
	            e.printStackTrace();
	        }			
		}
}

