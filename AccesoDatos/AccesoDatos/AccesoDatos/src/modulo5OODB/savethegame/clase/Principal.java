package modulo5OODB.savethegame.clase;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

import modulo5OODB.savethegame.Partida;

public class Principal {

	
	
	public static void main (String args[]) {
	
		Game partida  = new Game(200,55);
		guardarEstadoPartida(partida);
		
		 try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("src/data/partidaCLASE.ser"))) {
	           
			 Object obj = in.readObject();
			 
			 if(obj ==null ) {
				 if(obj instanceof Game) {
					 if (partida.equals(obj)){
						 
					 }
				 }
			 }
			 

			 
			 partida = (Game) in.readObject();
	         
			 
			 
			 System.out.println("Partida recibida: " + partida);
	        } catch (IOException | ClassNotFoundException e) {
	            e.printStackTrace();
	            return;
	        }
		
		
	}
	
	public static void guardarEstadoPartida(Game partida) {
		
			try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("src/data/partidaCLASE.ser"))) {
	            out.writeObject(partida);
	            System.out.println("Partida guardada y lista para enviar: " + partida);
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
		
	}
	public void cargarPartida() {
		
		
		

	}
	
	
	public void mostrarPartida() {
		
	}

	
}
