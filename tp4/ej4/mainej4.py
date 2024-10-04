import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QMessageBox
from Ingles import Ingles
from Frances import Frances
from Portugues import Portugues
class TraductorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Traductor de Idiomas')

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta de selección de idioma
        self.label_idioma = QLabel("Seleccione el idioma:")
        layout.addWidget(self.label_idioma)

        # ComboBox para seleccionar el idioma
        self.combo_idioma = QComboBox()
        self.combo_idioma.addItems(["Inglés", "Francés", "Portugués"])
        layout.addWidget(self.combo_idioma)

        # Etiqueta de selección de mensaje
        self.label_mensaje = QLabel("Seleccione el mensaje:")
        layout.addWidget(self.label_mensaje)

        # ComboBox para seleccionar el mensaje
        self.combo_mensaje = QComboBox()
        self.combo_mensaje.addItems(["Saludar", "Despedirse", "Perdon", "Pedir Café", "Cuánto cuesta", "Dónde queda"])
        layout.addWidget(self.combo_mensaje)

        # Botón para traducir
        self.boton_traducir = QPushButton("Traducir")
        layout.addWidget(self.boton_traducir)

        # Etiqueta para mostrar el resultado
        self.label_resultado = QLabel("")
        layout.addWidget(self.label_resultado)

        # Conectar el botón a la función de traducción
        self.boton_traducir.clicked.connect(self.traducir)

        # Configurar la ventana
        self.setLayout(layout)

    def traducir(self):
        idioma_seleccionado = self.combo_idioma.currentText()
        mensaje_seleccionado = self.combo_mensaje.currentText()

        # Crear el objeto del idioma seleccionado
        if idioma_seleccionado == "Inglés":
            idioma = Ingles()
        elif idioma_seleccionado == "Francés":
            idioma = Frances()
        else:
            idioma = Portugues()

        # Llamar al método correspondiente basado en el mensaje seleccionado
        if mensaje_seleccionado == "Saludar":
            traduccion = idioma.saludar()
        elif mensaje_seleccionado == "Despedirse":
            traduccion = idioma.despedirse()
        elif mensaje_seleccionado == "Perdon":
            traduccion = idioma.perdon()
        elif mensaje_seleccionado == "Pedir Café":
            traduccion = idioma.pedir_cafe()
        elif mensaje_seleccionado == "Cuánto cuesta":
            traduccion = idioma.cuanto_cuesta()
        elif mensaje_seleccionado == "Dónde queda":
            traduccion = idioma.donde_queda()
        else:
            QMessageBox.critical(self, "Error", "Seleccione un mensaje válido")
            return

        # Mostrar la traducción
        self.label_resultado.setText(f"Traducción: {traduccion}")

# Correr la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TraductorGUI()
    ventana.show()
    sys.exit(app.exec())
