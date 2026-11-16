package db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DB_Conexion {
    private static DB_Config config = new DB_Config();

    public static Connection obtenerConexion() throws SQLException {
        return DriverManager.getConnection(config.getURL(), config.getUSUARIO(), config.getCONTRASENA());
    }

    public static boolean primeraConexionExitosa() throws SQLException{
        return obtenerConexion() != null;
    }
}
