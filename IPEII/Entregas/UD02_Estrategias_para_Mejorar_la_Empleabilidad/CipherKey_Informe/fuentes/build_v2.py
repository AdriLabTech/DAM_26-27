import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)
from diag import ALL as D

REPO = "github.com/AdriLabTech/CipherKeyV2"
REL = "github.com/AdriLabTech/CipherKeyV2/releases/latest"

FONTS = """
"""

BASE = """
:root{
  --ink:#14212D; --text:#2A3947; --dim:#4C5D6D; --muted:#758391;
  --line:#D9E1E8; --soft:#F5F7F9; --soft2:#EDF2F6;
  --accent:#146C94; --accent-d:#0F5578; --accent-l:#E7F0F5;
  --ok:#157F5B; --err:#B42318; --warn:#A45A0A;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:var(--text);
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
img{max-width:100%}
a{color:var(--accent);text-decoration:none}

/* ───────────── INFORME ───────────── */
@page{size:A4;margin:0}
.page{width:210mm;height:297mm;background:#fff;position:relative;overflow:hidden;
  padding:24mm 19mm 17mm;page-break-after:always}
.page:last-child{page-break-after:auto}
.rh{position:absolute;left:19mm;right:19mm;top:11.5mm;display:flex;justify-content:space-between;
  font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
  border-bottom:.35mm solid var(--line);padding-bottom:2.2mm}
.rh b{font-weight:600;color:var(--dim)}
.rf{position:absolute;left:19mm;right:19mm;bottom:9mm;display:flex;justify-content:space-between;
  font-size:7pt;color:var(--muted);border-top:.35mm solid var(--line);padding-top:2.2mm}
.sec{display:flex;align-items:baseline;gap:4mm;border-bottom:.55mm solid var(--ink);
  padding-bottom:2.2mm;margin:0 0 4.2mm}
.sec .n{font-size:7.4pt;font-weight:700;letter-spacing:.16em;color:var(--accent);white-space:nowrap}
h1,h2,h3,h4{margin:0;color:var(--ink);font-family:'Inter Display','Inter',sans-serif;font-weight:600;letter-spacing:-.018em}
h2{font-size:19.5pt;line-height:1.12}
h3{font-size:10.6pt;line-height:1.3;margin:5mm 0 1.8mm;letter-spacing:-.01em}
p{margin:0 0 2.8mm;font-size:9.35pt;line-height:1.58}
.lead{font-size:11.1pt;line-height:1.5;color:var(--ink);margin-bottom:4mm}
.small{font-size:7.9pt;line-height:1.45;color:var(--muted)}
b,strong{font-weight:600;color:var(--ink)}
code{font-family:'Noto Sans Mono','DejaVu Sans Mono',monospace;font-size:8.4pt;
  background:var(--soft2);color:var(--ink);padding:.3mm 1.1mm;border-radius:.7mm}
ul{margin:0 0 3mm;padding-left:4.6mm}
li{font-size:9.3pt;line-height:1.52;margin-bottom:1.4mm;padding-left:.6mm}
li::marker{color:var(--accent)}
table{width:100%;border-collapse:collapse;margin:1.5mm 0 4mm;font-size:8.35pt;line-height:1.42}
th{text-align:left;font-size:6.9pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);border-bottom:.45mm solid var(--ink);padding:1.7mm 2.2mm;vertical-align:bottom}
td{padding:1.9mm 2.2mm;border-bottom:.25mm solid var(--line);vertical-align:top}
th[scope=row]{width:35mm;color:var(--dim);font-size:8.1pt;letter-spacing:0;text-transform:none;font-weight:600;
  border-bottom:.25mm solid var(--line)}
.kpis{display:flex;gap:4mm;margin:3mm 0 5mm}
.three{display:flex;gap:6mm;margin:3mm 0 4mm;border-top:.35mm solid var(--line);padding-top:3.4mm}
.three>div{flex:1}
.three h4{font-size:7.2pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);
  margin:0 0 1.4mm}
.three ul{margin:0;padding-left:3.4mm}
.three li{font-size:8.1pt;line-height:1.45;margin-bottom:.9mm}
.summary2{display:flex;gap:7mm;margin-top:4mm}
.summary2>div{flex:1;border-top:.55mm solid var(--accent);padding-top:2.4mm}
.summary2 .label{display:block;font-size:7.2pt;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
  color:var(--accent);margin-bottom:1.2mm}
.summary2 p{font-size:9pt;line-height:1.5;margin:0}
.kpi{flex:1;border-top:.6mm solid var(--accent);background:var(--soft);padding:3mm 3.5mm 3.2mm}
.kpi b{display:block;font-family:'Inter Display','Inter',sans-serif;font-size:25pt;line-height:1;
  letter-spacing:-.04em;color:var(--ink);font-weight:600}
.kpi span{display:block;font-size:7.4pt;line-height:1.35;color:var(--muted);margin-top:1.4mm;
  text-transform:uppercase;letter-spacing:.07em}
.note{background:var(--accent-l);border-left:1mm solid var(--accent);padding:3.2mm 4mm;margin:3.2mm 0 4mm}
.note > b:first-child{display:block;font-size:7.3pt;letter-spacing:.1em;text-transform:uppercase;color:var(--accent-d);margin-bottom:1.2mm}
.note p{font-size:9pt;margin:0;line-height:1.5}
.note p b{color:var(--ink);font-weight:600}
.note.warn{background:#FBF3E8;border-left-color:var(--warn)}
.note.warn > b:first-child{color:var(--warn)}
figure{margin:2.5mm 0 4.2mm}
figcaption{font-size:7.25pt;line-height:1.4;color:var(--muted);margin-top:1.4mm}
figcaption b{color:var(--dim);font-weight:600}
.shot{border:.3mm solid #C9D4DD;border-radius:1.2mm;background:#fff;display:block}
.shot-box{border:.3mm solid var(--line);background:var(--soft);padding:1.6mm;border-radius:1.4mm}
.row{display:flex;gap:4mm;align-items:flex-start}
.row>*{flex:1}
.grid4{display:flex;gap:3.2mm;align-items:flex-start}
.grid4>figure{flex:1;margin:0}
.grid4 figcaption{font-size:6.8pt}
.grid4 .thumb{height:36mm;border:.3mm solid #C9D4DD;border-radius:1.2mm;background:#fff;
  display:flex;align-items:center;justify-content:center;overflow:hidden}
.grid4 .thumb img{display:block;max-width:100%;max-height:100%;width:auto;height:auto}
.cover{padding:0;background:#fff}
.cover-band{position:absolute;right:0;top:0;width:63mm;height:297mm;background:#0E2131}
.cover-inner{position:absolute;left:22mm;top:22mm;width:125mm}
.cover-logo{width:57mm;display:block}
.cover-rule{width:18mm;height:1.1mm;background:var(--accent);margin:19mm 0 4.5mm}
.cover-kicker{font-size:7.6pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cover h1{font-size:36pt;line-height:1.06;margin:3.5mm 0 6mm;max-width:118mm;letter-spacing:-.035em}
.cover-sub{font-size:11.2pt;line-height:1.5;color:var(--dim);max-width:112mm}
.cover-shot{position:absolute;left:45mm;top:150mm;width:154mm;margin:0;z-index:3;
  border:.45mm solid #C9D4DD;background:#fff;padding:2.4mm;border-radius:2mm;
  box-shadow:0 6mm 18mm rgba(11,27,43,.16)}
.cover-shot img{display:block;width:100%;border-radius:1mm}
.cover-meta{position:absolute;left:22mm;bottom:18mm;width:120mm;display:grid;grid-template-columns:1fr 1fr;
  column-gap:8mm;row-gap:2.2mm;font-size:7.5pt;line-height:1.35;color:var(--dim)}
.cover-meta span{display:block;font-size:6.3pt;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);
  margin-bottom:.4mm}
.cover-meta b{font-weight:500;color:var(--ink)}
.cover-credit{position:absolute;right:8mm;bottom:10mm;width:47mm;color:#8FA6B6;font-size:6.4pt;
  line-height:1.5;letter-spacing:.06em;text-align:right;z-index:4}
.svgwrap svg text{font-family:'Inter',sans-serif !important}

/* ───────────── PRESENTACIÓN ───────────── */
@page{size:1280px 720px;margin:0}
.slide{width:1280px;height:720px;position:relative;overflow:hidden;background:#F7F5F0;
  page-break-after:always;font-family:'Inter',sans-serif;color:#14212D}
.slide:last-child{page-break-after:auto}
.slide figure{margin:0}
.s-rail{position:absolute;left:64px;right:64px;top:34px;display:flex;justify-content:space-between;
  align-items:center;font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#7C8996}
.s-rail .brand{display:flex;align-items:center;gap:9px}
.s-rail .dot{width:6px;height:6px;border-radius:50%;background:#1787C2;display:inline-block}
.s-rail .page{font-variant-numeric:tabular-nums}
.s-pad{position:absolute;left:64px;right:64px;top:92px;bottom:56px}
.eyebrow{font-size:11px;font-weight:700;letter-spacing:.19em;text-transform:uppercase;color:#1787C2;
  display:flex;align-items:center;gap:10px}
.eyebrow::before{content:"";width:22px;height:3px;background:#1787C2;display:block}
.slide h1{font-family:'Inter Display','Inter',sans-serif;font-weight:600;font-size:46px;line-height:1.05;
  letter-spacing:-.035em;margin:13px 0 0;max-width:640px}
.slide h1 em{font-style:normal;color:#1787C2}
.slide h2{font-family:'Inter Display','Inter',sans-serif;font-weight:600;font-size:30px;line-height:1.12;
  letter-spacing:-.03em;margin:0}
.lead{font-size:18px;line-height:1.45;color:#4E5F6E;max-width:520px;margin:14px 0 0}
.lead b{color:#14212D}
.sfoot{position:absolute;left:64px;right:64px;bottom:22px;display:flex;justify-content:space-between;
  font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#8B98A4}
.frame{background:#fff;border:1px solid #D2DBE3;border-radius:11px;padding:8px;
  box-shadow:0 22px 48px rgba(12,27,43,.16),0 2px 6px rgba(12,27,43,.06)}
.frame img{display:block;width:100%;border-radius:5px}
.cap{font-size:11px;line-height:1.35;color:#7B8895;margin-top:9px}
.cap b{color:#4E5F6E;font-weight:600}
.num-list{list-style:none;margin:0;padding:0}
.num-list li{display:flex;gap:14px;padding:12px 0;border-top:1px solid #DDE3E8;font-size:16px;line-height:1.35}
.num-list li:last-child{border-bottom:1px solid #DDE3E8}
.num-list .n{width:24px;flex:none;font-size:11px;font-weight:700;letter-spacing:.06em;color:#1787C2;padding-top:3px}
.num-list .t{font-weight:600;color:#14212D;display:block;font-size:16px;line-height:1.3}
.num-list .d{display:block;color:#62717F;font-size:13px;line-height:1.4;margin-top:3px}
.pain{list-style:none;margin:0;padding:0}
.pain li{display:flex;gap:13px;padding:13px 0;border-top:1px solid #DDE3E8;font-size:15.5px;line-height:1.38}
.pain li:last-child{border-bottom:1px solid #DDE3E8}
.pain .x{width:22px;height:22px;flex:none;border-radius:50%;background:#F6E7E5;color:#B42318;
  font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:1px}
.pain b{display:block;font-size:15.5px;color:#14212D}
.pain span{display:block;font-size:12.5px;color:#687784;margin-top:2px}
.quote{border-left:3px solid #1787C2;padding:2px 0 2px 15px;font-size:16px;line-height:1.4;color:#14212D;font-weight:500}
.cards3{display:flex;flex-direction:column;gap:0}
.card{border-top:1px solid #DDE3E8;padding:15px 0;display:flex;gap:14px;align-items:flex-start}
.card:last-of-type{border-bottom:1px solid #DDE3E8}
.card .ico{width:38px;height:38px;flex:none;border-radius:10px;background:#E7F0F5;color:#146C94;
  display:flex;align-items:center;justify-content:center}
.card h3{font-size:16px;line-height:1.25;margin:0 0 3px;font-family:'Inter',sans-serif;font-weight:600;letter-spacing:0}
.card p{font-size:12.5px;line-height:1.4;color:#687784;margin:0}
.small-note{font-size:11.5px;line-height:1.45;color:#7B8895;margin-top:14px;max-width:520px}
.small-note b{color:#4E5F6E}
.feat{display:flex;flex-direction:column;gap:0}
.feat .f{display:flex;gap:12px;padding:10px 0;border-top:1px solid #E0E5EA}
.feat .f:last-child{border-bottom:1px solid #E0E5EA}
.feat .n{width:20px;flex:none;font-size:10px;font-weight:700;color:#1787C2;letter-spacing:.05em;padding-top:2px}
.feat .t{font-size:14.5px;font-weight:600;color:#14212D;line-height:1.25;display:block}
.feat .d{font-size:11.5px;color:#6B7A87;line-height:1.35;display:block;margin-top:2px}
.reasons{display:grid;grid-template-columns:1fr 1fr;gap:0 28px}
.reason{padding:13px 0;border-top:1px solid #DDE3E8}
.reason:nth-last-child(-n+2){border-bottom:1px solid #DDE3E8}
.reason .n{font-size:10px;font-weight:700;color:#1787C2;letter-spacing:.08em;display:block;margin-bottom:4px}
.reason .t{font-size:14.5px;font-weight:600;color:#14212D;line-height:1.3;display:block}
.reason .d{font-size:11.5px;color:#6B7A87;line-height:1.38;display:block;margin-top:3px}
.statline{display:flex;gap:30px;margin-top:18px;padding-top:14px;border-top:1px solid #DDE3E8}
.stat b{display:block;font-family:'Inter Display','Inter',sans-serif;font-size:27px;line-height:1;
  letter-spacing:-.04em;color:#14212D;font-weight:600}
.stat span{display:block;font-size:9px;letter-spacing:.13em;text-transform:uppercase;color:#8B98A4;margin-top:4px}
.title-slide{background:#F7F5F0}
.title-logo{width:290px;display:block}
.title-statement{font-family:'Inter Display','Inter',sans-serif;font-weight:600;font-size:54px;line-height:1.02;
  letter-spacing:-.045em;color:#14212D;margin:18px 0 0;max-width:470px}
.title-statement em{font-style:normal;color:#1787C2}
.title-sub{font-size:18px;line-height:1.5;color:#5B6B79;margin:20px 0 0;max-width:400px}
.title-meta{position:absolute;left:64px;bottom:54px;font-size:10px;letter-spacing:.12em;text-transform:uppercase;
  color:#8B98A4;line-height:1.9}
.title-meta b{color:#4E5F6E;font-weight:600}
.title-shot{position:absolute;left:556px;top:138px;width:696px;z-index:2}
.title-glow{position:absolute;left:600px;top:104px;width:640px;height:500px;background:#E3EEF5;
  border-radius:18px;transform:rotate(-1.2deg);z-index:1}
.dark{background:#0B1A28;color:#EAF1F6}
.dark .s-rail{color:#8FA6B6}
.dark .sfoot{color:#7E94A5}
.dark h1,.dark .title-statement{color:#F4F8FB}
.dark .lead{color:#AFC1CE}
.dark .lead b{color:#EAF1F6}
.dark .eyebrow{color:#5FB3DD}
.dark .eyebrow::before{background:#5FB3DD}
.dark .cap{color:#8FA6B6}
.dark .cap b{color:#C7D6E1}
.dark .frame{border-color:#2E4659;background:#122636;box-shadow:0 26px 60px rgba(0,0,0,.4)}
.logo-card{display:inline-flex;align-items:center;justify-content:center;background:#fff;border-radius:12px;
  padding:12px 18px;width:250px}
.logo-card img{width:214px;display:block}
.cta{display:inline-flex;align-items:center;gap:12px;background:#1787C2;color:#fff;font-size:15px;font-weight:600;
  padding:13px 20px;border-radius:8px;text-decoration:none;margin-top:22px}
.cta span{font-size:18px;line-height:1}
.cta-url{font-size:11.5px;color:#8FA6B6;margin-top:12px;letter-spacing:.02em;word-break:break-all}
.platforms{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}
.chip{font-size:10.5px;color:#C7D6E1;border:1px solid #2E4659;background:#122636;border-radius:999px;
  padding:6px 11px;letter-spacing:.04em}
.dark-shot{position:absolute;right:64px;top:128px;width:476px;z-index:2}
.dark-note{position:absolute;left:64px;bottom:76px;width:420px;font-size:11px;color:#7E94A5;line-height:1.5}
.dark-note b{color:#C7D6E1}
.bleed{position:absolute;right:-36px;top:118px;width:740px;z-index:2}
.slide-tag{position:absolute;right:64px;top:30px;font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:#8B98A4}
"""

