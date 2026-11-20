# genera Guia_Presentacion_UD2.md y .pdf (misma estética Ryoku, A4)
import os, subprocess, html, re
HERE = os.path.dirname(os.path.abspath(__file__))

# (diapositiva, título, tiempo, idea, imprescindible[], cómo lo diría, si te preguntan[(P,R)])
G = [
(1, "Portada", "0:15",
 "Presentar el tema en una frase: hoy toca ver cómo hace un programa varias cosas a la vez.",
 ["Unidad 2 de PSP: programación multihilo."],
 "Vale, pues la unidad 2 de PSP va de hilos. O sea, cómo hacer que un mismo programa haga varias cosas a la vez y, sobre todo, cómo evitar que esas cosas se pisen entre ellas. Voy a ir de lo más básico a los problemas clásicos.",
 []),
(2, "Contenido", "0:15",
 "Dar el mapa: cinco bloques para que el público sepa a dónde vas.",
 ["Los cinco bloques: hilo, sección crítica, hilos en Java, sincronización, problemas clásicos."],
 "Lo he dividido en cinco partes. Primero qué es un hilo, luego el problema que traen, luego cómo se usan en Java, cómo se sincronizan, y al final tres problemas clásicos que se preguntan siempre. No me detengo aquí, empiezo.",
 []),
(3, "Hilo y proceso", "0:40",
 "Un hilo vive dentro de un proceso y comparte su memoria. Todo lo demás de la unidad sale de ahí.",
 ["Los hilos de un proceso comparten memoria, ficheros abiertos y variables globales.",
  "Cada hilo tiene lo suyo: sus registros y su pila.",
  "Por eso es más ligero que un proceso, y por eso es más peligroso."],
 "Fíjate en el dibujo. El proceso es la caja grande. Arriba, lo que comparten todos los hilos: la memoria, los ficheros abiertos, las variables globales. Y abajo cada hilo tiene lo suyo, que son sus registros y su pila. Un proceso nuevo tendría que copiar todo esto; un hilo no, así que es mucho más barato de crear. Pero ojo, que compartan memoria es justo lo que nos va a dar problemas dentro de nada.",
 [("¿Diferencia entre proceso e hilo?", "El proceso tiene su propio espacio de memoria y recursos. El hilo es una unidad de ejecución dentro de un proceso y comparte esos recursos con los demás hilos del mismo proceso."),
  ("¿Qué no se comparte?", "Los registros del procesador y la pila: es donde están las variables locales de cada método en ejecución.")]),
(4, "Ventajas y desafíos", "0:30",
 "Ser honesto: los hilos mejoran el rendimiento, pero cuestan en complejidad.",
 ["Ventajas: usan todos los núcleos, menos tiempo total, interfaz que no se congela.",
  "Desafíos: más complejo, hay que sincronizar, los fallos son difíciles de reproducir.",
  "Ejemplos: interfaces, servidores web (un hilo por conexión), audio y vídeo en tiempo real."],
 "¿Para qué los queremos? Pues para aprovechar todos los núcleos del procesador, para tardar menos y para que una aplicación no se quede congelada mientras hace algo pesado. Un servidor web, por ejemplo, usa un hilo por cada conexión. Pero tiene su parte mala: programarlo es más difícil y los errores son muy raros de reproducir. Ahora te enseño uno.",
 []),
(5, "Condición de carrera", "0:50",
 "Entender por qué dos hilos sobre la misma variable pierden una actualización. Es la diapositiva más importante.",
 ["contador = contador + 1 son tres pasos: leer, calcular, escribir.",
  "Si los dos hilos leen 0 antes de que nadie escriba, los dos escriben 1. Esperado: 2.",
  "Sección crítica: el código que toca el recurso compartido. Solo debe entrar un hilo a la vez."],
 "Mira, el contador empieza en cero y cada hilo le suma uno. Lo esperable es que acabe en dos. Pero sumar uno no es un paso, son tres: leer el valor, calcular el nuevo y escribirlo. Si el hilo A lee cero y justo antes de que escriba el hilo B también lee cero, los dos calculan uno y los dos escriben uno. Resultado: uno en vez de dos. Se ha perdido una suma. Eso es una condición de carrera, y el trozo de código donde pasa se llama sección crítica. La regla es que ahí dentro solo entre un hilo a la vez.",
 [("¿Qué es una condición de carrera?", "Que el resultado depende del orden en que se ejecutan los hilos. Aquí, dos hilos leen el mismo valor antes de que el otro lo actualice."),
  ("¿Qué es una sección crítica?", "El trozo de código que accede o modifica un recurso compartido y que no debe ejecutarse a la vez por varios hilos.")]),
(6, "Cinco herramientas", "0:35",
 "Ver el panorama de soluciones sin entrar en detalle; cada una vuelve luego.",
 ["Mutex: un cerrojo, un hilo dentro.",
  "Semáforo: deja pasar hasta N hilos.",
  "Monitor: cerrojo más esperar y avisar (wait/notify).",
  "Atómicas: operación indivisible sin bloqueo, como AtomicInteger.",
  "synchronized: la forma de Java de pedir el cerrojo.",
  "Peligros: deadlock y bloquear de más."],
 "Para resolverlo hay cinco herramientas. Un mutex es un cerrojo: solo entra uno. Un semáforo es parecido pero deja pasar hasta N. El monitor mezcla un cerrojo con la posibilidad de esperar y avisar. Las variables atómicas hacen la operación de golpe, sin bloqueo. Y synchronized es como Java te da el cerrojo. Todas tienen un riesgo: si bloqueas de menos hay carreras, si bloqueas de más pierdes rendimiento, y si se bloquean entre ellas tienes un deadlock.",
 [("¿Qué es un deadlock?", "Dos o más hilos esperando indefinidamente por recursos que otro tiene y nunca soltará."),
  ("¿Diferencia entre mutex y semáforo?", "El mutex deja entrar a uno. El semáforo de conteo deja entrar hasta N. Un semáforo con un solo permiso se comporta como un mutex.")]),
(7, "Crear hilos", "0:40",
 "Que quede claro que hay dos formas y que lo que arranca el hilo es start().",
 ["Runnable: una clase con run() que se pasa a un Thread.",
  "Thread: una clase que extiende Thread y sobrescribe run().",
  "También con lambda.",
  "start() crea el hilo nuevo. Llamar a run() directamente no crea ninguno."],
 "En Java hay dos formas. La primera es implementar Runnable: escribes el método run con lo que quieras hacer y se lo pasas a un Thread. La segunda es heredar de Thread y sobrescribir run. Y con lambda queda en una línea. Lo importante: lo que lanza el hilo es start. Si llamas a run directamente, se ejecuta como cualquier método, en el mismo hilo, y no has hecho nada concurrente.",
 [("¿Cuál es mejor, Runnable o Thread?", "Normalmente Runnable, porque Java solo permite heredar de una clase y así la tuya queda libre. Es una recomendación general, el temario enseña las dos."),
  ("¿Qué pasa si llamo a run() en vez de start()?", "Se ejecuta en el hilo actual, como una llamada normal. No hay hilo nuevo.")]),
(8, "Estados y control", "0:40",
 "Seguir la vida de un hilo y nombrar los métodos para controlarlo.",
 ["Estados: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED.",
  "start() pasa de NEW a RUNNABLE; al acabar run() pasa a TERMINATED.",
  "Métodos: join (esperar a que acabe otro), sleep (pausa), yield (ceder), interrupt, setPriority de 1 a 10.",
  "getState() te dice en qué estado está."],
 "Un hilo nace en NEW. Cuando haces start pasa a RUNNABLE, que es listo o ejecutándose. Desde ahí puede bloquearse esperando un monitor, esperar a que otro hilo haga algo con wait o join, o dormir un tiempo con sleep. Cuando termina el run, queda en TERMINATED. Y para controlarlo tienes join, que espera a que otro acabe, sleep, yield, interrupt y la prioridad, que va de uno a diez.",
 [("¿Para qué sirve join()?", "Para que un hilo, normalmente el principal, espere a que otro termine antes de seguir."),
  ("¿Qué hace interrupt()?", "Pide que el hilo se interrumpa. Si está en sleep o wait, salta InterruptedException; si no, el hilo puede comprobarlo con isInterrupted()."),
  ("¿La prioridad garantiza el orden?", "No del todo. Es una indicación para el planificador: valores del 1 al 10, y con la misma prioridad se alternan (round robin). No conviene basar la corrección del programa en ella.")]),
(9, "Experimento", "0:40",
 "Demostrar que no es teoría: lo medí. Y que el error es intermitente, que es lo que lo hace peligroso.",
 ["Dos hilos, un millón de sumas cada uno, esperado 2 000 000.",
  "Sin synchronized: 1 de 20 ejecuciones salió mal, llegó a dar 1 028 410.",
  "Con synchronized: 0 de 20, siempre 2 000 000.",
  "Medido en Java 27 con 20 núcleos (experimento/Carrera2.java)."],
 "Esto lo he probado yo. Dos hilos, cada uno suma un millón de veces. Debería salir dos millones. Sin synchronized lo repetí veinte veces y en una salió mal: un millón y pico. En las otras diecinueve salió bien. Y eso es lo malo, que casi siempre funciona y un día falla. Con synchronized, veinte de veinte bien. Así que un programa concurrente que parece que va bien no demuestra nada.",
 [("¿Por qué falla solo a veces?", "Porque depende de cómo se intercalen los hilos en cada ejecución. Si no coinciden justo en la zona crítica, el resultado sale bien."),
  ("¿Has dicho que salió mal 1 de 20, eso es siempre así?", "No: es lo que medí en mi equipo. En otro equipo o con otra carga puede variar. Lo importante es que no es 0 y que con synchronized sí fue 0.")]),
(10, "synchronized y monitor", "0:45",
 "Explicar el cerrojo del objeto y las tres formas de usar synchronized; despachar volatile en una frase.",
 ["Cada objeto tiene un cerrojo; solo un hilo lo tiene a la vez, el resto espera en cola.",
  "Método de instancia: el cerrojo es this. Método static: es la clase. Bloque: el objeto que indiques.",
  "volatile: garantiza que todos ven el valor actual (visibilidad), no la exclusión mutua.",
  "volatile sirve si un hilo escribe y los demás solo leen."],
 "En Java cada objeto tiene un cerrojo. Cuando un hilo entra en algo synchronized, coge ese cerrojo, y los demás se quedan esperando en la cola hasta que salga. Se puede poner en un método, y entonces el cerrojo es el propio objeto, en un método static, y el cerrojo es la clase, o en un bloque, donde tú dices qué objeto. Y una cosa que se confunde: volatile no es lo mismo. Volatile solo asegura que todos los hilos ven el valor más reciente, pero no impide que dos hilos entren a la vez.",
 [("¿Diferencia entre synchronized y volatile?", "synchronized da exclusión mutua y visibilidad. volatile solo visibilidad: no evita las condiciones de carrera en operaciones como contador++."),
  ("¿Qué pasa con dos métodos synchronized del mismo objeto?", "Comparten el mismo cerrojo, así que un hilo no puede estar en uno mientras otro está en el otro.")]),
(11, "wait y notify", "0:40",
 "Mostrar cómo esperar a que se cumpla una condición sin gastar CPU.",
 ["wait(): suelta el cerrojo y el hilo duerme en la cola de espera.",
  "notify() / notifyAll(): despierta a uno / a todos; vuelven a competir por el cerrojo.",
  "Solo dentro de synchronized.",
  "Siempre en un while, no en un if."],
 "A veces un hilo no puede seguir hasta que algo cambie, por ejemplo, que haya un dato. Para eso está wait: el hilo suelta el cerrojo y se duerme sin gastar procesador. Cuando otro hilo cambia el estado, llama a notify o notifyAll y el que dormía se despierta, pero tiene que volver a coger el cerrojo. Tres reglas: solo dentro de synchronized, siempre dentro de un while y, si tienes dudas, notifyAll.",
 [("¿Por qué while y no if?", "Porque al despertar hay que volver a comprobar la condición: puede haber cambiado entre el aviso y el momento en que el hilo recupera el cerrojo. (Es una buena práctica general; el temario usa while en sus ejemplos.)"),
  ("¿Diferencia entre sleep y wait?", "sleep pausa un tiempo y no suelta el cerrojo. wait suelta el cerrojo y espera a que otro hilo avise."),
  ("¿notify o notifyAll?", "notify despierta a uno cualquiera; notifyAll a todos. Con varios hilos esperando condiciones distintas, notifyAll es lo seguro.")]),
(12, "Productor-consumidor", "0:45",
 "Usar wait/notify en un caso real y explicar cómo se rompe si se hace mal.",
 ["Un búfer finito compartido: el productor no puede meter si está lleno; el consumidor no puede sacar si está vacío.",
  "Se resuelve con synchronized + while + wait + notify.",
  "Mal hecho (sleep/wakeup sin monitor) se puede perder el aviso y acabar en deadlock."],
 "Este es el ejemplo típico. Un productor mete datos en un búfer y un consumidor los saca. Si el búfer está lleno, el productor espera; si está vacío, espera el consumidor. Cada uno avisa al otro cuando cambia algo. Y el código es justo lo de antes: dentro de un synchronized, un while con la condición, un wait, y al terminar un notify. Si lo haces mal, sin monitor, puede pasar que el consumidor vea el búfer vacío, el productor meta un dato y avise justo antes de que el consumidor se duerma. Ese aviso se pierde, el consumidor duerme para siempre, el productor llena el búfer y también se duerme. Deadlock.",
 [("¿Qué es el aviso perdido?", "Un wakeup enviado a un hilo que todavía no estaba dormido. Se pierde, y luego ese hilo se duerme sin que nadie lo despierte. Con un monitor no ocurre porque comprobar la condición y dormirse es atómico respecto al cerrojo.")]),
(13, "Semáforos", "0:30",
 "Mostrar el semáforo como un contador de permisos.",
 ["new Semaphore(2): dos permisos.",
  "acquire() pide uno y espera si no hay; release() lo devuelve.",
  "Con tres hilos y dos permisos, el tercero espera a que alguien haga release.",
  "Con un permiso se comporta como un mutex."],
 "Un semáforo es un contador de permisos. Aquí creo uno con dos. El hilo uno y el dos hacen acquire y entran. El tres hace acquire y se queda esperando hasta que alguno haga release. Si lo creas con un solo permiso, funciona como un cerrojo normal.",
 [("¿Cuándo usar un semáforo y no synchronized?", "Cuando quieres limitar a N el acceso simultáneo a algo, por ejemplo N conexiones o N impresoras. synchronized solo deja uno.")]),
(14, "java.util.concurrent", "0:25",
 "Decir que en el día a día no se hace todo a mano: Java trae herramientas ya hechas.",
 ["ExecutorService: un pool de hilos con límite de tamaño.",
  "Callable: como Runnable pero devuelve un valor.",
  "Future: el resultado pendiente; get() espera si aún no está.",
  "También BlockingQueue, ConcurrentHashMap, AtomicInteger."],
 "Todo lo anterior se puede hacer a mano, pero Java ya trae cosas hechas. Un ExecutorService es un pool de hilos: le mandas tareas y él las reparte con un número limitado de hilos. Si la tarea devuelve algo, usas Callable, y lo que recibes es un Future. Sigues haciendo cosas y cuando necesitas el resultado llamas a get, que espera solo si todavía no ha terminado.",
 [("¿Runnable o Callable?", "Runnable no devuelve nada. Callable devuelve un valor con call() y puede lanzar excepciones."),
  ("¿Por qué un pool y no crear hilos cada vez?", "Porque limita cuántos hilos hay a la vez y los reutiliza; crear hilos sin límite gasta recursos.")]),
(15, "Cena de los filósofos", "0:40",
 "Mostrar un deadlock de verdad y las dos formas de romperlo.",
 ["Cinco filósofos, cinco tenedores; para comer hacen falta dos.",
  "Si todos cogen primero el de la derecha, nadie puede comer y nadie suelta: deadlock.",
  "Solución 1: romper la simetría (uno coge en orden contrario).",
  "Solución 2: coger los dos a la vez en un método synchronized de la mesa, con wait si falta alguno."],
 "Cinco filósofos en una mesa y cinco tenedores. Para comer necesitan dos. Si cada uno coge el de su derecha a la vez, todos se quedan con un tenedor esperando el otro, y nadie lo va a soltar. Eso es un deadlock. Hay dos formas de arreglarlo. Una, romper la simetría: que uno de ellos coja primero el otro tenedor. Dos, hacer que coger los dos tenedores sea una sola operación protegida, y si falta uno, esperas con wait y no te quedas con ninguno.",
 [("¿Por qué se produce el deadlock?", "Cada filósofo sostiene un recurso y espera otro que tiene su vecino, formando una espera circular."),
  ("¿Cómo se evita?", "Rompiendo la simetría del orden de adquisición o adquiriendo los dos recursos de forma atómica, como en la solución de la Mesa.")]),
(16, "Lectores y escritores", "0:30",
 "Explicar la regla: leer se comparte, escribir es exclusivo.",
 ["Varios lectores a la vez, porque leer no cambia el dato.",
  "Un escritor necesita el recurso en exclusiva.",
  "Se cuentan las peticiones de escritura para que los escritores no esperen eternamente."],
 "Último clásico. Varios hilos leen y alguno escribe. Leer no modifica nada, así que muchos lectores pueden ir a la vez. Escribir sí cambia el dato, así que el escritor tiene que estar solo. Y la solución del temario cuenta las peticiones de escritura pendientes, para que si llegan lectores nuevos, no dejen al escritor esperando para siempre.",
 [("¿Qué problema hay si solo se favorece a los lectores?", "Que si siempre llegan lectores, el escritor nunca entra: inanición. Por eso se tienen en cuenta las peticiones de escritura.")]),
(17, "Ideas clave", "0:30",
 "Cerrar con cinco ideas y dejar la puerta abierta a preguntas.",
 ["Hilo: comparte memoria, ligero y peligroso.",
  "Carrera: se pierde una actualización.",
  "Exclusión: synchronized, locks, semáforos, atómicas.",
  "Espera: wait y notify sin gastar CPU.",
  "Clásicos: mismos patrones en distintas formas."],
 "Para acabar, cinco ideas. Un hilo comparte la memoria del proceso, por eso es ligero pero peligroso. Cuando dos tocan lo mismo hay una condición de carrera. Se evita con exclusión mutua: synchronized, locks, semáforos o atómicas. Para esperar sin gastar procesador, wait y notify. Y los problemas clásicos son siempre el mismo patrón con otra cara. Eso es todo, si tenéis preguntas, adelante.",
 []),
]

