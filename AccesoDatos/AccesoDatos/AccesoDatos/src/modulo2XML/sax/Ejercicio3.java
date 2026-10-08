package modulo2XML.sax;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

public class Ejercicio3 extends DefaultHandler {
    boolean esNombre = false;
    boolean esDepartamento = false;
    boolean esSalario = false;
    String nombre = "";
    String departamento = "";

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        if (qName.equalsIgnoreCase("nombre")) {
            esNombre = true;
        } else if (qName.equalsIgnoreCase("departamento")) {
            esDepartamento = true;
        } else if (qName.equalsIgnoreCase("salario")) {
            esSalario = true;
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        if (esNombre) {
            nombre = new String(ch, start, length);
            esNombre = false;
        } else if (esDepartamento) {
            departamento = new String(ch, start, length);
            esDepartamento = false;
        } else if (esSalario && departamento.equals("IT")) {
            System.out.println("Empleado: " + nombre);
            System.out.println("Salario: " + new String(ch, start, length));
            esSalario = false;
        }
    }

    public static void main(String[] args) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser saxParser = factory.newSAXParser();
            Ejercicio3 handler = new Ejercicio3();
            saxParser.parse("src/data/empleados.xml", handler);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