def fig(svg, num, cap, width="100%", extra=""):
    return (f'<figure class="svgwrap {extra}" style="width:{width}">{svg}'
            f'<figcaption><b>Fig. {num}</b> — {cap}</figcaption></figure>')

def page(n, total, kicker, title, body, cls=""):
    return f'''
<section class="page {cls}">
 <div class="rh"><span><b>CipherKey</b> · Informe técnico</span><span>Versión 4.0.0</span></div>
 <div class="sec"><span class="n">{kicker}</span><h2>{title}</h2></div>
 {body}
 <div class="rf"><span>AdriLabTech · 30 de octubre de 2026</span><span>{n:02d} / {total:02d}</span></div>
</section>'''

TOTAL = 10

cover = f'''
<section class="page cover">
 <div class="cover-band"></div>
 <div class="cover-inner">
  <img class="cover-logo" src="img/logo-crop.png" alt="CipherKey">
  <div class="cover-rule"></div>
  <div class="cover-kicker">Informe técnico · Versión 4.0.0</div>
  <h1>La bóveda de contraseñas que vive en tu equipo.</h1>
  <p class="cover-sub">CipherKey es un gestor de contraseñas de escritorio, cifrado y totalmente offline. Un único fichero, una clave maestra y ningún servidor.</p>
 </div>
 <figure class="cover-shot"><img src="img/dashboard-light.png" alt="Panel principal de CipherKey"></figure>
 <div class="cover-meta">
  <div><span>Aplicación</span><b>CipherKey · CipherKeyV2</b></div>
  <div><span>Autor</span><b>AdriLabTech</b></div>
  <div><span>Tecnología</span><b>Java 25 · Swing + FlatLaf</b></div>
  <div><span>Licencia</span><b>MIT</b></div>
  <div><span>Repositorio</span><b>{REPO}</b></div>
  <div><span>Fecha</span><b>30 de octubre de 2026</b></div>
 </div>
 <div class="cover-credit">Documento técnico<br>Versión 4.0.0<br>Distribución pública</div>
</section>'''

