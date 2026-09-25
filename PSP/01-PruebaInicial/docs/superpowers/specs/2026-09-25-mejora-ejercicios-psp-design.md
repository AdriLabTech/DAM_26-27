# Diseño: mejora de los ejercicios PSP de Java

- **Fecha:** 2026-09-25
- **Proyecto:** `PSP/01-PruebaInicial`
- **Estado:** diseño aprobado para planificación
- **Java objetivo:** 26

## 1. Contexto

El proyecto contiene cuatro ejercicios de consola y dos modelos de dominio:

- `Ejercicio1`: calculadora básica.
- `Ejercicio2`: gestión de alumnos y cálculo de promedios.
- `Ejercicio3`: juego del ahorcado.
- `Ejercicio4`: verificador de palíndromos.

La revisión encontró fallos de compilación, cálculos incorrectos, entrada no validada, estado global, objetos que admiten estados inválidos, mensajes contradictorios y ausencia de pruebas. Maven declara Java 26 y compila cuando `JAVA_HOME` apunta a `/usr/lib/jvm/java-26-openjdk`. Con el Java 21 predeterminado del sistema, falla antes de generar clases.

No existe un enunciado externo. El diseño conserva la intención visible en el código y fija reglas explícitas para los casos que el proyecto no documenta.

## 2. Objetivos

1. Hacer que los cuatro ejercicios compilen y ejecuten su flujo principal con Java 26.
2. Corregir los cálculos, asignaciones, búsquedas y reglas de finalización defectuosas.
3. Validar entradas y estados de dominio sin finalizar la aplicación ante un dato incorrecto.
4. Separar reglas comprobables de la interacción con la consola.
5. Mejorar los mensajes y la legibilidad en español.
6. Añadir pruebas unitarias y de flujo de consola.
7. Aplicar optimizaciones que aporten claridad o eviten trabajo innecesario, sin introducir una arquitectura compleja.

## 3. Fuera de alcance

- Persistencia en archivos o bases de datos.
- Menú único para los cuatro ejercicios.
- Actualización de alumnos, porque el menú actual no incluye esa operación.
- Una interfaz web, framework de aplicaciones o arquitectura de comandos.
- Compatibilidad con Java 21, 17 u otras versiones anteriores.
- Cambios fuera de `PSP/01-PruebaInicial`.

## 4. Arquitectura

Cada ejercicio conserva su clase principal en `ejercicios` y separa dos responsabilidades:

- **Dominio:** reglas, cálculos, validaciones y transiciones de estado. No accede a `System.in` ni a `System.out`.
- **Coordinación de consola:** preguntas, menús, resultados y traducción de errores. Cada `main` delegará en un método `ejecutar(...)` que recibirá una `ConsolaEntrada`.

Estructura prevista:

```text
src/main/java/ejercicios/
├── Ejercicio1.java
├── Ejercicio2.java
├── Ejercicio3.java
├── Ejercicio4.java
├── ahorcado/
│   ├── EstadoJuego.java
│   ├── JuegoAhorcado.java
│   └── ResultadoIntento.java
├── calculadora/
│   ├── Calculadora.java
│   ├── DivisionPorCeroException.java
│   └── Operacion.java
├── consola/
│   ├── ConsolaEntrada.java
│   └── FinDeEntradaException.java
├── gestion/
│   ├── Alumno.java
│   ├── Asignatura.java
│   └── RegistroAlumnos.java
└── palindromos/
    ├── ResultadoPalindromo.java
    └── VerificadorPalindromos.java
```

Cada clase tendrá una sola razón para cambiar. Las clases de dominio no dependerán de clases de consola. Los modelos actuales se moverán de `ejercicios.model` a `ejercicios.gestion` para agrupar el dominio del ejercicio 2.

## 5. Consola compartida

`ConsolaEntrada` encapsulará un `Reader` y un `PrintWriter` inyectables. La configuración de producción los construirá sobre `System.in` y `System.out` con UTF-8. La clase implementará `AutoCloseable` y no se creará ningún `Scanner` estático.

La consola:

- Leerá líneas completas mediante `readLine()`.
- Permitirá punto o coma como separador decimal. Al mostrar resultados, usará coma decimal, un máximo de 12 decimales y omitirá los ceros finales.
- Recortará espacios exteriores.
- Repetirá una pregunta cuando el valor no cumpla el dominio.
- Diferenciará un valor vacío de una entrada inválida.
- Lanzará `FinDeEntradaException` cuando no exista otra línea. Cada `main` la capturará y mostrará un cierre breve.
- Mantendrá los mensajes de entrada y salida en español.

Las validaciones reutilizarán funciones pequeñas y explícitas. No se incorporará un framework de validación ni un parser general de comandos.

## 6. Ejercicio 1: calculadora

### Dominio

`Operacion` representará suma, resta, multiplicación y división. Su método de fábrica normalizará la entrada con `trim()` y `toLowerCase(Locale.ROOT)`, aceptará `s/r/m/d`, los nombres completos con o sin tilde, y rechazará cualquier otro valor.

