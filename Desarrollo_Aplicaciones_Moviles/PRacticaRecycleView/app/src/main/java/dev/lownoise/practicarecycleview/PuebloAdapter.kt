package dev.lownoise.practicarecycleview

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import java.text.NumberFormat
import java.util.Locale
class PuebloAdapter(
    private val pueblos: List<Pueblo>,
    private val onPuebloClick: (Pueblo) -> Unit
) : RecyclerView.Adapter<PuebloAdapter.PuebloViewHolder>() {
    private val formato = NumberFormat.getIntegerInstance(
        Locale.forLanguageTag("es-ES")
    )
    override fun getItemCount(): Int = pueblos.size
    override fun onCreateViewHolder(
        parent: ViewGroup,
        viewType: Int
    ): PuebloViewHolder {
        val vista = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_pueblo, parent, false)
        return PuebloViewHolder(vista)
    }
    override fun onBindViewHolder(
        holder: PuebloViewHolder,
        position: Int
    ) {
        holder.bind(pueblos[position], formato, onPuebloClick)
    }
    class PuebloViewHolder(itemView: View) :
        RecyclerView.ViewHolder(itemView) {
        private val nombre: TextView =
            itemView.findViewById(R.id.tvNombre)
        private val habitantes: TextView =
            itemView.findViewById(R.id.tvHabitantes)
        private val resena: TextView =
            itemView.findViewById(R.id.tvResena)
        fun bind(
            pueblo: Pueblo,
            formato: NumberFormat,
            onPuebloClick: (Pueblo) -> Unit
        ) {
            nombre.text = pueblo.nombre
            habitantes.text = itemView.context.getString(
                R.string.habitantes_formato,
                formato.format(pueblo.habitantes)
            )
            resena.text = pueblo.resena
            itemView.setOnClickListener {
                onPuebloClick(pueblo)
            }
        }
    }
}