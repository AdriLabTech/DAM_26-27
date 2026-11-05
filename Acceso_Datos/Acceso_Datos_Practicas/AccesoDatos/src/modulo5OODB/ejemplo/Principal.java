package modulo5OODB.ejemplo;

import javax.persistence.*;
import java.util.List;

public class Principal {
	 public static void main(String[] args) {
	      
		    EntityManagerFactory emf = Persistence.createEntityManagerFactory("objectdb:src/data/empresa.odb");
	        EntityManager em = emf.createEntityManager();


	        
	        Departamento dpto = new Departamento("Desarrollo");
	        Empleado emp1 = new Empleado("Alice", 50000);
	        Empleado emp2 = new Empleado("Bob", 55000);
	        Proyecto proyecto = new Proyecto("Sistema CRM");

	        // Inserción de datos
	        em.getTransaction().begin();
	        
	        
	        Departamento d1 = new Departamento("IT");
	        Departamento d2 = new Departamento("RRHH");
	        Departamento d3 = new Departamento("Azotes");

	        
	        Empleado e1 = new Empleado("Ana", 60000);
	        Empleado e2 = new Empleado("Luis", 45000);
	        Empleado e3 = new Empleado("Clara", 52000);
	        
	        Proyecto p1 = new Proyecto("Intranet");
	        Proyecto p2 = new Proyecto("Sistema Nóminas");
	        
	        d1.agregarEmpleado(e1);
	        d1.agregarEmpleado(e3);
	        d2.agregarEmpleado(e2);
	        
	        e1.asignarProyecto(p1);
	        e2.asignarProyecto(p2);
	        
	        em.persist(d1);
	        em.persist(d2);
	        em.persist(d3);

	        

	        em.getTransaction().commit();
	        
	        
	        
	        

	        TypedQuery<Empleado> query = em.createQuery("SELECT e FROM Empleado e WHERE e.departamento.nombre = 'Desarrollo'", Empleado.class);
	      
	        
	        List<Empleado> empleados = query.getResultList();

	        for (Empleado e : empleados) {
	            System.out.println("Empleado: " + e.nombre);
	        }
	        
	     // 1. Listado de todos los departamentos
	        List<Departamento> departamentos = em.createQuery("SELECT d FROM Departamento d", Departamento.class).getResultList();
	        for (Departamento d : departamentos) {
	            System.out.println("Departamento: " + d.nombre);
	        }

	        // 2. Empleados con salario mayor a 50000
	        List<Empleado> altosSalarios = em.createQuery("SELECT e FROM Empleado e WHERE e.salario > 50000", Empleado.class).getResultList();
	        for (Empleado e : altosSalarios) {
	            System.out.println("Empleado: " + e.nombre + " - Salario: " + e.salario);
	        }

	        // 3. Proyectos asignados a empleados
	        List<Proyecto> proyectos = em.createQuery("SELECT p FROM Proyecto p", Proyecto.class).getResultList();
	        for (Proyecto p : proyectos) {
	            System.out.println("Proyecto: " + p.nombre);
	        }

	        // 4. Número de empleados por departamento
	        List<Object[]> empleadosPorDpto = em.createQuery("SELECT d.nombre, COUNT(e) FROM Empleado e JOIN e.departamento d GROUP BY d.nombre").getResultList();
	        for (Object[] r : empleadosPorDpto) {
	            System.out.println("Departamento: " + r[0] + " - Empleados: " + r[1]);
	        }

	        // 5. Empleados sin proyecto asignado
	        List<Empleado> sinProyecto = em.createQuery("SELECT e FROM Empleado e WHERE e.proyecto IS NULL", Empleado.class).getResultList();
	        for (Empleado e : sinProyecto) {
	            System.out.println("Empleado sin proyecto: " + e.nombre);
	        }

	        

	        em.close();
	        emf.close();
	    }
}