using Ratatui;

namespace HabitLoggerTui;

/// <summary>
/// Interfaz de terminal (TUI) hecha con Ratatui.cs. Ratatui.cs se encarga de DIBUJAR;
/// las teclas se leen con Console.ReadKey porque en Windows el evento de teclado de
/// Ratatui.cs llega duplicado (una vez al pulsar y otra al soltar la tecla).
///
/// Funcionamiento: la variable _pantalla dice en que pantalla esta el usuario. Cada tecla se
/// manda al metodo de esa pantalla (Tecla...), que solo cambia las variables de estado
/// (seleccion, texto de los campos, mensaje...). Despues se vuelve a dibujar todo (Dibujar...)
/// a partir de ese estado. Es decir: teclado = modifica el estado, dibujado = lo pinta
/// </summary>
internal class Aplicacion
{
    // Pantallas: Menu (principal), Ver (lista solo de lectura), Elegir (lista para escoger el registro
    // a actualizar o eliminar), Formulario (fecha y cantidad) y Confirmar (pregunta antes de eliminar)
    private enum Pantalla { Menu, Ver, Elegir, Formulario, Confirmar }

    // Operacion en curso. Elegir y Formulario se reutilizan en varias operaciones y esto indica cual es
    private enum Accion { Insertar, Actualizar, Eliminar }

    // Tamano minimo de la ventana para que todo quepa (Ratatui.cs no parte las lineas largas, solo las corta)
    private const int AnchoMinimo = 80;
    private const int AltoMinimo = 14;

    private static readonly string[] OpcionesMenu =
    {
        "1. Ver registros",
        "2. Insertar registro",
        "3. Actualizar registro",
        "4. Eliminar registro",
        "0. Salir"
    };

    private static readonly Style EstiloSeleccion = new Style(fg: Color.Black, bg: Color.Cyan, bold: true);
    private static readonly Style EstiloCabecera = new Style(fg: Color.Yellow, bold: true);
    private static readonly Style EstiloActivo = new Style(fg: Color.Cyan, bold: true);
    private static readonly Style EstiloError = new Style(fg: Color.LightRed, bold: true);
    private static readonly Style EstiloCorrecto = new Style(fg: Color.LightGreen, bold: true);

    private readonly GestorHabitos _gestor;
    private readonly LogErrores _logErrores;

    // Los widgets de Ratatui.cs son recursos nativos: los guardamos para liberarlos despues de cada dibujado
    private readonly List<IDisposable> _widgets = new List<IDisposable>();

    private Pantalla _pantalla = Pantalla.Menu;
    private Accion _accion;
    private int _opcionMenu;                           // opcion elegida en el menu
    private List<Habito> _habitos = new List<Habito>();
    private int _seleccion;                            // fila elegida en la lista de registros
    private int _inicio;                               // primera fila visible de la lista
    private Habito? _elegido;                          // registro que se actualiza o elimina
    private string[] _campos = { "", "" };             // texto de los campos del formulario (fecha y cantidad)
    private int _foco;                                 // campo del formulario que se esta escribiendo
    private string _mensaje = "";
    private bool _mensajeEsError;

    public Aplicacion(GestorHabitos gestor, LogErrores logErrores)
    {
        _gestor = gestor;
        _logErrores = logErrores;
    }

    // Bucle principal de la TUI. En cada vuelta: 1) dibuja si hace falta y 2) mira si hay una tecla.
    // Termina cuando ProcesarTecla devuelve true (el usuario quiere salir)
    public void Ejecutar()
    {
        // Al crear el Terminal se activa el modo raw y la pantalla alternativa; al salir del "using" se restaura la consola
        using Terminal terminal = new Terminal().Raw(true).AltScreen(true).ShowCursor(false);

        // Ultimo tamano de la ventana con el que se dibujo (para detectar cuando cambia)
        int ancho = 0;
        int alto = 0;
        bool redibujar = true;
        bool salir = false;

        while (!salir)
        {
            // Redibujamos cuando cambia algo o cuando el usuario cambia el tamano de la ventana
            (int w, int h) = terminal.Size();
            if (redibujar || w != ancho || h != alto)
            {
                ancho = w;
                alto = h;
                redibujar = false;
                Dibujar(terminal, w, h);
            }

            // KeyAvailable no bloquea: asi el bucle sigue vivo y puede detectar el cambio de tamano
            // aunque el usuario no pulse nada. Sin tecla se duerme un poco para no gastar CPU
            if (Console.KeyAvailable)
            {
                salir = ProcesarTecla(Console.ReadKey(intercept: true));
                redibujar = true;
            }
            else
            {
                Thread.Sleep(30);
            }
        }
    }

