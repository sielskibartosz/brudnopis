import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from PySide6.QtGui import QColor

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moja interaktywna apka w PySide")
        self.resize(400, 300)

        # Licznik kliknięć
        self.click_count = 0

        # Etykieta powitalna
        self.label = QLabel("Wpisz swoje imię i kliknij przycisk", self)

        # Pole tekstowe do wpisania imienia
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Twoje imię")

        # Przycisk 1 - personalizowany komunikat
        self.button1 = QPushButton("Kliknij mnie")
        self.button1.clicked.connect(self.on_button_click)

        # Przycisk 2 - zmienia kolor etykiety losowo
        self.button2 = QPushButton("Zmień kolor etykiety")
        self.button2.clicked.connect(self.change_label_color)

        # Układ dla przycisków
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)

        # Układ główny
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_input)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def on_button_click(self):
        name = self.name_input.text().strip() or "Nieznajomy"
        self.click_count += 1
        self.label.setText(f"Cześć, {name}! Kliknąłeś {self.click_count} razy!")

    def change_label_color(self):
        # Losowy kolor RGB
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = QColor(r, g, b)
        self.label.setStyleSheet(f"color: {color.name()}; font-weight: bold;")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec())