`Calculadora`:

- Permitirá operandos negativos.
- Rechazará `NaN` y infinitos en la entrada y en el resultado.
- Resolverá la división por cero con una excepción específica, sin imprimir.
- Evitará los bucles basados en restas y las conversiones a `int`.

`Ejercicio1` solicitará primero una operación válida. Después solicitará ambos operandos. Mostrará `Resultado: <valor>` una sola vez y terminará.

La consola transformará las excepciones de dominio en mensajes como:

- `La operación indicada no existe. Usa s, r, m o d.`
- `No se puede dividir entre cero.`

### Casos límite

- Operación vacía, desconocida, con espacios o mayúsculas.
- `-5`, `0`, decimales y notación aceptada por `Double.parseDouble`.
- `NaN`, infinito, división por cero y desbordamiento del resultado.
- Entrada no numérica seguida de una entrada válida.

## 7. Ejercicio 2: gestión de alumnos

### Modelos

`Asignatura` será una clase con valores válidos desde su construcción:

- Nombre no nulo ni vacío, normalizado al recortar extremos y colapsar espacios consecutivos.
- Nota `double` finita entre `0` y `10`, ambos incluidos.

`Alumno` aplicará estas reglas:

- Nombre no nulo, no vacío y normalizado.
- Edad entre `1` y `120`, ambos incluidos.
- Lista de notas no nula, defensivamente copiada y expuesta solo como instantánea no modificable.
- Método `agregarAsignatura(...)` para ampliar notas.
- Método `promedio()` que devolverá `OptionalDouble.empty()` cuando no haya notas.

Se eliminarán los constructores que dejen campos nulos o incompletos.

### Registro

`RegistroAlumnos` encapsulará la lista y ofrecerá:

- `agregar(Alumno)`.
- `listar()` como copia o colección no modificable.
- `buscarPorNombre(String)`.
- `eliminarPorNombre(String)`.

Normalizará nombres recortando extremos y colapsando espacios consecutivos. La comparación ignorará mayúsculas y no dependerá del locale. El registro rechazará nombres duplicados para que las búsquedas y eliminaciones nunca sean ambiguas.

`Ejercicio2` conservará las opciones 1, 2, 3, 4 y 0. Permitirá de 0 a 20 notas por alumno para admitir el caso vacío y acotar una solicitud absurda. Un alumno sin notas se mostrará y su promedio se informará como no disponible.

La consola contemplará estos estados:

- Lista vacía.
- Alumno añadido.
- Nombre duplicado.
- Alumno no encontrado.
- Alumno eliminado.
- Alumno sin notas.

## 8. Ejercicio 3: ahorcado

`JuegoAhorcado` contendrá una palabra normalizada, el conjunto de letras usadas, el número de errores y el estado actual. Cada instancia representará una partida. El constructor rechazará palabras vacías o con caracteres fuera del alfabeto español.

Reglas:

- El alfabeto válido será `A-Z` más `Ñ`.
- Se aceptarán mayúsculas y minúsculas.
- Cada línea debe representar exactamente una letra.
- Una letra repetida o inválida no consumirá un error.
- Una letra nueva incorrecta consumirá uno de seis errores.
- Una letra correcta revelará todas sus apariciones.
- La victoria se comprobará después de revelar la letra y antes de evaluar la derrota.
- Una partida terminada no aceptará más cambios.
- La consola revelará la palabra al perder.

`ResultadoIntento` distinguirá `ACIERTO`, `FALLO`, `REPETIDA`, `INVALIDA` y `PARTIDA_TERMINADA`. `EstadoJuego` distinguirá `EN_CURSO`, `GANADO` y `PERDIDO`. `JuegoAhorcado` expondrá `intentar(char)`, `mascara()`, `erroresRestantes()`, `letrasUsadas()` y `estado()` para que la consola no reconstruya reglas.

La palabra se elegirá con `ThreadLocalRandom` en producción. `Ejercicio3.ejecutar(...)` recibirá un `Supplier<String>`; las pruebas suministrarán una palabra fija.

## 9. Ejercicio 4: palíndromos

`VerificadorPalindromos` expondrá una operación pura que clasifique la entrada como:

- `PALINDROMO`.
- `NO_PALINDROMO`.
- `SIN_CONTENIDO`.

La normalización:

1. Aplicará Unicode NFKD.
2. Convertirá a minúsculas con `Locale.ROOT`.
3. Eliminará marcas diacríticas.
4. Conservará solo letras y dígitos por punto de código.

Una entrada sin letras ni dígitos devolverá `SIN_CONTENIDO`. La comparación usará dos índices sobre la cadena normalizada y no construirá su inversa. El algoritmo tendrá complejidad lineal y espacio auxiliar lineal por la normalización.

`Ejercicio4` procesará una línea y terminará. La consola mostrará por separado la entrada sin contenido, el resultado positivo y el resultado negativo.

