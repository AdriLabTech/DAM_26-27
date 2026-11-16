package model;

public class Bus {
    private String id_Bus;
    private String tipo;
    private String licencia;

    public Bus(){}

    public Bus(String id_Bus, String tipo, String licencia){
        this.id_Bus = id_Bus;
        this.tipo = tipo;
        this.licencia = licencia;
    }

    public String getId_Bus() {
        return id_Bus;
    }

    public void setId_Bus(String id_Bus) {
        this.id_Bus = id_Bus;
    }

    public String getLicencia() {
        return licencia;
    }

    public void setLicencia(String licencia) {
        this.licencia = licencia;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return "[" +
                "id_Bus='" + id_Bus + '\'' +
                ", tipo='" + tipo + '\'' +
                ", licencia='" + licencia + '\'' +
                ']';
    }
}
