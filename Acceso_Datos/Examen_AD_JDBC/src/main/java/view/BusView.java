package view;

import controller.BusController;
import model.Bus;

import java.util.List;

public class BusView {
    private static BusController controller;

    public BusView(){
        controller = new BusController();
    }


    public static void mostrarTodosLosBuses(){
        List<Bus> buses = controller.obtenerTodosLosBuses();

        for (Bus b : buses){
            System.out.println("Bus -> " + b.toString());
            System.out.println("_".repeat(40));
        }
    }

    public static void mostrarBusBuscado(String id_b){
        Bus b = controller.buscarBus(id_b);

        if (b != null) {
            System.out.println("Bus encontrado!!!");
            System.out.println(b.toString());
        } else {
            System.err.println("[ERROR]: No hay bus con ese ID");
        }

    }

    public static void mostrarBusAnadido(Bus b){
        if (controller.buscarBus(b.getId_Bus()) != null){
            System.err.println("[ERROR]: El Bus ya existe");
        }else {

            if(controller.anadirNuevoBus(b)){
                System.out.println("Bus creado correctamente");
            } else {
                System.err.println("[ERROR]: registro no guardado");
            }
        }
    }

    public static void mostrarBusModificado(Bus nuevoBus, String id){
        Bus antiguoBus = controller.buscarBus(id);

        if (antiguoBus != null) {
            System.out.println("Bus encontrado!!! Pasando a su modificacion");
            antiguoBus.setTipo(nuevoBus.getTipo());
            antiguoBus.setLicencia(nuevoBus.getLicencia());

            System.out.println("Bus Modificado con exito");
        }else{
            System.err.println("[ERROR]: Id del bus no encontado");
        }

    }
}
