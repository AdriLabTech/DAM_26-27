<p align="center"><img src="docs/banner.svg" alt="Agenda de contactos" width="100%"></p>

# Agenda de contactos

**Proyecto integrador** de la presentación de la UD00 (Introducción a C# y .NET).

## 📝 Enunciado

Gestor completo de contactos en consola utilizando `Dictionary<string, string>`.

**Requisitos:** Menú interactivo: 1. Añadir contacto, 2. Buscar por nombre con `TryGetValue()`, 3. Listar todos, 4. Salir.

## 📁 Contenido

- `AgendaDeContactos/AgendaDeContactos.csproj`
- `AgendaDeContactos/ProyectoFinalAgenda.cs`

## 🚀 Ejecución

Necesitas el **SDK de .NET 10**.

```bash
dotnet run --project AgendaDeContactos
```


**Entrada de ejemplo:** `1 ⏎ Ana ⏎ 600112233 ⏎ 1 ⏎ Luis ⏎ 611 ⏎ 2 ⏎ Ana ⏎ 2 ⏎ Zoe ⏎ 3 ⏎ 9 ⏎ 4`

## 🧪 Salida

```text

=== AGENDA DE CONTACTOS ===
1. Anadir contacto
2. Buscar por nombre
3. Listar todos
4. Salir
Opcion: Nombre: Telefono: Contacto anadido.

=== AGENDA DE CONTACTOS ===
1. Anadir contacto
2. Buscar por nombre
3. Listar todos
4. Salir
Opcion: Nombre: Telefono: Contacto anadido.

=== AGENDA DE CONTACTOS ===
1. Anadir contacto
2. Buscar por nombre
3. Listar todos
4. Salir
Opcion: Nombre a buscar: Telefono: 600112233

…
```
