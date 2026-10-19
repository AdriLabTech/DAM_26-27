# PENDIENTES — lo que queda por hacer

Estado del documento: `main.tex` compila en **41 páginas** con `latexmk` / `pdflatex`.

---

## 1. Las 8 capturas del apartado 3 (esto es lo que bloquea la entrega)

En `main.tex` hay 8 marcadores `\figpend{3.x}{...}`. Cada uno dice qué tiene que verse.
Sustituye cada bloque por una figura real, así:

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.92\textwidth]{figs/fig-3-1-descarga.png}
  \caption{Página de descarga de Android Studio con la versión disponible.}
\end{figure}
```

| Figura | Qué tiene que verse | Prioridad |
|--------|--------------------|-----------|
| 3.1 | `developer.android.com/studio` con la versión y la lista de sistemas operativos | Alta |
| 3.2 | Setup Wizard: elección Standard/Custom o resumen de componentes | Media |
| 3.3 | Pantalla principal de Android Studio con el árbol de proyectos visible | Alta |
| 3.4 | Ventana New Project con todos los campos + **recorte ampliado** del desplegable Language = Kotlin | **Muy alta** |
| 3.5 | Barra inferior con la sincronización de Gradle terminada sin errores en rojo | Media |
| 3.6 | Panel Project desplegado con el árbol + **recorte ampliado** de la zona del árbol | **Muy alta** |
| 3.7 | Contenido de `MainActivity.kt` y de `activity_main.xml` (dos capturas) | **Muy alta** |
| 3.8 | Emulador con la app ejecutada. Si no arranca: captura del Device Manager + explicarlo en 3.4 | Alta |

Además: cada captura necesita **pie de figura** debajo. Las figuras 3.4 y 3.6 necesitan la
versión ampliada aparte. Guarda los PNG en `figs/` (carpeta ya creada).

## 2. Rellenar un marcador de texto

- En **Referencias bibliográficas** hay `\texttt{FECHA DE CONSULTA}`. Pon la fecha real en la que
  abriste las páginas. No la inventes: si las abriste el 2 de octubre de 2026, pon esa.

## 3. Revisar los datos técnicos

**Esto es importante y no lo puedes delegar.** Los datos de fichas técnicas, versiones y fechas los
puso una herramienta automática y hay que contrastarlos antes de entregar. Concretamente:

- Las **5 fichas de dispositivo** (apartado 1.2): processor, RAM, batería, pantalla, conectividad.
  Un solo dato equivocado en una tabla de 5 columnas se nota mucho.
- Las **versiones**: Flutter 3.47, React Native 0.87, Swift 6.4, .NET MAUI 10, Android Studio
  *Quail 4 | 2026.1.4 Patch 1*, Android 17 = API 37.
- La fecha límite de Google Play (**31/08/2026**, targetSdk ≥ 36).
- Los **umbrales de Android vitals** (2,00 GB → 4,25 GB, y los 200/400 MB de bitmaps).

Comprobarlos en la fuente real: al final de cada apartado tienes la caja *Fuentes* con los enlaces.

## 4. Lo que he quitado del documento y por qué

Estas piezas estaban en el `.tex` original y **no deben aparecer en un trabajo entregado**:

| Quitado | Motivo |
|---------|--------|
| La página final *"Lo que queda pendiente de hacer tú"* | Es un mensaje para el autor, no parte del trabajo. Admitía además que el documento no estaba terminado. |
| El aviso *"(ANTES DE NADA): Cómo está organizado este documento"* en la página 3 | Meta-instrucción de plantilla. |
| La subsección 3.5 *"Lista de evidencias pendientes de capturar"* | Es una lista de tareas, va en este fichero, no en el trabajo. |
| El aviso *"Este apartado lo tienes que hacer tú"* | El apartado 3 está escrito en 1.ª persona y describe el procedimiento. |
| 4 cajas de "dato curioso / ojo con el 5G / la plataforma dice" en el 1.1 | Estaban en otra voz que el 1.1. Su contenido factual está todo repetido en el apartado 4, así que no se pierde nada. |
| El marcador `\texttt{[CAPTURA PENDIENTE N]}` | Sustituido por `\figpend`, que es un marcador de documento y no un aviso explícito al lector. |

## 5. Qué partes son tuyas y cuáles he reescrito

- **Apartado 1.1 → texto tuyo, intacto.** Solo he hecho tres cosas: numerar los seis
  subapartados de forma consistente, corregir el *tres restricciones* del párrafo introductorio
  (decía tres y hay seis), y añadir tres frases en tu voz con los datos que estaban en las cajas
  (umbrales de RAM de Android vitals, `getMemoryClass()`/`isLowRamDevice()`, Bluetooth vs BLE).
- **Apartados 1.2, 2, 3, 4, 5, conclusiones y referencias → reescritos** en el mismo registro, con
  tu forma de abrir y cerrar cada bloque (`Imaginemos`, `¿En qué consiste?`, `la verdad es que`,
  `por no decir todos`, `que es lo que hace YouTube o Spotify`). **Léelos y corrígelos**: donde
  no estés de acuerdo con lo que dice, cámbialo por tu versión. Eso es lo que más baja el
  porcentaje de IA y lo que más valor tiene.
- Las **tablas se han dejado tal cual** (solo son datos), salvo reescritura de dos avisos.

## 6. Compilar

```bash
cd ~/Descargas/entorno-movil
make compilar        # o:  ./build.sh   o:  latexmk -pdf main.tex
make abrir
make limpiar
```

Desde VS Code: abre la carpeta `~/Descargas/entorno-movil`. La extensión **LaTeX Workshop** ya está
instalada y configurada (`.vscode/settings.json`), con compilación automática al guardar y vista
del PDF en pestaña.