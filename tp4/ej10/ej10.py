import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor

class MemoryGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Juego de Memoria")
        self.setGeometry(100, 100, 600, 400)

        # Colores
        self.colors = [QColor("red"), QColor("green"), QColor("blue"), QColor("yellow"), QColor("cyan"), QColor("magenta")]
        self.hidden_color = QColor("gray")
        self.color_pairs = self.colors * 2
        random.shuffle(self.color_pairs)

        # Interfaz
        self.initUI()

    def initUI(self):
        # Contador de tiempo
        self.time_label = QLabel("Tiempo: 0", self)
        self.time_label.setGeometry(250, 10, 100, 30)
        
        # Crear el layout de la cuadrícula para las tarjetas
        self.grid_layout = QGridLayout()
        self.widget = QWidget(self)
        self.widget.setGeometry(50, 50, 500, 300)
        self.widget.setLayout(self.grid_layout)

        # Crear botón para iniciar
        self.start_button = QPushButton("Iniciar Partida", self)
        self.start_button.setGeometry(250, 360, 100, 30)
        self.start_button.clicked.connect(self.start_game)

        # Crear las tarjetas
        self.buttons = []
        for i in range(12):
            button = QPushButton("", self)
            button.setStyleSheet(f"background-color: {self.hidden_color.name()}")
            button.setFixedSize(100, 100)
            button.clicked.connect(self.handle_card_click)
            self.buttons.append(button)
            self.grid_layout.addWidget(button, i // 4, i % 4)

        # Temporizadores
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.time_count = 0

        # Variables de juego
        self.first_card = None
        self.second_card = None
        self.pairs_found = 0
        self.is_flipping_back = False
        self.game_started = False

    def start_game(self):
        # Resetear juego
        random.shuffle(self.color_pairs)
        for button in self.buttons:
            button.setText("")
            button.setStyleSheet(f"background-color: {self.hidden_color.name()}")

        # Reiniciar las variables
        self.time_count = 0
        self.time_label.setText("Tiempo: 0")
        self.pairs_found = 0
        self.first_card = None
        self.second_card = None
        self.is_flipping_back = False
        self.game_started = True

        # Comenzar el contador de tiempo
        self.timer.start(1000)

    def update_time(self):
        if self.game_started:
            self.time_count += 1
            self.time_label.setText(f"Tiempo: {self.time_count}")

    def handle_card_click(self):
        if self.is_flipping_back or not self.game_started:
            return  # Si las tarjetas están volteándose o el juego no ha comenzado, no permitir clicks

        button = self.sender()
        index = self.buttons.index(button)

        if button.text() != "" or (self.first_card == button):
            return  # Ignorar si ya se encontró la pareja o si es la misma tarjeta

        button.setStyleSheet(f"background-color: {self.color_pairs[index].name()}")

        if self.first_card is None:
            self.first_card = button
        else:
            self.second_card = button
            self.check_for_match()

    def check_for_match(self):
        first_index = self.buttons.index(self.first_card)
        second_index = self.buttons.index(self.second_card)

        if self.color_pairs[first_index] == self.color_pairs[second_index]:
            self.first_card.setText("✔")
            self.second_card.setText("✔")
            self.pairs_found += 1
            self.first_card = None
            self.second_card = None
            if self.pairs_found == 6:
                self.end_game()
        else:
            self.is_flipping_back = True
            QTimer.singleShot(1000, self.flip_back_cards)

    def flip_back_cards(self):
        # Asegurarse de que las tarjetas no sean None antes de intentar voltearlas
        if self.first_card and self.second_card:
            self.first_card.setStyleSheet(f"background-color: {self.hidden_color.name()}")
            self.second_card.setStyleSheet(f"background-color: {self.hidden_color.name()}")

        self.first_card = None
        self.second_card = None
        self.is_flipping_back = False

    def end_game(self):
        self.timer.stop()
        self.game_started = False
        QMessageBox.information(self, "¡Felicidades!", f"¡Has encontrado todos los pares en {self.time_count} segundos!")
        self.reset_game()

    def reset_game(self):
        # Resetear juego a su estado inicial
        random.shuffle(self.color_pairs)
        for button in self.buttons:
            button.setText("")
            button.setStyleSheet(f"background-color: {self.hidden_color.name()}")

        self.time_count = 0
        self.time_label.setText("Tiempo: 0")
        self.pairs_found = 0
        self.first_card = None
        self.second_card = None
        self.is_flipping_back = False
        self.game_started = False

app = QApplication(sys.argv)
game = MemoryGame()
game.show()
sys.exit(app.exec())
