# Instalar Docker y Docker-Compose:
```bash
sudo pacman -Syu # -> Actualizamos el sistema
sudo pacman -S docker docker-compose
```
# Habilitamos el servicio de docker:
```bash
```bash
sudo systemctl enable docker
```
```
# Respuesta esperada:
```text
Created symlink '/etc/systemd/system/multi-user.target.wants/docker.service' → '/usr/lib/systemd/system/docker.service'.
```

# Activamos y habilitamos el servicio de docker:
```bash
sudo systemctl start docker.service
sudo systemctl enable docker.service
```

# Agregamos docker al conjunto de usuarios para no tener que usar SUDO:
```bash
sudo usermod -aG docker $USER
```
