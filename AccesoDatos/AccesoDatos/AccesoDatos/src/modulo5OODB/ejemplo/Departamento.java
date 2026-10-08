package modulo5OODB.ejemplo;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.*;

@Entity
public class Departamento {
		@Id
	    @GeneratedValue
	    private int id;
	    public String nombre;
	    @OneToMany(mappedBy = "departamento", cascade = CascadeType.ALL)
	    private List<Empleado> empleados = new ArrayList<>();
	    public Departamento(String nombre) { this.nombre = nombre; }
	    public Departamento() {}
	    public void agregarEmpleado(Empleado e) {
	        empleados.add(e);
	        e.setDepartamento(this);
	    }
}