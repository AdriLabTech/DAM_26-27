package dao;

import db.DB_Conexion;
import model.Bus;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class BusDAO {
    //Metodos CRUD
    //Consultar (Mostrar todos + buscar)
    public List<Bus> obtenerTodosLosBuses(){
        String consulta = "SELECT * FROM Bus";

        try(Connection con = DB_Conexion.obtenerConexion();
            PreparedStatement ps = con.prepareStatement(consulta);
            ResultSet rs = ps.executeQuery()) {
            List<Bus> buses = new ArrayList<>();

            while(rs.next()){ //Nuevo registro
                String id = rs.getString(1);
                String tipo = rs.getString(2);
                String licencia = rs.getString(3);

                buses.add(new Bus(id, tipo, licencia));
            }

            return buses;

        }catch (SQLException e){
            e.printStackTrace();
        }
        return null;
    }

    public Bus buscarBus(String id_b){
        String consulta = "SELECT * FROM Bus WHERE Id_B = ?;";

        try(Connection con = DB_Conexion.obtenerConexion();
            PreparedStatement ps = con.prepareStatement(consulta)){

            ps.setString(1, id_b);
            ResultSet rs = ps.executeQuery();

            while (rs.next()){
                String id = rs.getString(1);
                String tipo = rs.getString(2);
                String licencia = rs.getString(3);

                return new Bus(id, tipo, licencia);
            }

        }catch (SQLException e){
            e.printStackTrace();
        }
        return null;
    }


    //Anadir
    public boolean anadirNuevoBus(Bus nuevo){
        String consulta = "INSERT INTO Bus VALUES (?,?,?);";

        try (Connection con = DB_Conexion.obtenerConexion();
            PreparedStatement ps = con.prepareStatement(consulta)){
            ps.setString(1, nuevo.getId_Bus());
            ps.setString(2, nuevo.getTipo());
            ps.setString(3, nuevo.getLicencia());

            return ps.executeUpdate() > 0;

        } catch (SQLException e){
            e.printStackTrace();
        }
        return false;
    }

    //Modificar
    public Bus modificarBus(Bus nuevo, String id_busAntiguo){
        String consulta = "UPDATE Bus" +
                "SET Tipo = ?, Licencia = ?" +
                "WHERE Id_B = ?";

        try(Connection con = DB_Conexion.obtenerConexion();
            PreparedStatement ps = con.prepareStatement(consulta);
            ){

            ps.setString(1,nuevo.getTipo());
            ps.setString(2,nuevo.getLicencia());

            ps.setString(3, id_busAntiguo);

            ResultSet rs = ps.executeQuery();

            if (rs.next()){
                String id = rs.getString(1);
                String tipo = rs.getString(2);
                String licencia = rs.getString(3);

                return new Bus(id, tipo, licencia);
            }

        } catch (SQLException e){
            e.printStackTrace();
        }

        return null;
    }
}
