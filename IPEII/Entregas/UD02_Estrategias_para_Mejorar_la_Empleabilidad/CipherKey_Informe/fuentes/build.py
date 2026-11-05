import sys
sys.path.insert(0, ".")
from diag import ALL as D

WASHI = """--paper:#F3ECE0;--raised:#FAF5EC;--high:#E9E0D1;--ink:#26211C;--dim:#4A423A;--muted:#675D52;
--sec:#2B6A86;--brand:#E2342A;--brandt:#C42A21;--ok:#1F6F4D;--err:#B3261E;--line:rgba(38,33,28,.30);"""
GRAFITO = """--paper:#211D1A;--raised:#2A2521;--high:#352F2A;--ink:#ECE4D8;--dim:#C9C0B3;--muted:#A69D90;
--sec:#8FBDD1;--brand:#E2342A;--brandt:#F4665A;--ok:#7FD0AE;--err:#F27A70;--line:rgba(236,228,216,.30);"""

FONTS = """@font-face{font-family:'Komiki Mono';src:url('file:///home/adrian/.local/share/fonts/KomikiMono/KomikiMono-Regular.otf');font-weight:400}
@font-face{font-family:'Komiki Mono';src:url('file:///home/adrian/.local/share/fonts/KomikiMono/KomikiMono-Bold.otf');font-weight:700}"""

REPO = "github.com/AdriLabTech/CipherKeyV2"
REL = "github.com/AdriLabTech/CipherKeyV2/releases/latest"


def fig(svg, cap):
    return f'<figure>{svg}<figcaption>{cap}</figcaption></figure>'


def shot(src, cap, w=None, cls=""):
    st = f' style="width:{w}"' if w else ""
    return f'<figure class="shot {cls}"><img src="img/{src}"{st}><figcaption>{cap}</figcaption></figure>'


# ───────────────────────── INFORME (A4, Washi) ─────────────────────────
report_css = f"""{FONTS}
:root{{{WASHI}}}
@page{{size:A4;margin:18mm 17mm 20mm 17mm;
 @bottom-left{{content:"CipherKey 4.0.0 // Informe técnico";font:400 7.5pt 'Komiki Mono';color:#675D52}}
 @bottom-right{{content:counter(page) " / " counter(pages);font:400 7.5pt 'Komiki Mono';color:#675D52}}}}
@page:first{{margin:0;@bottom-left{{content:""}}@bottom-right{{content:""}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font:400 9.4pt/1.62 'Komiki Mono',monospace;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1,h2,h3{{margin:0;font-weight:700}}
.cover{{height:297mm;padding:26mm 22mm;position:relative;page-break-after:always;overflow:hidden;
 background:var(--paper);background-image:radial-gradient(rgba(38,33,28,.18) 1px,transparent 1.4px);background-size:16px 16px}}
.disc{{position:absolute;right:-30mm;top:-24mm;width:130mm;height:130mm;border-radius:50%;background:var(--brand);opacity:.12}}
.cover .tag{{font-size:8.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}}
.cover h1{{font-size:44pt;line-height:1.05;margin:14mm 0 6mm}}
.cover .sub{{font-size:13pt;line-height:1.5;max-width:128mm;color:var(--dim)}}
.cover img.logo{{position:absolute;right:22mm;top:92mm;width:62mm}}
.ficha{{position:absolute;left:22mm;right:22mm;bottom:22mm;border-top:2px solid var(--ink);padding-top:5mm;font-size:8.6pt}}
.ficha div{{display:flex;border-bottom:1px solid var(--line);padding:1.6mm 0}}
.ficha b{{width:42mm;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;font-size:7.6pt;padding-top:.4mm}}
h2{{font-size:17pt;margin:9mm 0 4mm;padding-top:3mm;border-top:2px solid var(--ink);break-after:avoid}}
h2 small{{display:block;font-size:8pt;letter-spacing:.12em;color:var(--brandt);margin-bottom:1.5mm}}
h3{{font-size:11pt;margin:6mm 0 2mm;break-after:avoid}}
p{{margin:0 0 3mm}}
.lead{{font-size:11pt;line-height:1.55}}
ul{{margin:0 0 3mm;padding-left:5mm}} li{{margin-bottom:1.2mm}}
code,.m{{background:var(--high);padding:0 1.2mm}}
table{{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:8.4pt;line-height:1.45;break-inside:avoid}}
th{{text-align:left;font-size:7.4pt;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--ink);padding:1.6mm 2mm}}
td{{padding:1.8mm 2mm;border-bottom:1px solid var(--line);vertical-align:top}}
tr:nth-child(even) td{{background:rgba(38,33,28,.05)}}
figure{{margin:3mm 0 5mm;break-inside:avoid}}
figcaption{{font-size:7.8pt;color:var(--muted);margin-top:1.5mm}}
figcaption::before{{content:"// "}}
figure.shot img{{display:block;border:1px solid var(--ink);max-width:100%}}
.row{{display:flex;gap:5mm;align-items:flex-start}} .row>*{{flex:1}}
.call{{border:2px solid var(--ink);border-left:6px solid var(--brand);background:var(--raised);padding:3mm 4mm;margin:3mm 0 4mm;break-inside:avoid}}
.call b{{display:block;font-size:7.6pt;letter-spacing:.1em;text-transform:uppercase;color:var(--brandt);margin-bottom:1mm}}
.nv{{color:var(--muted);font-style:italic}}
.pb{{break-before:page}}
a{{color:var(--sec)}}
"""

