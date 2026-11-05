import os
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

REPO = "github.com/AdriLabTech/CipherKeyV2"
REL = "github.com/AdriLabTech/CipherKeyV2/releases/latest"
FECHA = "30 de octubre de 2026"

CSS = """
:root{
  --ink:#14212D; --text:#2A3947; --dim:#4C5D6D; --muted:#758391;
  --line:#D9E1E8; --soft:#F5F7F9; --soft2:#EDF2F6;
  --accent:#146C94; --accent-d:#0F5578; --accent-l:#E7F0F5;
  --warn:#A45A0A;
  --raised:#FFFFFF; --paper:#FFFFFF; --sec:#DCE6EE; --brand:#146C94;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:var(--text);
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
img{max-width:100%}
a{color:var(--accent);text-decoration:none}

@page{size:A4;margin:0}
.page{width:210mm;height:297mm;background:#fff;position:relative;overflow:hidden;
  padding:24mm 19mm 16mm;page-break-after:always}
.page:last-child{page-break-after:auto}
.rh{position:absolute;left:19mm;right:19mm;top:11.5mm;display:flex;justify-content:space-between;
  font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
  border-bottom:.35mm solid var(--line);padding-bottom:2.2mm}
.rh b{font-weight:600;color:var(--dim)}
.rf{position:absolute;left:19mm;right:19mm;bottom:9mm;display:flex;justify-content:space-between;
  font-size:7pt;color:var(--muted);border-top:.35mm solid var(--line);padding-top:2.2mm}

h1,h2,h3,h4{margin:0;color:var(--ink);font-family:'Inter Display','Inter',sans-serif;
  font-weight:600;letter-spacing:-.018em}
p{margin:0 0 2.8mm;font-size:10pt;line-height:1.6}
b,strong{font-weight:600;color:var(--ink)}
code{font-family:'Noto Sans Mono','DejaVu Sans Mono',monospace;font-size:8.5pt;
  background:var(--soft2);color:var(--ink);padding:.3mm 1.1mm;border-radius:.7mm}

/* cabecera de portada */
.hero{display:flex;gap:9mm;align-items:flex-start;margin-bottom:10mm}
.hero-l{width:88mm;flex:none}
.logo{width:44mm;display:block;margin-bottom:7mm}
.kicker{font-size:7.1pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.hero h1{font-size:34pt;line-height:1.02;margin:3mm 0 3.8mm;letter-spacing:-.038em}
.hero-sub{font-size:11.2pt;line-height:1.52;color:var(--dim);margin:0}
.hero-shot{flex:1;margin:0}
.shot{border:.3mm solid #C9D4DD;border-radius:1.2mm;background:#fff;display:block;width:100%}
.shot-box{border:.3mm solid var(--line);background:var(--soft);padding:1.6mm;border-radius:1.4mm}
figcaption{font-size:6.9pt;line-height:1.4;color:var(--muted);margin-top:1.3mm}
figcaption b{color:var(--dim);font-weight:600}

/* secciones */
.sec{display:flex;align-items:baseline;gap:4mm;border-bottom:.5mm solid var(--ink);
  padding-bottom:2.1mm;margin:0 0 4.2mm}
.sec .n{font-size:7.2pt;font-weight:700;letter-spacing:.16em;color:var(--accent);white-space:nowrap}
.sec h2{font-size:19.5pt;line-height:1.1}
.block{margin-bottom:9.6mm}
.block:last-child{margin-bottom:0}
.lead{font-size:11pt;line-height:1.48;color:var(--ink);margin-bottom:3.4mm}

/* tablas */
table{width:100%;border-collapse:collapse;margin:1mm 0 0;font-size:9pt;line-height:1.46}
th{text-align:left;font-size:6.8pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);border-bottom:.45mm solid var(--ink);padding:1.9mm 2.2mm;vertical-align:bottom}
td{padding:2.2mm 2.2mm;border-bottom:.25mm solid var(--line);vertical-align:top}
th[scope=row]{width:36mm;color:var(--dim);font-size:8.7pt;letter-spacing:0;text-transform:none;
  font-weight:600;border-bottom:.25mm solid var(--line)}

/* listas */
ul{margin:0;padding-left:4.6mm}
li{font-size:9.9pt;line-height:1.52;margin-bottom:1.9mm;padding-left:.4mm}
li::marker{color:var(--accent)}

.note{background:var(--accent-l);border-left:1mm solid var(--accent);padding:3.6mm 4mm;margin:3.4mm 0 0}
.note > b:first-child{display:block;font-size:7.2pt;letter-spacing:.1em;text-transform:uppercase;
  color:var(--accent-d);margin-bottom:1.1mm}
.note p{font-size:9.7pt;margin:0;line-height:1.52}
.note.warn{background:#FBF3E8;border-left-color:var(--warn)}
.note.warn > b:first-child{color:var(--warn)}

/* público */
.aud{display:flex;flex-direction:column;gap:0}
.aud .r{display:flex;gap:4mm;padding:4.2mm 0;border-top:.25mm solid var(--line)}
.aud .r:last-child{border-bottom:.25mm solid var(--line)}
.aud .k{width:46mm;flex:none;font-size:9.4pt;font-weight:600;color:var(--ink);line-height:1.35}
.aud .d{font-size:9.4pt;line-height:1.48;color:var(--text)}

/* miniaturas */
.thumbs{display:flex;gap:3.2mm;margin-top:4.6mm}
.thumbs figure{flex:1;margin:0}
.thumbs .t{height:37mm;border:.3mm solid #C9D4DD;border-radius:1.2mm;background:#fff;
  display:flex;align-items:center;justify-content:center;overflow:hidden}
.thumbs .t img{display:block;max-width:100%;max-height:100%;width:auto;height:auto}
.thumbs figcaption{font-size:7pt;margin-top:1.3mm}

/* motivos */
.reasons{display:grid;grid-template-columns:1fr 1fr;gap:0 8mm;margin-top:1mm}
.reason{padding:3.7mm 0;border-top:.25mm solid var(--line)}
.reason:nth-last-child(-n+2){border-bottom:.25mm solid var(--line)}
.reason .n{font-size:6.9pt;font-weight:700;letter-spacing:.1em;color:var(--accent);display:block;margin-bottom:1.2mm}
.reason .t{font-size:10.2pt;font-weight:600;color:var(--ink);line-height:1.3;display:block}
.reason .d{font-size:9.2pt;line-height:1.46;color:var(--text);display:block;margin-top:1mm}

.kpis{display:flex;gap:4mm;margin:5mm 0 0}
.kpi{flex:1;border-top:.6mm solid var(--accent);background:var(--soft);padding:3.4mm 3.6mm 3.6mm}
.kpi b{display:block;font-family:'Inter Display','Inter',sans-serif;font-size:27pt;line-height:1;
  letter-spacing:-.04em;color:var(--ink);font-weight:600}
.kpi span{display:block;font-size:7.5pt;line-height:1.35;color:var(--muted);margin-top:1.2mm;
  text-transform:uppercase;letter-spacing:.07em}

.cta{display:flex;align-items:center;justify-content:space-between;gap:6mm;background:var(--ink);
  color:#fff;padding:6.2mm 7mm;margin-top:6mm;border-radius:1.2mm}
.cta h3{color:#fff;font-size:13.6pt;margin:0 0 1.4mm;letter-spacing:-.02em}
.cta p{margin:0;color:#AFC1CE;font-size:8.6pt;line-height:1.45}
.cta p b{color:#fff}
.cta .url{font-size:8.2pt;color:#CFE0EA;margin-top:1.6mm;letter-spacing:.01em;word-break:break-all}
.cta .btn{flex:none;background:#2C8FBE;color:#fff;font-size:9pt;font-weight:600;
  padding:2.6mm 4mm;border-radius:1mm;white-space:nowrap}
.cta-r{width:64mm;flex:none;text-align:right}
.chips{display:flex;gap:1.4mm;justify-content:flex-end;margin-top:3mm;flex-wrap:nowrap}
.chip{font-size:6.8pt;letter-spacing:.06em;color:#CFE0EA;border:.25mm solid #365264;
  border-radius:9mm;padding:1mm 2mm}

.quote{border-left:.9mm solid var(--accent);padding:.6mm 0 .6mm 4mm;margin:4mm 0 0;
  font-size:10.6pt;line-height:1.45;color:var(--ink);font-weight:500}
.small{font-size:7.6pt;line-height:1.45;color:var(--muted)}
"""

