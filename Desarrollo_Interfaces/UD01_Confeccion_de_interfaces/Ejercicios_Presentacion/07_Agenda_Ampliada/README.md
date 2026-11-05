<p align="center"><img src="docs/banner.svg" alt="Agenda ampliada" width="100%"></p>

# Agenda ampliada

**Actividad 2.9** de la presentación de la UD01 · Parte 2 (WPF): *Amplía la agenda*.

## 📝 Qué pide la actividad

1. ✅ Campo **Ciudad** (modelo, diálogo, tabla, JSON y CSV).
2. ✅ Botón **Exportar a CSV** (comando + `SaveFileDialog` a través del servicio de diálogos).
3. ✅ **Confirmación antes de eliminar** (servicio de diálogos).
4. ✅ Botón para **cambiar entre claro y oscuro** (`ThemeMode` desde un servicio).

Evaluación de la actividad: ViewModel sin controles (los diálogos y el tema van por interfaz), comandos con `CanExecute` (Editar y Eliminar sin selección, Exportar sin contactos) y validación visible (nombre obligatorio y correo válido, con el mensaje bajo el campo).

**Estructura:** `Contacto` (modelo con `ObservableValidator`), `ContactoRepositorio` (JSON en `~/.local/share/AgendaAmpliada/`), `ContactoCsv`, `IDialogoService` / `DialogoService`, `ITemaService` / `TemaService`, `MainViewModel`, `MainWindow` y `ContactoDialog`.

> Verificación: la lógica (validación, repositorio, CSV, filtro, nuevo/editar/eliminar con y sin confirmar, exportar y tema) se comprobó con 31 pruebas automáticas fuera del repositorio usando servicios simulados. Los diálogos reales (`ContactoDialog`, `SaveFileDialog`, `MessageBox`) y el cambio de tema no se han probado con clics.

## 📁 Contenido

- `AgendaAmpliada/AgendaAmpliada.csproj`
- `AgendaAmpliada/App.xaml`
- `AgendaAmpliada/App.xaml.cs`
- `AgendaAmpliada/Contacto.cs`
- `AgendaAmpliada/ContactoCsv.cs`
- `AgendaAmpliada/ContactoDialog.xaml`
- `AgendaAmpliada/ContactoDialog.xaml.cs`
- `AgendaAmpliada/ContactoRepositorio.cs`
- `AgendaAmpliada/DialogoService.cs`
- `AgendaAmpliada/IDialogoService.cs`
- `AgendaAmpliada/ITemaService.cs`
- `AgendaAmpliada/MainViewModel.cs`
- `AgendaAmpliada/MainWindow.xaml`
- `AgendaAmpliada/MainWindow.xaml.cs`

## 🚀 Ejecución

```bash
cd AgendaAmpliada
dotnet run
```

> 🐧 Usa `LibreWPF.Sdk` (preview) para ejecutarse en Linux. En Windows cambia el `Sdk` del `.csproj` por `Microsoft.NET.Sdk`.
