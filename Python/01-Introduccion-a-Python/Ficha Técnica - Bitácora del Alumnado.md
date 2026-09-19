---
# Ficha técnica 1 - UD1 — Introducción a Python y entornos de desarrollo
---
## Python aplicado a la Inteligencia Artificial -2º DAM


### Datos generales del alumno/a

| Campo              | Contenido                                             |
| ------------------ | ----------------------------------------------------- |
| Nombre y Apellidos | Adrián Velasco Mañas.                                 |
| Unidad didáctiva   | UD1 - Introducción a Python y entornos de desarrollo. |
| Fecha de Entrega   | 30/9/2026                                             |

### Ficha de actividad - Ejercicio 1

| Campo                                                       | Contenido                                                                                                                                                                                                |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 1                                                                                                                                                                                                        |
| Titulo de la Actividad                                      | Configuración del entorno de desarrollo.                                                                                                                                                                 |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                                                             |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                                                                |
| Objetivo de la actividad                                    | Configurar el entorno instalando Python y activando el entorno virtual.                                                                                                                                  |
| Descripción del proceso seguido                             | Instalamos Python (`sudo pacman -S python`) y comprobamos la versión (3.14.7). Creamos el entorno virtual (`python3 -m venv .venv`) y lo activamos (`source .venv/bin/activate`).                        |
| Codigo                                                      | Fichero `hola_entorno.py` junto a la captura `docs/capturas/a1_creacion_entorno.png`.                                                                                                                    |
| Resultado Obtenido                                          | El entorno fue creado correctamente.                                                                                                                                                                     |
| Dificultadoes encontradas y soluciones                      | Al tener una shell diferente a lo habitual, como son Bash o Zsh, Fish (mi shell de trabajo), la forma de activar el entorno virtual es diferente (el comando source apunta a `.venv/bin/activate.fish`). |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                                                      |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Adecuado.                                                                                                                                                                                                |

### Ficha de actividad - Ejercicio 2

| Campo                                                       | Contenido                                                                                                                          |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 2                                                                                                                                  |
| Titulo de la Actividad                                      | Hola, mundo personalizado.                                                                                                         |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                       |
| Fecha de Realización                                        | 16/9/2026                                                                                                                          |
| Objetivo de la actividad                                    | Mostrar los valores de las variables usando `print()`.                                                                             |
| Descripción del proceso seguido                             | Creamos un fichero de python, donde declararemos las variables que nos piden y, usando el metodo `print()`, imprimiremos su valor. |
| Codigo                                                      | Fichero `ejercicios/a2_hola.py` junto a la imagen `docs/capturas/a2_hola.png`.                                                     |
| Resultado Obtenido                                          | La ejecuccion del programa muestra los valores pedidos.                                                                            |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                           |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                         |

### Ficha de actividad - Ejercicio 3

| Campo                                                       | Contenido                                                                                                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 3                                                                                                                                                                   |
| Titulo de la Actividad                                      | Saludo Interactivo.                                                                                                                                                 |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                        |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                           |
| Objetivo de la actividad                                    | Preguntar al usuario por su nombre y mostrar por pantalla un mensaje personalizado usando su nombre.                                                                |
| Descripción del proceso seguido                             | Usando input, podemos guardar en una variable lo que introduzca el usuario (ese será el nombre). Una vez guardado, lo mostraremos por pantalla usando `print(f"")`. |
| Codigo                                                      | Fichero `ejercicios/a3_saludo.py` junto a la imagen `docs/capturas/a3_saludo.png`.                                                                                  |
| Resultado Obtenido                                          | La ejecuccion del programa muestra la bienvenida con el nombre del Usuario.                                                                                         |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                            |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                 |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                          |


### Ficha de actividad - Ejercicio 4