MEASURE = """<script>
(function(){
 function run(){
  var out=[];
  document.querySelectorAll('.page').forEach(function(el,i){
   var r=el.getBoundingClientRect(), mb=0, mr=0;
   el.querySelectorAll('*').forEach(function(c){
    if(c.closest('.rf,.rh')) return;
    var b=c.getBoundingClientRect();
    if(b.width>0&&b.height>0){mb=Math.max(mb,b.bottom-r.top);mr=Math.max(mr,b.right-r.left);}
   });
   out.push((i+1)+': '+Math.round(mb)+'/'+Math.round(r.height)+'  '+Math.round(mr)+'/'+Math.round(r.width));
  });
  var m=document.createElement('pre'); m.id='metrics'; m.style.display='none';
  m.textContent=out.join('\\n'); document.body.appendChild(m);
 }
 if(document.fonts&&document.fonts.ready){document.fonts.ready.then(run);}else{window.addEventListener('load',run);}
})();
</script>"""


def header():
    return '<div class="rh"><span><b>CipherKey</b> · Informe técnico</span><span>Versión 4.0.0</span></div>'


def footer(n):
    return f'<div class="rf"><span>AdriLabTech · {FECHA}</span><span>{n:02d} / 03</span></div>'


def sec(n, title):
    return f'<div class="sec"><span class="n">{n}</span><h2>{title}</h2></div>'


