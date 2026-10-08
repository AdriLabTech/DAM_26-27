package modulo2XML.sax;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

public class SAXExample {
    public static void main(String[] args) {
        try {
            // Creamos una fábrica de parsers SAX
            SAXParserFactory factory = SAXParserFactory.newInstance();

            // Obtenemos un parser SAX
            SAXParser saxParser = factory.newSAXParser();

            // Leemos el archivo XML con nuestro handler personalizado
            EstudianteHandler handler = new EstudianteHandler();
            saxParser.parse("src/data/personas.xml", handler);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