    // ------------------------------------------------------------------
    // TECLADO
    // ------------------------------------------------------------------

    // Reparte la tecla al metodo de la pantalla actual. Devuelve true cuando hay que salir de la aplicacion
    // (solo el menu puede pedirlo, ademas de Ctrl+C)
    private bool ProcesarTecla(ConsoleKeyInfo tecla)
    {
        // En modo raw Ctrl+C llega como una tecla mas: lo usamos para salir desde cualquier pantalla
        if (tecla.Key == ConsoleKey.C && tecla.Modifiers.HasFlag(ConsoleModifiers.Control))
        {
            return true;
        }

        // El mensaje de la linea inferior dura solo hasta la siguiente tecla
        _mensaje = "";

        // Este try/catch evita que un error en cualquier pantalla cierre la aplicacion
        try
        {
            if (_pantalla == Pantalla.Menu)
            {
                return TeclaMenu(tecla);
            }
            else if (_pantalla == Pantalla.Ver)
            {
                TeclaVer(tecla);
            }
            else if (_pantalla == Pantalla.Elegir)
            {
                TeclaElegir(tecla);
            }
            else if (_pantalla == Pantalla.Formulario)
            {
                TeclaFormulario(tecla);
            }
            else
            {
                TeclaConfirmar(tecla);
            }
        }
        catch (Exception ex)
        {
            _logErrores.Guardar("Pantalla " + _pantalla, ex);
            LogOperaciones.Escribir("ERROR en la pantalla " + _pantalla);
            IrAlMenu("Ha ocurrido un error y la operacion no se ha completado. Error guardado.", true);
        }

        return false;
    }

    private bool TeclaMenu(ConsoleKeyInfo tecla)
    {
        // El menu es "circular": desde la ultima opcion, bajar lleva a la primera y al reves.
        // Eso se consigue con el resto (%) de dividir entre el numero de opciones. Para subir se
        // suma Length antes de restar 1, porque en C# el resto de un numero negativo seria negativo
        if (tecla.Key == ConsoleKey.UpArrow)
        {
            _opcionMenu = (_opcionMenu + OpcionesMenu.Length - 1) % OpcionesMenu.Length;
        }
        else if (tecla.Key == ConsoleKey.DownArrow)
        {
            _opcionMenu = (_opcionMenu + 1) % OpcionesMenu.Length;
        }
        else if (tecla.Key == ConsoleKey.Enter)
        {
            return AbrirOpcion(_opcionMenu);
        }
        else if (tecla.Key == ConsoleKey.Escape)
        {
            return true;
        }
        else if (tecla.KeyChar >= '1' && tecla.KeyChar <= '4')
        {
            // Atajo: el numero de la opcion. Restar el caracter '1' convierte '1'..'4' en el indice 0..3
            _opcionMenu = tecla.KeyChar - '1';
            return AbrirOpcion(_opcionMenu);
        }
        else if (tecla.KeyChar == '0')
        {
            // "Salir" es la ultima opcion del menu (indice 4) aunque su numero sea el 0
            return AbrirOpcion(OpcionesMenu.Length - 1);
        }

        return false;
    }

    // Abre la opcion del menu. Devuelve true si la opcion es "Salir".
    // Indices: 0 = Ver, 1 = Insertar, 2 = Actualizar, 3 = Eliminar, 4 = Salir
    private bool AbrirOpcion(int indice)
    {
        if (indice == 4)
        {
            return true;
        }

        if (indice == 1)
        {
            _accion = Accion.Insertar;
            AbrirFormulario(null);
            return false;
        }

        // Ver, actualizar y eliminar necesitan la lista de registros
        _habitos = _gestor.ObtenerTodos();
        _seleccion = 0;
        _inicio = 0;

        if (indice == 0)
        {
            _pantalla = Pantalla.Ver;
            LogOperaciones.Escribir("VER registros");
            return false;
        }

        // Actualizar y eliminar primero necesitan que el usuario elija un registro. Si no hay ninguno,
        // no se cambia de pantalla: se queda en el menu con un mensaje de error
        _accion = indice == 2 ? Accion.Actualizar : Accion.Eliminar;
        if (_habitos.Count == 0)
        {
            _mensaje = "No hay registros.";
            _mensajeEsError = true;
            LogOperaciones.Escribir(_accion.ToString().ToUpper() + " cancelado: no hay registros");
        }
        else
        {
            _pantalla = Pantalla.Elegir;
        }
        return false;
    }