p1 = f'''
<section class="page">
 {header()}
 <div class="hero">
  <div class="hero-l">
   <img class="logo" src="img/logo-crop.png" alt="CipherKey">
   <div class="kicker">Informe técnico · Versión 4.0.0</div>
   <h1>CipherKey</h1>
   <p class="hero-sub">Las cinco preguntas esenciales del producto: qué es, qué problema resuelve, a quién sirve, qué hace y por qué usarlo.</p>
  </div>
  <figure class="hero-shot">
   <div class="shot-box"><img class="shot" src="img/dashboard-light.png" alt="Panel principal de CipherKey"></div>
   <figcaption><b>Panel principal</b> — categorías, lista de entradas y detalle con 2FA.</figcaption>
  </figure>
 </div>

 <div class="block">
  {sec("01 //", "Nombre")}
  <p class="lead">CipherKey — repositorio público <b>CipherKeyV2</b> — es un gestor de contraseñas de escritorio que reúne todas las credenciales en un único fichero cifrado y funciona sin conexión.</p>
  <table>
   <tr><th scope="row">Aplicación</th><td>CipherKey 4.0.0 · <b>CipherKeyV2</b></td></tr>
   <tr><th scope="row">Qué es</th><td>Gestor de contraseñas de escritorio con bóveda local cifrada.</td></tr>
   <tr><th scope="row">Modelo</th><td>Un fichero <code>.ckey</code> y una clave maestra. Sin cuenta, sin servidor y sin red.</td></tr>
   <tr><th scope="row">Tecnología</th><td>Java 25 · Swing + FlatLaf · licencia MIT.</td></tr>
   <tr><th scope="row">Repositorio</th><td>{REPO}</td></tr>
  </table>
 </div>

 <div class="block">
  {sec("02 //", "Problema que resuelve")}
  <p class="lead">Cada cuenta nueva añade una contraseña más que recordar. Cuando son decenas, aparecen los atajos: repetir la misma clave, apuntarla en cualquier sitio o dejarla en el navegador.</p>
  <ul>
   <li><b>Repetir la contraseña.</b> Una filtración en el servicio más débil abre todas las demás puertas.</li>
   <li><b>Apuntarla o delegarla.</b> Notas, papel y perfiles de navegador no tienen una clave maestra propia.</li>
   <li><b>Depender de la nube.</b> Funciona, pero la llave, la política y la disponibilidad las tiene un tercero.</li>
  </ul>
  <div class="note"><b>Lo que resuelve</b><p>Permite usar una contraseña distinta y fuerte en cada servicio <b>sin ceder los datos a nadie</b>: todo se cifra con AES-256-GCM en un fichero que solo se abre con la clave maestra del usuario.</p></div>
  <p class="quote">Una bóveda local, una clave maestra y ningún servidor: el problema deja de ser dónde confiar y pasa a ser cómo recordar una sola clave.</p>
 </div>
 {footer(1)}
</section>'''


