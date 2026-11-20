# genera index.html y Presentacion_PSP_UD2.pdf  (estilo Ryoku, igual que la UD1)
import html, subprocess, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def esc(s): return html.escape(s)

CSS = open(os.path.join(HERE, "ryoku.css")).read() + r"""
/* ---- ajustes UD2: texto más grande, acento vermellón para lo peligroso ---- */
.body{top:140px}
h2{font-size:78px}
ul.l li{font-size:31px}
p.s{font-size:30px}
.card{padding:30px 0 0}
.bad{color:var(--verm)!important}
.box.bad{border-color:var(--verm)}
.box.f.bad{background:var(--verm);color:#000;border-color:var(--verm)}
pre.code{font-size:27px;line-height:1.5}
.tag{display:inline-block;border:1px solid var(--line);padding:6px 16px;font:400 21px var(--mono);color:var(--ink);margin:0 10px 10px 0}
.tag.on{background:var(--ink);color:#000;border-color:var(--ink)}
.tag.bad{border-color:var(--verm);color:var(--verm)}
.num{font:400 22px var(--mono);letter-spacing:.2em;color:var(--muted)}
.cap{font:400 21px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.five{display:grid;grid-template-columns:repeat(5,1fr);gap:0}
.five>div{border-top:1px solid var(--strong);padding:26px 24px 0 0;margin-right:24px}
.five h3{font-size:44px;margin:10px 0 12px}
.five p{font:400 26px/1.4 var(--sans);color:var(--dim)}
.five .j{margin-top:20px;font:400 20px var(--mono);color:var(--ink)}
"""

slides = []
def S(sec, title, inner, cls=""): slides.append((sec, title, inner, cls))
def chrome(i, n, sec):
    if i == 1: return ''
    return f'<div class="top"><span>{sec}</span></div><div class="bot"><span></span><span>{i:02d}</span></div>'
def ttl(h, d=1): return f'<h2 class="a" style="--d:{d}">{h}</h2>'
def defs(i): return f'<defs><marker id="m{i}" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0 1L11 6L0 11z" fill="#cdc4ba" stroke="none"/></marker><marker id="r{i}" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0 1L11 6L0 11z" fill="#e2342a" stroke="none"/></marker></defs>'
INK = "#cdc4ba"; VERM = "#e2342a"; MUT = "#958f87"

# ---------------------------------------------------------------- 1 portada
S("Unidad 2", "Portada", """
<div class="body" style="top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
 <p class="eyebrow">Programación de servicios y procesos</p>
 <h1 style="margin-top:36px">Unidad 2.<br>Programación<br>multihilo</h1>
 <p class="lede" style="margin-top:70px;color:var(--ink)">Desarrollado por Adrián Velasco Mañas</p>
</div>
<svg style="position:absolute;right:150px;top:250px" viewBox="0 0 520 520" width="520" height="520" fill="none" stroke="#cdc4ba" stroke-width="2">
 <g stroke-opacity=".55"><path d="M40 260C140 260 140 90 260 90S380 90 480 90"/><path d="M40 260C140 260 140 260 260 260S380 260 480 260"/><path d="M40 260C140 260 140 430 260 430S380 430 480 430"/></g>
 <circle cx="40" cy="260" r="14" fill="#cdc4ba" stroke="none"/>
 <g fill="#000"><circle cx="260" cy="90" r="11"/><circle cx="260" cy="260" r="11"/><circle cx="260" cy="430" r="11"/></g>
 <circle cx="480" cy="90" r="9" fill="#cdc4ba" stroke="none"/><circle cx="480" cy="260" r="9" fill="#cdc4ba" stroke="none"/><circle cx="480" cy="430" r="9" fill="#cdc4ba" stroke="none"/>
</svg>""", cls="cover")

# ---------------------------------------------------------------- 2 contenido
items = [("01", "El hilo", "Qué es y en qué se diferencia de un proceso"),
         ("02", "La sección crítica", "Condiciones de carrera y cómo evitarlas"),
         ("03", "Hilos en Java", "Runnable, Thread, estados y control"),
         ("04", "Sincronización", "synchronized, wait/notify, semáforos"),
         ("05", "Problemas clásicos", "Productor-consumidor, filósofos, lectores-escritores")]
rows = "".join(f'<div class="a" style="--d:{i+2};display:grid;grid-template-columns:100px 1fr;align-items:center;gap:20px;padding:20px 0;border-bottom:1px solid var(--soft)"><span class="num" style="font-size:26px">{n}</span><div><h3 style="font-size:50px">{t}</h3><p class="cap" style="margin-top:8px;font-size:19px;text-transform:none;letter-spacing:.04em">{d}</p></div></div>' for i, (n, t, d) in enumerate(items))
S("Contenido", "Contenido", f"""
<div class="body">{ttl("Cinco bloques,<br><em>de menos a más difícil.</em>")}
<div style="margin-top:34px;width:1500px;border-top:1px solid var(--soft)">{rows}</div></div>""")