ERRATAS = [
 ("TIME_WAITING", "El temario escribe TIME_WAITING. La constante real de Java es TIMED_WAITING, y es la que sale en la diapositiva 8."),
 ("Ejemplo del semáforo", "En Hilo.java el mensaje «Semáforo liberado» se imprime antes del sleep y del release(), así que el mensaje se adelanta a lo que realmente pasa. No hace falta decirlo en la exposición."),
 ("volatile", "El temario dice que volatile hace que «solo exista una copia». En la práctica lo importante es la visibilidad: todos los hilos ven el último valor. Y no da exclusión mutua; por eso no sirve para contador++."),
 ("Filósofos: notify", "El comentario del código dice que solo funciona con notify y no con notifyAll. No te apoyes en eso en la exposición. Lo que sí es cierto es la idea de fondo: con todos cogiendo primero el tenedor derecho hay una espera circular."),
 ("Lectores-escritores", "En el código del temario leer() es synchronized y duerme dentro, así que en la práctica los lectores entran de uno en uno. La regla teórica del problema (varios lectores a la vez) es la de la diapositiva; si te preguntan, puedes decir que esa implementación lo serializa."),
 ("Productor-consumidor", "El ejemplo usa notify() y funciona con un productor y un consumidor. Con varios de cada uno habría que usar notifyAll."),
]

