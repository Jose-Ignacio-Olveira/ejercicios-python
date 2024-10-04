import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QButtonGroup, QMessageBox
from FormatoEEUU import FormatoEEUU
from FormatoArgentina import FormatoArgentina
from FechaInvalidaException import FechaInvalidaException
class FormateoGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formateo de Datos')

        # Layout principal
        layout = QVBoxLayout()

        # Campos para ingresar el dinero
        self.label_dinero = QLabel("Cantidad de dinero:")
        self.input_dinero = QLineEdit()
        layout.addWidget(self.label_dinero)
        layout.addWidget(self.input_dinero)

        # Campos para ingresar la fecha
        self.label_fecha = QLabel("Fecha (Día, Mes, Año):")
        self.input_dia = QLineEdit()
        self.input_mes = QLineEdit()
        self.input_anio = QLineEdit()
        layout.addWidget(self.label_fecha)
        layout.addWidget(self.input_dia)
        layout.addWidget(self.input_mes)
        layout.addWidget(self.input_anio)

        # Radio buttons para seleccionar el formato
        self.radio_eeuu = QRadioButton("Formato estadounidense")
        self.radio_arg = QRadioButton("Formato argentino")
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_eeuu)
        self.button_group.addButton(self.radio_arg)
        layout.addWidget(self.radio_eeuu)
        layout.addWidget(self.radio_arg)

        # Botón de formateo
        self.boton_formatear = QPushButton("Formatear")
        layout.addWidget(self.boton_formatear)

        # Etiquetas para mostrar los resultados
        self.label_resultado_moneda = QLabel("")
        self.label_resultado_fecha = QLabel("")
        layout.addWidget(self.label_resultado_moneda)
        layout.addWidget(self.label_resultado_fecha)

        # Conectar el botón a la función
        self.boton_formatear.clicked.connect(self.formatear_datos)

        # Configurar la ventana
        self.setLayout(layout)

    def formatear_datos(self):
        try:
            cantidad = float(self.input_dinero.text())
            dia = int(self.input_dia.text())
            mes = int(self.input_mes.text())
            anio = int(self.input_anio.text())

            # Validar fecha
            if dia < 1 or dia > 31 or mes < 1 or mes > 12:
                raise FechaInvalidaException()

            # Elegir el formato basado en el radio button
            if self.radio_eeuu.isChecked():
                formato = FormatoEEUU()
            elif self.radio_arg.isChecked():
                formato = FormatoArgentina()
            else:
                raise Exception("Seleccione un formato")

            # Mostrar resultados formateados
            self.label_resultado_moneda.setText(f"Moneda: {formato.formatear_moneda(cantidad)}")
            self.label_resultado_fecha.setText(f"Fecha: {formato.formatear_fecha(dia, mes, anio)}")

        except FechaInvalidaException as e:
            QMessageBox.critical(self, "Error", str(e))
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese valores numéricos válidos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

# Correr la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FormateoGUI()
    ventana.show()
    sys.exit(app.exec())