# ---------------------------------------------------------------- 3 hilo vs proceso
S("01 · El hilo", "Hilo y proceso", f"""
<div class="body">{ttl("Un hilo es una vía de ejecución<br><em>dentro de un proceso.</em>")}
<svg class="a" style="--d:3;margin-top:34px" viewBox="0 0 1680 560" width="1680" height="560" fill="none" stroke="{INK}">
 <rect x="2" y="2" width="1676" height="556" stroke-opacity=".5"/>
 <text x="36" y="48" fill="{INK}" stroke="none" font-size="22" letter-spacing="5">PROCESO</text>
 <rect x="36" y="76" width="1608" height="130" fill="{INK}" stroke="none"/>
 <text x="70" y="122" fill="#000" stroke="none" font-size="19" letter-spacing="4">COMPARTIDO POR TODOS LOS HILOS</text>
 <g fill="#000" stroke="none" font-size="30" text-anchor="middle"><text x="290" y="176">Memoria</text><text x="840" y="176">Ficheros abiertos</text><text x="1390" y="176">Variables globales</text></g>
 <g>
  <rect x="36" y="244" width="500" height="280" stroke-opacity=".7"/><rect x="590" y="244" width="500" height="280" stroke-opacity=".7"/><rect x="1144" y="244" width="500" height="280" stroke-opacity=".7"/>
  <g fill="{INK}" stroke="none" font-size="30"><text x="66" y="296">Hilo 1</text><text x="620" y="296">Hilo 2</text><text x="1174" y="296">Hilo 3</text></g>
  <g fill="{MUT}" stroke="none" font-size="18" letter-spacing="4"><text x="66" y="332">PROPIO</text><text x="620" y="332">PROPIO</text><text x="1174" y="332">PROPIO</text></g>
  <g stroke-opacity=".6"><rect x="66" y="360" width="200" height="130"/><rect x="290" y="360" width="214" height="130"/><rect x="620" y="360" width="200" height="130"/><rect x="844" y="360" width="214" height="130"/><rect x="1174" y="360" width="200" height="130"/><rect x="1398" y="360" width="214" height="130"/></g>
  <g fill="{INK}" stroke="none" font-size="26" text-anchor="middle"><text x="166" y="432">Registros</text><text x="397" y="432">Pila</text><text x="720" y="432">Registros</text><text x="951" y="432">Pila</text><text x="1274" y="432">Registros</text><text x="1505" y="432">Pila</text></g>
 </g>
</svg>
<p class="note a" style="--d:5;margin-top:26px;font-size:31px"><b>Proceso:</b> programa en ejecución con su propia memoria. &nbsp; <b>Hilo:</b> comparte esa memoria, y por eso es más ligero… y más peligroso.</p></div>""")

# ---------------------------------------------------------------- 4 ventajas / desafíos
S("01 · El hilo", "Ventajas y desafíos", f"""
<div class="body">{ttl("Más rendimiento,<br><em>a cambio de más cuidado.</em>")}
<div class="grid g2 a" style="--d:3;margin-top:40px;gap:60px">
 <div class="card hi" style="border-top:1px solid var(--strong)"><p class="mono" style="color:var(--ink);margin-bottom:12px">+ Ventajas</p>
  <ul class="l"><li><b>Aprovechan</b> todos los núcleos.</li><li><b>Menos tiempo</b> total: tareas en paralelo.</li><li><b>Interfaz fluida</b> mientras algo trabaja detrás.</li></ul></div>
 <div class="card"><p class="mono bad" style="margin-bottom:12px">− Desafíos</p>
  <ul class="l"><li>Programarlo es <b>más complejo</b>.</li><li>Hay que <b>sincronizar</b> lo compartido.</li><li>Los fallos son <b>difíciles de reproducir</b>.</li></ul></div>
</div>
<div class="a" style="--d:5;margin-top:56px"><p class="cap" style="margin-bottom:16px">Dónde se usan</p>
 <span class="tag on">Interfaces de usuario</span><span class="tag on">Servidores web · un hilo por conexión</span><span class="tag on">Audio y vídeo en tiempo real</span></div></div>""")

