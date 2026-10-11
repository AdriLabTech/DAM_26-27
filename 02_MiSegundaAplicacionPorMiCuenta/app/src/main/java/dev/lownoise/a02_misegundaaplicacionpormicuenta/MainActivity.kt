package dev.lownoise.a02_misegundaaplicacionpormicuenta

import android.os.Bundle
import android.widget.Button
import android.widget.CheckBox
import android.widget.EditText
import android.widget.LinearLayout
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.google.android.material.textfield.TextInputLayout

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val buttonAddTask = findViewById<Button>(R.id.addTask)

        val contenedorInputs = findViewById<LinearLayout>(R.id.contenedorInputs)

        var counter = 1
        buttonAddTask.setOnClickListener {
            val nuevoInput: CheckBox = createTask(counter)
            counter += 1;

            contenedorInputs.addView(nuevoInput)
        }
    }

    fun createTask(counter: Int) : CheckBox {
        val nuevoInput = CheckBox(this)
        nuevoInput.hint = "Tarea $counter"
        nuevoInput.layoutParams = LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT,
            LinearLayout.LayoutParams.WRAP_CONTENT
        )

        return nuevoInput
    }
}