report_body = f"""
<section class="cover">
 <div class="disc"></div>
 <div class="tag">Informe técnico · versión 4.0.0</div>
 <h1>CipherKey</h1>
 <div class="sub">Gestor de contraseñas cifrado, de escritorio y 100&nbsp;% offline.<br>Tu seguridad no debería depender de terceros.</div>
 <img class="logo" src="img/logo.png">
 <div class="ficha">
  <div><b>Aplicación</b>CipherKey (repositorio CipherKeyV2)</div>
  <div><b>Autor</b>AdriLabTech</div>
  <div><b>Tecnología</b>Java 25 · Swing + FlatLaf · Maven · JUnit</div>
  <div><b>Licencia</b>MIT</div>
  <div><b>Repositorio</b>{REPO}</div>
  <div><b>Fecha</b>30 de octubre de 2026</div>
 </div>
</section>

<h2 style="margin-top:0;border-top:0;padding-top:0"><small>01 // RESUMEN</small>La aplicación en una página</h2>
<p class="lead"><b>CipherKey</b> es un gestor de contraseñas de escritorio. Guarda todas tus credenciales en <b>un único fichero cifrado</b> (<code>.ckey</code>) que solo se abre con <b>una clave maestra</b>. No tiene servidor, cuenta ni conexión de red: el fichero vive en tu equipo y solo tú decides dónde.</p>
<table>
<tr><th style="width:34mm">Nombre</th><td>CipherKey (versión actual 4.0.0, repositorio <span class="m">CipherKeyV2</span>)</td></tr>
<tr><th>Problema</th><td>Tener decenas de cuentas obliga a repetir contraseñas, apuntarlas o confiar en un servicio ajeno.</td></tr>
<tr><th>Solución</th><td>Una bóveda local cifrada con Argon2id + AES-256-GCM, con generador, auditoría, 2FA (TOTP) e importación.</td></tr>
<tr><th>Para quién</th><td>Quien quiere control total de sus datos y no necesita sincronizar con la nube ni autorrelleno en el navegador.</td></tr>
<tr><th>Disponibilidad</th><td>Existe y se puede descargar: release 4.0.0 con instaladores para Linux, Windows y macOS (sección 07).</td></tr>
</table>
{fig(D['problema'](), 'El problema y la solución de un vistazo.')}

<h2><small>02 // EL PROBLEMA</small>Demasiadas cuentas, demasiada confianza ajena</h2>
<p>Cada servicio exige una contraseña. La memoria humana no escala, así que aparecen cuatro atajos, todos con un coste:</p>
<table>
<tr><th style="width:44mm">Atajo habitual</th><th>Riesgo</th></tr>
<tr><td><b>Repetir la contraseña</b></td><td>Una sola filtración en un servicio débil compromete todas las demás cuentas.</td></tr>
<tr><td><b>Dejar que el navegador la guarde</b></td><td>Queda atada al navegador y al perfil, sin una clave maestra propia y específica.</td></tr>
<tr><td><b>Apuntarla en notas o papel</b></td><td>Se pierde, se copia o se lee sin ninguna barrera.</td></tr>
<tr><td><b>Usar un gestor en la nube</b></td><td>Funciona bien, pero tus datos viven en el servidor de un tercero y dependes de su cuenta, su disponibilidad y su política.</td></tr>
</table>
<div class="call"><b>Lo que CipherKey resuelve</b>Dar una forma segura y cómoda de usar contraseñas distintas y fuertes en cada sitio, <u>sin</u> ceder los datos a nadie: el cifrado, el fichero y la clave están en tu poder.</div>

<h2><small>03 // RESPONSABILIDADES</small>Qué hace CipherKey y qué no</h2>
{fig(D['responsabilidades'](), 'Las seis responsabilidades de la aplicación.')}
<table>
<tr><th style="width:30mm">Responsabilidad</th><th>Qué hace</th></tr>
<tr><td><b>Custodiar</b></td><td>Cifra la bóveda con AES-256-GCM, la guarda de forma atómica (fichero temporal + <code>fsync</code> + renombrado) y conserva un <code>.bak</code> de la versión anterior.</td></tr>
<tr><td><b>Organizar</b></td><td>Entradas con usuario, contraseña, sitio web y notas; categorías, favoritas y búsqueda instantánea por cualquier campo.</td></tr>
<tr><td><b>Generar</b></td><td>Generador de 8 a 64 caracteres (con opción sin caracteres ambiguos) y medidor de fuerza en vivo.</td></tr>
<tr><td><b>Proteger</b></td><td>Bloqueo automático por inactividad (5 min por defecto, configurable), portapapeles que se vacía a los 30 s y clave derivada puesta a cero al bloquear.</td></tr>
<tr><td><b>Auditar</b></td><td>Detecta contraseñas débiles, repetidas, sin cambiar en más de un año o vacías, y guarda el historial de las últimas 10 por entrada.</td></tr>
<tr><td><b>Interoperar</b></td><td>Códigos 2FA (TOTP) por entrada, importación CSV (Bitwarden, Chrome/Edge/Firefox, KeePass), exportación CSV y copia de seguridad cifrada.</td></tr>
</table>
<p><b>Fuera de su alcance (por diseño):</b> sincronizar entre dispositivos, autorrellenar en el navegador y recuperar una clave maestra olvidada.</p>

<h2><small>04 // LA APLICACIÓN</small>Cómo se ve y cómo se usa</h2>
<p>Las capturas son de la propia aplicación (datos de ejemplo), en tema claro y oscuro; el tema se recuerda entre sesiones.</p>
<div class="row">{shot('login-light.png','Acceso: bóvedas recientes o «Examinar…».')}{shot('login-dark.png','Mismo acceso en tema oscuro.')}</div>
{shot('dashboard-light.png','Ventana principal: barra lateral con categorías, lista ordenable y panel de detalle con código 2FA.', w='88%')}
<div class="row">{shot('entry.png','Editar entrada: usuario, contraseña, sitio, categoría, 2FA y notas.')}{shot('generator.png','Generador con medidor de fuerza.')}</div>
<div class="row">{shot('audit.png','Auditoría: contraseñas débiles, repetidas o antiguas.')}{shot('dashboard-dark.png','Panel principal en tema oscuro.')}</div>

<h2><small>05 // CÓMO FUNCIONA</small>Arquitectura y formato de la bóveda</h2>
<p>El código (~4.050 líneas en <code>src/main</code>) sigue una arquitectura inspirada en MVC con capas separadas. La lógica de seguridad y de persistencia no depende de la interfaz, por lo que se puede probar sin abrir ninguna ventana.</p>
{fig(D['arquitectura'](), 'Capas de la aplicación (paquetes dev.view, controller, model, security y persistence).')}
<h3>El fichero .ckey (formato v2)</h3>
<p>Una bóveda es un único fichero. Su cabecera guarda los parámetros de derivación de clave, de modo que se pueden endurecer en el futuro sin romper bóvedas existentes.</p>
{fig(D['formato'](), 'Estructura del fichero (anchuras no a escala).')}
<h3>Apertura de una bóveda</h3>
{fig(D['flujo'](), 'Flujo de apertura: si algo no cuadra, el tag de autenticación falla y no se muestra ningún dato.')}

<h2><small>06 // SEGURIDAD Y POR QUÉ USARLA</small>Decisiones de seguridad</h2>
<table>
<tr><th style="width:36mm">Aspecto</th><th>Implementación</th></tr>
<tr><td><b>Derivación de clave</b></td><td>Argon2id (BouncyCastle): 64 MiB, 3 iteraciones, sal aleatoria de 32 bytes. Parámetros validados al abrir para rechazar valores absurdos.</td></tr>
<tr><td><b>Cifrado</b></td><td>AES-256-GCM con nonce aleatorio de 12 bytes nuevo en cada guardado.</td></tr>
<tr><td><b>Integridad</b></td><td>La cabecera se autentica como AAD: cualquier alteración invalida la bóveda.</td></tr>
<tr><td><b>Memoria</b></td><td>La contraseña maestra no se conserva tras abrir; la clave derivada se pone a cero al bloquear.</td></tr>
<tr><td><b>Red</b></td><td>Ninguna. La aplicación no abre conexiones.</td></tr>
</table>
{fig(D['offline'](), 'Modelo de confianza: todo ocurre dentro de tu equipo.')}

<h3>Por qué deberías usarla</h3>
<ul>
<li><b>Control total.</b> Un fichero que tú guardas, copias o cifras donde quieras. Sin cuenta, sin suscripción, sin servidor al que confiar nada.</li>
<li><b>Seguridad por diseño y no por promesa.</b> Argon2id y AES-GCM, formato documentado y código abierto (MIT) que cualquiera puede revisar.</li>
<li><b>Cómoda de adoptar.</b> Importa tus contraseñas desde Bitwarden, Chrome/Edge/Firefox o KeePass y puedes exportarlas cuando quieras: no te ata.</li>
<li><b>Se instala sin fricción.</b> Los paquetes incluyen su propio Java; no necesitas instalar nada más.</li>
<li><b>Más que guardar.</b> Genera, mide, audita y muestra el código 2FA junto a la contraseña.</li>
</ul>
<table>
<tr><th style="width:30mm">&nbsp;</th><th>CipherKey</th><th>Gestor en la nube</th><th>Navegador</th></tr>
<tr><td><b>Dónde están los datos</b></td><td>Tu equipo</td><td>Servidor del proveedor (cifrados)</td><td>Perfil del navegador</td></tr>
<tr><td><b>Cuenta necesaria</b></td><td>No</td><td>Sí</td><td>Normalmente sí</td></tr>
<tr><td><b>Sincroniza dispositivos</b></td><td>No (lo haces tú copiando el fichero)</td><td>Sí</td><td>Sí</td></tr>
<tr><td><b>Autorrelleno</b></td><td>No</td><td>Sí</td><td>Sí</td></tr>
<tr><td><b>Código abierto</b></td><td>Sí (MIT)</td><td>Depende</td><td>Depende</td></tr>
</table>
<div class="call"><b>Cuándo no es la mejor opción</b>Si necesitas sincronización automática entre varios dispositivos o autorrelleno en el navegador, un gestor en la nube cubre mejor ese caso. CipherKey apuesta por lo contrario: máxima autonomía y mínima superficie de ataque.</div>

<h2 class="pb"><small>07 // EXISTE Y SE PUEDE DESCARGAR</small>La aplicación es real y está publicada</h2>
<p>CipherKey no es una maqueta: el código está en un repositorio público de GitHub y la versión 4.0.0 se publicó como <i>release</i> con instaladores para tres sistemas operativos. Las dos capturas siguientes se tomaron el 30 de octubre de 2026 sin iniciar sesión (aparece «Sign in»), lo que confirma que son públicas.</p>
{shot('gh-repo.png', f'Repositorio público {REPO}: código en Java (98,7 %), licencia MIT, 5 commits y una release «Latest».', w='86%')}
{shot('gh-release.png', 'Release CipherKey 4.0.0 con los 9 recursos descargables y sus hashes SHA-256.', w='86%')}
<table>
<tr><th>Sistema</th><th>Archivo</th><th style="width:20mm">Tamaño</th></tr>
<tr><td>Debian / Ubuntu</td><td><code>cipherkey_4.0.0_amd64.deb</code></td><td>30,1 MB</td></tr>
<tr><td>Cualquier Linux</td><td><code>CipherKey-4.0.0-linux-x64.tar.gz</code></td><td>38,1 MB</td></tr>
<tr><td>Windows</td><td><code>CipherKey-4.0.0.msi</code> · <code>…-windows-x64.zip</code> (portable)</td><td>34,6 / 33,2 MB</td></tr>
<tr><td>macOS (Apple Silicon)</td><td><code>CipherKey-4.0.0.dmg</code></td><td>36,7 MB</td></tr>
<tr><td>Cualquiera con Java 25</td><td><code>cipherkey-4.0.0.jar</code></td><td>8,84 MB</td></tr>
</table>
<p>Descarga: <a href="https://{REL}">{REL}</a>. Cada release incluye <code>SHA256SUMS.txt</code> para comprobar la descarga con <code>sha256sum -c</code>.</p>
{fig(D['pipeline'](), 'Publicación automática: una etiqueta de versión genera los paquetes de los tres sistemas.')}

<h2><small>08 // CALIDAD Y ESTADO</small>Verificación, historial y límites</h2>
<ul>
<li><b>Pruebas:</b> 52 pruebas unitarias (JUnit) sobre el formato y la criptografía de la bóveda (contraseña incorrecta, manipulación de cabecera y datos, cambio de clave, guardado atómico, parámetros KDF absurdos), el generador, TOTP, auditoría y CSV. <span id="testres"></span></li>
<li><b>Integración continua:</b> GitHub Actions ejecuta <code>mvn verify</code> con JDK 25 en cada push y pull request.</li>
<li><b>Historial:</b> Beta → 1.0 (clave maestra y generador) → 2.0 (gestión de bóvedas y modo oscuro) → 3.0 (2FA por email, retirado por no proteger el fichero) → <b>4.0</b> (formato v2, rediseño, TOTP, auditoría, paquetes nativos).</li>
</ul>
<h3>Limitaciones honestas</h3>
<ul>
<li><b>Sin recuperación:</b> si olvidas la clave maestra, los datos no se pueden recuperar. Es consecuencia directa de que nadie más tiene la clave.</li>
<li><b>Ataque offline:</b> quien consiga el <code>.ckey</code> puede intentar adivinar la clave sin límite de intentos; la defensa real es Argon2id y una clave maestra larga. El límite de intentos del acceso es solo de usabilidad.</li>
<li><b>Instaladores sin firmar:</b> Windows mostrará SmartScreen y macOS pedirá abrirla con clic derecho la primera vez.</li>
<li><b>Sin auditoría externa:</b> <span class="nv">no consta una revisión de seguridad independiente del código</span>; el cifrado se apoya en primitivas estándar (JCA y BouncyCastle) pero la aplicación como conjunto no ha sido auditada por terceros.</li>
<li><b>Los instaladores nativos no se han probado aquí:</b> este informe se basa en el código, las pruebas y las capturas del repositorio, no en una instalación en cada sistema.</li>
</ul>
<h3>Hoja de ruta</h3>
<p>Protección adicional de la bóveda (archivo de clave o FIDO2/WebAuthn) en lugar del antiguo 2FA por email · escaneo del QR del 2FA desde una imagen · bloqueo al suspender el equipo y limpieza del portapapeles al bloquear.</p>
<p style="margin-top:6mm;color:var(--muted);font-size:8pt">Fuentes: README, código fuente, informes de pruebas y página de la release del repositorio {REPO} (versión 4.0.0, commit 6e7b71a).</p>
"""

