package modulo2XML.sax;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

public class Ejercicio1 extends DefaultHandler {
    boolean esTitulo = false;
    boolean esAutor = false;
    boolean esPrecio = false;

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        if (qName.equalsIgnoreCase("titulo")) {
            esTitulo = true;
        } else if (qName.equalsIgnoreCase("autor")) {
            esAutor = true;
        } else if (qName.equalsIgnoreCase("precio")) {
            esPrecio = true;
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        if (esTitulo) {
            System.out.println("Título: " + new String(ch, start, length));
            esTitulo = false;
        } else if (esAutor) {
            System.out.println("Autor: " + new String(ch, start, length));
            esAutor = false;
        } else if (esPrecio) {
            System.out.println("Precio: " + new String(ch, start, length));
            esPrecio = false;
        }
    }
    
    public static void main(String[] args) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser saxParser = factory.newSAXParser();
            Ejercicio1 handler = new Ejercicio1();
            saxParser.parse("libros.xml", handler);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

