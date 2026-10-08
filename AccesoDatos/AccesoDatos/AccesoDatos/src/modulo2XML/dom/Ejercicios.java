package modulo2XML.dom;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

import java.io.File;
import java.util.Scanner;


public class Ejercicios {

	public static void main(String[] args) {

		/*
		 *  TransformerFactory transformerFactory = TransformerFactory.newInstance();
			Transformer transformer = transformerFactory.newTransformer();
			
			// Configurar propiedades de salida para el formateo
			transformer.setOutputProperty(javax.xml.transform.OutputKeys.INDENT, "yes");
			transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");  // Indentación de 4 espacios
			transformer.setOutputProperty(javax.xml.transform.OutputKeys.OMIT_XML_DECLARATION, "no");  // No omitir la declaración XML
			transformer.setOutputProperty(javax.xml.transform.OutputKeys.ENCODING, "UTF-8");  // Codificación UTF-8
			
			
			STANDALONE Esta propiedad indica si el documento XML es independiente de otros documentos externos.
			transformer.setOutputProperty(javax.xml.transform.OutputKeys.STANDALONE, "yes");

		 * 
		 * 
		 */
		
		//ejercicio1();
		//ejercicio3();
		//ejercicio2();

		//ejercicio4();
		ejercicio5();
	}

