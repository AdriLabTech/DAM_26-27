package modulo2XML.xpath;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

public class Ejercicio1 {
    public static void main(String[] args) {
        try {
            // Cargar el documento XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse("src/data/libros.xml");

            // Crear objeto XPath
            XPathFactory xPathFactory = XPathFactory.newInstance();
            XPath xpath = xPathFactory.newXPath();

            // Consultar los títulos, autores y precios
            NodeList titulos = (NodeList) xpath.evaluate("*", document, XPathConstants.NODESET);
            NodeList autores = (NodeList) xpath.evaluate("/libros/libro/autor", document, XPathConstants.NODESET);
            NodeList precios = (NodeList) xpath.evaluate("/libros/libro/precio", document, XPathConstants.NODESET);

            // Mostrar los resultados
            for (int i = 0; i < titulos.getLength(); i++) {
                System.out.println("Título: " + titulos.item(i).getTextContent());
                System.out.println("Autor: " + autores.item(i).getTextContent());
                System.out.println("Precio: " + precios.item(i).getTextContent());
                System.out.println();
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
