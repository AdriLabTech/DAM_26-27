package dev.lownoise.practicarecycleview

import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import java.text.NumberFormat
import java.util.Locale
class MainActivity : AppCompatActivity() {
    private lateinit var recycler: RecyclerView
    private var enCuadricula = false
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(
            findViewById(R.id.main)
        ) { vista, insets ->
            val barras = insets.getInsets(
                WindowInsetsCompat.Type.systemBars()
            )
            vista.setPadding(barras.left, barras.top, barras.right, barras.bottom)
            insets
        }
        recycler = findViewById(R.id.recyclerPueblos)
        enCuadricula = savedInstanceState?.getBoolean("cuadricula") ?: false
        aplicarVista(enCuadricula)
        recycler.adapter = PuebloAdapter(pueblosCordoba) { pueblo ->
            mostrarFicha(pueblo)
        }
        findViewById<Button>(R.id.btnLista).setOnClickListener {
            aplicarVista(false)
        }
        findViewById<Button>(R.id.btnCuadricula).setOnClickListener {
            aplicarVista(true)
        }
    }
    private fun aplicarVista(cuadricula: Boolean) {
        enCuadricula = cuadricula
        recycler.layoutManager = if (cuadricula) {
            GridLayoutManager(this, 2)
        } else {
            LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false)
        }
    }
    override fun onSaveInstanceState(outState: Bundle) {
        outState.putBoolean("cuadricula", enCuadricula)
        super.onSaveInstanceState(outState)
    }
    private fun mostrarFicha(pueblo: Pueblo) {
        val formato = NumberFormat.getIntegerInstance(
            Locale.forLanguageTag("es-ES")
        )
        val poblacion = getString(
            R.string.habitantes_formato,
            formato.format(pueblo.habitantes)
        )
        AlertDialog.Builder(this)
            .setTitle(pueblo.nombre)
            .setMessage(getString(R.string.detalle_formato, poblacion, pueblo.resena))
            .setPositiveButton(R.string.cerrar_ficha, null)
            .show()
    }
}