CONSEJOS = [
 "No leas la diapositiva. Está hecha con poco texto a propósito: la diapositiva da el dibujo, tú pones las palabras.",
 "Usa tus palabras. La rúbrica premia explicar con claridad y fluidez con tus propias palabras y responder preguntas (4 puntos de 10, la parte más pesada). Los textos «cómo lo diría» son una referencia, no un guion que memorizar.",
 "Tiempo objetivo: unos 10 minutos (es lo que pide la rúbrica). La suma de los tiempos de abajo da unos 10 minutos (9:50). Si vas pasado de tiempo, recorta las diapositivas 13, 14 y 16 a una frase cada una.",
 "Los puntos de «que salga sí o sí» son lo mínimo que debe quedar dicho en cada diapositiva. Lo demás es opcional.",
 "Pon ejemplos: el servidor web (un hilo por conexión) y el experimento de la diapositiva 9 son tus dos mejores ejemplos para captar la atención.",
 "Antes de presentar, ejecuta tú mismo experimento/Carrera2.java para ver el fallo con tus ojos (java Carrera2). Si no falla en esa ejecución, repite: es intermitente, y eso también es parte de la explicación.",
 "Si te hacen una pregunta que no sabes, di lo que sí sabes del tema y reconoce el límite. Es mejor que inventar.",
]

