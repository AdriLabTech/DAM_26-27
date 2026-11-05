package modulo2XML.dom;

import java.io.File;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import org.w3c.dom.Element;

public class leerXML {
	
	public static void main(String[] args) {

		try {
			
			
		File xmlFile = new File("src/data/personas.xml");
		
		 // Verificar si el archivo existe
        if (!xmlFile.exists()) {
            System.out.println("El archivo XML no existe.");
            return;
        }
        
        
        DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
        Document doc = dBuilder.parse(xmlFile);
        doc.getDocumentElement().normalize();
        
        // Comprobar si el documento no es nulo
        if (doc != null) {
            System.out.println("El archivo XML se ha leído con éxito.");
            
            NodeList nList = doc.getElementsByTagName("persona");
            
            
            System.out.println("Número de personas: " + nList.getLength());
            
            for (int i = 0; i < nList.getLength(); i++) {
                Element element = (Element) nList.item(i);
                String nombre = element.getElementsByTagName("nombre").item(0).getTextContent();
                String edad = element.getElementsByTagName("edad").item(0).getTextContent();
                
                System.out.println("Nombre: " + nombre + ", Edad: " + edad);
            }
        } else
			System.out.println("El documento XML es nulo.");
		
		} catch (ParserConfigurationException | SAXException | IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
