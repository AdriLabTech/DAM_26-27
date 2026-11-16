package controller;

import model.Bus;
import service.BusService;

import java.util.List;

public class BusController {
    private BusService service;

    public BusController(){
        this.service = new BusService();
    }

    public List<Bus> obtenerTodosLosBuses(){
        return service.obtenerTodosLosBuses();
    }

    public Bus buscarBus(String id_bus){
        return service.buscarBus(id_bus);
    }

    public boolean anadirNuevoBus(Bus nuevo){
        return service.anadirNuevoBus(nuevo);
    }

    public Bus modificarBus(Bus nuevo, String id_busAntiguo){
        return service.modificarBus(nuevo, id_busAntiguo);
    }
}