# ───────────────────────── PRESENTACIÓN (1280×720, Grafito) ─────────────────────────
deck_css = f"""{FONTS}
:root{{{GRAFITO}}}
@page{{size:1280px 720px;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font:400 22px/1.5 'Komiki Mono',monospace;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.s{{width:1280px;height:720px;position:relative;overflow:hidden;page-break-after:always;padding:56px 72px;
 background:var(--paper);background-image:radial-gradient(rgba(236,228,216,.13) 1px,transparent 1.4px);background-size:16px 16px}}
.s:last-child{{page-break-after:auto}}
.disc{{position:absolute;right:-90px;top:-90px;width:380px;height:380px;border-radius:50%;background:var(--brand);opacity:.12}}
.k{{font-size:14px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);position:relative}}
h1{{margin:0;font-size:84px;line-height:1.05}}
h2{{margin:6px 0 22px;font-size:40px;line-height:1.15;position:relative}}
p{{margin:0 0 14px;position:relative}}
.sub{{font-size:26px;color:var(--dim);max-width:760px}}
.foot{{position:absolute;left:72px;right:72px;bottom:24px;display:flex;justify-content:space-between;font-size:12px;color:var(--muted)}}
.row{{display:flex;gap:28px;align-items:flex-start;position:relative}} .row>*{{flex:1}}
.col{{position:relative}}
figure{{margin:0}} figcaption{{font-size:13px;color:var(--muted);margin-top:8px}} figcaption::before{{content:"// "}}
img{{display:block;border:2px solid var(--ink)}}
ul{{margin:0;padding:0;list-style:none;position:relative}}
li{{padding-left:26px;margin-bottom:12px;position:relative;font-size:21px}}
li::before{{content:"";position:absolute;left:0;top:11px;width:10px;height:10px;background:var(--brand)}}
li small{{display:block;font-size:15px;color:var(--dim)}}
table{{border-collapse:collapse;width:100%;font-size:17px;line-height:1.35;position:relative}}
th{{text-align:left;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--ink);padding:8px 10px}}
td{{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}}
.big{{font-size:68px;font-weight:700;line-height:1}}
.stat{{border:2px solid var(--ink);background:var(--raised);padding:16px 18px;position:relative}}
.stat .big{{font-size:46px}} .stat div+div{{font-size:15px;color:var(--dim);margin-top:6px}}
.call{{border:2px solid var(--ink);border-left:8px solid var(--brand);background:var(--raised);padding:14px 18px;position:relative;font-size:19px}}
.ok{{color:var(--ok)}} .er{{color:var(--err)}} b{{font-weight:700}}
a{{color:var(--sec)}}
"""

