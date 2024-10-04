import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,QPushButton, QLabel, QMessageBox)
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')

        # Layout principal
        self.layout = QVBoxLayout()

        # Etiqueta para mostrar la operación
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        # Campos de entrada
        self.num1_input = QLineEdit()
        self.num2_input = QLineEdit()
        self.layout.addWidget(QLabel("Número 1:"))
        self.layout.addWidget(self.num1_input)
        self.layout.addWidget(QLabel("Número 2:"))
        self.layout.addWidget(self.num2_input)

        # Botones para operaciones
        self.boton_sumar = QPushButton("Sumar")
        self.boton_restar = QPushButton("Restar")
        self.boton_multiplicar = QPushButton("Multiplicar")
        self.boton_dividir = QPushButton("Dividir")
        self.boton_reiniciar = QPushButton("Reiniciar")

        # Conectar botones a las funciones
        self.boton_sumar.clicked.connect(self.sumar)
        self.boton_restar.clicked.connect(self.restar)
        self.boton_multiplicar.clicked.connect(self.multiplicar)
        self.boton_dividir.clicked.connect(self.dividir)
        self.boton_reiniciar.clicked.connect(self.reiniciar)

        # Añadir botones al layout
        self.layout.addWidget(self.boton_sumar)
        self.layout.addWidget(self.boton_restar)
        self.layout.addWidget(self.boton_multiplicar)
        self.layout.addWidget(self.boton_dividir)
        self.layout.addWidget(self.boton_reiniciar)

        # Configurar el layout de la ventana
        self.setLayout(self.layout)

    def sumar(self):
        self.calcular("sumar")

    def restar(self):
        self.calcular("restar")

    def multiplicar(self):
        self.calcular("multiplicar")

    def dividir(self):
        self.calcular("dividir")

    def calcular(self, operacion):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            resultado = None

            if operacion == "sumar":
                resultado = num1 + num2
                self.display.setText(f"{num1} + {num2} = {resultado}")
            elif operacion == "restar":
                resultado = num1 - num2
                self.display.setText(f"{num1} - {num2} = {resultado}")
            elif operacion == "multiplicar":
                resultado = num1 * num2
                self.display.setText(f"{num1} * {num2} = {resultado}")
            elif operacion == "dividir":
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
                self.display.setText(f"{num1} / {num2} = {resultado}")

        except ZeroDivisionError:
            QMessageBox.critical(self, "Error", "No se puede dividir por cero.")
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese números válidos.")

    def reiniciar(self):
        self.display.clear()
        self.num1_input.clear()
        self.num2_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())