# ---------------------------------------------------------------- 5 condición de carrera
S("02 · Sección crítica", "Condición de carrera", f"""
<div class="body">{ttl("Dos hilos, una variable:<br><em>se pierde una suma.</em>")}
<svg class="a" style="--d:3;margin-top:30px" viewBox="0 0 1680 520" width="1680" height="520" fill="none" stroke="{INK}">
 {defs(5)}
 <text x="0" y="40" fill="{MUT}" stroke="none" font-size="20" letter-spacing="4">contador = contador + 1      ·      contador empieza en 0</text>
 <g fill="{INK}" stroke="none" font-size="28"><text x="0" y="170">Hilo A</text><text x="0" y="330">Hilo B</text></g>
 <path d="M150 150H1600" stroke-opacity=".3" stroke-dasharray="3 8"/><path d="M150 310H1600" stroke-opacity=".3" stroke-dasharray="3 8"/>
 <g font-size="26" text-anchor="middle">
  <rect x="250" y="120" width="260" height="64" fill="{INK}" stroke="none"/><text x="380" y="162" fill="#000" stroke="none">lee 0</text>
  <rect x="250" y="280" width="260" height="64" fill="{INK}" stroke="none"/><text x="380" y="322" fill="#000" stroke="none">lee 0</text>
  <rect x="640" y="120" width="260" height="64" stroke-opacity=".7"/><text x="770" y="162" fill="{INK}" stroke="none">calcula 1</text>
  <rect x="640" y="280" width="260" height="64" stroke-opacity=".7"/><text x="770" y="322" fill="{INK}" stroke="none">calcula 1</text>
  <rect x="1030" y="120" width="260" height="64" stroke="{VERM}"/><text x="1160" y="162" fill="{VERM}" stroke="none">escribe 1</text>
  <rect x="1030" y="280" width="260" height="64" stroke="{VERM}"/><text x="1160" y="322" fill="{VERM}" stroke="none">escribe 1</text>
 </g>
 <path d="M1330 232H1480" stroke="{VERM}" marker-end="url(#r5)"/>
 <g text-anchor="middle" stroke="none"><text x="1560" y="228" fill="{VERM}" font-size="64">1</text><text x="1560" y="270" fill="{MUT}" font-size="19" letter-spacing="3">ESPERADO: 2</text></g>
 <path d="M150 440H1600" stroke-opacity=".5" marker-end="url(#m5)"/><text x="1600" y="480" fill="{MUT}" stroke="none" font-size="18" letter-spacing="4" text-anchor="end">TIEMPO</text>
</svg>
<p class="note a" style="--d:5;margin-top:10px;font-size:31px"><b>Sección crítica:</b> el trozo de código que toca un recurso compartido. Solo debe entrar <b>un hilo a la vez</b>.</p></div>""")

# ---------------------------------------------------------------- 6 cinco soluciones
five = [("01", "Mutex", "Un cerrojo: solo un hilo dentro.", "lock() / unlock()"),
        ("02", "Semáforo", "Deja pasar hasta N hilos a la vez.", "Semaphore"),
        ("03", "Monitor", "Cerrojo + esperar y avisar.", "wait() / notify()"),
        ("04", "Atómicas", "Operación indivisible, sin bloqueo.", "AtomicInteger"),
        ("05", "synchronized", "La forma de Java de exigir el cerrojo.", "método o bloque")]
cards = "".join(f'<div class="a" style="--d:{i+3}"><span class="num">{n}</span><h3>{t}</h3><p>{d}</p><div class="j">{j}</div></div>' for i, (n, t, d, j) in enumerate(five))
S("02 · Sección crítica", "Soluciones", f"""
<div class="body">{ttl("Cinco herramientas<br><em>para una exclusión mutua.</em>")}
<div class="five" style="margin-top:84px">{cards}</div>
<p class="note a" style="--d:9;margin-top:90px;font-size:31px">Cuidado con el <b class="bad">deadlock</b> (todos esperando a todos) y con bloquear de más: <b>demasiados cerrojos = poca concurrencia</b>.</p></div>""")

# ---------------------------------------------------------------- 7 crear hilos
S("03 · Hilos en Java", "Crear hilos", f"""
<div class="body">{ttl("Dos formas de crear un hilo,<br><em>un solo botón para arrancarlo.</em>")}
<div class="grid g2 a" style="--d:3;margin-top:60px;gap:50px">
 <div><p class="mono" style="color:var(--ink);margin-bottom:12px">A · Implementar Runnable</p>
<pre class="code"><span class="k">class</span> Tarea <span class="k">implements</span> Runnable {{
  <span class="k">public void</span> run() {{
    System.out.println(<span class="s">"Hola"</span>);
  }}
}}

Thread t = <span class="k">new</span> Thread(<span class="k">new</span> Tarea());
t.<span class="k">start</span>();</pre></div>
 <div><p class="mono" style="color:var(--ink);margin-bottom:12px">B · Extender Thread</p>
<pre class="code"><span class="k">class</span> MiHilo <span class="k">extends</span> Thread {{
  <span class="k">public void</span> run() {{
    System.out.println(<span class="s">"Hola"</span>);
  }}
}}

<span class="k">new</span> MiHilo().<span class="k">start</span>();</pre></div>
</div>
<div class="grid g2 a" style="--d:5;margin-top:56px;gap:50px">
 <p class="note" style="font-size:30px"><b>Con lambda:</b> <code style="font-size:26px">new Thread(() -&gt; ...).start()</code></p>
 <p class="note" style="font-size:30px;border-color:var(--verm)"><b class="bad">start()</b> crea el hilo. <b>run()</b> a secas solo ejecuta el método, sin hilo nuevo.</p></div></div>""")

# ---------------------------------------------------------------- 8 estados y control
def st(x, y, w, t, sub, fill=False, bad=False):
    c = VERM if bad else INK
    return (f'<rect x="{x}" y="{y}" width="{w}" height="84" fill="{INK if fill else "#000"}" stroke="{c}" stroke-opacity="{1 if fill else .7}"/>'
            f'<text x="{x+w/2}" y="{y+40}" text-anchor="middle" font-size="26" fill="{"#000" if fill else c}" stroke="none">{t}</text>'
            f'<text x="{x+w/2}" y="{y+68}" text-anchor="middle" font-size="16" letter-spacing="2" fill="{"#222" if fill else MUT}" stroke="none">{sub}</text>')
