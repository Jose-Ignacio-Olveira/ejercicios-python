import sys
import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox

class FileCopyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Copiar Archivo')
        self.setGeometry(100, 100, 400, 200)
        
        # Layout principal
        layout = QVBoxLayout()

        # Etiquetas para mostrar el archivo seleccionado y la ubicación de destino
        self.file_label = QLabel('Archivo seleccionado: Ninguno', self)
        self.dest_label = QLabel('Ubicación de destino: Ninguna', self)
        
        # Botón para seleccionar un archivo
        self.select_file_button = QPushButton('Seleccionar Archivo', self)
        self.select_file_button.clicked.connect(self.select_file)

        # Botón para seleccionar una ubicación de destino
        self.select_dest_button = QPushButton('Seleccionar Ubicación de Destino', self)
        self.select_dest_button.clicked.connect(self.select_destination)

        # Botón para copiar el archivo
        self.copy_button = QPushButton('Copiar Archivo', self)
        self.copy_button.clicked.connect(self.copy_file)
        self.copy_button.setEnabled(False)  # Deshabilitar hasta que se seleccionen ambos

        # Agregar widgets al layout
        layout.addWidget(self.file_label)
        layout.addWidget(self.select_file_button)
        layout.addWidget(self.dest_label)
        layout.addWidget(self.select_dest_button)
        layout.addWidget(self.copy_button)

        # Configurar el layout en la ventana
        self.setLayout(layout)

    def select_file(self):
        # Abrir un cuadro de diálogo para seleccionar un archivo
        file_path, _ = QFileDialog.getOpenFileName(self, 'Seleccionar Archivo')

        if file_path:
            self.file_path = file_path
            self.file_label.setText(f'Archivo seleccionado: {file_path}')
            self.check_ready_to_copy()

    def select_destination(self):
        # Abrir un cuadro de diálogo para seleccionar una carpeta de destino
        dest_path = QFileDialog.getExistingDirectory(self, 'Seleccionar Ubicación de Destino')

        if dest_path:
            self.dest_path = dest_path
            self.dest_label.setText(f'Ubicación de destino: {dest_path}')
            self.check_ready_to_copy()

    def check_ready_to_copy(self):
        # Habilitar el botón de copia si ambos (archivo y destino) están seleccionados
        if hasattr(self, 'file_path') and hasattr(self, 'dest_path'):
            self.copy_button.setEnabled(True)

    def copy_file(self):
        try:
            # Copiar el archivo a la ubicación de destino
            shutil.copy(self.file_path, self.dest_path)
            QMessageBox.information(self, 'Éxito', 'Archivo copiado exitosamente.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'No se pudo copiar el archivo: {e}')

# Iniciar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileCopyApp()
    window.show()
    sys.exit(app.exec())