p2 = page(2, TOTAL, "01 // Resumen ejecutivo", "La aplicación en una página", f'''
<p class="lead">CipherKey reúne todas las credenciales del usuario en un único fichero cifrado (<code>.ckey</code>) que solo se abre con una clave maestra. No requiere servidor, cuenta ni conexión de red: el fichero reside en el equipo y su titular decide dónde guardarlo.</p>
<table>
 <tr><th scope="row">Aplicación</th><td>CipherKey 4.0.0, repositorio público <b>CipherKeyV2</b></td></tr>
 <tr><th scope="row">Problema</th><td>La multiplicación de cuentas empuja a reutilizar contraseñas, anotarlas o delegar su custodia en un tercero.</td></tr>
 <tr><th scope="row">Solución</th><td>Una bóveda local cifrada con Argon2id y AES-256-GCM, con generador, auditoría, 2FA TOTP e importación desde otros gestores.</td></tr>
 <tr><th scope="row">Público</th><td>Usuarios que priorizan el control de sus datos y no necesitan sincronización en la nube ni autorrelleno en el navegador.</td></tr>
 <tr><th scope="row">Estado</th><td>Publicada. La release 4.0.0 incluye instaladores para Linux, Windows y macOS, además de un JAR universal.</td></tr>
</table>
<div class="kpis">
 <div class="kpi"><b>1</b><span>fichero cifrado con todas las credenciales</span></div>
 <div class="kpi"><b>0</b><span>conexiones de red, cuentas o servidores</span></div>
 <div class="kpi"><b>256</b><span>bits de clave en AES-GCM</span></div>
</div>
<p>El diseño prioriza la autonomía: no hay un servicio que pueda caer, cambiar de condiciones o exponer los datos. La contrapartida es explícita y se documenta en este informe: CipherKey no sincroniza dispositivos, no se integra en el navegador y no permite recuperar una clave maestra olvidada.</p>
<div class="three">
 <div><h4>Bóveda</h4><ul>
  <li>Fichero <code>.ckey</code> único y cifrado.</li>
  <li>Guardado atómico con copia de seguridad.</li>
  <li>Bloqueo por inactividad y clave borrada al cerrar.</li>
 </ul></div>
 <div><h4>Herramientas</h4><ul>
  <li>Generador de 8 a 64 caracteres.</li>
  <li>Auditoría de contraseñas débiles o repetidas.</li>
  <li>2FA TOTP e historial por entrada.</li>
 </ul></div>
 <div><h4>Distribución</h4><ul>
  <li>Importación y exportación CSV.</li>
  <li>Paquetes nativos para tres sistemas.</li>
  <li>Código abierto con licencia MIT.</li>
 </ul></div>
</div>
<div class="note"><b>Verificable, no una maqueta</b><p>El código es abierto (MIT), las pruebas se ejecutan en integración continua y la versión 4.0.0 está publicada como release descargable. El informe se apoya en el repositorio, las pruebas y las capturas de la aplicación.</p></div>
''')

