package modulo2XML;

import java.io.*;


import org.xmldb.api.DatabaseManager;
import org.xmldb.api.base.Collection;
import org.xmldb.api.base.Database;
import org.xmldb.api.base.XMLDBException;
import org.xmldb.api.modules.CollectionManagementService;
import org.xmldb.api.modules.XMLResource;
import org.xmldb.api.modules.XPathQueryService;

public class EjemploExistDb {
    public static void main(String[] args) throws Exception {
     
    	// URL de conexión al servidor eXist-db
        String uri = "xmldb:exist://localhost:8080/exist/xmlrpc";
        
        // Usuario y contraseña
        String user = "admin";
        String password = "1234";
        
        // Inicialización del driver de eXist-db
        Class<?> cl = Class.forName("org.exist.xmldb.DatabaseImpl");
        Database database = (Database) cl.getDeclaredConstructor().newInstance();
        database.setProperty("create-database", "true");
       
        DatabaseManager.registerDatabase(database);
        
        // Conexión a la colección raíz
        Collection col = DatabaseManager.getCollection(uri + "/db", user, password);
        
        Collection col2 = DatabaseManager.getCollection(uri + "/db/Tienda", user, password);

        //crearColeccionAddXML(col);
       // addXmlColeccion(col2);
        consultaDatos(col);
        
        col.close();  // Cerrar la colección
        col2.close();
    }

	private static void consultaDatos(Collection col) {
		try {
      // Servicio de consultas XPath
      XPathQueryService service = (XPathQueryService) col.getService("XPathQueryService", "1.0");
      
      
      // Consulta XPath
      String query = "for $book in doc(\"/db/libreria/libros.xml\")//libros\n"
      		+ "return $book//libro[titulo=\"Para gustos colores\"]/autor";
      var result = service.query(query);
      
      // Mostrar resultados
      for (int i = 0; i < result.getSize(); i++) {
          System.out.println(result.getResource(i).getContent());
      }
		} catch (XMLDBException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
      
		
	}

	private static void addXmlColeccion(Collection col2) {
	    // Paso 3: Crear o cargar el recurso XML (el archivo generado)
        
		try {
		File file = new File("src/main/java/com/cf/librerias/ejemploExist/personas.xml");
        
        if(!file.exists())
        	System.out.println("No Existe");
       
        XMLResource document;
		
			document = (XMLResource) col2.createResource(file.getName(), "XMLResource");
		
        document.setContent(file); // Asociar el archivo al recurso

        // Paso 4: Almacenar el documento en la colección
        col2.storeResource(document);
        System.out.println("Documento XML insertado en la colección.");		
		} catch (XMLDBException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void crearColeccionAddXML(Collection col) {
		  //Crear una nueva colección
        CollectionManagementService mgtService;
		try {
			mgtService = (CollectionManagementService) col.getService("CollectionManagementService", "1.0");
	
        String newCollectionName = "Tienda";  // Nombre de la nueva colección
        Collection newCollection = mgtService.createCollection(newCollectionName);
        System.out.println("Colección creada: " + newCollection.getName());
        

    
		} catch (XMLDBException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

