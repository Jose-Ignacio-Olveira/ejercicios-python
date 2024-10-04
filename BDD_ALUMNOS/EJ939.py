from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
import sys


# Clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


# Clase Alumno (herencia de Persona)
class Alumno(Persona):
    def __init__(self, nombre, edad, matricula, carrera):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.carrera = carrera

    def __str__(self):
        return f"{super().__str__()}, Matrícula: {self.matricula}, Carrera: {self.carrera}"


# Base de Datos Alumnos
class BaseDeDatosAlumnos:
    def __init__(self):
        self.alumnos = []

    def alta(self, alumno):
        self.alumnos.append(alumno)

    def baja(self, matricula):
        alumno_a_borrar = self.buscar(matricula)
        if alumno_a_borrar:
            self.alumnos.remove(alumno_a_borrar)
            return True
        return False

    def modificar(self, matricula, nombre=None, edad=None, carrera=None):
        alumno = self.buscar(matricula)
        if alumno:
            if nombre:
                alumno.nombre = nombre
            if edad:
                alumno.edad = edad
            if carrera:
                alumno.carrera = carrera
            return True
        return False

    def buscar(self, matricula):
        for alumno in self.alumnos:
            if alumno.matricula == matricula:
                return alumno
        return None

    def listar(self):
        return self.alumnos


# Interfaz gráfica con PyQt6
class InterfazBaseDatos(QWidget):
    def __init__(self):
        super().__init__()

        self.db = BaseDeDatosAlumnos()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Base de Datos de Alumnos")

        # Layouts
        vbox = QVBoxLayout()

        # Labels y Entry fields
        hbox1 = QHBoxLayout()
        self.lbl_nombre = QLabel("Nombre")
        self.nombre = QLineEdit()
        hbox1.addWidget(self.lbl_nombre)
        hbox1.addWidget(self.nombre)

        hbox2 = QHBoxLayout()
        self.lbl_edad = QLabel("Edad")
        self.edad = QLineEdit()
        hbox2.addWidget(self.lbl_edad)
        hbox2.addWidget(self.edad)

        hbox3 = QHBoxLayout()
        self.lbl_matricula = QLabel("Matrícula")
        self.matricula = QLineEdit()
        hbox3.addWidget(self.lbl_matricula)
        hbox3.addWidget(self.matricula)

        hbox4 = QHBoxLayout()
        self.lbl_carrera = QLabel("Carrera")
        self.carrera = QLineEdit()
        hbox4.addWidget(self.lbl_carrera)
        hbox4.addWidget(self.carrera)

        # Botones
        hbox5 = QHBoxLayout()
        self.btn_alta = QPushButton("Alta", self)
        self.btn_alta.clicked.connect(self.alta)
        self.btn_baja = QPushButton("Baja", self)
        self.btn_baja.clicked.connect(self.baja)
        self.btn_modificar = QPushButton("Modificar", self)
        self.btn_modificar.clicked.connect(self.modificar)
        hbox5.addWidget(self.btn_alta)
        hbox5.addWidget(self.btn_baja)
        hbox5.addWidget(self.btn_modificar)

        # Botón de Listar
        self.btn_listar = QPushButton("Listar", self)
        self.btn_listar.clicked.connect(self.listar)

        # Caja de texto para mostrar los alumnos
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)

        # Añadir los layouts
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addWidget(self.btn_listar)
        vbox.addWidget(self.output_text)

        # Establecer el layout principal
        self.setLayout(vbox)

    # Funciones de los botones
    def alta(self):
        nombre = self.nombre.text()
        edad = self.edad.text()
        matricula = self.matricula.text()
        carrera = self.carrera.text()

        if nombre and edad and matricula and carrera:
            try:
                alumno = Alumno(nombre, int(edad), matricula, carrera)
                self.db.alta(alumno)
                self.mostrar_mensaje("Alta", "Alumno registrado con éxito")
                self.limpiar_campos()
            except ValueError:
                self.mostrar_mensaje("Error", "Edad debe ser un número")
        else:
            self.mostrar_mensaje("Error", "Por favor, completa todos los campos")

    def baja(self):
        matricula = self.matricula.text()
        if matricula:
            if self.db.baja(matricula):
                self.mostrar_mensaje("Baja", "Alumno eliminado con éxito")
            else:
                self.mostrar_mensaje("Error", "Alumno no encontrado")
        else:
            self.mostrar_mensaje("Error", "Por favor, ingresa una matrícula")

    def modificar(self):
        matricula = self.matricula.text()
        nombre = self.nombre.text()
        edad = self.edad.text()
        carrera = self.carrera.text()

        if matricula:
            try:
                if self.db.modificar(matricula, nombre, int(edad) if edad else None, carrera):
                    self.mostrar_mensaje("Modificar", "Alumno modificado con éxito")
                else:
                    self.mostrar_mensaje("Error", "Alumno no encontrado")
            except ValueError:
                self.mostrar_mensaje("Error", "Edad debe ser un número")
        else:
            self.mostrar_mensaje("Error", "Por favor, ingresa una matrícula para modificar")

    def listar(self):
        self.output_text.clear()
        alumnos = self.db.listar()
        if alumnos:
            for alumno in alumnos:
                self.output_text.append(str(alumno))
        else:
            self.output_text.append("No hay alumnos registrados")

    def mostrar_mensaje(self, titulo, mensaje):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.exec()

    def limpiar_campos(self):
        self.nombre.clear()
        self.edad.clear()
        self.matricula.clear()
        self.carrera.clear()


# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InterfazBaseDatos()
    ventana.show()
    sys.exit(app.exec())