p3 = page(3, TOTAL, "02 // El problema", "Demasiadas cuentas, demasiada confianza", f'''
<p class="lead">La memoria humana no escala al ritmo de los servicios digitales. Cuando aparecen decenas de cuentas, surgen cuatro atajos. Todos resuelven el momento; ninguno resuelve el riesgo.</p>
<table>
 <tr><th style="width:42mm">Atajo habitual</th><th>Consecuencia</th></tr>
 <tr><td><b>Repetir la contraseña</b></td><td>Una filtración en el servicio más débil compromete el resto de cuentas.</td></tr>
 <tr><td><b>Dejarla en el navegador</b></td><td>Queda vinculada a un perfil y a un navegador, sin una clave maestra propia.</td></tr>
 <tr><td><b>Apuntarla en notas o papel</b></td><td>Se pierde, se copia o se lee sin ninguna barrera de cifrado.</td></tr>
 <tr><td><b>Usar un gestor en la nube</b></td><td>Funciona, pero los datos viven en un servidor ajeno y dependen de una cuenta, una cuota y una política externa.</td></tr>
</table>
{fig(D['problema'](), 1, 'Del problema a la solución: sustituir la dispersión por una bóveda local.', '165mm')}
<div class="note"><b>Lo que resuelve CipherKey</b><p>Ofrece una forma segura y cómoda de usar contraseñas distintas y fuertes en cada servicio <b>sin ceder los datos a nadie</b>: el cifrado, el fichero y la clave permanecen bajo el control del usuario.</p></div>
<p>El coste de los atajos no es solo técnico. También es operativo: rotar contraseñas, reconstruir accesos tras una filtración o confiar en la continuidad de un proveedor consume tiempo y atención. CipherKey reduce esa carga a un gesto: abrir la bóveda con una clave.</p>
''')

p4 = page(4, TOTAL, "03 // Alcance funcional", "Qué hace CipherKey y qué deja fuera", f'''
<p class="lead">La aplicación cubre el ciclo completo de una credencial: custodiarla, organizarla, generarla, protegerla, auditarla e intercambiarla con otros formatos. El alcance está deliberadamente acotado.</p>
{fig(D['responsabilidades'](), 2, 'Las seis responsabilidades funcionales de CipherKey.', '160mm')}
<table>
 <tr><th style="width:31mm">Responsabilidad</th><th>Implementación</th></tr>
 <tr><td><b>Custodiar</b></td><td>Cifrado AES-256-GCM y guardado atómico (fichero temporal, <code>fsync</code> y renombrado) con copia <code>.bak</code> de la versión anterior.</td></tr>
 <tr><td><b>Organizar</b></td><td>Entradas con usuario, contraseña, sitio web y notas; categorías, favoritas y búsqueda instantánea por cualquier campo.</td></tr>
 <tr><td><b>Generar</b></td><td>Contraseñas de 8 a 64 caracteres, opción sin caracteres ambiguos y medidor de fuerza en vivo.</td></tr>
 <tr><td><b>Proteger</b></td><td>Bloqueo automático por inactividad (5 minutos por defecto, configurable), portapapeles que se vacía a los 30 segundos y clave derivada borrada al bloquear.</td></tr>
 <tr><td><b>Auditar</b></td><td>Detección de contraseñas débiles, repetidas, vacías o sin cambiar en más de un año; historial de las últimas 10 por entrada.</td></tr>
 <tr><td><b>Interoperar</b></td><td>Códigos 2FA TOTP por entrada, importación CSV (Bitwarden, Chrome/Edge/Firefox, KeePass), exportación CSV y copia de seguridad cifrada.</td></tr>
</table>
<div class="note warn"><b>Fuera de alcance, por diseño</b><p><b>Sincronización entre dispositivos</b> (se resuelve copiando el fichero), <b>autorrelleno en el navegador</b> y <b>recuperación de una clave maestra olvidada</b>. Son límites conscientes, no carencias pendientes: sostienen el modelo de confianza.</p></div>
''')

