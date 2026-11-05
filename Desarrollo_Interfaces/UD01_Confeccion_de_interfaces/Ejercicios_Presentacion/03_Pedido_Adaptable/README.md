<p align="center"><img src="docs/banner.svg" alt="Pedido adaptable" width="100%"></p>

# Pedido adaptable

**Actividad 2.4** de la presentación de la UD01 · Parte 2 (WPF): *Un formulario que se adapta*.

## 📝 Qué pide la actividad

1. ✅ Ventana «Pedido» con dos grupos: **Datos** y **Resumen** (`GroupBox`).
2. ✅ Colocados en un `Grid` de dos columnas.
3. ✅ Si el ancho es menor de 520, el resumen pasa debajo (`SizeChanged` + `Reorganizar()`).
4. ✅ `MinWidth="360"` y `MinHeight="300"`.

El resumen se actualiza al escribir gracias a bindings entre elementos, sin código.

## 📁 Contenido

- `Pedido/App.xaml`
- `Pedido/App.xaml.cs`
- `Pedido/MainWindow.xaml`
- `Pedido/MainWindow.xaml.cs`
- `Pedido/Pedido.csproj`

## 🚀 Ejecución

```bash
cd Pedido
dotnet run
```

> 🐧 Usa `LibreWPF.Sdk` (preview) para ejecutarse en Linux. En Windows cambia el `Sdk` del `.csproj` por `Microsoft.NET.Sdk`.