N = [0]


def slide(k, title, body, foot=True):
    N[0] += 1
    f = f'<div class="foot"><span>CipherKey 4.0.0</span><span>{N[0]:02d}</span></div>' if foot else ""
    t = f"<h2>{title}</h2>" if title else ""
    return f'<section class="s"><div class="disc"></div><div class="k">{k}</div>{t}{body}{f}</section>'


def im(src, w=None, h=None):
    st = ""
    if w:
        st += f"width:{w}px;"
    if h:
        st += f"height:{h}px;"
    return f'<img src="img/{src}" style="{st}">'


slides = []
slides.append(slide("Informe técnico · presentación", "", f"""
<h1 style="margin-top:96px">CipherKey</h1>
<p class="sub" style="margin-top:20px">Gestor de contraseñas cifrado, de escritorio y 100&nbsp;% offline.</p>
<p class="sub" style="font-size:20px;margin-top:10px">Tu seguridad no debería depender de terceros.</p>
<img src="img/logo.png" style="position:absolute;right:70px;top:250px;width:420px;border:0">
<div style="position:absolute;left:72px;bottom:56px;font-size:16px;color:var(--dim);line-height:1.8">
versión 4.0.0 · Java 25 · licencia MIT<br>{REPO}</div>""", foot=False))

slides.append(slide("01 // El problema", "Demasiadas cuentas, demasiada confianza ajena", f"""
<div style="width:1040px;margin:0 auto">{D['problema']()}</div>
<p style="font-size:19px;color:var(--dim);margin-top:10px">Repetir, apuntar o confiar en un tercero tiene siempre un coste. CipherKey lo evita guardándolo todo en un fichero tuyo.</p>"""))