p5 = page(5, TOTAL, "04 // La aplicación", "La interfaz, en detalle", f'''
<p class="lead">La versión 4.0.0 incorpora un rediseño completo con temas claro y oscuro. El tema se recuerda entre sesiones y la interfaz mantiene la misma estructura: categorías a la izquierda, lista central y detalle a la derecha.</p>
<figure class="shot-box" style="margin-top:3mm;margin-bottom:3mm">
 <img class="shot" src="img/dashboard-light.png" alt="Panel principal en tema claro" style="width:100%;display:block">
 <figcaption style="padding:0 1mm"><b>Fig. 3</b> — Panel principal: barra lateral, lista ordenable, buscador y detalle con código 2FA.</figcaption>
</figure>
<div class="grid4">
 <figure><div class="thumb"><img src="img/login-light.png" alt="Acceso a la bóveda"></div><figcaption><b>Acceso</b> — bóvedas recientes o «Examinar…».</figcaption></figure>
 <figure><div class="thumb"><img src="img/entry.png" alt="Edición de una entrada"></div><figcaption><b>Entrada</b> — usuario, contraseña, sitio, categoría, 2FA y notas.</figcaption></figure>
 <figure><div class="thumb"><img src="img/generator.png" alt="Generador de contraseñas"></div><figcaption><b>Generador</b> — de 8 a 64 caracteres y medidor de fuerza.</figcaption></figure>
 <figure><div class="thumb"><img src="img/audit.png" alt="Auditoría de contraseñas"></div><figcaption><b>Auditoría</b> — débiles, repetidas o antiguas.</figcaption></figure>
</div>
<p style="margin-top:4mm">La búsqueda se activa con <code>Ctrl+F</code> y recorre todos los campos. El panel de detalle permite mostrar, copiar y ocultar la contraseña, además de mostrar el código TOTP con su cuenta atrás. El portapapeles se vacía automáticamente a los 30 segundos y la aplicación se bloquea tras cinco minutos de inactividad.</p>
''')

p6 = page(6, TOTAL, "05 // Arquitectura", "Capas separadas y un formato documentado", f'''
<p class="lead">El código, de aproximadamente 4.050 líneas en <code>src/main</code>, sigue una arquitectura inspirada en MVC. La seguridad y la persistencia no dependen de la interfaz, por lo que se pueden probar sin abrir ninguna ventana.</p>
{fig(D['arquitectura'](), 4, 'Capas de la aplicación: vista, controlador, modelo, seguridad y persistencia.', '160mm')}
<h3>El fichero <code>.ckey</code> (formato v2)</h3>
<p>Una bóveda es un único fichero. La cabecera guarda los parámetros de derivación de clave, de modo que pueden endurecerse en el futuro sin invalidar las bóvedas existentes. La cabecera se autentica como datos adicionales (AAD): cualquier alteración invalida el conjunto.</p>
{fig(D['formato'](), 5, 'Estructura del fichero: cabecera autenticada y bloque cifrado con AES-256-GCM.', '160mm')}
<p class="small">La contraseña maestra nunca se almacena. Argon2id la convierte, junto con una sal aleatoria de 32 bytes, en la clave de 256 bits que alimenta AES-GCM. El nonce se renueva en cada guardado.</p>
''')

p7 = page(7, TOTAL, "06 // Seguridad", "Decisiones de seguridad y flujo de apertura", f'''
<p class="lead">La seguridad se apoya en primitivas estándar y en una regla sencilla: si algo no cuadra, no se muestra ningún dato. El tag de autenticación de AES-GCM actúa como última barrera.</p>
<table>
 <tr><th style="width:36mm">Aspecto</th><th>Implementación</th></tr>
 <tr><td><b>Derivación de clave</b></td><td>Argon2id (BouncyCastle): 64 MiB, 3 iteraciones y sal aleatoria de 32 bytes. Los parámetros se validan al abrir para rechazar valores absurdos.</td></tr>
 <tr><td><b>Cifrado</b></td><td>AES-256-GCM con un nonce aleatorio de 12 bytes nuevo en cada guardado.</td></tr>
 <tr><td><b>Integridad</b></td><td>La cabecera se autentica como AAD; cualquier modificación invalida la bóveda.</td></tr>
 <tr><td><b>Memoria</b></td><td>La contraseña maestra no se conserva tras abrir. La clave derivada se pone a cero al bloquear.</td></tr>
 <tr><td><b>Red</b></td><td>Ninguna. La aplicación no abre conexiones de red.</td></tr>
</table>
{fig(D['flujo'](), 6, 'Flujo de apertura: validación de cabecera, derivación con Argon2id y descifrado autenticado.', '150mm')}
{fig(D['offline'](), 7, 'Modelo de confianza: todo el proceso ocurre dentro del equipo del usuario.', '140mm')}
<p>Este diseño tiene una consecuencia deliberada: quien obtenga el fichero puede intentar adivinar la clave sin límite de intentos. La defensa real es Argon2id y una clave maestra larga; el límite de intentos de la pantalla de acceso es una medida de usabilidad, no de seguridad.</p>
''')