| Campo                                                       | Contenido                                                                                                                                                                          |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 4                                                                                                                                                                                  |
| Titulo de la Actividad                                      | Variables básicas.                                                                                                                                                                 |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                                       |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                                          |
| Objetivo de la actividad                                    | Declarar 4 variables y mostrar sus tipos.                                                                                                                                          |
| Descripción del proceso seguido                             | Usando input, podemos guardar en las 4 variable lo que introduzca el usuario. Con esos datos, usamos `print(f"{type(<VARIABLE>)}")` para mostrar el tipo de dato de cada variable. |
| Codigo                                                      | Fichero `ejercicios/a4_variables.py` junto a la imagen `docs/capturas/a4_variables.png`.                                                                                           |
| Resultado Obtenido                                          | La ejecuccion del programa muestra los cuatro tipos de dato de las variables.                                                                                                      |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                                           |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                                |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                                         |


### Ficha de actividad - Ejercicio 5

| Campo                                                       | Contenido                                                                                                                                                                                  |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Nº de Actividad                                             | 5                                                                                                                                                                                          |
| Titulo de la Actividad                                      | Comprobando el tipado dinámico.                                                                                                                                                            |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                                               |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                                                  |
| Objetivo de la actividad                                    | Declarar una variable con un valor numerico, mostrar su tipo; y cambiar su valor por una cadena de texto para mostrar el nuevo tipo de dato.                                               |
| Descripción del proceso seguido                             | Guardamos dentro de la variable 'dato' el valor `10`, mostramos su tipo usando `print(f"{type(dato)}")`. Posteriormente modificamos el valor de la variable y volvemos a imprimir su tipo. |
| Codigo                                                      | Fichero `ejercicios/a5_tipado_dinamico.py` junto a la imagen `docs/capturas/a5_tipado_dinamico.png`.                                                                                       |
| Resultado Obtenido                                          | La ejecuccion del programa muestra ambos tipos de dato, tanto `<class 'int'>` como `<class 'str'>`.                                                                                        |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                                                   |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                                        |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                                                 |


### Ficha de actividad - Ejercicio 6

| Campo                                                       | Contenido                                                                                                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 6                                                                                                                                                                   |
| Titulo de la Actividad                                      | Varias lineas con print().                                                                                                                                          |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                        |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                           |
| Objetivo de la actividad                                    | Mostrar varias variables dentro de una sola llamada a `print()`, separando cada elemento usando el operador `sep`.                                                  |
| Descripción del proceso seguido                             | Instanciamos las 3 variables y usamos el print concatenando cada variable entre comas, dejando al final el operador sep: `print(nombre, edad, ciudad, sep=' \| ')`. |
| Codigo                                                      | Fichero `ejercicios/a6_varios_prints.py` junto a la imagen `docs/capturas/a6_varios_prints.png`.                                                                    |
| Resultado Obtenido                                          | La ejecuccion del programa muestra el valor de las 3 variables separadas por el contenido del separador.                                                            |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                            |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                 |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                          |



### Ficha de actividad - Ejercicio 7

| Campo                                                       | Contenido                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 7                                                                                                                                                                                                                                                                   |
| Titulo de la Actividad                                      | Calculadora básica.                                                                                                                                                                                                                                                 |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                                                                                                                        |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                                                                                                                           |
| Objetivo de la actividad                                    | Pedir dos numeros y mostrar el resultado de la suma, la resta, la multiplicacion, la division, la division entera, el modulo y la potencia de dichos numeros.                                                                                                       |
| Descripción del proceso seguido                             | Usando unicamente el metodo `input()` obtendremos una cadena de texto, asi que para obtener un numero entero, usaremos `int(input())`. Una vez tengamos las variables, procedemos con las operaciones (`+,-,*,/,//,%,**`) para finalmente lo mostramos por pantalla |
| Codigo                                                      | Fichero `ejercicios/a7_calculadora.py` junto a la imagen `docs/capturas/a7_calculadora.png`.                                                                                                                                                                        |
| Resultado Obtenido                                          | La ejecuccion del programa muestra el resultado correcto de todas las operaciones                                                                                                                                                                                   |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                                                                                                                            |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                                                                                                                 |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                                                                                                                          |



### Ficha de actividad - Ejercicio 8

