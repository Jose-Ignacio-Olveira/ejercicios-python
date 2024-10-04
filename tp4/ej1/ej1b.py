import sys
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox

class InputDialog(QWidget):
    def __init__(self):
        super().__init__()

        # Solicitar texto al usuario
        texto, ok = QInputDialog.getText(self, "Entrada de texto", "Ingrese algún texto:")

        # Mostrar el texto ingresado en un cuadro de diálogo
        if ok and texto:
            QMessageBox.information(self, "Texto ingresado", f"Usted ingresó: {texto}")
        else:
            QMessageBox.information(self, "Texto ingresado", "No se ingresó ningún texto.")

# Iniciar la aplicación
app = QApplication(sys.argv)
window = InputDialog()
sys.exit(app.exec())
