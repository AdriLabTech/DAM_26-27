package modulo2XML.sax;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

public class Ejercicio2 extends DefaultHandler {
    int contadorPeliculas = 0;

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        if (qName.equalsIgnoreCase("pelicula")) {
            contadorPeliculas++;
        }
    }

    @Override
    public void endDocument() throws SAXException {
        System.out.println("Número total de películas: " + contadorPeliculas);
    }

    public static void main(String[] args) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser saxParser = factory.newSAXParser();
            Ejercicio2 handler = new Ejercicio2();
            saxParser.parse("src/data/peliculas.xml", handler);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