    private void TeclaVer(ConsoleKeyInfo tecla)
    {
        if (tecla.Key == ConsoleKey.Escape || tecla.Key == ConsoleKey.Enter)
        {
            IrAlMenu();
        }
        else
        {
            MoverSeleccion(tecla);
        }
    }

    private void TeclaElegir(ConsoleKeyInfo tecla)
    {
        if (tecla.Key == ConsoleKey.Escape)
        {
            IrAlMenu();
        }
        else if (tecla.Key == ConsoleKey.Enter)
        {
            // Se recuerda el registro elegido; lo usan el formulario (actualizar) y la confirmacion (eliminar)
            _elegido = _habitos[_seleccion];
            if (_accion == Accion.Actualizar)
            {
                AbrirFormulario(_elegido);
            }
            else
            {
                _pantalla = Pantalla.Confirmar;
            }
        }
        else
        {
            MoverSeleccion(tecla);
        }
    }

    // Flechas, AvPag, RePag, Inicio y Fin para moverse por la lista de registros
    private void MoverSeleccion(ConsoleKeyInfo tecla)
    {
        if (tecla.Key == ConsoleKey.UpArrow)
        {
            _seleccion--;
        }
        else if (tecla.Key == ConsoleKey.DownArrow)
        {
            _seleccion++;
        }
        else if (tecla.Key == ConsoleKey.PageUp)
        {
            _seleccion -= 10;
        }
        else if (tecla.Key == ConsoleKey.PageDown)
        {
            _seleccion += 10;
        }
        else if (tecla.Key == ConsoleKey.Home)
        {
            _seleccion = 0;
        }
        else if (tecla.Key == ConsoleKey.End)
        {
            _seleccion = _habitos.Count - 1;
        }

        // La seleccion nunca se sale de la lista: Min impide pasarse del ultimo registro y Max impide bajar de 0
        _seleccion = Math.Max(0, Math.Min(_seleccion, _habitos.Count - 1));
    }

    // Prepara el formulario de fecha y cantidad. Sin registro (insertar) los campos empiezan vacios;
    // con registro (actualizar) empiezan con los valores actuales para que el usuario solo cambie lo que quiera
    private void AbrirFormulario(Habito? habito)
    {
        _pantalla = Pantalla.Formulario;
        _foco = 0;

        if (habito == null)
        {
            _campos = new string[] { "", "" };
        }
        else
        {
            // Al actualizar, el formulario empieza con los valores actuales
            _campos = new string[] { habito.FechaTexto, habito.Cantidad.ToString() };
        }
    }

    // Ratatui.cs no tiene un widget para escribir texto, asi que el campo se maneja a mano:
    // _campos[_foco] es el texto del campo activo y cada tecla lo modifica
    private void TeclaFormulario(ConsoleKeyInfo tecla)
    {
        if (tecla.Key == ConsoleKey.Escape)
        {
            LogOperaciones.Escribir(_accion.ToString().ToUpper() + " cancelado por el usuario");
            IrAlMenu();
        }
        else if (tecla.Key == ConsoleKey.Tab || tecla.Key == ConsoleKey.UpArrow || tecla.Key == ConsoleKey.DownArrow)
        {
            // Solo hay dos campos (0 y 1): 1 - _foco alterna entre ellos (1-0 = 1 y 1-1 = 0)
            _foco = 1 - _foco;
        }
        else if (tecla.Key == ConsoleKey.Enter)
        {
            // En el primer campo Enter pasa al segundo; en el segundo, intenta guardar
            if (_foco == 0)
            {
                _foco = 1;
            }
            else
            {
                EnviarFormulario();
            }
        }
        else if (tecla.Key == ConsoleKey.Backspace)
        {
            // Borrar = quedarse con el texto sin su ultimo caracter
            if (_campos[_foco].Length > 0)
            {
                _campos[_foco] = _campos[_foco].Substring(0, _campos[_foco].Length - 1);
            }
        }
        // Cualquier otra tecla se anade al texto, salvo las de control (Alt, F1, flechas...) que no
        // tienen caracter. El limite de 10 caracteres es el largo de una fecha (dd/MM/yyyy)
        else if (!char.IsControl(tecla.KeyChar) && _campos[_foco].Length < 10)
        {
            _campos[_foco] += tecla.KeyChar;
        }
    }

