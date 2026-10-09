# Guía completa de Docker y Docker Compose en Arch Linux

> Probada con Docker 29.9, Docker Compose 5.6 y kernel 7.x en Arch (octubre 2026). Los comandos de `docker compose` son el plugin moderno (con espacio), **no** el antiguo `docker-compose` con guion.

Continúa a [[00_PrimerosPasos]] (instalación básica) y [[01_CrearImagen]].

## Índice
1. [Conceptos clave](#1-conceptos-clave)
2. [Instalación y configuración en Arch](#2-instalación-y-configuración-en-arch)
3. [Comandos básicos de Docker](#3-comandos-básicos-de-docker)
4. [Imágenes y Dockerfile](#4-imágenes-y-dockerfile)
5. [Volúmenes y datos](#5-volúmenes-y-datos)
6. [Redes](#6-redes)
7. [Docker Compose](#7-docker-compose)
8. [Ejemplo para esta asignatura: Odoo + PostgreSQL](#8-ejemplo-para-esta-asignatura-odoo--postgresql)
9. [Ejemplo de desarrollo: Spring Boot + PostgreSQL](#9-ejemplo-de-desarrollo-spring-boot--postgresql)
10. [Limpieza y mantenimiento](#10-limpieza-y-mantenimiento)
11. [Seguridad](#11-seguridad)
12. [Solución de problemas](#12-solución-de-problemas)
13. [Chuleta rápida](#13-chuleta-rápida)

---

## 1. Conceptos clave

| Concepto | Qué es |
|---|---|
| **Imagen** | Plantilla inmutable de solo lectura (sistema de ficheros + metadatos). Se construye por capas. |
| **Contenedor** | Instancia en ejecución de una imagen: un proceso aislado (namespaces + cgroups) sobre el kernel del host. |
| **Registry** | Almacén de imágenes (Docker Hub, GHCR…). `docker pull` descarga, `docker push` sube. |
| **Volumen** | Almacenamiento persistente gestionado por Docker; sobrevive al contenedor. |
| **Red** | Red virtual donde los contenedores se resuelven por nombre (DNS interno). |
| **Dockerfile** | Receta para construir una imagen. |
| **Compose** | Fichero YAML que describe una aplicación multicontenedor (servicios, redes, volúmenes) y la levanta con un comando. |

Un contenedor **no es una máquina virtual**: comparte el kernel del host. Es efímero: lo que no esté en un volumen se pierde al borrarlo.

---

## 2. Instalación y configuración en Arch

### 2.1 Paquetes

```bash
sudo pacman -Syu
sudo pacman -S docker docker-compose docker-buildx
```

- `docker`: daemon (`dockerd`) y cliente.
- `docker-compose`: plugin `docker compose` (v2+).
- `docker-buildx`: plugin `docker buildx` (BuildKit). En Arch va **aparte**; sin él, `docker build` avisa de que usa el constructor antiguo (deprecado).

### 2.2 Servicio

```bash
sudo systemctl enable --now docker.service   # arrancar ahora y en cada inicio
systemctl status docker                      # comprobar
```

> Si prefieres que el daemon **no** arranque siempre (ahorra RAM), usa solo `sudo systemctl start docker` cuando lo necesites. Con **socket activation** arranca bajo demanda:
> `sudo systemctl enable --now docker.socket` (en vez de `docker.service`).

### 2.3 Usar Docker sin `sudo`

```bash
sudo usermod -aG docker $USER
```

Cierra sesión y vuelve a entrar (o `newgrp docker` en esa terminal). Comprueba con `id` que aparece `docker`.

> ⚠️ **El grupo `docker` equivale a root** en tu máquina: quien esté en él puede montar `/` dentro de un contenedor. Es aceptable en un equipo personal; no añadas usuarios que no sean de confianza. Alternativa más segura: [Docker rootless](#112-docker-rootless).

### 2.4 Verificación

```bash
docker version
docker compose version
docker run --rm hello-world
```

Si `hello-world` imprime «Hello from Docker!», todo funciona.

### 2.5 Configuración del daemon (opcional)

Fichero `/etc/docker/daemon.json` (no existe por defecto; créalo). Reinicia con `sudo systemctl restart docker` tras cambiarlo.

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "10m", "max-file": "3" },
  "default-address-pools": [
    { "base": "172.30.0.0/16", "size": "24" }
  ]
}
```

- `log-driver: local` con rotación evita que los logs llenen el disco.
- `default-address-pools` se usa si las redes de Docker chocan con tu VPN o red de casa (ver [12](#12-solución-de-problemas)).

### 2.6 Dónde guarda los datos

`/var/lib/docker` (imágenes, volúmenes, capas). Puede crecer mucho; vigílalo con `docker system df`.

---

## 3. Comandos básicos de Docker

### 3.1 Ejecutar contenedores

```bash
docker run hello-world                       # ejecuta y termina
docker run -d --name web -p 8080:80 nginx    # en segundo plano, puerto host:contenedor
docker run -it --rm alpine sh                # interactivo, se borra al salir
docker run -d --name db -e POSTGRES_PASSWORD=secreto -v pgdata:/var/lib/postgresql postgres:18
```

| Flag | Significado |
|---|---|
| `-d` | Segundo plano (detached) |
| `-it` | Terminal interactiva |
| `--rm` | Borra el contenedor al terminar |
| `--name` | Nombre del contenedor |
| `-p host:cont` | Publica un puerto. Usa `127.0.0.1:8080:80` para no exponerlo a la red |
| `-e VAR=valor` | Variable de entorno |
| `-v vol:/ruta` | Volumen nombrado; `-v ./dir:/ruta` es un bind mount |
| `--network` | Red a la que conectar |
| `--restart unless-stopped` | Reinicio automático |

### 3.2 Gestionar contenedores

```bash
docker ps                # en ejecución
docker ps -a             # todos
docker stop web          # parada limpia (SIGTERM, luego SIGKILL a los 10 s)
docker start web
docker restart web
docker rm web            # borrar (parado); -f fuerza
docker logs -f --tail 100 web
docker exec -it web sh   # shell dentro de un contenedor en marcha
docker inspect web       # JSON con toda la configuración
docker stats             # CPU/RAM en vivo
docker top web           # procesos
docker cp web:/etc/nginx/nginx.conf .   # copiar ficheros
```

### 3.3 Imágenes

```bash
docker images                 # listar
docker pull postgres:18       # descargar
docker rmi postgres:18        # borrar
docker tag miapp:1.0 miapp:latest
docker history miapp:1.0      # capas
docker image prune            # borrar imágenes colgantes
```

> Usa siempre **etiquetas concretas** (`postgres:18`, no `postgres:latest`) para que el entorno sea reproducible.

---

## 4. Imágenes y Dockerfile

### 4.1 Instrucciones principales

| Instrucción | Función |
|---|---|
| `FROM` | Imagen base |
| `WORKDIR` | Directorio de trabajo |
| `COPY` / `ADD` | Copia ficheros (prefiere `COPY`) |
| `RUN` | Ejecuta un comando **al construir** (crea una capa) |
| `ENV` / `ARG` | Variable de entorno en ejecución / variable solo de build |
| `EXPOSE` | Documenta el puerto (no lo publica) |
| `USER` | Usuario con el que corre el proceso |
| `CMD` | Comando por defecto (sustituible al hacer `docker run`) |
| `ENTRYPOINT` | Ejecutable fijo; `CMD` pasa a ser sus argumentos |
| `HEALTHCHECK` | Cómo comprobar que la app está sana |

### 4.2 Ejemplo: aplicación Spring Boot (multi-stage)

```dockerfile
# ---- Etapa 1: compilar ----
FROM maven:3-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -q dependency:go-offline          # capa cacheada mientras no cambie el pom
COPY src ./src
RUN mvn -q package -DskipTests

# ---- Etapa 2: imagen final, mínima ----
FROM eclipse-temurin:21-jre
WORKDIR /app
RUN useradd --system --uid 1001 appuser
COPY --from=build /app/target/*.jar app.jar
USER appuser
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

La imagen final no lleva Maven ni el código fuente: es más pequeña y tiene menos superficie de ataque.

### 4.3 `.dockerignore`

Junto al Dockerfile, para no enviar basura al contexto de build:

```
.git
target/
node_modules/
.env
*.log
```

### 4.4 Construir y probar

```bash
docker build -t miapp:1.0 .
docker run --rm -p 8080:8080 miapp:1.0
```

### 4.5 Buenas prácticas

- Ordena las instrucciones de **menos a más cambiante** para aprovechar la caché de capas (dependencias antes que el código).
- Un proceso por contenedor.
- No ejecutes como root (`USER`).
- Nunca metas secretos en el Dockerfile ni en `ENV`: quedan en las capas de la imagen.
- Fija versiones de la imagen base.

---

## 5. Volúmenes y datos

Tres formas de dar almacenamiento a un contenedor:

| Tipo | Sintaxis | Cuándo usarlo |
|---|---|---|
| **Volumen nombrado** | `-v datos:/ruta` | Datos persistentes (bases de datos). Lo gestiona Docker. |
| **Bind mount** | `-v ./codigo:/ruta` | Compartir una carpeta de tu host (desarrollo, configuración). |
| **tmpfs** | `--tmpfs /ruta` | Datos temporales en RAM. |

```bash
docker volume create datos
docker volume ls
docker volume inspect datos
docker volume rm datos
```

### Copia de seguridad de un volumen

```bash
# Backup a un tar.gz en el directorio actual
docker run --rm -v datos:/origen:ro -v "$PWD":/backup alpine \
  tar czf /backup/datos.tar.gz -C /origen .

# Restaurar
docker run --rm -v datos:/destino -v "$PWD":/backup alpine \
  tar xzf /backup/datos.tar.gz -C /destino
```

Para PostgreSQL es mejor un volcado lógico: `docker exec db pg_dump -U usuario basedatos > backup.sql`.

### Permisos en bind mounts (típico en Arch/Linux)

Los ficheros creados por el contenedor pertenecen al UID con el que corre el proceso (a menudo root). Si necesitas que sean tuyos: `docker run --user "$(id -u):$(id -g)" …` o `user: "${UID}:${GID}"` en Compose.

---

## 6. Redes

```bash
docker network ls
docker network create mired
docker network inspect mired
docker run -d --name api --network mired miapp
docker network connect mired otro-contenedor
```

| Driver | Uso |
|---|---|
| `bridge` | Por defecto. Red privada en el host. |
| `host` | Comparte la red del host (sin aislamiento ni `-p`). |
| `none` | Sin red. |

**Importante:** en una red *definida por el usuario* (no la `bridge` por defecto) los contenedores se resuelven **por nombre**. Desde `api`, la base de datos es `db:5432`, no `localhost`.

`localhost` dentro de un contenedor es **el propio contenedor**, no tu máquina. Para llegar al host desde un contenedor, añade `extra_hosts: ["host.docker.internal:host-gateway"]`.

---

## 7. Docker Compose

Compose describe todo el stack en `compose.yaml` (nombre preferido actualmente; `docker-compose.yml` también funciona).

### 7.1 Estructura

```yaml
name: mi-proyecto              # nombre del proyecto (prefijo de redes/volúmenes)

services:
  db:
    image: postgres:18
    restart: unless-stopped
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app -d app"]
      interval: 5s
      timeout: 3s
      retries: 10

  api:
    build: .
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "127.0.0.1:8080:8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/app

volumes:
  pgdata:
```

Compose crea automáticamente una red por proyecto en la que cada servicio es accesible por su nombre.

### 7.2 Claves de servicio más usadas

| Clave | Función |
|---|---|
| `image` / `build` | Imagen a usar / contexto y Dockerfile a construir |
| `ports` | Puertos publicados |
| `environment` / `env_file` | Variables de entorno |
| `volumes` | Volúmenes y bind mounts |
| `depends_on` | Orden de arranque (con `condition: service_healthy` espera a que esté sano) |
| `healthcheck` | Comprobación de salud |
| `restart` | `no`, `always`, `on-failure`, `unless-stopped` |
| `command` / `entrypoint` | Sobrescriben los de la imagen |
| `networks` | Redes a las que se une |
| `profiles` | Servicios opcionales que solo arrancan si se piden |
| `deploy.resources.limits` | Límites de CPU/RAM |
| `secrets` | Secretos montados en `/run/secrets/` |

### 7.3 Variables y `.env`

Compose lee automáticamente un fichero `.env` junto al `compose.yaml` para **sustituir `${VARIABLES}`** en el YAML:

```bash
# .env   (NO subir a git)
DB_PASSWORD=cambia_esto
```

```yaml
environment:
  POSTGRES_PASSWORD: ${DB_PASSWORD}                # obligatoria si falta -> vacía
  OTRA: ${OTRA:-valor_por_defecto}                 # con valor por defecto
  OBLIGATORIA: ${DB_PASSWORD:?falta DB_PASSWORD}   # error claro si no existe
```

Añade `.env` a `.gitignore` y sube un `.env.example` sin valores reales. Distingue: `.env` rellena el YAML; `env_file:` inyecta variables dentro del contenedor.

### 7.4 Comandos de Compose

```bash
docker compose up -d              # crear y arrancar (segundo plano)
docker compose up -d --build      # reconstruyendo imágenes
docker compose down               # parar y borrar contenedores y red (conserva volúmenes)
docker compose down -v            # ¡también borra los volúmenes (datos)!
docker compose ps                 # estado
docker compose logs -f api        # logs de un servicio
docker compose exec db psql -U app app   # comando en un servicio en marcha
docker compose run --rm api sh    # contenedor puntual
docker compose restart api
docker compose stop / start       # parar / arrancar sin borrar
docker compose pull               # actualizar imágenes
docker compose build --no-cache   # reconstruir sin caché
docker compose config             # valida y muestra el YAML ya resuelto
docker compose --profile debug up -d
```

> Antes de ejecutar nada nuevo: `docker compose config` valida la sintaxis y muestra qué valores toman las variables.

### 7.5 Desarrollo vs. producción

Con ficheros de override:

- `compose.yaml`: base común.
- `compose.override.yaml`: se aplica **automáticamente** encima (ideal para desarrollo: bind mounts, puertos de debug).
- `compose.prod.yaml`: `docker compose -f compose.yaml -f compose.prod.yaml up -d`.

### 7.6 `watch` (recarga en desarrollo)

```yaml
services:
  api:
    build: .
    develop:
      watch:
        - action: rebuild
          path: ./src
```

`docker compose watch` reconstruye al cambiar el código.

---

## 8. Ejemplo para esta asignatura: Odoo + PostgreSQL

Sistemas de Gestión Empresarial suele usar un ERP como **Odoo**. Este `compose.yaml` levanta Odoo con su base de datos.

> ⚠️ Comprueba la versión de Odoo y de PostgreSQL que exige tu curso (`odoo:<versión>` en [Docker Hub](https://hub.docker.com/_/odoo)). Los números de abajo son un punto de partida, no verificados contra tu temario.

```yaml
name: odoo

services:
  db:
    image: postgres:16
    restart: unless-stopped
    environment:
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: ${DB_PASSWORD:?define DB_PASSWORD en .env}
      POSTGRES_DB: postgres
    volumes:
      - odoo-db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U odoo"]
      interval: 5s
      timeout: 3s
      retries: 10

  odoo:
    image: odoo:17
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "127.0.0.1:8069:8069"
    environment:
      HOST: db
      USER: odoo
      PASSWORD: ${DB_PASSWORD}
    volumes:
      - odoo-data:/var/lib/odoo          # filestore (adjuntos, sesiones)
      - ./addons:/mnt/extra-addons       # tus módulos propios
      - ./config:/etc/odoo               # odoo.conf opcional

volumes:
  odoo-db:
  odoo-data:
```

Uso:

```bash
mkdir -p odoo/addons odoo/config && cd odoo
echo 'DB_PASSWORD=una_clave_larga' > .env
docker compose up -d
docker compose logs -f odoo     # esperar a "HTTP service (werkzeug) running"
# Abrir http://localhost:8069 y crear la base de datos
```

Útil en desarrollo de módulos:

```bash
docker compose exec odoo odoo -d mibd -u mi_modulo --stop-after-init   # actualizar módulo
docker compose restart odoo                                            # tras cambiar Python
docker compose exec db psql -U odoo -d mibd                            # entrar a la BD
```

**Pitfalls habituales:**
- `down -v` borra la base de datos y los adjuntos. Usa `down` a secas.
- Si cambias la versión **mayor** de PostgreSQL con datos existentes, el contenedor no arrancará: hay que migrar con `pg_dump`/`pg_restore`.
- Si cambias la versión mayor de Odoo, la base de datos requiere migración.

---

## 9. Ejemplo de desarrollo: Spring Boot + PostgreSQL

Solo la base de datos en Docker y la app en tu IDE (flujo más cómodo para desarrollar):

```yaml
name: dev-db

services:
  db:
    image: postgres:18
    ports:
      - "127.0.0.1:5432:5432"
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: dev
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql

volumes:
  pgdata:
```

Si ya tienes **PostgreSQL local** en el puerto 5432, usa otro puerto de host (`"127.0.0.1:5433:5432"`) o habrá conflicto de puertos.

> Desde PostgreSQL 18 la imagen oficial guarda los datos en `/var/lib/postgresql` (subdirectorio por versión) y no en `/var/lib/postgresql/data`. Para 16 o anteriores, el volumen va en `/var/lib/postgresql/data`. Verifícalo en la documentación de la imagen si cambias de versión.

---

## 10. Limpieza y mantenimiento

```bash
docker system df                 # qué ocupa el espacio
docker container prune           # contenedores parados
docker image prune -a            # imágenes sin usar
docker volume prune              # volúmenes sin usar (¡datos!)
docker builder prune             # caché de build
docker system prune              # contenedores, redes e imágenes colgantes
docker system prune -a --volumes # TODO lo no usado, incluidos volúmenes
```

> ⚠️ `--volumes` y `volume prune` **borran datos de bases de datos** de contenedores parados. Revisa `docker volume ls` antes.

Actualizar a las últimas imágenes de un stack:

```bash
docker compose pull && docker compose up -d
```

---

## 11. Seguridad

### 11.1 Reglas básicas

- Publica puertos solo en loopback si no necesitas acceso externo: `127.0.0.1:8080:80`.
- No ejecutes contenedores como root cuando sea evitable (`user:` / `USER`).
- Imágenes oficiales o verificadas, con versión fijada.
- Secretos fuera de las imágenes y del repositorio (`.env` en `.gitignore`).
- No montes `/var/run/docker.sock` en contenedores salvo necesidad real: da control total del host.
- Contenedor endurecido en Compose:
  ```yaml
  read_only: true
  cap_drop: [ALL]
  security_opt: ["no-new-privileges:true"]
  ```
- **Docker y el cortafuegos:** Docker manipula `iptables`/`nftables` directamente. Un puerto publicado con `-p 8080:80` **se salta reglas de `ufw`/`firewalld`** y queda abierto a la red. Por eso conviene el prefijo `127.0.0.1:`.

### 11.2 Docker rootless

Ejecuta el daemon sin privilegios de root (más seguro, con limitaciones en puertos <1024 y rendimiento de red). En Arch: paquete `docker-rootless-extras` (AUR), y `dockerd-rootless-setuptool.sh install`. Consulta la documentación oficial antes de activarlo: requiere `subuid`/`subgid` configurados.

---

## 12. Solución de problemas

| Síntoma | Causa y solución |
|---|---|
| `Cannot connect to the Docker daemon` | Daemon parado: `sudo systemctl start docker`. |
| `permission denied … /var/run/docker.sock` | No estás en el grupo `docker`, o no has reiniciado sesión. `sudo usermod -aG docker $USER` y relogin. |
| `port is already allocated` / `address already in use` | Otro proceso usa el puerto. Búscalo: `ss -tlnp \| grep :5432`. Cambia el puerto de host. |
| El contenedor sale en seguida | `docker logs <nombre>` y `docker compose logs <servicio>`. Mira el código de salida con `docker ps -a`. |
| La app no conecta con la BD | Estás usando `localhost` en vez del nombre del servicio (`db`). O la BD aún no está lista: usa `healthcheck` + `depends_on: condition: service_healthy`. |
| Cambié el `.env`/`environment` de la BD y no hace efecto | Las variables de inicialización de Postgres solo se aplican **la primera vez** (con volumen vacío). Para reiniciar de cero: `docker compose down -v`. |
| Sin Internet dentro de contenedores / DNS falla | Suele ser conflicto con VPN o `systemd-resolved`; prueba `docker run --rm alpine ping -c1 1.1.1.1`. Si IP funciona y nombre no, configura `"dns": ["1.1.1.1"]` en `daemon.json`. |
| Redes Docker chocan con tu VPN/red local | Cambia `default-address-pools` en `daemon.json` (ver 2.5). |
| `docker build` avisa de «legacy builder» | Falta `docker-buildx`: `sudo pacman -S docker-buildx`. |
| Disco lleno | `docker system df` y [limpieza](#10-limpieza-y-mantenimiento). |
| Tras actualizar el kernel dejan de funcionar las redes | Faltan módulos del kernel cargados: reinicia el equipo (en Arch el kernel se actualiza y los módulos antiguos desaparecen). |
| Ficheros del bind mount con dueño `root` | Ejecuta el contenedor con `user: "${UID}:${GID}"` o corrige con `sudo chown`. |

Diagnóstico general:

```bash
journalctl -u docker -e              # logs del daemon
docker info                          # configuración efectiva
docker compose config                # YAML resuelto
docker events                        # eventos en vivo
```

---

## 13. Chuleta rápida

```bash
# Instalación (Arch)
sudo pacman -S docker docker-compose docker-buildx
sudo systemctl enable --now docker
sudo usermod -aG docker $USER        # y relogin

# Día a día
docker compose up -d                 # levantar
docker compose logs -f               # ver logs
docker compose ps                    # estado
docker compose exec <srv> sh         # entrar
docker compose down                  # parar y borrar (conserva datos)

# Limpieza
docker system df
docker system prune
```
