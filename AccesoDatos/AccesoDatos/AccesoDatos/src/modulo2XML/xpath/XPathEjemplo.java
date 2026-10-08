package modulo2XML.xpath;

import javax.xml.parsers.DocumentBuilderFactory;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathFactory;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathConstants;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import java.io.File;

/**
 * 
 *  /: El carácter de barra indica el inicio desde la raíz del documento XML.
	//: Selecciona nodos en todo el documento, sin importar dónde se encuentren.
	[]: Los corchetes se utilizan para aplicar condiciones o filtros.
	Por ejemplo, [1] selecciona el primer nodo en una secuencia.
	Las expresiones dentro de corchetes como [precio > 20] sirven para aplicar condiciones.
	@: Se usa para seleccionar un atributo.
	Por ejemplo, @categoria selecciona el atributo categoria de un elemento.
	text(): Selecciona el contenido de texto de un elemento.
	count(): Una función de XPath que cuenta el número de nodos coincidentes con la expresión.
 * 
 * 
 */


public class XPathEjemplo {

	 public static void main(String[] args) {
	      
		 try {
	         
	            // Obtenemos la ruta del proyecto
	            String rutaProyecto = System.getProperty("user.dir");
	            

	            // Ruta de la imagen original dentro de la carpeta 'src'
	            String rutaXMLOriginal = rutaProyecto + "/src/data/libros.xml";
	            
	            // Cargar el archivo XML
	            File archivoXML = new File(rutaXMLOriginal);
	            
	            
	            
	            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	            
	            Document documento = dBuilder.parse(archivoXML);

	            
	            // ENFATIZO NORMALIZAR SIEMPRE 
	            // Normalizar el documento XML (opcional pero recomendado)
	            documento.getDocumentElement().normalize();

	            // Crear el objeto XPath
	            XPath xPath = XPathFactory.newInstance().newXPath();
	            
	            // Ejemplo: 
	            String expresion4 = "/";
	            String titulo = xPath.compile(expresion4).evaluate(documento);
	            System.out.println("\nResultado: " + titulo);

	            // Ejemplo: Obtener todos los títulos de los libros
	            String expresion1 = "/libros/libro/titulo";
	            XPathExpression expr1 = xPath.compile(expresion1);
	            NodeList nodos = (NodeList) expr1.evaluate(documento, XPathConstants.NODESET);

	            System.out.println("Títulos de los libros:");
	            for (int i = 0; i < nodos.getLength(); i++) {
	                System.out.println(nodos.item(i).getTextContent());
	            }
	            
	            // //producto[precio > 50]
	            //  count(//empleado[salario > 2000])


	            // Ejemplo: Obtener el título del libro cuyo autor es "Ana García"
	            String expresion2 = "/libros/libro[autor='Ana García']/titulo";
	            String titulo1 = xPath.compile(expresion2).evaluate(documento);
	            System.out.println("\nLibro de Ana García: " + titulo1);

	            // Ejemplo: Contar cuántos libros hay
	            String expresion3 = "count(/libros/libro)";
	            Double cantidadLibros = (Double) xPath.compile(expresion3).evaluate(documento, XPathConstants.NUMBER);
	            System.out.println("\nNúmero de libros: " + cantidadLibros.intValue());

	        } catch (Exception e) {
	            e.printStackTrace();
	        }
	    }

}