p8 = page(8, TOTAL, "07 // Valor diferencial", "Por qué usar CipherKey", f'''
<ul>
 <li><b>Control total.</b> Un fichero que el usuario guarda, copia o cifra donde quiera. Sin cuenta, sin suscripción y sin servidor al que confiar nada.</li>
 <li><b>Seguridad por diseño, no por promesa.</b> Argon2id y AES-GCM, formato documentado y código abierto (MIT) que cualquiera puede revisar.</li>
 <li><b>Adopción sin fricción.</b> Importa contraseñas desde Bitwarden, Chrome/Edge/Firefox o KeePass, y permite exportarlas cuando quiera: no ata al usuario.</li>
 <li><b>Instalación sencilla.</b> Los paquetes incluyen su propio Java; no es necesario instalar nada más.</li>
 <li><b>Más que un almacén.</b> Genera, mide, audita y muestra el código 2FA junto a cada contraseña.</li>
</ul>
<table>
 <tr><th style="width:32mm"></th><th>CipherKey</th><th>Gestor en la nube</th><th>Navegador</th></tr>
 <tr><td><b>Dónde están los datos</b></td><td>Equipo del usuario</td><td>Servidor del proveedor (cifrados)</td><td>Perfil del navegador</td></tr>
 <tr><td><b>Cuenta necesaria</b></td><td>No</td><td>Sí</td><td>Normalmente sí</td></tr>
 <tr><td><b>Sincroniza dispositivos</b></td><td>No (copia manual)</td><td>Sí</td><td>Sí</td></tr>
 <tr><td><b>Autorrelleno</b></td><td>No</td><td>Sí</td><td>Sí</td></tr>
 <tr><td><b>Código abierto</b></td><td>Sí (MIT)</td><td>Depende</td><td>Depende</td></tr>
</table>
<div class="note warn"><b>Cuándo no es la mejor opción</b><p>Si se necesita sincronización automática entre varios dispositivos o autorrelleno en el navegador, un gestor en la nube cubre mejor ese caso. CipherKey apuesta por lo contrario: máxima autonomía y mínima superficie de ataque.</p></div>
<p>La comparación no pretende declarar un ganador universal. CipherKey es la elección coherente cuando la prioridad es que los datos no salgan del equipo y cuando el usuario acepta gestionar copias y actualizaciones por su cuenta.</p>
<div class="summary2">
 <div><span class="label">La propuesta</span><p>Seguridad fuerte, control del fichero y herramientas útiles sin crear una dependencia nueva. Un producto que se puede auditar, copiar y abandonar sin perder los datos.</p></div>
 <div><span class="label">La renuncia</span><p>Comodidad de la nube: sincronización automática y autorrelleno. CipherKey cambia esas funciones por autonomía y una superficie de ataque menor.</p></div>
</div>
''')

p9 = page(9, TOTAL, "08 // Disponibilidad", "Una aplicación real, publicada y descargable", f'''
<p class="lead">CipherKey no es una maqueta. El código está en un repositorio público de GitHub y la versión 4.0.0 se publicó como release con instaladores para tres sistemas operativos. Las capturas se tomaron sin iniciar sesión, lo que confirma que la página es pública.</p>
<figure class="shot-box" style="margin-top:2mm;margin-bottom:3mm">
 <img class="shot" src="img/gh-release-crop.png" alt="Release 4.0.0 en GitHub" style="width:100%;display:block">
 <figcaption style="padding:0 1mm"><b>Fig. 8</b> — Release 4.0.0: nueve recursos descargables, hashes SHA-256 y código fuente.</figcaption>
</figure>
<table>
 <tr><th>Sistema</th><th>Archivo</th><th style="width:24mm">Tamaño</th></tr>
 <tr><td>Debian / Ubuntu</td><td><code>cipherkey_4.0.0_amd64.deb</code></td><td>30,1 MB</td></tr>
 <tr><td>Cualquier Linux</td><td><code>CipherKey-4.0.0-linux-x64.tar.gz</code></td><td>38,1 MB</td></tr>
 <tr><td>Windows</td><td><code>CipherKey-4.0.0.msi</code> · <code>…-windows-x64.zip</code> (portable)</td><td style="white-space:nowrap">34,6 / 33,2 MB</td></tr>
 <tr><td>macOS (Apple Silicon)</td><td><code>CipherKey-4.0.0.dmg</code></td><td>36,7 MB</td></tr>
 <tr><td>Cualquiera con Java 25</td><td><code>cipherkey-4.0.0.jar</code></td><td>8,84 MB</td></tr>
</table>
<p>Descarga: <a href="https://{REL}">{REL}</a>. Cada release incluye <code>SHA256SUMS.txt</code> para verificar la descarga con <code>sha256sum -c</code>. Los instaladores no están firmados: Windows mostrará SmartScreen y macOS pedirá abrir la aplicación con clic derecho la primera vez.</p>
''')

p10 = page(10, TOTAL, "09 // Calidad y límites", "Verificación, historial y hoja de ruta", f'''
<ul>
 <li><b>Pruebas:</b> 52 pruebas unitarias (JUnit) sobre el formato y la criptografía de la bóveda, el generador, TOTP, auditoría y CSV. Cubren contraseña incorrecta, manipulación de cabecera y datos, cambio de clave, guardado atómico y parámetros KDF inválidos.</li>
 <li><b>Integración continua:</b> GitHub Actions ejecuta <code>mvn verify</code> con JDK 25 en cada push y pull request.</li>
 <li><b>Historial:</b> beta → 1.0 (clave maestra y generador) → 2.0 (gestión de bóvedas y modo oscuro) → 3.0 (2FA por email, retirado) → <b>4.0</b> (formato v2, rediseño, TOTP, auditoría y paquetes nativos).</li>
</ul>
{fig(D['pipeline'](), 9, 'Publicación automática: una etiqueta de versión genera los paquetes de los tres sistemas.', '132mm')}
<h3>Limitaciones honestas</h3>
<ul>
 <li><b>Sin recuperación:</b> si se olvida la clave maestra, los datos no se pueden recuperar. Es la consecuencia directa de que nadie más tenga la clave.</li>
 <li><b>Ataque offline:</b> quien consiga el <code>.ckey</code> puede intentar adivinar la clave sin límite de intentos. La defensa real es Argon2id y una clave maestra larga.</li>
 <li><b>Instaladores sin firmar:</b> Windows mostrará SmartScreen y macOS pedirá confirmación la primera vez.</li>
 <li><b>Sin auditoría externa:</b> no consta una revisión de seguridad independiente. El cifrado se apoya en primitivas estándar (JCA y BouncyCastle), pero el conjunto no ha sido auditado por terceros.</li>
 <li><b>Paquetes nativos no probados aquí:</b> este informe se basa en el código, las pruebas y las capturas del repositorio, no en una instalación en cada sistema.</li>
</ul>
<h3>Hoja de ruta</h3>
<p>Protección adicional de la bóveda mediante archivo de clave o FIDO2/WebAuthn, escaneo del QR de 2FA desde una imagen, bloqueo al suspender el equipo y limpieza del portapapeles al bloquear.</p>
<p class="small" style="margin-top:5mm">Fuentes: README, código fuente, informes de pruebas y página de la release del repositorio {REPO} (versión 4.0.0, commit 6e7b71a).</p>
''')

report = cover + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10