slides.append(slide("02 // La idea", "Un fichero, una clave, ningún servidor", f"""
<div class="row" style="margin-top:20px">
 <div class="stat"><div class="big">1</div><div>fichero cifrado <b>.ckey</b> con todas tus credenciales</div></div>
 <div class="stat"><div class="big">1</div><div>clave maestra que solo tú conoces</div></div>
 <div class="stat"><div class="big">0</div><div>conexiones de red, cuentas o servidores</div></div>
</div>
<div style="width:1000px;margin:30px auto 0">{D['offline']()}</div>"""))

slides.append(slide("03 // Responsabilidades", "Qué hace la aplicación", f"""
<div style="width:1060px;margin:0 auto">{D['responsabilidades']()}</div>
<p style="font-size:18px;color:var(--dim);margin-top:14px"><b>Por diseño no hace:</b> sincronizar entre dispositivos, autorrellenar en el navegador ni recuperar una clave olvidada.</p>"""))

slides.append(slide("04 // La aplicación", "Acceso: elige tu bóveda y desbloquea", f"""
<div class="row" style="margin-top:6px">
 <figure>{im('login-light.png', 520)}<figcaption>Tema claro</figcaption></figure>
 <figure>{im('login-dark.png', 520)}<figcaption>Tema oscuro, recordado entre sesiones</figcaption></figure>
</div>
<p style="font-size:18px;color:var(--dim);margin-top:14px">Bóvedas recientes en el desplegable. Crear una nueva exige una clave de 8+ caracteres con medidor de fuerza.</p>"""))