def secs(t):
    m, s = t.split(":"); return int(m)*60 + int(s)
total = sum(secs(g[2]) for g in G)
TOT = f"{total//60}:{total%60:02d}"

# ----------------------------------------------------------------- Markdown
md = ["# Guía de exposición · PSP UD2 · Programación multihilo", "",
      f"17 diapositivas · tiempo previsto {TOT} · fichero: `Presentacion_PSP_UD2.pdf`", "",
      "## Antes de empezar", ""]
md += [f"- {c}" for c in CONSEJOS]
md += ["", "## Tiempos", "", "| Diap. | Tema | Tiempo |", "|---|---|---|"]
md += [f"| {g[0]} | {g[1]} | {g[2]} |" for g in G]
md += [f"| | **Total** | **{TOT}** |", ""]
for (n, t, tm, idea, must, say, qa) in G:
    md += [f"## {n}. {t} · {tm}", "", f"**Idea:** {idea}", "", "**Que salga sí o sí**", ""]
    md += [f"- {m}" for m in must]
    md += ["", "**Cómo lo diría**", "", f"> {say}", ""]
    if qa:
        md += ["**Si te preguntan**", ""]
        for q, a in qa: md += [f"- *{q}* {a}"]
        md += [""]
md += ["## Preguntas que se pueden colar (sin diapositiva propia)", "",
       "- *¿Qué diferencia hay entre concurrencia y paralelismo?* Concurrencia: varias tareas progresando en un mismo intervalo, aunque sea en un solo núcleo. Paralelismo: varias ejecutándose realmente a la vez en varios núcleos.",
       "- *¿Se puede evitar el deadlock?* Sí: evitando la espera circular (orden fijo de adquisición), cogiendo todos los recursos a la vez o limitando cuántos hilos compiten.",
       "", "## Cosas del temario que conviene no repetir tal cual", ""]
