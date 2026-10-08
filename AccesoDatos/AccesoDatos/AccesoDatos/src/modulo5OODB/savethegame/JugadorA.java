package modulo5OODB.savethegame;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;

public class JugadorA {
    public static void main(String[] args) {
        Partida partida = new Partida("JugadorA", 1, 1000);

        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("partida.ser"))) {
            out.writeObject(partida);
            System.out.println("Partida guardada y lista para enviar: " + partida);
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Envía el archivo 'partida.ser' al Jugador B.");
    }
}
