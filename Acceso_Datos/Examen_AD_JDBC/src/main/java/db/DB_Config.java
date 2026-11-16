package db;

public class DB_Config {
    private final String URL = "jdbc:mariadb://localhost:3306/Mi_Aucorsa";
    private final String USUARIO = "root";
    private final String CONTRASENA = "root";

    public String getURL() {
        return this.URL;
    }

    public String getUSUARIO() {
        return this.USUARIO;
    }

    public String getCONTRASENA() {
        return this.CONTRASENA;
    }
}
