# Práctica ConstraintLayout: respuestas a las preguntas de consolidación

PMDM · 2.º DAM. Las capturas citadas están en `~/Imágenes/Screenshots/Moviles` (`P<paso>_<tema>[_PruebaN].png`).

**1. ¿Qué diferencia hay entre LinearLayout y ConstraintLayout?**
`LinearLayout` apila sus hijos en una sola dirección (vertical u horizontal) y reparte el espacio con `layout_weight`. Para diseños complejos hay que anidar varios layouts. `ConstraintLayout` coloca cada vista mediante restricciones respecto al contenedor o a otras vistas, en ambos ejes a la vez. Casi todo se resuelve con una jerarquía plana (un solo contenedor), que mide y dibuja más rápido y es más fácil de mantener.

**2. ¿Qué significa 0dp en una dimensión de una vista dentro de ConstraintLayout?**
Significa *match constraints*: la dimensión no se fija ni depende del contenido, sino que se calcula para ocupar el espacio entre las dos restricciones de ese eje. Con `Start` y `End` conectados, la anchura es la distancia entre ambos límites (ver `P5_CrearAnchoDisponible`). No hace desaparecer la vista. Si falta una de las dos restricciones no hay espacio delimitado y no funciona igual.

**3. ¿Cuándo es adecuado `wrap_content` y cuándo `0dp`?**
`wrap_content` cuando el tamaño debe depender del contenido (títulos, botones con texto, etiquetas). `0dp` cuando la vista debe adaptarse al espacio disponible entre restricciones: campos de texto que ocupan el ancho, vistas entre dos guías, o botones que reparten espacio con pesos en una cadena.

**4. ¿Qué diferencia hay entre margin y padding?**
*Margin* es espacio exterior: separa la vista de las demás o de los bordes del contenedor. *Padding* es espacio interior: separa el contenido de la vista de sus propios bordes. En `P6_MargenesEspacioInterior_Prueba1/2` el `marginTop` desplaza el campo y el `padding` lo hace más alto por dentro.

**5. ¿Qué restricciones necesita una vista para que horizontal bias tenga efecto?**
Restricciones en los dos lados del eje horizontal: `Start` y `End` (a `parent` u otras vistas). Así hay un intervalo en el que desplazarla. El mismo principio vale para el vertical: `Top` y `Bottom`. Con una sola restricción no hay intervalo y el bias se ignora.

**6. ¿Qué diferencia hay entre spread, spread_inside y packed?**
- `spread` (por defecto): reparte el espacio libre a partes iguales entre los extremos y las vistas.
- `spread_inside`: las vistas de los extremos pegadas a los límites de la cadena y el espacio sobrante entre las vistas.
- `packed`: agrupa las vistas juntas en el centro; el grupo se desplaza con bias.

Ver `P9_CadenaHorizontal` (spread), `P10_EstilosCadena_Prueba1_spread_inside` y `P10_EstilosCadena_Prueba2_packed`.

**7. ¿Qué condiciones necesita una cadena para repartir el espacio mediante pesos?**
Que la cadena esté completa, conectada de extremo a extremo (primer elemento al límite inicial, cada uno con el siguiente, último al límite final), y que las vistas tengan `0dp` en el eje de la cadena. Cada vista lleva `layout_constraintHorizontal_weight` (o `Vertical`). El espacio se reparte en proporción a los pesos.

**8. ¿Qué ventaja ofrece una Guideline porcentual frente a un margen fijo?**
Mantiene la proporción al cambiar el tamaño o la orientación de la pantalla: al 25 % del ancho sigue en el 25 % en un móvil pequeño o en una tablet. Un margen fijo en dp es la misma distancia absoluta y en pantallas distintas se ve desproporcionado.

**9. ¿En qué se diferencia una Guideline de una Barrier?**
Ambas son referencias invisibles. La *Guideline* se coloca donde decidimos nosotros (`begin`, `end` o `percent`) y no depende de ninguna vista. La *Barrier* calcula su posición a partir de los límites de las vistas listadas en `constraint_referenced_ids` (por ejemplo, el extremo final de la etiqueta más ancha).

**10. ¿Qué sucede si cambia el tamaño de una vista utilizada por una Barrier?**
La barrera se recalcula y se coloca en el nuevo extremo de la vista más extrema. Las vistas conectadas a ella se desplazan automáticamente. En `P14_Barrier_Prueba1` la etiqueta del correo es más larga y los tres campos se mueven.

**11. ¿Qué diferencia hay entre invisible y gone?**
`invisible` no se dibuja pero conserva su espacio en el diseño. `gone` no se dibuja y no ocupa espacio: es como si no existiera, así que las vistas conectadas a ella se recolocan (y se usa `layout_goneMargin*` como margen alternativo).

**12. ¿Por qué conviene evitar posicionar vistas mediante coordenadas absolutas?**
Porque la interfaz deja de adaptarse: Android tiene muchísimos tamaños, densidades y orientaciones, y una posición en x/y fija se ve cortada, solapada o desplazada. Tampoco se adapta a cambios de idioma, tamaño de fuente o textos dinámicos, y el diseño es frágil: al mover una vista hay que recalcular a mano las demás. Con restricciones, la relación se mantiene.