slides.append(slide("04 // La aplicación", "Ventana principal", f"""
<div class="row" style="align-items:center">
 <figure style="flex:none">{im('dashboard-dark.png', 800)}<figcaption>Panel principal (datos de ejemplo)</figcaption></figure>
 <ul style="flex:1;margin-left:6px">
  <li>Barra lateral<small>todas, favoritas y categorías</small></li>
  <li>Lista ordenable<small>doble clic o Enter para editar</small></li>
  <li>Panel de detalle<small>mostrar, copiar y código 2FA con cuenta atrás</small></li>
  <li>Búsqueda instantánea<small>Ctrl+F</small></li>
 </ul>
</div>"""))

slides.append(slide("04 // La aplicación", "Entradas, generador y auditoría", f"""
<div class="row" style="align-items:flex-start">
 <figure style="flex:none">{im('entry.png', 360)}<figcaption>Entrada con 2FA y notas</figcaption></figure>
 <div class="col" style="flex:none;width:400px"><figure>{im('generator.png', 400)}<figcaption>Generador 8–64 caracteres</figcaption></figure>
 <p style="margin-top:20px;font-size:17px;color:var(--dim)">El historial guarda las últimas 10 contraseñas de cada entrada.</p></div>
 <figure style="flex:none">{im('audit.png', 360)}<figcaption>Auditoría: débiles, repetidas, antiguas</figcaption></figure>
</div>"""))

