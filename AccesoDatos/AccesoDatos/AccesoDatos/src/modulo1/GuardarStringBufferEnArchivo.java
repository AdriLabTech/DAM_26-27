package modulo1;

import java.io.FileWriter;
import java.io.IOException;

public class GuardarStringBufferEnArchivo {
    public static void main(String[] args) {
        // Verificar si el usuario ha proporcionado el nombre del archivo como argumento
        if (args.length < 1) {
            System.out.println("Por favor, indica el nombre del archivo como argumento.");
            System.exit(0);
        }

        String nombreArchivo = args[0]; // Nombre del archivo desde los argumentos

        // Crear un StringBuffer y construir una cadena dinámica
        StringBuffer contenido = new StringBuffer();
        contenido.append("Este es un ejemplo de uso de StringBuffer.\n");
        contenido.append("Podemos añadir varias líneas de texto de manera eficiente.\n");
        contenido.append("Esta cadena será guardada en el archivo: " + nombreArchivo + "\n");

        // Guardar el contenido del StringBuffer en el archivo indicado
        try {
            FileWriter escritor = new FileWriter("src/data/" + nombreArchivo);

            // Escribir el contenido del StringBuffer en el archivo
            escritor.write(contenido.toString());

            // Cerrar el escritor para liberar recursos
            escritor.close();

            System.out.println("El contenido ha sido guardado en el archivo: " + nombreArchivo);
        } catch (IOException e) {
            System.out.println("Ocurrió un error al escribir en el archivo.");
            e.printStackTrace();
        }
    }
}