| Campo                                                       | Contenido                                                                                                                                                             |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 8                                                                                                                                                                     |
| Titulo de la Actividad                                      | Calculadora de IMC.                                                                                                                                                   |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                          |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                             |
| Objetivo de la actividad                                    | Calcular el indice de masa corporal pidiendo datos al usuario y aplicando la formula.                                                                                 |
| Descripción del proceso seguido                             | Pedimos los datos al usuario, guardamos en una variable el resultado de aplicar la formula con los datos del usuario y lo mostramos por pantalla usando el `print()`. |
| Codigo                                                      | Fichero `ejercicios/a8_calculadora_imc.py` junto a la imagen `docs/capturas/a8_calculadora_imc.png`.                                                                  |
| Resultado Obtenido                                          | La ejecuccion del programa muestra correctamente el IMC con los datos del usuario.                                                                                    |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                              |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                   |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                            |



### Ficha de actividad - Ejercicio 9

| Campo                                                       | Contenido                                                                                                                                                               |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 9                                                                                                                                                                       |
| Titulo de la Actividad                                      | Conversor de unidades de Temperatura.                                                                                                                                   |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                            |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                               |
| Objetivo de la actividad                                    | Pedir al usuario la temperatura en Celsis y mostrar la conversion a Fahrenheit con un decimal.                                                                          |
| Descripción del proceso seguido                             | Pedimos la temperatura usando `input()` (casteandolo a float). Aplicamos la formula y la mostramos por pantalla, usando round para determinar la cantidad de decimales. |
| Codigo                                                      | Fichero `ejercicios/a9_conversor_temperatura.py` junto a la imagen `docs/capturas/a9_conversor_temperatura.png`.                                                        |
| Resultado Obtenido                                          | La ejecuccion del programa muestra la conversion con un decimal correctamente.                                                                                          |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                                |
| Uso de Inteligencia Artificial                              | No, aunque he investigado en `StackOverFlow` como usar el metodo `round()` con decimales.                                                                               |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                              |



### Ficha de actividad - Ejercicio 10

| Campo                                                       | Contenido                                                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 10                                                                                                                  |
| Titulo de la Actividad                                      | Conversor de unidades de longitud.                                                                                  |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                        |
| Fecha de Realización                                        | 16/9/2026                                                                                                           |
| Objetivo de la actividad                                    | Pedir al usuario una distancia en Km y mostrar su equivalencia en metros, millas y millas nauticas con 3 decimales. |
| Descripción del proceso seguido                             |                                                                                                                     |
| Codigo                                                      | Fichero `ejercicios/a10_conversor_longitud.py` junto a la imagen `docs/capturas/a10_conversor_longitud.png`.        |
| Resultado Obtenido                                          |                                                                                                                     |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                            |
| Uso de Inteligencia Artificial                              | No.                                                                                                                 |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                          |



### Ficha de actividad - Ejercicio 11

| Campo                                                       | Contenido                                                                                                                                                                 |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 11                                                                                                                                                                        |
| Titulo de la Actividad                                      | Comprobacion de mayoria de edad y descuento.                                                                                                                              |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                              |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                                 |
| Objetivo de la actividad                                    | Pide al usuario edad y si tiene carnet y mostrar el valor boleano de las dos condiciones dadas.                                                                           |
| Descripción del proceso seguido                             | Primero capturo las variables por medio de `input()` y posteriormente guardo cada condicion en una variable (booleana). Finalmente muestro el valor dentro del `input()`. |
| Codigo                                                      | Fichero `ejercicios/a11_comprobacion_edad_y_descuento.py` junto a la imagen `docs/capturas/a11_comprobar_edad_y_descuento.png`.                                           |
| Resultado Obtenido                                          | Para cada casuistica, el programa responde con los valores booleanos correctos.                                                                                           |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                                  |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                       |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                                |



### Ficha de actividad - Ejercicio 12