	private static void ejercicio1() {
		 try {
	            // Crear el documento
	            DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
	            DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
	            Document doc = docBuilder.newDocument();

	            // Crear el elemento raíz
	            Element rootElement = doc.createElement("tienda");
	            doc.appendChild(rootElement);

	            // Crear la primera canción
	            Element cancion1 = doc.createElement("cancion");
	            rootElement.appendChild(cancion1);

	            Element titulo1 = doc.createElement("titulo");
	            titulo1.appendChild(doc.createTextNode("Imagine"));
	            cancion1.appendChild(titulo1);

	            Element artista1 = doc.createElement("artista");
	            artista1.appendChild(doc.createTextNode("John Lennon"));
	            cancion1.appendChild(artista1);

	            Element duracion1 = doc.createElement("duracion");
	            duracion1.appendChild(doc.createTextNode("3:05"));
	            cancion1.appendChild(duracion1);

	            // Crear la segunda canción
	            Element cancion2 = doc.createElement("cancion");
	            rootElement.appendChild(cancion2);

	            Element titulo2 = doc.createElement("titulo");
	            titulo2.appendChild(doc.createTextNode("Billie Jean"));
	            cancion2.appendChild(titulo2);

	            Element artista2 = doc.createElement("artista");
	            artista2.appendChild(doc.createTextNode("Michael Jackson"));
	            cancion2.appendChild(artista2);

	            Element duracion2 = doc.createElement("duracion");
	            duracion2.appendChild(doc.createTextNode("4:54"));
	            cancion2.appendChild(duracion2);

	            // Guardar el archivo XML
	            TransformerFactory transformerFactory = TransformerFactory.newInstance();
	            Transformer transformer = transformerFactory.newTransformer();
	            transformer.setOutputProperty(javax.xml.transform.OutputKeys.INDENT, "yes");
				transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");  // Indentación de 4 espacios
				transformer.setOutputProperty(javax.xml.transform.OutputKeys.OMIT_XML_DECLARATION, "no");  // No omitir la declaración XML
				transformer.setOutputProperty(javax.xml.transform.OutputKeys.ENCODING, "UTF-8"); 
	            DOMSource source = new DOMSource(doc);
	            StreamResult result = new StreamResult(new File("src/data/canciones.xml"));
	            transformer.transform(source, result);

	            System.out.println("Archivo XML creado con éxito.");

	        } catch (Exception e) {
	            e.printStackTrace();
	        }		
	}
	private static void ejercicio2() {
		 try {
	            // Cargar el archivo XML
	            File archivo = new File("src/data/canciones.xml");
	            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	            Document doc = dBuilder.parse(archivo);
	            doc.getDocumentElement().normalize();

	            // Obtener todas las canciones
	            NodeList listaCanciones = doc.getElementsByTagName("cancion");

	            // Recorrer las canciones
	            for (int i = 0; i < listaCanciones.getLength(); i++) {
	                Element cancion = (Element) listaCanciones.item(i);
	                String titulo = cancion.getElementsByTagName("titulo").item(0).getTextContent();
	                String artista = cancion.getElementsByTagName("artista").item(0).getTextContent();
	                String duracion = cancion.getElementsByTagName("duracion").item(0).getTextContent();

	                System.out.println("Canción: " + titulo);
	                System.out.println("Artista: " + artista);
	                System.out.println("Duración: " + duracion);
	                System.out.println("----------");
	            }

	        } catch (Exception e) {
	            e.printStackTrace();
	        }
	}
	private static void ejercicio3() {
		 try {
	            // Cargar el archivo XML
	            File archivo = new File("src/data/canciones.xml");
	            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	            Document doc = dBuilder.parse(archivo);
	            doc.getDocumentElement().normalize();

	            // Obtener todas las canciones
	            NodeList listaCanciones = doc.getElementsByTagName("cancion");

	            // Pedir al usuario que elija una canción para modificar
	            Scanner scanner = new Scanner(System.in);
	            System.out.println("Elige la canción que deseas modificar (1 a " + listaCanciones.getLength() + "): ");
	            int index = scanner.nextInt() - 1;
	            scanner.nextLine();  // Limpiar el buffer
	            
	            System.out.println("Introduce la nueva duración: ");
	            String nuevaDuracion = scanner.nextLine();

	            // Modificar la duración
	            Element cancion = (Element) listaCanciones.item(index);
	            cancion.getElementsByTagName("duracion").item(0).setTextContent(nuevaDuracion);
	            cancion.setAttribute("id", "Valor");
	            // Guardar el archivo actualizado
	            TransformerFactory transformerFactory = TransformerFactory.newInstance();
	            Transformer transformer = transformerFactory.newTransformer();
	            DOMSource source = new DOMSource(doc);
	            StreamResult result = new StreamResult(new File("src/data/canciones_modificadas.xml"));
	            transformer.transform(source, result);

	            System.out.println("Archivo XML modificado con éxito.");

	        } catch (Exception e) {
	            e.printStackTrace();
	        }
		
	}
	private static void ejercicio4() {
		  try {
	            // Cargar el archivo XML
	            File archivo = new File("src/data/canciones.xml");
	            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	            Document doc = dBuilder.parse(archivo);
	          //  doc.getDocumentElement().normalize();

	            // Pedir al usuario los datos de la nueva canción
	            Scanner scanner = new Scanner(System.in);
	            System.out.println("Introduce el título de la nueva canción: ");
	            String titulo = scanner.nextLine();

	            System.out.println("Introduce el artista de la nueva canción: ");
	            String artista = scanner.nextLine();

	            System.out.println("Introduce la duración de la nueva canción: ");
	            String duracion = scanner.nextLine();

	            // Crear el nuevo elemento 'cancion'
	            Element nuevaCancion = doc.createElement("cancion");
	            Element nuevoTitulo = doc.createElement("titulo");
	            nuevoTitulo.appendChild(doc.createTextNode(titulo));
	            nuevaCancion.appendChild(nuevoTitulo);

	            Element nuevoArtista = doc.createElement("artista");
	            nuevoArtista.appendChild(doc.createTextNode(artista));
	            nuevaCancion.appendChild(nuevoArtista);

	            Element nuevaDuracion = doc.createElement("duracion");
	            nuevaDuracion.appendChild(doc.createTextNode(duracion));
	            nuevaCancion.appendChild(nuevaDuracion);

	            // Añadir la nueva canción al archivo XML
	            doc.getDocumentElement().appendChild(nuevaCancion);

	            // Guardar el archivo actualizado
	            TransformerFactory transformerFactory = TransformerFactory.newInstance();
	            Transformer transformer = transformerFactory.newTransformer();
	        	transformer.setOutputProperty(javax.xml.transform.OutputKeys.INDENT, "yes");
				transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "1");  // Indentación de 4 espacios
	            DOMSource source = new DOMSource(doc);
	            StreamResult result = new StreamResult(new File("src/data/canciones_actualizadas.xml"));
	            transformer.transform(source, result);

	            System.out.println("Nueva canción añadida con éxito.");

	        } catch (Exception e) {
	            e.printStackTrace();
	        }
		
	}
	private static void ejercicio5() {
		 try {
	            // Cargar el archivo XML
	            File archivo = new File("src/data/canciones.xml");
	            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
	            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
	            Document doc = dBuilder.parse(archivo);
	            doc.getDocumentElement().normalize();

	            // Obtener todas las canciones
	            NodeList listaCanciones = doc.getElementsByTagName("cancion");

	            // Validar la estructura
	            for (int i = 0; i < listaCanciones.getLength(); i++) {
	                Element cancion = (Element) listaCanciones.item(i);
	                String titulo = cancion.getElementsByTagName("titulo").item(0).getTextContent();
	                String artista = cancion.getElementsByTagName("artista").item(0).getTextContent();
	                String duracion = cancion.getElementsByTagName("duracion").item(0).getTextContent();

	                if (titulo.isEmpty() || artista.isEmpty() || duracion.isEmpty()) {
	                    System.out.println("Error: La canción " + (i + 1) + " está incompleta.");
	                } else {
	                    System.out.println("Canción " + (i + 1) + " válida.");
	                }
	            }

	        } catch (Exception e) {
	            e.printStackTrace();
	        }		
	}

}
