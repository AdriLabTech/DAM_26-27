# Diagramas SVG a tinta (Ryoku Kami). Colores por variables CSS: --ink, --sec, --paper, --raised, --dim.
F = "font-family:'Komiki Mono',monospace"


def svg(w, h, body):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:100%;height:auto;{F}">{body}</svg>')


def t(x, y, s, size=15, bold=False, anchor="middle", fill="var(--ink)", extra=""):
    w = "font-weight:700;" if bold else ""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
            f'style="{w}{F}" fill="{fill}" {extra}>{s}</text>')


def box(x, y, w, h, title=None, sub=None, shift=True, fill="var(--raised)", tsize=15, ssize=12, accent=False):
    out = ""
    if shift:
        out += f'<rect x="{x+6}" y="{y+6}" width="{w}" height="{h}" fill="var(--sec)" opacity=".28"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="var(--ink)" stroke-width="2"/>'
    if accent:
        out += f'<rect x="{x}" y="{y}" width="6" height="{h}" fill="var(--brand)"/>'
    if title and sub:
        out += t(x + w / 2, y + h / 2 - 3, title, tsize, True)
        out += t(x + w / 2, y + h / 2 + 17, sub, ssize, fill="var(--dim)")
    elif title:
        out += t(x + w / 2, y + h / 2 + tsize * 0.35, title, tsize, True)
    return out


def arrow(x1, y1, x2, y2, dash=False):
    d = ' stroke-dasharray="6 5"' if dash else ""
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx = [x2 - 11 * math.cos(a - .4), y2 - 11 * math.sin(a - .4)]
    hy = [x2 - 11 * math.cos(a + .4), y2 - 11 * math.sin(a + .4)]
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="var(--ink)" stroke-width="2"{d}/>'
            f'<polyline points="{hx[0]:.1f},{hx[1]:.1f} {x2},{y2} {hy[0]:.1f},{hy[1]:.1f}" fill="none" stroke="var(--ink)" stroke-width="2"/>')


def cap(x, y, s, w=None):
    return t(x, y, s, 11, True, "start", "var(--muted)", 'letter-spacing=".08em"')


