package modulo5OODB.savethegame;
import java.io.Serializable;

public class Partida implements Serializable {
    private String jugador;
    private int nivel;
    private int puntuacion;

    public Partida(String jugador, int nivel, int puntuacion) {
        this.jugador = jugador;
        this.nivel = nivel;
        this.puntuacion = puntuacion;
    }

    public void actualizarProgreso(int nuevoNivel, int nuevaPuntuacion) {
        this.nivel = nuevoNivel;
        this.puntuacion = nuevaPuntuacion;
    }

    @Override
    public String toString() {
        return "Jugador: " + jugador + ", Nivel: " + nivel + ", Puntuación: " + puntuacion;
    }
}