    // Valida los dos campos. Si todo es correcto guarda el registro; si no, muestra el error
    // y deja el cursor en el campo equivocado para que el usuario lo corrija
    private void EnviarFormulario()
    {
        if (!Validacion.EsFechaValida(_campos[0], out DateTime fecha, out string error))
        {
            MostrarErrorDeEntrada(_campos[0], error);
            _foco = 0;
            return;
        }

        if (!Validacion.EsCantidadValida(_campos[1], out int cantidad, out error))
        {
            MostrarErrorDeEntrada(_campos[1], error);
            _foco = 1;
            return;
        }

        if (_accion == Accion.Insertar)
        {
            _gestor.Insertar(fecha, cantidad);
            IrAlMenu("Registro insertado.", false);
        }
        else
        {
            // El "!" indica que _elegido no es null: en Actualizar siempre se paso antes por la pantalla Elegir
            _gestor.Actualizar(_elegido!.Id, fecha, cantidad);
            IrAlMenu("Registro actualizado.", false);
        }
    }

    private void MostrarErrorDeEntrada(string texto, string error)
    {
        _mensaje = error;
        _mensajeEsError = true;
        LogOperaciones.Escribir("Entrada no valida '" + texto + "': " + error);
    }

    private void TeclaConfirmar(ConsoleKeyInfo tecla)
    {
        if (tecla.KeyChar == 's' || tecla.KeyChar == 'S')
        {
            _gestor.Eliminar(_elegido!.Id);
            IrAlMenu("Registro eliminado.", false);
        }
        else if (tecla.KeyChar == 'n' || tecla.KeyChar == 'N' || tecla.Key == ConsoleKey.Escape)
        {
            LogOperaciones.Escribir("ELIMINAR cancelado: Id=" + _elegido!.Id);
            IrAlMenu("Operacion cancelada.", false);
        }
    }

    // Vuelve al menu dejando un mensaje (verde si es correcto, rojo si es error) en la linea inferior.
    // Los valores por defecto permiten llamarlo sin mensaje: IrAlMenu()
    private void IrAlMenu(string mensaje = "", bool esError = false)
    {
        _pantalla = Pantalla.Menu;
        _mensaje = mensaje;
        _mensajeEsError = esError;
    }

    // ------------------------------------------------------------------
    // DIBUJADO
    // ------------------------------------------------------------------

    // Guarda el widget para liberarlo cuando termine el dibujado y lo devuelve tal cual,
    // asi se puede escribir: Paragraph p = Nuevo(new Paragraph(...));
    private T Nuevo<T>(T widget) where T : IDisposable
    {
        _widgets.Add(widget);
        return widget;
    }

