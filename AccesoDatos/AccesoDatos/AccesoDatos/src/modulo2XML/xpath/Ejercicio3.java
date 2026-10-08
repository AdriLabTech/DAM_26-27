package modulo2XML.xpath;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

public class Ejercicio3 {
    public static void main(String[] args) {
        try {
            // Cargar el documento XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse("empleados.xml");

            // Crear objeto XPath
            XPathFactory xPathFactory = XPathFactory.newInstance();
            XPath xpath = xPathFactory.newXPath();

            // Consultar los empleados del departamento IT
            NodeList empleadosIT = (NodeList) xpath.evaluate("/empresa/empleado[departamento='IT']", document, XPathConstants.NODESET);

            // Mostrar los resultados
            for (int i = 0; i < empleadosIT.getLength(); i++) {
                String nombre = xpath.evaluate("nombre", empleadosIT.item(i));
                String salario = xpath.evaluate("salario", empleadosIT.item(i));
                System.out.println("Empleado: " + nombre);
                System.out.println("Salario: " + salario);
                System.out.println();
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

