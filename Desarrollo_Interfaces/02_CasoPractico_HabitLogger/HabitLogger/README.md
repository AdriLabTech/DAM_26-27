# 📝 HabitLogger (versión consola)

**Registro de hábitos por consola escrito en C#.**

Cada hábito (agua, lectura, ejercicio…) tiene su propia tabla en una base de datos SQLite, con las columnas `Id`, `Fecha` y `Cantidad`. Desde un menú numerado puedes crear hábitos y consultar, insertar, actualizar o eliminar sus registros.

> 🖥️ Existe también una versión con interfaz de terminal: [HabitLoggerTui](../HabitLoggerTui/README.md).

## ✨ Funciones

- Crear hábitos (el nombre del hábito es el nombre de su tabla).
- Ver, insertar, actualizar y eliminar registros de un hábito.
- Listar todos los hábitos creados.
- Validación de lo que escribe el usuario (nombres, fechas y cantidades).
- Log diario de operaciones en `logs/dd_MM_yyyy.log`.
- Los errores se guardan en la tabla `Errores` de la BD y la aplicación sigue funcionando.

## 🚀 Ejecución

Necesitas tener instalado el **SDK de .NET 10**.

```bash
dotnet run --project HabitLogger
```

## 🕹️ Menú

```text
=== REGISTRO DE HABITOS ===
1. Crear un Hábito
2. Ver registros
3. Insertar registro
4. Actualizar registro
5. Eliminar registro
6. Mostrar todos los hábitos
0. Salir
```

Las opciones 2 a 5 piden primero el nombre del hábito sobre el que trabajar.

## 🗂️ Estructura

| Archivo | Responsabilidad |
|---|---|
| `Program.cs` | Punto de entrada, menú y bucle principal |
| `Entrada.cs` | Lectura y validación de lo que escribe el usuario |
| `GestorHabitos.cs` | Operaciones sobre los hábitos y sus registros |
| `DataBaseConnector/` | Conexión única y compartida con SQLite |
| `LogErrores.cs` | Guarda los errores en la tabla `Errores` |
| `LogOperaciones.cs` | Escribe el log diario de operaciones |

## 💾 Datos

La base de datos (`mi_bbdd.bd`) y la carpeta `logs/` se crean junto al ejecutable (`bin/`) la primera vez que se arranca la aplicación.

## 🧰 Tecnologías

- C# / .NET 10
- SQLite con `Microsoft.Data.Sqlite`