slides.append(slide("05 // Cómo funciona", "Arquitectura en capas", f"""
<div style="width:1080px;margin:0 auto">{D['arquitectura']()}</div>
<p style="font-size:18px;color:var(--dim);margin-top:0">~4.050 líneas de código. Seguridad y persistencia se prueban sin abrir ninguna ventana.</p>"""))

slides.append(slide("05 // Cómo funciona", "El formato .ckey v2", f"""
<div style="width:1136px;margin:16px auto 0">{D['formato']()}</div>"""))

slides.append(slide("05 // Cómo funciona", "Apertura de una bóveda", f"""
<div style="width:1136px;margin:16px auto 0">{D['flujo']()}</div>"""))

slides.append(slide("06 // Seguridad", "Decisiones de seguridad", f"""
<div class="row" style="gap:36px">
<div class="col" style="flex:1.25"><table>
<tr><th>Aspecto</th><th>Implementación</th></tr>
<tr><td><b>Clave</b></td><td>Argon2id · 64 MiB · 3 iteraciones · sal 32 B</td></tr>
<tr><td><b>Cifrado</b></td><td>AES-256-GCM, nonce nuevo en cada guardado</td></tr>
<tr><td><b>Integridad</b></td><td>Cabecera autenticada (AAD)</td></tr>
<tr><td><b>Guardado</b></td><td>Atómico + copia .bak</td></tr>
<tr><td><b>Portapapeles</b></td><td>Se vacía a los 30 s</td></tr>
<tr><td><b>Bloqueo</b></td><td>Por inactividad (5 min)</td></tr>
</table></div>
<div class="col" style="flex:1">
<div class="call" style="margin-bottom:16px"><b class="er">Límites honestos</b><br>Sin recuperación de clave. Quien tenga el .ckey puede atacarlo offline: la defensa real es Argon2id + clave larga. Sin auditoría externa.</div>
<div class="call" style="border-left-color:var(--ok)"><b class="ok">Verificado</b><br>52 pruebas unitarias en verde y CI con <code>mvn verify</code>.</div>
</div></div>"""))

