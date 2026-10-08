package modulo2XML.sax;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class EstudianteHandler extends DefaultHandler {

    boolean esNombre = false;
    boolean esEdad = false;

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        if (qName.equalsIgnoreCase("nombre")) {
            esNombre = true;  // Detectamos cuando comienza la etiqueta <nombre>
        } else if (qName.equalsIgnoreCase("edad")) {
            esEdad = true;  // Detectamos cuando comienza la etiqueta <edad>
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        if (esNombre) {
            System.out.println("Nombre: " + new String(ch, start, length));
            esNombre = false;  // Reiniciamos el estado después de leer el nombre
        } else if (esEdad) {
            System.out.println("Edad: " + new String(ch, start, length));
            esEdad = false;  // Reiniciamos el estado después de leer la edad
        }
    }

    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        // Aquí puedes realizar acciones al final de una etiqueta, si es necesario.
    }
}
