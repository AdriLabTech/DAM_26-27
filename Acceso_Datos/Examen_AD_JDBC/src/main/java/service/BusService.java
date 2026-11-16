package service;

import dao.BusDAO;
import model.Bus;

import java.util.List;

public class BusService {
    private BusDAO dao;

    public BusService(){
        this.dao = new BusDAO();
    }

    public List<Bus> obtenerTodosLosBuses(){
        return dao.obtenerTodosLosBuses();
    }

    public Bus buscarBus(String id_bus){
        return dao.buscarBus(id_bus);
    }

    public boolean anadirNuevoBus(Bus nuevo){
        return dao.anadirNuevoBus(nuevo);
    }

    public Bus modificarBus(Bus nuevo, String id_busAntiguo){
        return dao.modificarBus(nuevo, id_busAntiguo);
    }
}
