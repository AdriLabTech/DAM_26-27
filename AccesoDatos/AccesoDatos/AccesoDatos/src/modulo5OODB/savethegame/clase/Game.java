package modulo5OODB.savethegame.clase;

import java.io.Serializable;


public class Game implements Serializable{
	
	private int score = 0;
	private int level = 0;
	
    private static final long serialVersionUID = 123456789L; // Cambiado de 1L a 2L
	
	Game(int score, int level){
		this.score = score;
		this.level = level;
	}

	public int getScore() {
		return score;
	}

	public void setScore(int score) {
		this.score = score;
	}

	public int getLevel() {
		return level;
	}

	public void setLevel(int level) {
		this.level = level;
	}

	@Override
	public String toString() {
		return "Game [score=" + score + ", level=" + level + "]";
	}	
	

}
