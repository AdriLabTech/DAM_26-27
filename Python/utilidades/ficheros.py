# Fichero de utilidades para ficheros
import os

"""
A. Comprobación de rutas y archivos
Estos métodos evitan que tengas que repetir continuamente comprobaciones con os o pathlib.
Método	Función
existe_ruta(ruta)	Comprueba si existe una ruta.
es_fichero(ruta)	Comprueba si la ruta apunta a un archivo.
es_directorio(ruta)	Comprueba si la ruta apunta a un directorio.
esta_vacio(ruta)	Comprueba si un archivo tiene cero bytes.
obtener_nombre(ruta)	Devuelve el nombre del archivo, incluida su extensión.
obtener_extension(ruta)	Devuelve la extensión, por ejemplo .txt.
obtener_tamano(ruta)	Devuelve el tamaño del archivo en bytes.
crear_directorio(ruta)	Crea un directorio, incluidos los directorios padres que falten.
listar_ficheros(ruta)	Devuelve los archivos de un directorio.
buscar_ficheros(ruta, patron)	Busca archivos por patrón, por ejemplo *.txt.
"""


def existe_ruta(ruta):
    return os.path.exists(ruta)


def es_fichero(ruta):
    return os.path.isfile(ruta)


def es_directorio(ruta):
    return os.path.isdir(ruta)


def obtener_extension(ruta):
    if existe_ruta(ruta) and es_fichero(ruta):
        partes = ruta.split(".")
        return partes[-1]


"""
B. Lectura y escritura
Estos serían los métodos que más utilizarías en los ejercicios de clase.
Método	Función
leer_fichero(ruta)	Lee un archivo de texto completo.
escribir_fichero(ruta, contenido)	Escribe texto, sustituyendo el contenido anterior.
anadir_contenido(ruta, contenido)	Añade texto al final sin borrar lo existente.
leer_lineas(ruta)	Devuelve las líneas del archivo en una lista.
escribir_lineas(ruta, lineas)	Escribe una colección de líneas.
contar_lineas(ruta)	Cuenta las líneas del archivo.
buscar_texto(ruta, texto)	Comprueba si un texto aparece en el archivo.
reemplazar_texto(ruta, anterior, nuevo)	Sustituye las apariciones de un texto.
copiar_fichero(origen, destino)	Copia un archivo a otra ubicación.
mover_fichero(origen, destino)	Mueve un archivo.
renombrar_fichero(ruta, nuevo_nombre)	Cambia el nombre del archivo.
eliminar_fichero(ruta)	Elimina un archivo.
"""

"""
C. Gestión de datos y formatos
Cuando avances, te vendrá bien poder trabajar con datos estructurados sin repetir la lógica de apertura y cierre de archivos.
Método	Función
leer_json(ruta)	Lee un archivo JSON y devuelve sus datos.
escribir_json(ruta, datos)	Guarda datos en formato JSON.
leer_csv(ruta)	Lee un CSV y devuelve sus filas.
escribir_csv(ruta, datos, cabeceras)	Guarda datos tabulares en un CSV.
leer_fichero_seguro(ruta, predeterminado)	Devuelve un valor predeterminado si el archivo no existe.
crear_copia_seguridad(ruta, destino)	Crea una copia de un archivo.
calcular_hash_fichero(ruta)	Calcula un hash para comprobar la integridad de un archivo.
comparar_ficheros(ruta1, ruta2)	Comprueba si dos archivos tienen el mismo contenido.
obtener_tamano_directorio(ruta)	Calcula el tamaño total de los archivos de un directorio.
"""