S("03 · Hilos en Java", "Estados y control", f"""
<div class="body">{ttl("Un hilo nace, trabaja, espera<br><em>y termina.</em>")}
<svg class="a" style="--d:3;margin-top:22px" viewBox="0 0 1680 470" width="1680" height="470" fill="none" stroke="{INK}">
 {defs(8)}
 {st(0, 70, 250, "NEW", "creado, sin arrancar")}
 {st(400, 70, 340, "RUNNABLE", "listo o ejecutándose", True)}
 {st(1430, 70, 250, "TERMINATED", "ha acabado")}
 <g stroke-opacity=".7" marker-end="url(#m8)"><path d="M255 112H395"/><path d="M745 112H1425"/></g>
 <text x="325" y="96" fill="{MUT}" stroke="none" font-size="18" text-anchor="middle">start()</text>
 <text x="1085" y="96" fill="{MUT}" stroke="none" font-size="18" text-anchor="middle">run() termina</text>
 <g stroke-opacity=".5"><path d="M570 154V222"/><path d="M220 222H1220"/><path d="M220 222V285" marker-end="url(#m8)"/><path d="M720 222V285" marker-end="url(#m8)"/><path d="M1220 222V285" marker-end="url(#m8)"/></g>
 <text x="600" y="206" fill="{MUT}" stroke="none" font-size="18">se bloquea o espera…  y cuando acaba, vuelve a RUNNABLE</text>
 {st(0, 290, 440, "BLOCKED", "espera un monitor", False)}
 {st(500, 290, 440, "WAITING", "wait() · join()", False)}
 {st(1000, 290, 440, "TIMED_WAITING", "sleep(ms) · wait(ms)", False)}
</svg>
<div class="a" style="--d:5;margin-top:18px"><span class="tag on">join()</span><span class="tag on">sleep(ms)</span><span class="tag on">yield()</span><span class="tag on">interrupt()</span><span class="tag on">setPriority(1…10)</span><span class="cap" style="margin-left:14px">getState() devuelve el estado</span></div></div>""")

# ---------------------------------------------------------------- 9 experimento
S("03 · Hilos en Java", "Sin sincronizar", f"""
<div class="body">{ttl("Sin sincronizar,<br><em>el error es intermitente.</em>")}
<div style="display:grid;grid-template-columns:780px 1fr;gap:80px;margin-top:40px">
 <div class="a" style="--d:3"><pre class="code" style="font-size:28px"><span class="k">class</span> Contador {{
  <span class="k">private int</span> c;

  <span class="c">// c++ = leer, sumar, escribir</span>
  <span class="k">void</span> inc() {{ c++; }}

  <span class="k">synchronized void</span> incS() {{ c++; }}
}}</pre>
 <p class="cap" style="margin-top:22px">2 hilos · 1 000 000 sumas cada uno · esperado: 2 000 000</p></div>
 <div class="a" style="--d:4">
  <div style="border-top:1px solid var(--strong);padding:22px 0 30px"><p class="cap bad">Sin synchronized</p><p style="font:400 112px/1.1 var(--mono);color:var(--verm);margin-top:6px">1 de 20</p><p class="s" style="font-size:28px">ejecuciones erróneas · llegó a dar <b class="hl">1 028 410</b></p></div>
  <div style="border-top:1px solid var(--strong);padding:22px 0 0"><p class="cap">Con synchronized</p><p style="font:400 112px/1.1 var(--mono);color:var(--ink);margin-top:6px">0 de 20</p><p class="s" style="font-size:28px">siempre <b class="hl">2 000 000</b></p></div>
 </div></div>
<p class="cap a" style="--d:6;margin-top:36px;font-size:17px">Medido en Java 27, 20 núcleos. Que casi nunca falle es justo lo que hace tan difícil depurarlo.</p></div>""")