def sun(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="var(--brand)" opacity=".12"/>'


# 1. El problema: hoy vs con CipherKey
def problema():
    b = sun(800, 70, 60)
    b += cap(20, 28, "01 // HOY")
    risks = [("Contraseña repetida", "una filtración las abre todas"),
             ("Guardada en el navegador", "sin clave maestra propia"),
             ("Apuntada en notas o papel", "se pierde o se copia"),
             ("Servicio en la nube", "tu seguridad depende de un tercero")]
    for i, (a, s) in enumerate(risks):
        b += box(20, 44 + i * 74, 330, 58, a, s, tsize=14, ssize=11.5)
    b += arrow(372, 190, 470, 190)
    b += cap(490, 28, "02 // CON CIPHERKEY")
    b += box(490, 44, 330, 290, shift=True)
    b += f'<rect x="560" y="90" width="190" height="150" fill="none" stroke="var(--ink)" stroke-width="2"/>'
    b += f'<rect x="566" y="96" width="190" height="150" fill="var(--sec)" opacity=".28"/>'
    b += f'<rect x="560" y="90" width="190" height="150" fill="var(--paper)" stroke="var(--ink)" stroke-width="2"/>'
    b += t(655, 150, "bóveda.ckey", 18, True)
    b += t(655, 176, "AES-256-GCM", 12, fill="var(--dim)")
    b += t(655, 196, "un solo fichero", 12, fill="var(--dim)")
    b += t(655, 280, "1 clave maestra", 16, True)
    b += t(655, 304, "100% offline · en tu equipo", 12, fill="var(--dim)")
    return svg(840, 350, b)


# 2. Responsabilidades
def responsabilidades():
    b = sun(60, 330, 50)
    b += box(250, 8, 340, 54, "CipherKey", "gestor de contraseñas offline", tsize=18, accent=True)
    items = [("Custodiar", "cifra y guarda la bóveda"),
             ("Organizar", "categorías, favoritas, búsqueda"),
             ("Generar", "contraseñas y medidor de fuerza"),
             ("Proteger", "bloqueo y portapapeles"),
             ("Auditar", "débiles, repetidas, antiguas"),
             ("Interoperar", "CSV, copia de seguridad, 2FA")]
    xs = [20, 300, 580]
    for i, (a, s) in enumerate(items):
        x = xs[i % 3]
        y = 120 if i < 3 else 230
        b += box(x, y, 240, 70, a, s, tsize=15, ssize=11)
        if i < 3:
            b += f'<line x1="{x+120}" y1="62" x2="{x+120}" y2="120" stroke="var(--ink)" stroke-width="2"/>'
            b += f'<line x1="{x+120}" y1="190" x2="{x+120}" y2="230" stroke="var(--ink)" stroke-width="1.5" stroke-dasharray="4 4"/>'
    return svg(840, 330, b)


# 3. Arquitectura en capas
def arquitectura():
    b = sun(780, 40, 46)
    b += box(20, 14, 800, 52, "View · Swing + FlatLaf", "LoginDialog · MainFrame · Sidebar · DetailPanel · EntryDialog · AuditDialog", ssize=11.5)
    b += arrow(420, 70, 420, 98)
    b += box(20, 102, 800, 52, "Controller · PasswordManager", "casos de uso: abrir, guardar, buscar, importar, bloquear", ssize=11.5)
    b += arrow(420, 158, 420, 186)
    cols = [("Model", "PasswordEntry", "PasswordHistoryItem"),
            ("Security", "VaultCrypto · Totp · PasswordAudit", "PasswordGenerator · SecureClipboard"),
            ("Persistence", "Vault · AppPrefs", "Csv · EntryCsv")]
    xs = [20, 230, 560]
    ws = [190, 310, 260]
    for (n, a, c), x, w in zip(cols, xs, ws):
        b += f'<rect x="{x+6}" y="196" width="{w}" height="92" fill="var(--sec)" opacity=".28"/>'
        b += f'<rect x="{x}" y="190" width="{w}" height="92" fill="var(--raised)" stroke="var(--ink)" stroke-width="2"/>'
        b += t(x + w / 2, 214, n, 15, True)
        b += t(x + w / 2, 242, a, 10.5, fill="var(--dim)")
        b += t(x + w / 2, 262, c, 10.5, fill="var(--dim)")
    b += arrow(690, 284, 690, 316)
    b += box(560, 320, 260, 44, "disco · bóveda.ckey", None, tsize=14, fill="var(--paper)")
    b += f'<line x1="420" y1="282" x2="420" y2="300" stroke="none"/>'
    return svg(840, 378, b)


# 4. Formato .ckey
def formato():
    fields = [("CKEY", "4 B", 62), ("ver", "1", 42), ("KDF", "1", 42), ("mem", "4", 52), ("iter", "4", 52),
              ("par", "1", 42), ("sal", "32 B", 100), ("nonce", "12 B", 80), ("texto cifrado + tag GCM", "n + 16 B", 268)]
    b = ""
    x = 20
    xs = []
    for i, (n, s, w) in enumerate(fields):
        fill = "var(--paper)" if i < 7 else ("var(--raised)" if i == 7 else "var(--sec)")
        op = ' opacity=".35"' if i == 8 else ""
        if i == 8:
            b += f'<rect x="{x}" y="70" width="{w}" height="64" fill="var(--sec)" opacity=".30"/>'
            b += f'<rect x="{x}" y="70" width="{w}" height="64" fill="none" stroke="var(--ink)" stroke-width="2"/>'
        else:
            b += f'<rect x="{x}" y="70" width="{w}" height="64" fill="{fill}" stroke="var(--ink)" stroke-width="2"/>'
        sz = 12 if i < 8 else 13
        if i == 8:
            b += t(x + w / 2, 98, "texto cifrado", 13, True)
            b += t(x + w / 2, 116, "+ tag GCM (16 B)", 12, fill="var(--dim)")
        else:
            b += t(x + w / 2, 98, n, sz, True)
            b += t(x + w / 2, 118, s, 11, fill="var(--dim)")
        xs.append((x, w))
        x += w
    hx1, hx2 = 20, xs[6][0] + xs[6][1]
    b += f'<path d="M{hx1} 62 V50 H{hx2} V62" fill="none" stroke="var(--ink)" stroke-width="2"/>'
    b += t((hx1 + hx2) / 2, 38, "cabecera · 47 bytes · en claro pero autenticada (AAD)", 13, True)
    b += f'<path d="M{xs[7][0]} 142 V154 H{xs[8][0]+xs[8][1]} V142" fill="none" stroke="var(--ink)" stroke-width="2"/>'
    b += t((xs[7][0] + xs[8][0] + xs[8][1]) / 2, 176, "AES-256-GCM · nonce nuevo en cada guardado", 13, True)
    b += t(20, 214, "Argon2id (64 MiB · 3 iteraciones) convierte clave maestra + sal en la clave de 256 bits.", 12, anchor="start", fill="var(--dim)")
    b += t(20, 234, "Si alguien toca un solo byte de la cabecera, el tag GCM deja de validar.", 12, anchor="start", fill="var(--dim)")
    return svg(840, 250, b)


# 5. Flujo de apertura
def flujo():
    b = sun(790, 60, 44)
    steps = [("1 · Entrada", "fichero .ckey", "+ clave maestra"),
             ("2 · Cabecera", "valida magic y", "parámetros KDF"),
             ("3 · Argon2id", "deriva la clave", "de 256 bits"),
             ("4 · AES-GCM", "descifra con la", "cabecera como AAD")]
    x = 14
    for i, (a, l1, l2) in enumerate(steps):
        b += f'<rect x="{x+6}" y="26" width="168" height="92" fill="var(--sec)" opacity=".28"/>'
        b += f'<rect x="{x}" y="20" width="168" height="92" fill="var(--raised)" stroke="var(--ink)" stroke-width="2"/>'
        b += t(x + 84, 48, a, 14, True)
        b += t(x + 84, 76, l1, 11.5, fill="var(--dim)")
        b += t(x + 84, 94, l2, 11.5, fill="var(--dim)")
        if i < 3:
            b += arrow(x + 172, 66, x + 204, 66)
        x += 208
    # decisión
    b += arrow(742, 112, 742, 160)
    b += t(742, 152, "", 10)
    b += box(560, 164, 250, 50, "Tag válido ✓", "entradas en memoria", tsize=14, ssize=11.5, shift=False)
    b += f'<rect x="560" y="164" width="6" height="50" fill="var(--ok)"/>'
    b += box(560, 232, 250, 50, "Tag inválido ✕", "clave errónea o bóveda alterada", tsize=14, ssize=11, shift=False)
    b += f'<rect x="560" y="232" width="6" height="50" fill="var(--err)"/>'
    b += f'<path d="M742 112 V138 H520 V257 H560" fill="none" stroke="var(--ink)" stroke-width="2"/>'
    b += f'<polyline points="549,251 560,257 549,263" fill="none" stroke="var(--ink)" stroke-width="2"/>'
    b += t(20, 190, "La contraseña maestra no se conserva", 12, anchor="start", fill="var(--dim)")
    b += t(20, 210, "tras abrir: solo queda la clave derivada,", 12, anchor="start", fill="var(--dim)")
    b += t(20, 230, "que se pone a cero al bloquear.", 12, anchor="start", fill="var(--dim)")
    return svg(840, 296, b)


# 6. Modelo offline
def offline():
    b = sun(60, 40, 40)
    b += f'<rect x="20" y="40" width="470" height="200" fill="none" stroke="var(--ink)" stroke-width="2" stroke-dasharray="7 5"/>'
    b += cap(30, 30, "TU EQUIPO")
    b += box(50, 90, 170, 90, "CipherKey", "Java + Swing", tsize=16)
    b += box(300, 90, 160, 90, "bóveda.ckey", "cifrada", tsize=15)
    b += arrow(226, 135, 294, 135)
    b += arrow(294, 150, 226, 150)
    # nube tachada
    b += cap(570, 30, "FUERA")
    b += box(570, 90, 230, 90, "Red · nube · cuenta", "sin servidores, sin envío", tsize=14, ssize=11.5, fill="var(--paper)", shift=False)
    b += f'<line x1="500" y1="135" x2="560" y2="135" stroke="var(--ink)" stroke-width="2" stroke-dasharray="6 5"/>'
    b += f'<line x1="514" y1="112" x2="546" y2="158" stroke="var(--err)" stroke-width="4"/>'
    b += f'<line x1="546" y1="112" x2="514" y2="158" stroke="var(--err)" stroke-width="4"/>'
    b += t(420, 218, "Sin dependencias de red: no hay nada que filtrar.", 12, fill="var(--dim)", anchor="end")
    return svg(840, 256, b)


# 7. Pipeline de distribución
def pipeline():
    b = sun(790, 40, 40)
    b += box(14, 70, 150, 70, "git tag", "v4.x.y", tsize=15)
    b += arrow(168, 105, 206, 105)
    b += box(210, 70, 170, 70, "GitHub Actions", "release.yml", tsize=14)
    for i, os_ in enumerate(["Linux", "Windows", "macOS"]):
        y = 20 + i * 72
        b += arrow(384, 105, 430, y + 26)
        b += box(434, y, 120, 52, os_, "jpackage + JRE", tsize=13, ssize=10.5, shift=False)
        b += arrow(558, y + 26, 600, 105)
    b += box(604, 40, 222, 130, shift=True)
    b += t(715, 78, "GitHub Release", 15, True)
    b += t(715, 106, "deb · tar.gz · msi", 11.5, fill="var(--dim)")
    b += t(715, 126, "zip · dmg · jar", 11.5, fill="var(--dim)")
    b += t(715, 146, "SHA256SUMS", 11.5, fill="var(--dim)")
    b += t(14, 252, "La etiqueta debe coincidir con la versión del pom.xml o el workflow falla.", 12, anchor="start", fill="var(--dim)")
    b += t(14, 272, "Cada paquete lleva su propio Java: no hay que instalar nada más.", 12, anchor="start", fill="var(--dim)")
    return svg(840, 284, b)


ALL = dict(problema=problema, responsabilidades=responsabilidades, arquitectura=arquitectura,
           formato=formato, flujo=flujo, offline=offline, pipeline=pipeline)
