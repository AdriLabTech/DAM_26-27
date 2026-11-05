<p align="center"><img src="docs/banner.svg" alt="Conversor MVVM" width="100%"></p>

# Conversor MVVM

**Actividad 2.7** de la presentación de la UD01 · Parte 2 (WPF): *Conversor de temperaturas con MVVM*.

## 📝 Qué pide la actividad

1. ✅ ViewModel con `[ObservableProperty]` `Celsius`.
2. ✅ Propiedad `Fahrenheit` calculada que cambia al escribir (`[NotifyPropertyChangedFor]`).
3. ✅ Comando `Anotar` que guarda el valor en una `ObservableCollection`.
4. ✅ Cero manejadores de eventos en la ventana (el code-behind está vacío).

## 📁 Contenido

- `ConversorTemperaturas/App.xaml`
- `ConversorTemperaturas/App.xaml.cs`
- `ConversorTemperaturas/ConversorTemperaturas.csproj`
- `ConversorTemperaturas/ConversorViewModel.cs`
- `ConversorTemperaturas/MainWindow.xaml`
- `ConversorTemperaturas/MainWindow.xaml.cs`

## 🚀 Ejecución

```bash
cd ConversorTemperaturas
dotnet run
```

> 🐧 Usa `LibreWPF.Sdk` (preview) para ejecutarse en Linux. En Windows cambia el `Sdk` del `.csproj` por `Microsoft.NET.Sdk`.