p2 = f'''
<section class="page">
 {header()}
 <div class="block">
  {sec("03 //", "A quién va dirigida")}
  <p class="lead">A quien prefiere tener el control de sus datos antes que la comodidad de la sincronización.</p>
  <div class="aud">
   <div class="r"><div class="k">Particulares</div><div class="d">Decenas de cuentas personales en una sola bóveda que se copia, se mueve o se guarda donde quieran.</div></div>
   <div class="r"><div class="k">Profesionales y autónomos</div><div class="d">Credenciales de clientes, servicios y proyectos separadas por categorías y protegidas con 2FA.</div></div>
   <div class="r"><div class="k">Equipos pequeños</div><div class="d">Un fichero compartido de forma controlada, sin cuenta corporativa ni proveedor externo.</div></div>
  </div>
  <div class="note warn"><b>Cuándo no es la mejor opción</b><p>Si se necesita sincronización automática entre dispositivos o autorrelleno en el navegador, un gestor en la nube cubre mejor ese caso. CipherKey prioriza la autonomía, no la comodidad de la nube.</p></div>
 </div>

 <div class="block">
  {sec("04 //", "Funcionalidad")}
  <p class="lead">Cubre el ciclo completo de una credencial en seis responsabilidades, todas ejecutadas en local.</p>
  <table>
   <tr><th style="width:30mm">Responsabilidad</th><th>Cómo lo hace</th></tr>
   <tr><td><b>Custodiar</b></td><td>AES-256-GCM, guardado atómico y copia <code>.bak</code> de la versión anterior.</td></tr>
   <tr><td><b>Organizar</b></td><td>Categorías, favoritas y búsqueda instantánea por cualquier campo.</td></tr>
   <tr><td><b>Generar</b></td><td>Contraseñas de 8 a 64 caracteres, sin caracteres ambiguos y con medidor de fuerza.</td></tr>
   <tr><td><b>Proteger</b></td><td>Bloqueo por inactividad y portapapeles que se vacía a los 30 segundos.</td></tr>
   <tr><td><b>Auditar</b></td><td>Contraseñas débiles, repetidas o antiguas, con historial por entrada.</td></tr>
   <tr><td><b>Interoperar</b></td><td>2FA TOTP, importación CSV (Bitwarden, navegadores, KeePass) y copia cifrada.</td></tr>
  </table>
  <div class="thumbs">
   <figure><div class="t"><img src="img/login-light.png" alt="Acceso a la bóveda"></div><figcaption><b>Acceso</b> — bóvedas recientes.</figcaption></figure>
   <figure><div class="t"><img src="img/entry.png" alt="Edición de una entrada"></div><figcaption><b>Entrada</b> — datos y 2FA.</figcaption></figure>
   <figure><div class="t"><img src="img/generator.png" alt="Generador de contraseñas"></div><figcaption><b>Generador</b> — 8 a 64 caracteres.</figcaption></figure>
   <figure><div class="t"><img src="img/audit.png" alt="Auditoría de contraseñas"></div><figcaption><b>Auditoría</b> — débiles o repetidas.</figcaption></figure>
  </div>
 </div>
 {footer(2)}
</section>'''