md += [f"- **{a}.** {b}" for a, b in ERRATAS]
md += [""]
open(os.path.join(HERE, "Guia_Presentacion_UD2.md"), "w").write("\n".join(md))

# ----------------------------------------------------------------- HTML / PDF
e = html.escape
IMG = os.path.join(HERE, "guia_img"); os.makedirs(IMG, exist_ok=True)
subprocess.run(["pdftoppm", "-r", "48", "-png", os.path.join(HERE, "Presentacion_PSP_UD2.pdf"), os.path.join(IMG, "d")], check=True)
CSS = """
@page{size:A4;margin:0}
:root{--ink:#cdc4ba;--dim:#b0a9a0;--muted:#958f87;--soft:rgba(205,196,186,.16);--strong:rgba(205,196,186,.42);--verm:#e2342a}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{color:var(--ink);font:400 11.5pt/1.5 "Space Grotesk",system-ui,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:210mm;height:297mm;padding:15mm 17mm 12mm;background:#000;break-after:page;overflow:hidden;position:relative;display:flex;flex-direction:column}
.pg:last-child{break-after:auto}
.foot{position:absolute;left:17mm;right:17mm;bottom:8mm;display:flex;justify-content:space-between;font:400 7.5pt "Space Mono",monospace;letter-spacing:.18em;text-transform:uppercase;color:#6d6963;border-top:1px solid var(--soft);padding-top:3mm}
.eb{font:400 8pt "Space Mono",monospace;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
h1{font:400 40pt/1 "Fraunces",serif;letter-spacing:-.02em;margin:10mm 0 6mm}
h2{font:400 22pt/1.1 "Fraunces",serif;letter-spacing:-.01em}
h3{font:400 8pt "Space Mono",monospace;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin:4mm 0 1.5mm}
ul{list-style:none}
li{padding:1.3mm 0 1.3mm 6mm;font-size:10.5pt;border-bottom:1px solid var(--soft);position:relative;color:var(--dim)}
li::before{content:"–";position:absolute;left:0;color:var(--muted)}
.say{border-left:2px solid var(--ink);padding:1mm 0 1mm 5mm;color:var(--ink);font-size:11pt;line-height:1.5}
.idea{color:var(--dim);margin-top:3mm;font-size:11pt}
.head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4mm}
.n{font:400 34pt "Fraunces",serif;color:var(--verm);margin-right:5mm}
.t{font:400 21pt "Fraunces",serif}
.tm{font:400 9pt "Space Mono",monospace;color:var(--ink);border:1px solid var(--strong);padding:1mm 3mm}
.thumb{display:block;width:86%;border:1px solid var(--strong)}
table{width:100%;border-collapse:collapse;margin-top:3mm}
td,th{padding:2.1mm 0;border-bottom:1px solid var(--soft);text-align:left;font-size:11pt;color:var(--dim)}
th{font:400 8pt "Space Mono",monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
td:first-child{font-family:"Space Mono",monospace;color:var(--muted);width:16mm}
td:last-child,th:last-child{text-align:right;font-family:"Space Mono",monospace}
.qa p{margin:1.5mm 0;color:var(--dim);font-size:10pt;line-height:1.45}.qa b{color:var(--ink);font-weight:500}
.e{margin:3mm 0;color:var(--dim)}.e b{color:var(--ink);font-weight:500}
.card{border-top:1px solid var(--strong);padding-top:3mm}
"""
NP = len(G) + 3
def foot(k): return f'<div class="foot"><span>PSP · UD2 · Guía de exposición</span><span>{k:02d} / {NP:02d}</span></div>'
def li(items): return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"
pg = []
pg.append(f"""<div class="pg"><p class="eb">Programación de servicios y procesos</p><h1>Guía de exposición<br>Unidad 2 · Multihilo</h1>
<p class="idea">17 diapositivas · {TOT} previstos · Presentacion_PSP_UD2.pdf</p>
<h3 style="margin-top:12mm">Antes de empezar</h3>{li(CONSEJOS)}{foot(1)}</div>""")
pg.append(f"""<div class="pg"><p class="eb">Resumen</p><h2 style="margin:3mm 0 4mm">Tiempos por diapositiva</h2>
<table><tr><th>Diap.</th><th>Tema</th><th>Tiempo</th></tr>""" +
 "".join(f"<tr><td>{g[0]:02d}</td><td>{e(g[1])}</td><td>{g[2]}</td></tr>" for g in G) +
 f"<tr><td></td><td style='color:var(--ink)'>Total</td><td style='color:var(--ink)'>{TOT}</td></tr></table>{foot(2)}</div>")