# ---------------------------------------------------------------- 10 synchronized / monitor
S("04 · Sincronización", "synchronized", f"""
<div class="body">{ttl("Cada objeto tiene un cerrojo.<br><em>synchronized lo pide.</em>")}
<div style="display:grid;grid-template-columns:820px 1fr;gap:70px;margin-top:30px">
 <svg class="a" style="--d:3" viewBox="0 0 820 480" width="820" height="480" fill="none" stroke="{INK}">
  {defs(10)}
  <text x="0" y="30" fill="{MUT}" stroke="none" font-size="17" letter-spacing="4">COLA DEL CERROJO</text>
  <g font-size="22" text-anchor="middle"><rect x="0" y="60" width="130" height="60" stroke-opacity=".6" stroke-dasharray="5 5"/><text x="65" y="98" fill="{INK}" stroke="none">Hilo 3</text><rect x="150" y="60" width="130" height="60" stroke-opacity=".6" stroke-dasharray="5 5"/><text x="215" y="98" fill="{INK}" stroke="none">Hilo 2</text></g>
  <path d="M300 90H400" stroke-opacity=".7" marker-end="url(#m10)"/>
  <rect x="420" y="20" width="390" height="430" stroke-opacity=".7"/>
  <text x="440" y="56" fill="{MUT}" stroke="none" font-size="17" letter-spacing="4">OBJETO · SECCIÓN CRÍTICA</text>
  <rect x="450" y="150" width="330" height="80" fill="{INK}" stroke="none"/><text x="615" y="200" text-anchor="middle" fill="#000" stroke="none" font-size="26">Hilo 1 dentro</text>
  <text x="615" y="300" text-anchor="middle" fill="{INK}" stroke="none" font-size="22">1 cerrojo</text>
  <text x="615" y="340" text-anchor="middle" fill="{MUT}" stroke="none" font-size="19">1 hilo a la vez</text>
 </svg>
 <div class="a" style="--d:4"><dl class="rows" style="border-top:1px solid var(--soft)">
  <div style="padding:22px 0"><dt style="width:260px;color:var(--ink);font-size:19px">Método</dt><dd style="text-align:left;font:400 26px var(--sans);color:var(--dim)">cerrojo = <b class="hl">this</b></dd></div>
  <div style="padding:22px 0"><dt style="width:260px;color:var(--ink);font-size:19px">Método static</dt><dd style="text-align:left;font:400 26px var(--sans);color:var(--dim)">cerrojo = <b class="hl">la clase</b></dd></div>
  <div style="padding:22px 0"><dt style="width:260px;color:var(--ink);font-size:19px">Bloque</dt><dd style="text-align:left;font:400 26px var(--sans);color:var(--dim)">el objeto que <b class="hl">tú indiques</b></dd></div></dl>
  <p class="note" style="margin-top:34px;font-size:28px"><b>volatile</b> garantiza que todos ven el valor actual (visibilidad), <b>no</b> la exclusión. Sirve si un hilo escribe y el resto lee.</p></div>
</div></div>""")

# ---------------------------------------------------------------- 11 wait / notify
S("04 · Sincronización", "wait y notify", f"""
<div class="body">{ttl("Esperar sin gastar CPU:<br><em>wait y notify.</em>")}
<svg class="a" style="--d:3;margin-top:34px" viewBox="0 0 1680 330" width="1680" height="330" fill="none" stroke="{INK}">
 {defs(11)}
 <g font-size="25" text-anchor="middle">
  <rect x="0" y="40" width="360" height="110" fill="{INK}" stroke="none"/><text x="180" y="86" fill="#000" stroke="none">Hilo en synchronized</text><text x="180" y="122" fill="#333" stroke="none" font-size="19">la condición no se cumple</text>
  <rect x="520" y="40" width="360" height="110" stroke-opacity=".7"/><text x="700" y="86" fill="{INK}" stroke="none">wait()</text><text x="700" y="122" fill="{MUT}" stroke="none" font-size="19">suelta el cerrojo y duerme</text>
  <rect x="1040" y="40" width="300" height="110" stroke-opacity=".7" stroke-dasharray="6 6"/><text x="1190" y="86" fill="{INK}" stroke="none">Cola de espera</text><text x="1190" y="122" fill="{MUT}" stroke="none" font-size="19">sin consumir CPU</text>
 </g>
 <g stroke-opacity=".7" marker-end="url(#m11)"><path d="M365 95H515"/><path d="M885 95H1035"/></g>
 <path d="M1190 160C1190 290 700 290 500 200" stroke-opacity=".6" marker-end="url(#m11)" stroke-dasharray="3 6"/>
 <g fill="{INK}" stroke="none" font-size="22" text-anchor="middle"><text x="900" y="285">otro hilo: notify() / notifyAll()</text></g>
 <text x="1420" y="104" fill="{MUT}" stroke="none" font-size="20">vuelve a competir</text><text x="1420" y="134" fill="{MUT}" stroke="none" font-size="20">por el cerrojo</text>
</svg>
<div class="grid g3 a" style="--d:5;margin-top:26px;gap:50px">
 <div style="border-top:1px solid var(--strong);padding-top:18px"><p class="num">01</p><p class="s" style="font-size:29px;margin-top:8px">Solo dentro de <b class="hl">synchronized</b>.</p></div>
 <div style="border-top:1px solid var(--strong);padding-top:18px"><p class="num">02</p><p class="s" style="font-size:29px;margin-top:8px">Siempre en un <b class="hl">while</b>, no en un if.</p></div>
 <div style="border-top:1px solid var(--strong);padding-top:18px"><p class="num">03</p><p class="s" style="font-size:29px;margin-top:8px">En duda, <b class="hl">notifyAll()</b>.</p></div>
</div></div>""")