p3 = f'''
<section class="page">
 {header()}
 <div class="block">
  {sec("05 //", "Por qué debemos usarla")}
  <p class="lead">Porque resuelve el problema sin crear una dependencia nueva: seguridad fuerte, control del fichero y herramientas útiles en una sola aplicación de escritorio.</p>
  <div class="reasons">
   <div class="reason"><span class="n">01</span><span class="t">Control real</span><span class="d">El fichero es del usuario: se copia, se mueve o se cifra donde quiera. Sin cuenta ni suscripción.</span></div>
   <div class="reason"><span class="n">02</span><span class="t">Seguridad verificable</span><span class="d">Argon2id + AES-256-GCM, formato documentado y código abierto (MIT) que cualquiera puede revisar.</span></div>
   <div class="reason"><span class="n">03</span><span class="t">Cero fricción</span><span class="d">Importa desde Bitwarden, navegadores o KeePass; los paquetes incluyen su propio Java.</span></div>
   <div class="reason"><span class="n">04</span><span class="t">Más que un almacén</span><span class="d">Genera, audita y muestra el código 2FA junto a cada contraseña.</span></div>
  </div>
  <div class="kpis">
   <div class="kpi"><b>1</b><span>fichero cifrado con todas las credenciales</span></div>
   <div class="kpi"><b>0</b><span>conexiones de red, cuentas o servidores</span></div>
   <div class="kpi"><b>256</b><span>bits de clave en AES-GCM</span></div>
  </div>
 </div>

 <div class="block">
  <h3 style="font-size:9pt;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:2mm">Frente a las alternativas</h3>
  <table>
   <tr><th style="width:40mm"></th><th>CipherKey</th><th>Gestor en la nube</th><th>Navegador</th></tr>
   <tr><td><b>Dónde están los datos</b></td><td>En el equipo del usuario</td><td>En un servidor ajeno</td><td>En el perfil del navegador</td></tr>
   <tr><td><b>Cuenta necesaria</b></td><td>No</td><td>Sí</td><td>Normalmente sí</td></tr>
   <tr><td><b>Sincronización</b></td><td>Manual (copiar el fichero)</td><td>Automática</td><td>Automática</td></tr>
   <tr><td><b>Código abierto</b></td><td>Sí (MIT)</td><td>Depende</td><td>Depende</td></tr>
  </table>
  <div class="note warn"><b>La renuncia, explícita</b><p>CipherKey no sincroniza dispositivos ni rellena formularios del navegador, y una clave maestra olvidada no se puede recuperar. Son límites conscientes que sostienen el modelo de confianza.</p></div>
 </div>

 <div class="cta">
  <div>
   <h3>Descargar CipherKey 4.0.0</h3>
   <p>Disponible para Linux, Windows y macOS. <b>Sin cuenta y sin suscripción.</b></p>
   <div class="url">{REL}</div>
  </div>
  <div class="cta-r">
   <span class="btn">Descargar →</span>
   <div class="chips"><span class="chip">.deb</span><span class="chip">.tar.gz</span><span class="chip">.msi</span><span class="chip">.dmg</span><span class="chip">.jar</span></div>
  </div>
 </div>
 <p class="small" style="margin-top:3mm">Fuentes: repositorio {REPO}, código y pruebas de la versión 4.0.0 (commit 6e7b71a). Las capturas pertenecen a la aplicación real.</p>
 {footer(3)}
</section>'''

doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
       f'<title>CipherKey 4.0.0 — Informe técnico resumido</title>'
       f'<style>{CSS}</style></head><body>{p1}{p2}{p3}{MEASURE}</body></html>')

open("informe-resumen.html", "w", encoding="utf-8").write(doc)
print("ok", len(doc))