    // Dibuja la pantalla completa. Cada vez se crean los widgets desde cero (las listas de Ratatui.cs
    // no se pueden vaciar), se juntan en una lista de DrawCommand (que widget + en que rectangulo)
    // y se pintan todos a la vez. w y h son el ancho y alto actuales de la ventana
    private void Dibujar(Terminal terminal, int w, int h)
    {
        List<DrawCommand> comandos = new List<DrawCommand>();

        if (w < AnchoMinimo || h < AltoMinimo)
        {
            // Ratatui.cs 0.3.3 no parte las lineas largas (Wrap no tiene efecto), por eso el aviso va en dos lineas
            Paragraph aviso = Nuevo(new Paragraph("Ventana demasiado pequena.")
                .NewLine()
                .AppendSpan("Minimo " + AnchoMinimo + "x" + AltoMinimo + ". Ampliala.", new Style()));
            comandos.Add(DrawCommand.Paragraph(aviso, new Rect(0, 0, w, h)));
        }
        else
        {
            // Arriba el titulo (3 filas), abajo el mensaje y la ayuda (1 fila cada uno) y en medio el contenido.
            // Rect(x, y, ancho, alto) es la zona de la ventana donde se pinta cada widget (y = fila, empezando en 0).
            // Por eso el contenido empieza en la fila 3 y tiene h - 5 filas de alto (3 de titulo + 2 de abajo)
            Paragraph titulo = Nuevo(new Paragraph("REGISTRO DE HABITOS").Title(null, true).Align(Alignment.Center));
            comandos.Add(DrawCommand.Paragraph(titulo, new Rect(0, 0, w, 3)));

            Rect contenido = new Rect(0, 3, w, h - 5);
            if (_pantalla == Pantalla.Menu)
            {
                DibujarMenu(comandos, contenido);
            }
            else if (_pantalla == Pantalla.Ver || _pantalla == Pantalla.Elegir)
            {
                DibujarLista(comandos, contenido);
            }
            else if (_pantalla == Pantalla.Formulario)
            {
                DibujarFormulario(comandos, contenido);
            }
            else
            {
                DibujarConfirmacion(comandos, contenido);
            }

            Paragraph mensaje = Nuevo(new Paragraph("").AppendSpan(_mensaje, _mensajeEsError ? EstiloError : EstiloCorrecto));
            comandos.Add(DrawCommand.Paragraph(mensaje, new Rect(0, h - 2, w, 1)));

            Paragraph ayuda = Nuevo(new Paragraph(TextoDeAyuda()));
            comandos.Add(DrawCommand.Paragraph(ayuda, new Rect(0, h - 1, w, 1)));
        }

        // Todos los widgets se pintan juntos en un unico frame
        terminal.DrawFrame(comandos.ToArray());

        // Ya pintados, se liberan los recursos nativos de los widgets (si no, se acumularian en cada dibujado)
        foreach (IDisposable widget in _widgets)
        {
            widget.Dispose();
        }
        _widgets.Clear();
    }

    private string TextoDeAyuda()
    {
        if (_pantalla == Pantalla.Menu)
        {
            return "Flechas: mover | Enter: elegir | 0-4: atajo | Esc: salir";
        }
        else if (_pantalla == Pantalla.Ver)
        {
            return "Flechas, AvPag, RePag: desplazar | Esc: volver";
        }
        else if (_pantalla == Pantalla.Elegir)
        {
            return "Flechas: mover | Enter: elegir | Esc: volver";
        }
        else if (_pantalla == Pantalla.Formulario)
        {
            return "Tab o flechas: cambiar de campo | Enter: siguiente / guardar | Esc: cancelar";
        }
        return "s: eliminar | n o Esc: cancelar";
    }

    // Ratatui.cs no pinta por si solo el resaltado de la fila elegida (con DrawCommand no hay estado de
    // seleccion). Por eso aqui, en la lista y en el formulario se marca a mano: "> " delante y un color distinto
    private void DibujarMenu(List<DrawCommand> comandos, Rect contenido)
    {
        Ratatui.List menu = Nuevo(new Ratatui.List().Title("Menu", true));
        for (int i = 0; i < OpcionesMenu.Length; i++)
        {
            if (i == _opcionMenu)
            {
                menu.AppendItem("> " + OpcionesMenu[i], EstiloSeleccion);
            }
            else
            {
                menu.AppendItem("  " + OpcionesMenu[i]);
            }
        }
        // Alto = opciones + 2 filas del borde
        comandos.Add(DrawCommand.List(menu, new Rect(contenido.X, contenido.Y, contenido.Width, OpcionesMenu.Length + 2)));
    }

