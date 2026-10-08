package modulo2XML.dom;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import java.io.File;

public class CrearXML {
    public static void main(String[] args) {
        try {
            // Crear un nuevo documento XML
            DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
            Document doc = docBuilder.newDocument();
            

            // Crear el elemento raíz
            Element raizPadre = doc.createElement("personas");
         //  rootElement.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance");
         //   rootElement.setAttribute("xsi:noNamespaceSchemaLocation", "src/data/personas.xsd");
            doc.appendChild(raizPadre);

            // Crear primer elemento persona
            Element persona1 = doc.createElement("persona");
            raizPadre.appendChild(persona1);

            // Añadir nombre a la primera persona
            Element nombre1 = doc.createElement("nombre");
            nombre1.appendChild(doc.createTextNode("Juan"));
            persona1.appendChild(nombre1);

            // Añadir edad a la primera persona
            Element edad1 = doc.createElement("edad");
            edad1.appendChild(doc.createTextNode("30"));
            persona1.appendChild(edad1);

            // Crear segundo elemento persona
            Element persona2 = doc.createElement("persona");
            raizPadre.appendChild(persona2);

            // Añadir nombre a la segunda persona
            Element nombre2 = doc.createElement("nombre");
            nombre2.appendChild(doc.createTextNode("Ana"));
            persona2.appendChild(nombre2);

            // Añadir edad a la segunda persona
            Element edad2 = doc.createElement("edad");
            edad2.appendChild(doc.createTextNode("25"));
            persona2.appendChild(edad2);

            // Guardar el documento XML en un archivo
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            transformer.setOutputProperty(javax.xml.transform.OutputKeys.INDENT, "yes");
            
            /*
             *   // Definir propiedades de salida
    transformer.setOutputProperty(javax.xml.transform.OutputKeys.ENCODING, "UTF-8");  // Codificación UTF-8
    transformer.setOutputProperty(javax.xml.transform.OutputKeys.INDENT, "yes");  // Con indentación
    transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");  // 4 espacios
    transformer.setOutputProperty(javax.xml.transform.OutputKeys.OMIT_XML_DECLARATION, "no");  // Mantener declaración XML
    transformer.setOutputProperty(javax.xml.transform.OutputKeys.STANDALONE, "yes");  // Documento standalone
             * 
             * 
             * 
             */
            
            
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File("src/data/personasCreadas.xml"));
            transformer.transform(source, result);

            System.out.println("Archivo XML creado con éxito: personasCreadas.xml");

        } catch (Exception e) {
            System.out.println("Error al crear el archivo XML: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
