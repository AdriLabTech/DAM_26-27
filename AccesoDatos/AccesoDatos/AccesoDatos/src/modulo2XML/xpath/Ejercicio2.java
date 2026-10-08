package modulo2XML.xpath;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

public class Ejercicio2 {
    public static void main(String[] args) {
        try {
            // Cargar el documento XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse("peliculas.xml");

            // Crear objeto XPath
            XPathFactory xPathFactory = XPathFactory.newInstance();
            XPath xpath = xPathFactory.newXPath();

            // Consultar el número de películas
            NodeList peliculas = (NodeList) xpath.evaluate("/cine/pelicula", document, XPathConstants.NODESET);
            System.out.println("Número total de películas: " + peliculas.getLength());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