slides.append(slide("07 // Por qué usarla", "Control total, sin ceder datos", f"""
<table style="margin-top:6px">
<tr><th></th><th>CipherKey</th><th>Gestor en la nube</th><th>Navegador</th></tr>
<tr><td><b>Dónde están los datos</b></td><td>Tu equipo</td><td>Servidor del proveedor</td><td>Perfil del navegador</td></tr>
<tr><td><b>Cuenta necesaria</b></td><td class="ok">No</td><td>Sí</td><td>Normalmente</td></tr>
<tr><td><b>Código abierto</b></td><td class="ok">Sí (MIT)</td><td>Depende</td><td>Depende</td></tr>
<tr><td><b>Sincroniza dispositivos</b></td><td class="er">No</td><td class="ok">Sí</td><td class="ok">Sí</td></tr>
<tr><td><b>Autorrelleno</b></td><td class="er">No</td><td class="ok">Sí</td><td class="ok">Sí</td></tr>
</table>
<div class="row" style="margin-top:22px;gap:22px">
<div class="call">Importa desde <b>Bitwarden, Chrome/Edge/Firefox y KeePass</b> y exporta a CSV: no te ata.</div>
<div class="call">Paquetes con <b>su propio Java</b>: instalar y usar.</div></div>"""))

slides.append(slide("08 // Existe y es descargable", "El repositorio es público", f"""
<div class="row" style="align-items:flex-start;gap:34px">
<figure style="flex:none">{im('gh-repo.png', 690)}<figcaption>Captura de {REPO} sin iniciar sesión</figcaption></figure>
<ul style="flex:1;margin-top:8px">
<li>Código abierto<small>Java 98,7 % · licencia MIT</small></li>
<li>Release 4.0.0<small>marcada «Latest»</small></li>
<li>Pruebas y CI<small>GitHub Actions con JDK 25</small></li>
</ul></div>"""))

slides.append(slide("08 // Existe y es descargable", "Release 4.0.0: instaladores para tres sistemas", f"""
<div class="row" style="align-items:flex-start;gap:34px">
<figure style="flex:none">{im('gh-release.png', 620)}<figcaption>9 recursos con hash SHA-256</figcaption></figure>
<table style="font-size:15px;flex:1.1;margin-top:4px">
<tr><th>Sistema</th><th>Archivo</th></tr>
<tr><td>Debian / Ubuntu</td><td>.deb · 30,1 MB</td></tr>
<tr><td>Linux</td><td>.tar.gz · 38,1 MB</td></tr>
<tr><td>Windows</td><td>.msi · 34,6 MB<br>.zip portable</td></tr>
<tr><td>macOS (ARM)</td><td>.dmg · 36,7 MB</td></tr>
<tr><td>Con Java 25</td><td>.jar · 8,84 MB</td></tr>
</table></div>
<p style="font-size:17px;margin-top:16px;color:var(--dim)">{REL}</p>"""))

slides.append(slide("08 // Existe y es descargable", "Publicación automática", f"""
<div style="width:1136px;margin:20px auto 0">{D['pipeline']()}</div>
<p style="font-size:18px;color:var(--dim);margin-top:16px">Los instaladores no están firmados: Windows mostrará SmartScreen y macOS pedirá abrirla con clic derecho la primera vez.</p>"""))

slides.append(slide("09 // Cierre", "Qué te llevas", f"""
<ul style="margin-top:10px">
<li><b>Problema:</b> contraseñas repetidas, dispersas o en manos de terceros.</li>
<li><b>Solución:</b> una bóveda local cifrada con Argon2id + AES-256-GCM.</li>
<li><b>Responsabilidades:</b> custodiar, organizar, generar, proteger, auditar e interoperar.</li>
<li><b>Por qué usarla:</b> control total, código abierto y sin cuenta.</li>
<li><b>Pendiente:</b> archivo de clave o FIDO2, QR desde imagen, bloqueo al suspender.</li>
</ul>
<div class="call" style="margin-top:24px"><b>Descárgala:</b> <a href="https://{REL}">{REL}</a></div>"""))


def page(css, body, title):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>{body}</body></html>'


import re
tests = sys.argv[1] if len(sys.argv) > 1 else ""
rb = report_body.replace('<span id="testres"></span>', tests)
open("informe.html", "w").write(page(report_css, rb, "CipherKey 4.0.0 — Informe técnico"))
open("presentacion.html", "w").write(page(deck_css, "".join(slides), "CipherKey 4.0.0 — Presentación"))
print("slides", N[0])
