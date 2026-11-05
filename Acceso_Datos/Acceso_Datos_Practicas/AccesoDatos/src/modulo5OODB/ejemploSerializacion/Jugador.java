package modulo5OODB.ejemploSerializacion;

import java.io.Serializable;

public class Jugador implements Serializable {
    private String nombre;
    private int nivel;
    private int puntuacion;
    public int dificultad; 
    //public String apellido;
    
    //private static final long serialVersionUID = 1L; // Cambiado de 1L a 2L


    public Jugador(String nombre, int nivel, int puntuacion) {
        this.nombre = nombre;
        this.nivel = nivel;
        this.puntuacion = puntuacion;
        this.dificultad = 10;
    }

    @Override
    public String toString() {
        return "Jugador [nombre=" + nombre + ", nivel=" + nivel + ", puntuacion=" + puntuacion + "]";
    }

	public int getNivel() {
		return nivel;
	}

	public void setNivel(int nivel) {
		this.nivel = nivel;
	}

	public int getPuntuacion() {
		return puntuacion;
	}

	public void setPuntuacion(int puntuacion) {
		this.puntuacion = puntuacion;
	}
}