    // Lista de registros (cabecera + filas). Se usa para ver y para elegir el registro a actualizar o eliminar
    private void DibujarLista(List<DrawCommand> comandos, Rect contenido)
    {
        // Filas que caben: alto - 2 bordes - 1 cabecera
        int filasVisibles = Math.Max(1, contenido.Height - 3);

        // Scroll: _inicio es la primera fila de la lista que se ve en pantalla, y solo se dibujan
        // las filas de _inicio a _inicio + filasVisibles - 1 (una "ventana" sobre la lista completa).
        // Si la seleccion se sale por arriba, la ventana sube hasta ella; si se sale por abajo, baja lo
        // justo para que la seleccion quede en la ultima fila visible. Si no se sale, la ventana no se mueve
        if (_seleccion < _inicio)
        {
            _inicio = _seleccion;
        }
        if (_seleccion >= _inicio + filasVisibles)
        {
            _inicio = _seleccion - filasVisibles + 1;
        }

        string titulo = "Registros";
        if (_pantalla == Pantalla.Elegir)
        {
            titulo = _accion == Accion.Actualizar ? "Elige el registro a actualizar" : "Elige el registro a eliminar";
        }
        if (_habitos.Count > 0)
        {
            titulo += " (" + (_seleccion + 1) + "/" + _habitos.Count + ")";
        }

        Ratatui.List lista = Nuevo(new Ratatui.List().Title(titulo, true));
        // PadLeft/PadRight rellenan con espacios hasta un ancho fijo para que las columnas queden
        // alineadas (los numeros a la derecha y la fecha a la izquierda). Cabecera y filas usan los mismos anchos
        lista.AppendItem("  " + "Id".PadLeft(5) + "  " + "Fecha".PadRight(10) + "  " + "Cantidad".PadLeft(10), EstiloCabecera);

        if (_habitos.Count == 0)
        {
            lista.AppendItem("  No hay registros.");
        }

        // Solo se recorren las filas visibles (la ventana de scroll), no todos los registros
        for (int i = _inicio; i < _habitos.Count && i < _inicio + filasVisibles; i++)
        {
            Habito habito = _habitos[i];
            string fila = habito.Id.ToString().PadLeft(5) + "  " + habito.FechaTexto.PadRight(10) + "  " + habito.Cantidad.ToString().PadLeft(10);

            if (i == _seleccion)
            {
                lista.AppendItem("> " + fila, EstiloSeleccion);
            }
            else
            {
                lista.AppendItem("  " + fila);
            }
        }
        comandos.Add(DrawCommand.List(lista, contenido));
    }

    // Dibuja la cabecera y los dos campos, cada uno en una caja de 3 filas (borde + texto + borde)
    private void DibujarFormulario(List<DrawCommand> comandos, Rect contenido)
    {
        string accion = _accion == Accion.Insertar ? "Insertar registro" : "Actualizar registro (Id " + _elegido!.Id + ")";
        Paragraph cabecera = Nuevo(new Paragraph("").AppendSpan(accion, EstiloCabecera));
        comandos.Add(DrawCommand.Paragraph(cabecera, new Rect(contenido.X + 2, contenido.Y, contenido.Width - 4, 1)));

        string[] titulos =
        {
            "Fecha (dd/MM/yyyy, o escribe 'hoy')",
            "Cantidad (numero entero, minimo 1)"
        };

        for (int i = 0; i < 2; i++)
        {
            bool activo = i == _foco;

            // El campo activo se marca con "> " y con un cursor "_" al final del texto
            string texto = activo ? _campos[i] + "_" : _campos[i];
            Paragraph campo = Nuevo(new Paragraph("")
                .Title((activo ? "> " : "  ") + titulos[i], true)
                .AppendSpan(texto, activo ? EstiloActivo : new Style()));

            // i * 3 coloca cada caja justo debajo de la anterior (el campo 0 en la fila 1, el campo 1 en la 4)
            comandos.Add(DrawCommand.Paragraph(campo, new Rect(contenido.X + 2, contenido.Y + 1 + i * 3, contenido.Width - 4, 3)));
        }
    }

    private void DibujarConfirmacion(List<DrawCommand> comandos, Rect contenido)
    {
        Paragraph confirmacion = Nuevo(new Paragraph("")
            .Title("Confirmar eliminacion", true)
            .AppendSpan("Vas a eliminar este registro:", new Style())
            .NewLine()
            .AppendSpan("  " + _elegido!, EstiloActivo)
            .NewLine()
            .NewLine()
            .AppendSpan("Seguro que quieres eliminarlo? (s/n)", EstiloCabecera));

        comandos.Add(DrawCommand.Paragraph(confirmacion, new Rect(contenido.X + 2, contenido.Y, contenido.Width - 4, 7)));
    }
}
