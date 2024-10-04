import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox, QFileDialog
)
from PyQt6.QtGui import QPixmap


# Clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Clase Alumno hereda de Persona
class Alumno(Persona):
    def __init__(self, nombre, edad, matricula, carrera, imagen=""):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.carrera = carrera
        self.imagen = imagen


# Simulación de Base de Datos en memoria
class BaseDeDatosAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar(self, alumno):
        self.alumnos.append(alumno)

    def eliminar(self, alumno):
        self.alumnos.remove(alumno)

    def modificar(self, alumno, nuevos_datos):
        alumno.nombre = nuevos_datos['nombre']
        alumno.edad = nuevos_datos['edad']
        alumno.matricula = nuevos_datos['matricula']
        alumno.carrera = nuevos_datos['carrera']
        alumno.imagen = nuevos_datos['imagen']

    def listar(self, filtro_nombre="", filtro_matricula="", filtro_carrera=""):
        resultado = []
        for alumno in self.alumnos:
            if (filtro_nombre.lower() in alumno.nombre.lower() and
                filtro_matricula in alumno.matricula and
                filtro_carrera.lower() in alumno.carrera.lower()):
                resultado.append(alumno)
        return resultado


# Ventana de alta de alumno
class VentanaAltaAlumno(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Alta de Alumno")
        layout = QVBoxLayout()

        self.lbl_nombre = QLabel("Nombre:")
        self.nombre = QLineEdit()

        self.lbl_edad = QLabel("Edad:")
        self.edad = QLineEdit()

        self.lbl_matricula = QLabel("Matrícula:")
        self.matricula = QLineEdit()

        self.lbl_carrera = QLabel("Carrera:")
        self.carrera = QLineEdit()

        self.lbl_imagen = QLabel("Imagen:")
        self.imagen = QLabel()

        # Botón para seleccionar imagen
        self.btn_imagen = QPushButton("Seleccionar Imagen")
        self.btn_imagen.clicked.connect(self.seleccionar_imagen)

        # Botón de alta
        self.btn_alta = QPushButton("Alta")
        self.btn_alta.clicked.connect(self.alta)

        layout.addWidget(self.lbl_nombre)
        layout.addWidget(self.nombre)
        layout.addWidget(self.lbl_edad)
        layout.addWidget(self.edad)
        layout.addWidget(self.lbl_matricula)
        layout.addWidget(self.matricula)
        layout.addWidget(self.lbl_carrera)
        layout.addWidget(self.carrera)
        layout.addWidget(self.lbl_imagen)
        layout.addWidget(self.imagen)
        layout.addWidget(self.btn_imagen)
        layout.addWidget(self.btn_alta)

        self.setLayout(layout)

    def seleccionar_imagen(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Images (*.png *.jpg *.bmp)")
        if filename:
            self.imagen.setPixmap(QPixmap(filename).scaled(100, 100))
            self.ruta_imagen = filename
        else:
            self.ruta_imagen = ""

    def alta(self):
        nombre = self.nombre.text()
        edad = self.edad.text()
        matricula = self.matricula.text()
        carrera = self.carrera.text()
        imagen = getattr(self, 'ruta_imagen', "")

        if not nombre or not edad or not matricula or not carrera:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        nuevo_alumno = Alumno(nombre, edad, matricula, carrera, imagen)
        self.db.agregar(nuevo_alumno)
        self.accept()


# Ventana de detalles del alumno
class VentanaAlumno(QDialog):
    def __init__(self, alumno, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.alumno = alumno
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"Detalles de {self.alumno.nombre}")
        layout = QVBoxLayout()

        self.lbl_nombre = QLabel(f"Nombre: {self.alumno.nombre}")
        self.lbl_edad = QLabel(f"Edad: {self.alumno.edad}")
        self.lbl_matricula = QLabel(f"Matrícula: {self.alumno.matricula}")
        self.lbl_carrera = QLabel(f"Carrera: {self.alumno.carrera}")

        self.lbl_imagen = QLabel()
        if self.alumno.imagen:
            self.lbl_imagen.setPixmap(QPixmap(self.alumno.imagen).scaled(100, 100))

        self.btn_modificar = QPushButton("Modificar")
        self.btn_modificar.clicked.connect(self.modificar_alumno)

        self.btn_baja = QPushButton("Dar de Baja")
        self.btn_baja.clicked.connect(self.baja_alumno)

        layout.addWidget(self.lbl_nombre)
        layout.addWidget(self.lbl_edad)
        layout.addWidget(self.lbl_matricula)
        layout.addWidget(self.lbl_carrera)
        layout.addWidget(self.lbl_imagen)
        layout.addWidget(self.btn_modificar)
        layout.addWidget(self.btn_baja)

        self.setLayout(layout)

    def modificar_alumno(self):
        nuevos_datos = {
            'nombre': self.alumno.nombre,
            'edad': self.alumno.edad,
            'matricula': self.alumno.matricula,
            'carrera': self.alumno.carrera,
            'imagen': self.alumno.imagen
        }
        ventana_modificar = VentanaAltaAlumno(self.db, self)
        if ventana_modificar.exec():
            self.db.modificar(self.alumno, nuevos_datos)
            self.accept()

    def baja_alumno(self):
        self.db.eliminar(self.alumno)
        self.accept()


# Ventana de búsqueda avanzada
class VentanaBusquedaAvanzada(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Búsqueda Avanzada")

        layout = QVBoxLayout()

        self.lbl_nombre = QLabel("Nombre:")
        self.filtro_nombre = QLineEdit()

        self.lbl_matricula = QLabel("Matrícula:")
        self.filtro_matricula = QLineEdit()

        self.lbl_carrera = QLabel("Carrera:")
        self.filtro_carrera = QLineEdit()

        self.btn_buscar = QPushButton("Buscar")
        self.btn_buscar.clicked.connect(self.buscar)

        layout.addWidget(self.lbl_nombre)
        layout.addWidget(self.filtro_nombre)
        layout.addWidget(self.lbl_matricula)
        layout.addWidget(self.filtro_matricula)
        layout.addWidget(self.lbl_carrera)
        layout.addWidget(self.filtro_carrera)
        layout.addWidget(self.btn_buscar)

        self.setLayout(layout)

    def buscar(self):
        filtro_nombre = self.filtro_nombre.text()
        filtro_matricula = self.filtro_matricula.text()
        filtro_carrera = self.filtro_carrera.text()

        alumnos = self.db.listar(filtro_nombre=filtro_nombre,
                                 filtro_matricula=filtro_matricula,
                                 filtro_carrera=filtro_carrera)

        self.parent().lista_alumnos.clear()
        for alumno in alumnos:
            item = QListWidgetItem(f"{alumno.nombre} ({alumno.matricula})")
            item.setData(1, alumno)
            self.parent().lista_alumnos.addItem(item)

        self.accept()


# Ventana principal
class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.db = BaseDeDatosAlumnos()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Alumnos")

        layout = QVBoxLayout()

        self.lbl_filtro = QLabel("Buscar:")
        self.filtro = QLineEdit()
        self.filtro.textChanged.connect(self.actualizar_lista)

        self.lista_alumnos = QListWidget()
        self.lista_alumnos.itemDoubleClicked.connect(self.ver_alumno)

        self.btn_alta = QPushButton("Dar de Alta")
        self.btn_alta.clicked.connect(self.alta_alumno)

        self.btn_busqueda_avanzada = QPushButton("Búsqueda Avanzada")
        self.btn_busqueda_avanzada.clicked.connect(self.busqueda_avanzada)

        layout.addWidget(self.lbl_filtro)
        layout.addWidget(self.filtro)
        layout.addWidget(self.lista_alumnos)
        layout2= QHBoxLayout()
        layout.addLayout(layout2)
        layout2.addWidget(self.btn_busqueda_avanzada)
        layout2.addWidget(self.btn_alta)

        self.setLayout(layout)
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_alumnos.clear()

        texto_filtro = self.filtro.text().lower()
        alumnos = self.db.listar()

        for alumno in alumnos:
            if (texto_filtro in alumno.nombre.lower() or
                texto_filtro in alumno.matricula or
                texto_filtro in alumno.carrera.lower()):
                item = QListWidgetItem(f"{alumno.nombre} ({alumno.matricula})")
                item.setData(1, alumno)
                self.lista_alumnos.addItem(item)

    def alta_alumno(self):
        ventana_alta = VentanaAltaAlumno(self.db, self)
        if ventana_alta.exec():
            self.actualizar_lista()

    def ver_alumno(self, item):
        alumno = item.data(1)
        ventana_alumno = VentanaAlumno(alumno, self.db, self)
        if ventana_alumno.exec():
            self.actualizar_lista()

    def busqueda_avanzada(self):
        ventana_busqueda = VentanaBusquedaAvanzada(self.db, self)
        ventana_busqueda.exec()
        self.actualizar_lista()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())

