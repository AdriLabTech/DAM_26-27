package modulo5OODB.ejemplo;

import javax.persistence.*;

/**
 * Clase desarooarlash asd 
 * a
 * 
 * 
 */
@Entity
public class Empleado {
	 @Id
	    @GeneratedValue
	    private int id;
	    public String nombre;
	    public double salario;
	    @ManyToOne
	    private Departamento departamento;
	    @OneToOne(cascade = CascadeType.ALL)
	    private Proyecto proyecto;
	    public Empleado(String nombre, double salario) { this.nombre = nombre; this.salario = salario; }
	    public Empleado() {}
	    /**
	     * 
	     * 
	     * @param departamento parametros para pasra la clase de poer
	     */
	    public void setDepartamento(Departamento departamento) { this.departamento = departamento; }
	    
	    /**
	     * 
	     * @param proyecto 
	     */
	    public void asignarProyecto(Proyecto proyecto) { this.proyecto = proyecto; }

}
