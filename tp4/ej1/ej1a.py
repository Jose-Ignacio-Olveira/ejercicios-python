import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox

class ConfirmDialog(QWidget):
    def __init__(self):
        super().__init__()

        # Crear y mostrar el cuadro de diálogo de confirmación
        respuesta = QMessageBox.question(
            self, 
            "Confirmación", 
            "¿Está seguro que quiere dar de baja al usuario?", 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        # Verificar la respuesta
        if respuesta == QMessageBox.StandardButton.Yes:
            print("Usuario dado de baja.")
        else:
            print("Acción cancelada.")

# Iniciar la aplicación
app = QApplication(sys.argv)
window = ConfirmDialog()
sys.exit(app.exec())