MEASURE = '''<script>
(function(){
 function run(){
  var out=[];
  document.querySelectorAll('.page,.slide').forEach(function(el,i){
   var r=el.getBoundingClientRect(), mb=0, mr=0;
   el.querySelectorAll('*').forEach(function(c){
    if(c.closest('.sfoot,.s-rail,.rf,.rh')) return;
    var b=c.getBoundingClientRect();
    if(b.width>0&&b.height>0){mb=Math.max(mb,b.bottom-r.top);mr=Math.max(mr,b.right-r.left);}
   });
   el.setAttribute('data-geom', Math.round(mb)+'x'+Math.round(mr)+' of '+Math.round(r.height)+'x'+Math.round(r.width));
   out.push((i+1)+': '+Math.round(mb)+'/'+Math.round(r.height)+'  '+Math.round(mr)+'/'+Math.round(r.width));
  });
  var m=document.createElement('pre'); m.id='metrics'; m.style.display='none';
  m.textContent=out.join('\\n'); document.body.appendChild(m);
 }
 if(document.fonts&&document.fonts.ready){document.fonts.ready.then(run);}else{window.addEventListener('load',run);}
})();
</script>'''

_COMMON, _REST = BASE.split("/* ───────────── INFORME ───────────── */")
_REPORT_CSS, _DECK_CSS = _REST.split("/* ───────────── PRESENTACIÓN ───────────── */")

def html_doc(css, body, title):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{title}</title><style>{_COMMON}{css}</style></head><body>{body}{MEASURE}</body></html>'

open("informe-v2.html", "w", encoding="utf-8").write(
    html_doc(_REPORT_CSS, report, "CipherKey 4.0.0 — Informe técnico"))
print("informe ok")

# ───────────────────────── PRESENTACIÓN · 6 DIAPOSITIVAS ─────────────────────────
def sslide(n, kicker, title, body, cls="", extra=""):
    return f'''
<section class="slide {cls}">
 <div class="s-rail"><span class="brand"><i class="dot"></i> CipherKey · Informe de producto</span><span>2026</span></div>
 <div class="s-pad">
  <div class="eyebrow">{kicker}</div>
  <h1>{title}</h1>
  {body}
 </div>
 {extra}
 <div class="sfoot"><span>CipherKey 4.0.0</span><span>{n:02d} / 06</span></div>
</section>'''

ICON_USER = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="8" r="3.4"/><path d="M5.5 20c.7-3.6 3.2-5.6 6.5-5.6s5.8 2 6.5 5.6"/></svg>'
ICON_BRIEF = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><rect x="3" y="7.5" width="18" height="12" rx="2"/><path d="M9 7.5V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1.5M3 12.5h18"/></svg>'
ICON_USERS = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="9" cy="8.5" r="3"/><path d="M3.5 19c.6-3.1 2.7-4.8 5.5-4.8s4.9 1.7 5.5 4.8"/><path d="M16 6.2a2.8 2.8 0 0 1 0 5.2M17.5 14.5c2 .4 3.2 1.9 3.6 4.3"/></svg>'

slides = []

# 01 · Portada
slides.append(f'''
<section class="slide title-slide">
 <div class="s-rail"><span class="brand"><i class="dot"></i> CipherKey · Informe de producto</span><span>2026</span></div>
 <div class="s-pad">
  <img class="title-logo" src="img/logo-crop.png" alt="CipherKey">
  <div class="title-statement">La bóveda de contraseñas que vive en <em>tu equipo.</em></div>
  <p class="title-sub">Cifrado local, sin cuentas ni servidores. Tú tienes el fichero; tú tienes la clave.</p>
 </div>
 <div class="title-glow"></div>
 <figure class="title-shot"><div class="frame"><img src="img/dashboard-light.png" alt="Panel principal de CipherKey"></div></figure>
 <div style="position:absolute;left:530px;top:556px;background:#fff;border:1px solid #D2DBE3;border-radius:999px;
   padding:8px 14px;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#4E5F6E;
   box-shadow:0 8px 20px rgba(12,27,43,.12);z-index:4"><span style="display:inline-block;width:7px;height:7px;
   border-radius:50%;background:#1787C2;margin-right:7px;vertical-align:1px"></span>100 % offline</div>
 <div class="title-meta">Versión 4.0.0 &nbsp;·&nbsp; Java 25 &nbsp;·&nbsp; Licencia MIT<br><b>{REPO}</b></div>
 <div class="sfoot"><span>AdriLabTech</span><span>01 / 06</span></div>
</section>''')

# 02 · Problema
slides.append(sslide(2, "01 / El problema", "Demasiadas cuentas.<br>Demasiada <em>confianza.</em>", f'''
<p class="lead" style="max-width:520px">Repetir contraseñas, apuntarlas o delegar en la nube resuelve el momento, no el riesgo. El coste aparece cuando algo falla.</p>
<ul class="pain" style="max-width:540px;margin-top:10px">
 <li><span class="x">×</span><div><b>Una filtración, todas las cuentas</b><span>Reutilizar la misma contraseña multiplica el daño de cualquier brecha.</span></div></li>
 <li><span class="x">×</span><div><b>Datos fuera de control</b><span>Notas, papel o el perfil del navegador no tienen una clave maestra propia.</span></div></li>
 <li><span class="x">×</span><div><b>Dependencia de terceros</b><span>La nube funciona, pero la llave la tiene otro: su cuenta, su política, su disponibilidad.</span></div></li>
</ul>
<div class="quote" style="max-width:520px;margin-top:22px">Una sola contraseña reutilizada puede abrir todas las demás puertas.</div>
''', extra=f'''
<figure style="position:absolute;right:64px;top:142px;width:462px;z-index:2">
 <div class="frame"><img src="img/login-light.png" alt="Pantalla de acceso a CipherKey"></div>
 <figcaption class="cap"><b>El punto de partida</b> — una bóveda local, una clave maestra, ningún servidor.</figcaption>
</figure>'''))