# ---------------------------------------------------------------- 12 productor consumidor
S("05 · Problemas clásicos", "Productor-consumidor", f"""
<div class="body">{ttl("Productor y consumidor<br><em>comparten un búfer.</em>")}
<svg class="a" style="--d:3;margin-top:24px" viewBox="0 0 1680 250" width="1680" height="250" fill="none" stroke="{INK}">
 {defs(12)}
 <rect x="0" y="70" width="300" height="100" fill="{INK}" stroke="none"/><text x="150" y="130" text-anchor="middle" fill="#000" stroke="none" font-size="30">Productor</text>
 <rect x="1380" y="70" width="300" height="100" fill="{INK}" stroke="none"/><text x="1530" y="130" text-anchor="middle" fill="#000" stroke="none" font-size="30">Consumidor</text>
 <g stroke-opacity=".7" marker-end="url(#m12)"><path d="M305 120H460"/><path d="M1220 120H1375"/></g>
 <g><rect x="470" y="70" width="150" height="100" stroke-opacity=".7"/><rect x="620" y="70" width="150" height="100" fill="{INK}" fill-opacity=".25" stroke-opacity=".7"/><rect x="770" y="70" width="150" height="100" fill="{INK}" fill-opacity=".25" stroke-opacity=".7"/><rect x="920" y="70" width="150" height="100" fill="{INK}" fill-opacity=".25" stroke-opacity=".7"/><rect x="1070" y="70" width="150" height="100" stroke-opacity=".7"/></g>
 <text x="845" y="40" text-anchor="middle" fill="{MUT}" stroke="none" font-size="19" letter-spacing="5">BÚFER FINITO</text>
 <text x="150" y="220" text-anchor="middle" fill="{MUT}" stroke="none" font-size="21">lleno → wait()</text>
 <text x="1530" y="220" text-anchor="middle" fill="{MUT}" stroke="none" font-size="21">vacío → wait()</text>
</svg>
<div class="grid g2 a" style="--d:5;margin-top:22px;gap:60px">
<pre class="code" style="font-size:26px"><span class="k">synchronized</span> (cont) {{
  <span class="k">while</span> (!cont.datoDisponible())
    cont.<span class="k">wait</span>();
  dato = cont.get();
  cont.<span class="k">notify</span>();
}}</pre>
<div><p class="note" style="font-size:29px"><b>Cada uno avisa al otro</b> al cambiar el estado del búfer.</p>
<p class="note" style="font-size:29px;margin-top:26px;border-color:var(--verm)"><b class="bad">Mal hecho</b> (sleep/wakeup sin monitor) el aviso se pierde y ambos duermen para siempre.</p></div></div></div>""")

# ---------------------------------------------------------------- 13 semáforos
def slot(x, t, on, wait=False):
    if wait: return f'<rect x="{x}" y="0" width="200" height="74" stroke="{INK}" stroke-opacity=".6" stroke-dasharray="6 6"/><text x="{x+100}" y="46" text-anchor="middle" fill="{INK}" stroke="none" font-size="24">{t}</text>'
    return f'<rect x="{x}" y="0" width="200" height="74" fill="{INK}" stroke="none"/><text x="{x+100}" y="46" text-anchor="middle" fill="#000" stroke="none" font-size="24">{t}</text>'
S("04 · Sincronización", "Semáforos", f"""
<div class="body">{ttl("Un semáforo deja pasar<br><em>hasta N hilos.</em>")}
<div style="display:grid;grid-template-columns:1fr 700px;gap:70px;margin-top:70px">
 <div class="a" style="--d:3">
  <p class="cap" style="margin-bottom:14px">new Semaphore(2) · permisos = 2</p>
  <svg viewBox="0 0 640 74" width="640" height="74" fill="none">{slot(0,"Hilo 1",1)}{slot(220,"Hilo 2",1)}</svg>
  <p class="cap" style="margin:34px 0 14px">esperando permiso</p>
  <svg viewBox="0 0 640 74" width="640" height="74" fill="none">{slot(0,"Hilo 3",0,True)}</svg>
  <p class="note" style="margin-top:40px;font-size:29px">Cuando uno hace <b>release()</b>, el hilo 3 entra. <b>Semaphore(1)</b> se comporta como un mutex.</p></div>
 <div class="a" style="--d:4"><pre class="code" style="font-size:26px">Semaphore sem = <span class="k">new</span> Semaphore(<span class="k">2</span>);

sem.<span class="k">acquire</span>();   <span class="c">// pide permiso</span>
<span class="c">// sección crítica</span>
sem.<span class="k">release</span>();   <span class="c">// lo devuelve</span></pre>
 <dl class="rows" style="margin-top:28px"><div><dt>acquire()</dt><span class="ld"></span><dd style="font:400 22px var(--sans);color:var(--dim)">espera si no hay</dd></div><div><dt>release()</dt><span class="ld"></span><dd style="font:400 22px var(--sans);color:var(--dim)">libera un permiso</dd></div></dl></div></div></div>""")

