package modulo5OODB.savethegame;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;

public class JugadorB {
    public static void main(String[] args) {
        Partida partida;

        // Deserializar la partida
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("partida.ser"))) {
            partida = (Partida) in.readObject();
            System.out.println("Partida recibida: " + partida);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
            return;
        }

        // Actualizar el progreso de la partida
        partida.actualizarProgreso(2, 2000);
        System.out.println("Partida actualizada: " + partida);

        // Volver a enviar el archivo actualizado
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("partida_actualizada.ser"))) {
            out.writeObject(partida);
            System.out.println("Partida actualizada enviada de regreso al Jugador A.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}