# 03 · A quién va dirigida
slides.append(sslide(3, "02 / A quién va dirigida", "Para quien quiere control,<br>no sincronización.", f'''
<div class="cards3" style="max-width:610px;margin-top:14px">
 <div class="card"><div class="ico">{ICON_USER}</div><div><h3>Particulares</h3><p>Decenas de cuentas personales y una sola bóveda que copiar, mover o guardar donde quieran.</p></div></div>
 <div class="card"><div class="ico">{ICON_BRIEF}</div><div><h3>Profesionales y autónomos</h3><p>Credenciales de clientes, servicios y proyectos separadas por categorías y protegidas con 2FA.</p></div></div>
 <div class="card"><div class="ico">{ICON_USERS}</div><div><h3>Equipos pequeños</h3><p>Un fichero compartido de forma controlada, sin depender de una cuenta corporativa ni de un proveedor.</p></div></div>
</div>
<p class="small-note"><b>No es la mejor opción</b> si se necesita sincronización automática entre dispositivos o autorrelleno en el navegador. CipherKey prioriza la autonomía, no la comodidad de la nube.</p>
''', extra=f'''
<figure style="position:absolute;right:64px;top:112px;width:366px;z-index:2">
 <div class="frame"><img src="img/entry.png" alt="Edición de una entrada en CipherKey"></div>
 <figcaption class="cap"><b>Una entrada, todo el contexto</b> — usuario, contraseña, sitio, 2FA y notas.</figcaption>
</figure>'''))

# 04 · Funcionalidad
slides.append(sslide(4, "03 / Funcionalidad", "Todo el ciclo<br>de la contraseña,<br>en local.", f'''
<div class="feat" style="margin-top:16px;max-width:360px">
 <div class="f"><span class="n">01</span><div><span class="t">Custodiar</span><span class="d">AES-256-GCM, guardado atómico y copia <code>.bak</code>.</span></div></div>
 <div class="f"><span class="n">02</span><div><span class="t">Organizar</span><span class="d">Categorías, favoritas y búsqueda instantánea.</span></div></div>
 <div class="f"><span class="n">03</span><div><span class="t">Generar</span><span class="d">De 8 a 64 caracteres y medidor de fuerza.</span></div></div>
 <div class="f"><span class="n">04</span><div><span class="t">Proteger</span><span class="d">Bloqueo por inactividad y portapapeles que se vacía.</span></div></div>
 <div class="f"><span class="n">05</span><div><span class="t">Auditar</span><span class="d">Débiles, repetidas o antiguas, con historial.</span></div></div>
 <div class="f"><span class="n">06</span><div><span class="t">Interoperar</span><span class="d">2FA TOTP, importación CSV y copia cifrada.</span></div></div>
</div>
''', extra=f'''
<figure style="position:absolute;left:500px;top:114px;width:700px;z-index:1">
 <div class="frame"><img src="img/dashboard-light.png" alt="Panel principal de CipherKey"></div>
</figure>
<figure style="position:absolute;left:452px;top:468px;width:222px;z-index:3">
 <div class="frame"><img src="img/generator.png" alt="Generador de contraseñas"></div>
</figure>
<figure style="position:absolute;left:922px;top:472px;width:252px;z-index:3">
 <div class="frame"><img src="img/audit.png" alt="Auditoría de contraseñas"></div>
</figure>'''))

# 05 · Por qué usarla
slides.append(sslide(5, "04 / Por qué usar CipherKey", "Tus contraseñas no salen<br>de <em>tu equipo.</em>", f'''
<p class="lead" style="max-width:510px">Seguridad, comodidad y control en una sola aplicación de escritorio. El resumen de lo que CipherKey aporta frente a las alternativas.</p>
<div class="reasons" style="max-width:530px;margin-top:12px">
 <div class="reason"><span class="n">01</span><span class="t">Control real</span><span class="d">Un fichero que puedes copiar, mover o cifrar donde quieras. Sin cuenta ni suscripción.</span></div>
 <div class="reason"><span class="n">02</span><span class="t">Seguridad verificable</span><span class="d">Argon2id + AES-256-GCM, formato documentado y código abierto (MIT).</span></div>
 <div class="reason"><span class="n">03</span><span class="t">Cero fricción</span><span class="d">Importa desde Bitwarden, navegadores o KeePass; los paquetes incluyen su Java.</span></div>
 <div class="reason"><span class="n">04</span><span class="t">Más que un almacén</span><span class="d">Genera, audita y muestra el 2FA junto a cada contraseña.</span></div>
</div>
<div class="statline" style="max-width:530px">
 <div class="stat"><b>1</b><span>fichero cifrado</span></div>
 <div class="stat"><b>0</b><span>conexiones</span></div>
 <div class="stat"><b>256</b><span>bits AES-GCM</span></div>
</div>
''', extra=f'''
<figure style="position:absolute;right:42px;top:132px;width:612px;z-index:2">
 <div class="frame"><img src="img/dashboard-dark.png" alt="Panel principal en tema oscuro"></div>
 <figcaption class="cap"><b>Panel principal</b> — tema oscuro, datos de ejemplo.</figcaption>
</figure>'''))

# 06 · Cierre / descarga
slides.append(f'''
<section class="slide dark">
 <div class="s-rail"><span class="brand"><i class="dot" style="background:#5FB3DD"></i> CipherKey · Informe de producto</span><span>2026</span></div>
 <div class="s-pad" style="width:590px">
  <div class="logo-card"><img src="img/logo-crop.png" alt="CipherKey"></div>
  <div class="eyebrow" style="margin-top:24px">05 / Empieza aquí</div>
  <h1 style="color:#F4F8FB;margin-top:12px">Descárgala.<br>Tus datos son <em style="font-style:normal;color:#5FB3DD">tuyos.</em></h1>
  <p class="lead" style="max-width:480px;margin-top:14px">Una aplicación real, publicada y lista para usar en Linux, Windows y macOS.</p>
  <a class="cta" href="https://{REL}">Descargar CipherKey 4.0.0 <span>→</span></a>
  <div class="cta-url">{REL}</div>
  <div class="platforms"><span class="chip">.deb</span><span class="chip">.tar.gz</span><span class="chip">.msi</span><span class="chip">.dmg</span><span class="chip">.jar</span></div>
  <div class="dark-note">Release 4.0.0 · 9 paquetes · <b>SHA-256</b> incluido<br>Licencia MIT · Sin cuenta · Sin suscripción</div>
 </div>
 <figure class="dark-shot">
  <div class="frame"><img src="img/login-dark.png" alt="Pantalla de acceso en tema oscuro"></div>
  <figcaption class="cap"><b>Abre tu bóveda</b> — el mismo acceso, en tema oscuro.</figcaption>
 </figure>
 <div class="sfoot"><span>AdriLabTech · CipherKeyV2</span><span>06 / 06</span></div>
</section>''')

deck = "".join(slides)
open("presentacion-v2.html", "w", encoding="utf-8").write(
    html_doc(_DECK_CSS, deck, "CipherKey 4.0.0 — Presentación"))
print("deck ok")