# ---------------------------------------------------------------- 14 alto nivel
S("04 · Sincronización", "Alto nivel", f"""
<div class="body">{ttl("Java ya trae lo difícil hecho:<br><em>java.util.concurrent.</em>")}
<svg class="a" style="--d:3;margin-top:60px" viewBox="0 0 1680 190" width="1680" height="190" fill="none" stroke="{INK}">
 {defs(14)}
 <rect x="0" y="40" width="300" height="100" stroke-opacity=".7"/><text x="150" y="98" text-anchor="middle" fill="{INK}" stroke="none" font-size="28">Tareas</text>
 <rect x="440" y="20" width="460" height="140" fill="{INK}" stroke="none"/><text x="670" y="82" text-anchor="middle" fill="#000" stroke="none" font-size="30">ExecutorService</text><text x="670" y="122" text-anchor="middle" fill="#222" stroke="none" font-size="20">pool de N hilos</text>
 <rect x="1040" y="40" width="300" height="100" stroke-opacity=".7"/><text x="1190" y="98" text-anchor="middle" fill="{INK}" stroke="none" font-size="28">Future</text>
 <rect x="1480" y="40" width="200" height="100" stroke-opacity=".7" stroke-dasharray="6 6"/><text x="1580" y="98" text-anchor="middle" fill="{INK}" stroke="none" font-size="26">get()</text>
 <g stroke-opacity=".7" marker-end="url(#m14)"><path d="M305 90H435"/><path d="M905 90H1035"/><path d="M1345 90H1475"/></g>
</svg>
<div class="grid g2 a" style="--d:5;margin-top:70px;gap:60px">
<pre class="code" style="font-size:24px">ExecutorService pool =
  Executors.<span class="k">newFixedThreadPool</span>(<span class="k">4</span>);
Future&lt;Integer&gt; f =
  pool.<span class="k">submit</span>(() -&gt; calcular());
<span class="c">// ...mientras tanto, sigues trabajando</span>
<span class="k">int</span> r = f.<span class="k">get</span>();   <span class="c">// espera si no ha acabado</span>
pool.<span class="k">shutdown</span>();</pre>
<ul class="l" style="font-size:31px"><li><b>Callable</b>: como Runnable, pero devuelve valor.</li><li><b>BlockingQueue</b>: cola que bloquea si está vacía.</li><li><b>ConcurrentHashMap</b>, <b>AtomicInteger</b>…</li></ul></div></div>""")

# ---------------------------------------------------------------- 15 filósofos
import math
def phil():
    cx, cy, R = 280, 280, 190
    out = []
    for k in range(5):
        a = -math.pi/2 + k*2*math.pi/5
        x, y = cx + R*math.cos(a), cy + R*math.sin(a)
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="{INK}" stroke="none"/><text x="{x:.0f}" y="{y+9:.0f}" text-anchor="middle" fill="#000" stroke="none" font-size="26">F{k+1}</text>')
        a2 = a + math.pi/5
        x2, y2 = cx + 118*math.cos(a2), cy + 118*math.sin(a2)
        x3, y3 = cx + 222*math.cos(a2), cy + 222*math.sin(a2)
        out.append(f'<path d="M{x2:.0f} {y2:.0f}L{x3:.0f} {y3:.0f}" stroke="{VERM}" stroke-width="5"/>')
    return "".join(out)
S("05 · Problemas clásicos", "Filósofos", f"""
<div class="body">{ttl("Cinco filósofos, cinco tenedores<br><em>y un interbloqueo.</em>")}
<div style="display:grid;grid-template-columns:560px 1fr;gap:70px;margin-top:10px;align-items:center">
 <svg class="a" style="--d:3" viewBox="0 0 560 560" width="560" height="560" fill="none">
  <circle cx="280" cy="280" r="100" stroke="{INK}" stroke-opacity=".3"/>
  {phil()}
 </svg>
 <div class="a" style="--d:4">
  <p class="s" style="font-size:31px">Para comer hacen falta <b class="hl">dos tenedores</b>. Si todos cogen primero el de su derecha, <b class="bad">nadie puede comer y nadie suelta</b>.</p>
  <p class="cap" style="margin:40px 0 4px">Cómo se rompe el bloqueo</p>
  <ul class="l"><li><b>Romper la simetría:</b> uno coge los tenedores en orden contrario.</li><li><b>Coger los dos a la vez:</b> un método <code style="font-size:26px">synchronized</code> en la mesa; si falta uno, <code style="font-size:26px">wait()</code>.</li></ul></div>
</div></div>""")