| Campo                                                       | Contenido                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 12                                                                                                                                                                                                                                                                                          |
| Titulo de la Actividad                                      | Precedencia de Operadores.                                                                                                                                                                                                                                                                  |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                                                                                                                                                |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                                                                                                                                                   |
| Objetivo de la actividad                                    | Analiza un codigo dado para dedudir el resultado final, teniendo en cuenta la prioridad de las operaciones.                                                                                                                                                                                 |
| Descripción del proceso seguido                             | Analizando la operacion, deducí que primeramente se tenian que resolver las operaciones jerarquicamente arriba en la escala de prioridad (potencias -> multiplicaiones/divisiones -> suma/resta), de izquierda a derecha. Con un poco de calculo mental, el resultado que me salia era `7`. |
| Codigo                                                      | Fichero `ejercicios/a12_precedencia_operadores.py` junto a la imagen `docs/capturas/a12_precedencia_operadores.png`.                                                                                                                                                                        |
| Resultado Obtenido                                          | El resultado de la operación que habia deducido antes de probarlo en el programa es correcto.                                                                                                                                                                                               |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                                                                                                                                                    |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                                                                                                                                         |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                                                                                                                                                  |



### Ficha de actividad - Ejercicio 13

| Campo                                                       | Contenido                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nº de Actividad                                             | 13                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Titulo de la Actividad                                      | Depuracion de tipos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Tipo (Obligatoria / Voluntaria)                             | Obligatoria.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Fecha de Realización                                        | 16/9/2026                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Objetivo de la actividad                                    | Analiza un codigo erroneo para averiguar el tipo de fallo, por que surgue y como solucionarlo                                                                                                                                                                                                                                                                                                                                                                                         |
| Descripción del proceso seguido                             | Analizando y ejecutando el codigo, nos damos cuenta de que la ejecuccion se interrumpe a causa de un error de tipado (`TypeError`) en una linea concreta. El problema es que se captura la entrada del usuario como una cadena de texto y despues se opera como si fuera un numero (por eso se interrumpe la ejecuccion). La solucion es convertir la variable donde se guarda la entrada del usuario en un decimal (`float(input())`). De esa forma, se trabaja siempre con numeros. |
| Codigo                                                      | Fichero `ejercicios/a13_depuracion_tipos.py` junto a la imagen `docs/capturas/a13_depuracion_tipos.png`.                                                                                                                                                                                                                                                                                                                                                                              |
| Resultado Obtenido                                          | Al castear la variable a un float, el programa funciona correctamente.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Dificultadoes encontradas y soluciones                      | Ninguna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Uso de Inteligencia Artificial                              | No.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Autoevaluacion (Excelente/Adecuado/Suficiente/Insuficiente) | Excelente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |


### Registro resumen de la unidad (rellenar al finalizar todas las actividades)

| Nº Actividad | Titulo                                      | Tipo        | Completada (Si/No) | Autoevaluacion |
| ------------ | ------------------------------------------- | ----------- | ------------------ | -------------- |
| 1            | Configuracion del entorno de desarrollo     | Obligatoria | Si                 | Adecuado       |
| 2            | Hola, mundo personalizado                   | Obligatoria | Si                 | Excelente      |
| 3            | Saludo interactivo                          | Obligatoria | Si                 | Excelente      |
| 4            | Variables básicas                           | Obligatoria | Si                 | Excelente      |
| 5            | Comprobando el tipado dinámico              | Obligatoria | Si                 | Excelente      |
| 6            | Varias lineas con print()                   | Obligatoria | Si                 | Excelente      |
| 7            | Calculadora básoca                          | Obligatoria | Si                 | Excelente      |
| 8            | Calculadora de IMC                          | Obligatoria | Si                 | Excelente      |
| 9            | Conversor de unidades de temperatura        | Obligatoria | Si                 | Excelente      |
| 10           | Conversor de unidades de longitud           | Obligatoria | Si                 | Excelente      |
| 11           | Comprobacion de mayoria de edad y descuento | Obligatoria | Si                 | Excelente      |
| 12           | Precedencia de Operadores                   | Obligatoria | Si                 | Excelente      |
| 13           | Depuracion de Tipos                         | Obligatoria | Si                 | Excelente      |
