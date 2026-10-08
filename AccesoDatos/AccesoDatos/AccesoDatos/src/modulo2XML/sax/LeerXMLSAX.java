package modulo2XML.sax;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

/**
 * Diferencias entre SAX y DOM
Modelo de procesamiento:
DOM: Carga todo el documento XML en memoria como un árbol de nodos. Esto te permite navegar y modificar el documento de forma flexible, pero consume mucha memoria si el archivo es grande.
SAX: No carga todo el documento en memoria. Procesa el XML secuencialmente, disparando eventos cada vez que encuentra un elemento, lo que es mucho más eficiente para archivos grandes. No puedes modificar ni navegar por el documento de la misma manera que con DOM.
Memoria:
DOM: Requiere más memoria porque todo el documento se carga en RAM.
SAX: Usa menos memoria, ya que procesa el archivo línea por línea y no carga todo en memoria.
Accesibilidad:
DOM: Permite acceder a cualquier parte del documento en cualquier momento, ya que el documento está completamente cargado.
SAX: No permite acceso aleatorio al documento. Procesa el documento de manera secuencial y dispara eventos a medida que lee.
Modificaciones:
DOM: Permite modificar la estructura del documento XML (añadir, eliminar o modificar nodos).
SAX: No permite modificar el documento directamente, es solo para leer.
 * 
 */


public class LeerXMLSAX {

    public static void main(String[] args) {
        try {
            // Crear el SAXParserFactory y el SAXParser
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser saxParser = factory.newSAXParser();

            // Definir el manejador de eventos
            DefaultHandler handler = new DefaultHandler() {
                String currentElement = "";
             
                
                
                // Método que se ejecuta cuando encuentra el inicio de un elemento
                public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
                    currentElement = qName;
                    System.out.println("Inicio del elemento: " + qName);
                   
                    
                    /**
                     * Si utilizamos If para setear los datos, es recomendable identificar si existen
                    if (qName.equalsIgnoreCase("titulo")) {
                        titulo = true;
                    }
                    if (qName.equalsIgnoreCase("autor")) {
                        autor = true;
                    }
                    if (qName.equalsIgnoreCase("precio")) {
                        precio = true;
                    }
                    */
                    
                }

                // Método que se ejecuta cuando encuentra contenido entre elementos
                public void characters(char ch[], int start, int length) throws SAXException {
                    switch (currentElement.toLowerCase()) {
                        case "titulo":
                            System.out.println("Título: " + new String(ch, start, length));
                            break;
                        case "autor":
                            System.out.println("Autor: " + new String(ch, start, length));
                            break;
                        case "precio":
                            System.out.println("Precio: " + new String(ch, start, length));
                            break;
                        case "año":
                            System.out.println("Año: " + new String(ch, start, length));
                            break;
                        default:
                            break;
                    }
                }

                // Método que se ejecuta cuando encuentra el final de un elemento
                public void endElement(String uri, String localName, String qName) throws SAXException {
                    System.out.println("Fin del elemento: " + qName);
                    currentElement = "";  // Reseteamos el elemento actual
                }
            };

            // Leer el archivo XML
            saxParser.parse("src/Data/libros.xml", handler);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