# ---------------------------------------------------------------- 16 lectores-escritores
S("05 · Problemas clásicos", "Lectores y escritores", f"""
<div class="body">{ttl("Muchos pueden leer;<br><em>escribir, solo uno.</em>")}
<svg class="a" style="--d:3;margin-top:60px" viewBox="0 0 1680 330" width="1680" height="330" fill="none" stroke="{INK}">
 {defs(16)}
 <g font-size="26" text-anchor="middle">
  <rect x="0" y="30" width="240" height="80" stroke-opacity=".7"/><text x="120" y="80" fill="{INK}" stroke="none">Lector 1</text>
  <rect x="0" y="130" width="240" height="80" stroke-opacity=".7"/><text x="120" y="180" fill="{INK}" stroke="none">Lector 2</text>
  <rect x="0" y="230" width="240" height="80" stroke-opacity=".7"/><text x="120" y="280" fill="{INK}" stroke="none">Lector 3</text>
  <rect x="620" y="60" width="440" height="210" fill="{INK}" stroke="none"/><text x="840" y="150" fill="#000" stroke="none" font-size="34">Recurso</text><text x="840" y="196" fill="#222" stroke="none" font-size="20">dato compartido</text>
  <rect x="1440" y="115" width="240" height="100" stroke="{VERM}"/><text x="1560" y="175" fill="{VERM}" stroke="none">Escritor</text>
 </g>
 <g stroke-opacity=".6" marker-end="url(#m16)"><path d="M250 70L610 120"/><path d="M250 170H610"/><path d="M250 270L610 215"/></g>
 <path d="M1430 165H1070" stroke="{VERM}" marker-end="url(#r16)"/>
 <text x="430" y="20" fill="{MUT}" stroke="none" font-size="18" letter-spacing="4" text-anchor="middle">A LA VEZ</text><text x="1250" y="140" fill="{VERM}" stroke="none" font-size="18" letter-spacing="4" text-anchor="middle">EN EXCLUSIVA</text>
</svg>
<div class="grid g3 a" style="--d:5;margin-top:60px;gap:50px">
 <div style="border-top:1px solid var(--strong);padding-top:18px"><p class="num">01</p><p class="s" style="font-size:29px;margin-top:8px">Leer no cambia nada: <b class="hl">se comparte</b>.</p></div>
 <div style="border-top:1px solid var(--strong);padding-top:18px"><p class="num">02</p><p class="s" style="font-size:29px;margin-top:8px">Escribir sí: <b class="hl">nadie más dentro</b>.</p></div>
 <div style="border-top:1px solid var(--strong);padding-top:18px"><p class="num">03</p><p class="s" style="font-size:29px;margin-top:8px">Se cuentan las <b class="hl">peticiones de escritura</b> para que no esperen eternamente.</p></div>
</div></div>""")

# ---------------------------------------------------------------- 17 ideas clave
keys = [("Hilo", "Comparte la memoria del proceso; por eso es ligero y peligroso."),
        ("Carrera", "Dos hilos tocan lo mismo a la vez y se pierde una actualización."),
        ("Exclusión", "synchronized, locks, semáforos o atómicas: un hilo (o N) a la vez."),
        ("Espera", "wait() y notify() para esperar sin gastar CPU."),
        ("Clásicos", "Productor-consumidor, filósofos, lectores-escritores: mismos patrones.")]
kr = "".join(f'<div class="a" style="--d:{i+2};display:grid;grid-template-columns:90px 330px 1fr;gap:20px;align-items:baseline;padding:24px 0;border-bottom:1px solid var(--soft)"><span class="num" style="font-size:24px">0{i+1}</span><h3 style="font-size:44px">{a}</h3><p class="s" style="font-size:28px">{b}</p></div>' for i, (a, b) in enumerate(keys))
S("Ideas clave", "Ideas clave", f"""
<div class="body">{ttl("Lo esencial,<br><em>en cinco líneas.</em>")}
<div style="margin-top:40px;width:1500px;border-top:1px solid var(--soft)">{kr}</div></div>""")

# ---------------------------------------------------------------- salida
n = len(slides)
secs = "".join(f'<section class="slide{" on" if i == 0 else ""}" data-i="{i}">{chrome(i+1, n, s)}{inner}</section>' for i, (s, t, inner, c) in enumerate(slides))
JS = """
const S=[...document.querySelectorAll('.slide')];let i=0;const st=document.getElementById('stage');
function fit(){const k=Math.min(innerWidth/1920,innerHeight/1080);st.style.transform=`translate(-50%,-50%) scale(${k})`}
function go(n){n=Math.max(0,Math.min(S.length-1,n));S[i].classList.remove('on');i=n;S[i].classList.add('on');
 document.getElementById('hud').textContent=(i+1)+' / '+S.length;try{history.replaceState(null,'','#'+(i+1))}catch(e){}}
addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' ','Enter'].includes(e.key)){e.preventDefault();go(i+1)}
 else if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();go(i-1)}
 else if(e.key==='Home')go(0);else if(e.key==='End')go(S.length-1);
 else if(e.key==='f')document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()});
addEventListener('click',e=>go(e.clientX>innerWidth/2?i+1:i-1));
addEventListener('resize',fit);fit();
const h=parseInt(location.hash.slice(1));go(h>0?h-1:0);
"""
out = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PSP Unidad 2 · Programación multihilo</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400&family=Space+Grotesk:wght@400;500&family=Space+Mono:wght@400;700&family=Noto+Sans+JP:wght@400&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div id="stage">{secs}</div><div id="hud"></div><script>{JS}</script></body></html>"""
open(os.path.join(HERE, "index.html"), "w").write(out)
print(n, "slides")
if "--pdf" in sys.argv:
    pdf = os.path.join(HERE, "Presentacion_PSP_UD2.pdf")
    subprocess.run(["chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=15000", f"--print-to-pdf={pdf}", "file://" + os.path.join(HERE, "index.html")],
                   check=True, stderr=subprocess.DEVNULL)
    print("pdf ->", pdf)
