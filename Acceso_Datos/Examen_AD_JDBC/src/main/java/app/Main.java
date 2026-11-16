package app;

import db.DB_Conexion;
import model.Bus;
import utils.Utils;
import view.BusView;

import java.sql.Connection;
import java.sql.SQLException;

public class Main {
    private static Connection con;

    static {
        try {
            con = DB_Conexion.obtenerConexion();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws SQLException{
        System.out.println("GESTIÓN DE AUCROSA");
        System.out.println("conectando con la base de datos...");

        if (DB_Conexion.primeraConexionExitosa()){
            System.out.println("Base de datos conectada!");
        }

        BusView view = new BusView();

        int opcionUsuario;

        do {
            opcionUsuario = Utils.mostrarOpciones();

            switch (opcionUsuario){
                case 0 -> {
                    System.out.println("Saliendo...");
                }
                 case 1 -> {
                     view.mostrarTodosLosBuses();
                 }

                 case 2 -> {
                    String id = Utils.pedirCadenaAlUsuario("Introduce el Id del bus: ");
                    view.mostrarBusBuscado(id);
                 }

                 case 3 -> {
                     String id_Bus = Utils.pedirCadenaAlUsuario("Introduce un Id para el bus: ");
                     String tipo = Utils.pedirCadenaAlUsuario("Introduce un Tipo de Bus: ");
                     String liciencia = Utils.pedirCadenaAlUsuario("Introduce una Licencia de Bus: ");

                    Bus b = new Bus(id_Bus, tipo, liciencia);
                    view.mostrarBusAnadido(b);
                 }

                 case 4 -> {
                    String id_Bus = Utils.pedirCadenaAlUsuario("Introduce el Id del bus que quieras modificar: ");
                    String nuevoTipo = Utils.pedirCadenaAlUsuario("Introduce el nuevo tipo para el Bus: ");
                    String nuevaLicencia = Utils.pedirCadenaAlUsuario("Introduce la nueva Licencia para el Bus: ");

                    Bus b = new Bus(id_Bus, nuevoTipo, nuevaLicencia);
                    view.mostrarBusModificado(b, id_Bus);
                 }
            }

        } while (opcionUsuario != 0);
    }
}
