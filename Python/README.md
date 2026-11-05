<p align="center"><img src="docs/banner.svg" alt="Python" width="100%"></p>

# 🐍 Python · Programación e Inteligencia Artificial

**Actividades resueltas de las tres primeras unidades de Python, más una mini librería de utilidades con sus pruebas.**

Cada actividad es un script independiente con su enunciado comentado al principio.

## 🗂️ Contenido

| Carpeta | Tema | Actividades |
|---|---|:--:|
| [`UD01_Introduccion_a_Python`](UD01_Introduccion_a_Python/Ejercicios) | Entorno, tipos, operadores, entrada/salida y depuración | 19 |
| [`UD02_Control_de_Flujo_y_Estructuras_de_Datos`](UD02_Control_de_Flujo_y_Estructuras_de_Datos/Ejercicios) | Condicionales, bucles, listas, diccionarios y funciones | 42 |
| [`UD03_Archivos_Errores_y_Modularizacion`](UD03_Archivos_Errores_y_Modularizacion/Ejercicios) | Lectura y escritura de ficheros, excepciones y módulos | 17 |
| [`Examen_UD02`](Examen_UD02) | Examen de la unidad 2 (2 ejercicios) | 2 |
| [`utilidades`](utilidades) | Paquete `ficheros` con funciones reutilizables de rutas y ficheros | — |
| [`pruebas`](pruebas) | Pruebas de `utilidades` | — |

## 🚀 Ejecución

Necesitas **Python 3.10 o superior**; no hay dependencias externas.

```bash
python3 UD01_Introduccion_a_Python/Ejercicios/a1_hola_entorno.py
```

Algunos ejercicios piden datos por teclado.

## 🧪 Pruebas

Las pruebas usan solo `unittest` de la librería estándar:

```bash
python3 -m unittest discover -s pruebas -v
```

## 🧰 Tecnologías

- Python 3 · `os`, `unittest`
