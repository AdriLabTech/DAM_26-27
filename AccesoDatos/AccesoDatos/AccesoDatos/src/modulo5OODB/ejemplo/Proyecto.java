package modulo5OODB.ejemplo;


import javax.persistence.*;
import java.util.List;

@Entity
class Proyecto {
    @Id
    @GeneratedValue
    private int id;
    public String nombre;
    public Proyecto(String nombre) {
        this.nombre = nombre;
    }
    public Proyecto() {}
}