## 10. Errores e interacción

- Las clases de dominio lanzarán `IllegalArgumentException` para invariantes inválidas y `DivisionPorCeroException` para esa condición.
- La consola traducirá esas excepciones a mensajes comprensibles.
- Los menús estarán numerados, con títulos y separadores sencillos.
- Los mensajes evitarán `!!!`, abreviaturas ambiguas y textos contradictorios.
- Un error de entrada volverá a solicitar el mismo dato.
- El fin de entrada cerrará el ejercicio con un mensaje controlado.
- Ningún dominio escribirá en `System.out`.

Ejemplo de estilo:

```text
=== Calculadora ===
Operación (s/r/m/d): suma
Primer número: 2,5
Segundo número: 4
Resultado: 6,5
```

## 11. Legibilidad y buenas prácticas

- Código, identificadores, comentarios y mensajes estarán en español.
- Cada clase pública tendrá JavaDoc breve sobre su responsabilidad.
- Los comentarios explicarán reglas o decisiones no evidentes. El código no llevará comentarios línea por línea.
- Se usarán campos privados, parámetros `final` cuando ayuden a documentar la ausencia de mutación y variables de alcance mínimo.
- Se eliminarán variables estáticas mutables, asignaciones ambiguas y estados incompletos.
- Los mensajes de `toString()` usarán un formato legible.
- Se aplicarán copias defensivas en modelos y colecciones públicas.
- Se usarán `switch` expressions y registros inmutables solo cuando reduzcan código sin ocultar reglas.

## 12. Optimización

El proyecto aplicará optimizaciones que favorezcan la claridad o eviten trabajo innecesario:

- `Set<Character>` para letras usadas.
- Comparación de palíndromos con dos índices.
- Selección uniforme de palabras.
- Evitar concatenación repetida de cadenas inmutables.
- Mantener búsqueda lineal para la pequeña colección de alumnos; un índice no ofrece una ventaja relevante aquí.
- Evitar Streams cuando un bucle exprese la regla con mayor claridad.

No se añadirán cachés, concurrencia, pooling ni índices sin una necesidad demostrada.

## 13. Maven y pruebas

`pom.xml` usará:

- `maven.compiler.release=26`.
- UTF-8.
- `maven-compiler-plugin` 3.15.0.
- `maven-surefire-plugin` 3.5.4.
- `org.junit.jupiter:junit-jupiter` 5.14.4 con alcance de prueba.

Cada dominio tendrá pruebas unitarias. Cada `main` delegará en un método que acepte `ConsolaEntrada`, lo que permitirá probar al menos un flujo completo con `StringReader` y un `PrintWriter` capturado.

Matriz mínima:

| Área | Casos |
|---|---|
| Calculadora | Cuatro operaciones, alias, mayúsculas, negativos, cero, división por cero, `NaN`, infinito y reintento. |
| Alumnos | Invariantes, promedio normal y ausente, nombres con espacios, duplicados, búsqueda, borrado, encapsulación y límites. |
| Ahorcado | Victoria, derrota en sexto error, repetición, entrada inválida, `Ñ`, letras múltiples, estados finales y partidas independientes. |
| Palíndromos | Casos clásicos, Unicode, diacríticos, símbolos, entrada vacía, ausencia de contenido, locale y EOF. |
| Consola | Entrada inválida seguida de válida, mensajes correctos y ausencia de stack traces. |

Las pruebas del ahorcado usarán una palabra fija. Las pruebas del selector comprobarán sus límites sin depender de secuencias aleatorias impredecibles.

## 14. Criterios de aceptación

1. El comando siguiente termina con `BUILD SUCCESS`:

   ```bash
   JAVA_HOME=/usr/lib/jvm/java-26-openjdk \
   PATH=/usr/lib/jvm/java-26-openjdk/bin:$PATH \
   mvn clean verify
   ```

2. Surefire informa una cantidad mayor que cero de pruebas ejecutadas.
3. Los cuatro ejercicios conservan sus puntos de entrada y flujos principales.
4. Cada ejercicio dispone de pruebas de dominio y de al menos un flujo de consola.
5. Las entradas inválidas provocan un reintento o una salida controlada, nunca una excepción técnica visible.
6. No quedan `Scanner` estáticos, divisiones por cero sin control, resultados `NaN` sin explicación, mensajes contradictorios ni errores de asignación.
7. El diff no contiene cambios fuera de `PSP/01-PruebaInicial`.

## 15. Riesgos y mitigaciones

- **Reglas no documentadas:** este documento fija las políticas elegidas y sus pruebas.
- **Más clases que en el código original:** cada clase representa una regla comprobable; los `main` siguen siendo puntos de entrada sencillos.
- **Aleatoriedad en pruebas:** el selector será inyectable.
- **Entrada de consola con distinta codificación:** los adaptadores de producción usarán UTF-8 explícito.
- **Modificaciones ajenas en el repositorio:** los comandos y commits se limitarán a `PSP/01-PruebaInicial`.