for k, (n, t, tm, idea, must, say, qa) in enumerate(G):
    qh = ""
    if qa: qh = "<h3>Si te preguntan</h3><div class='qa'>" + "".join(f"<p><b>{e(q)}</b> {e(a)}</p>" for q, a in qa) + "</div>"
    pg.append(f"""<div class="pg"><div class="head"><div><span class="n">{n:02d}</span><span class="t">{e(t)}</span></div><span class="tm">{tm}</span></div>
<img class="thumb" src="guia_img/d-{n:02d}.png"><p class="idea">{e(idea)}</p>
<h3>Que salga sí o sí</h3>{li(must)}<h3>Cómo lo diría</h3><p class="say">{e(say)}</p>{qh}{foot(n+2)}</div>""")
pg.append(f"""<div class="pg"><p class="eb">Anexo</p><h2 style="margin:3mm 0 4mm">Cosas del temario que conviene no repetir tal cual</h2>
{''.join(f"<div class='card e'><b>{e(a)}.</b> {e(b)}</div>" for a, b in ERRATAS)}
<h3 style="margin-top:8mm">Preguntas que se pueden colar</h3><div class='qa'>
<p><b>¿Diferencia entre concurrencia y paralelismo?</b> Concurrencia: varias tareas progresando en un mismo intervalo, aunque sea en un solo núcleo. Paralelismo: varias ejecutándose realmente a la vez en varios núcleos.</p>
<p><b>¿Se puede evitar el deadlock?</b> Sí: evitando la espera circular (orden fijo de adquisición), cogiendo todos los recursos a la vez o limitando cuántos hilos compiten.</p></div>{foot(NP)}</div>""")
doc = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Guía de exposición UD2</title><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400&family=Space+Grotesk:wght@400;500&family=Space+Mono:wght@400&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>{"".join(pg)}</body></html>'
hp = os.path.join(HERE, "guia.html"); open(hp, "w").write(doc)
subprocess.run(["chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                f"--print-to-pdf={os.path.join(HERE,'Guia_Presentacion_UD2.pdf')}", "file://" + hp], check=True, stderr=subprocess.DEVNULL)
print("guía ok", TOT)
