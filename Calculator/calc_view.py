import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class SimpleCalcView(QWidget):
    calc_model = None

    buttons = [
        ('AC', 0, 0), ('C', 0, 1), ('.', 0, 2), ('/', 0, 3),
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
        ('0', 4, 0), ('(',4,1),(')', 4, 2), ('=', 4, 3)
    ]

    def on_button_pressed(self):
        btn = self.sender()
        key_text = btn.text()
        self.calc_model.command(key_text)
        self.result_label.setText(self.calc_model.get_display())

    def keyPressEvent(self, event):
        print(event.key(), Qt.Key.Key_Backspace)
        key_text = event.text()
        if event.key() == Qt.Key.Key_Backspace:
            key_text = 'C'
        elif event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            key_text = '='

        self.calc_model.command(key_text)
        self.result_label.setText(self.calc_model.get_display())

    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        self.result_label = QLabel("0")
        self.result_label.setFont(QFont('Monospace', 20, QFont.Weight.Normal, False))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.result_label)


        main_layout.addLayout(self.create_buttons(self.buttons))
        self.setLayout(main_layout)


    def create_buttons(self, buttons):

        buttons_layout = QGridLayout()
        for (text, row, col) in buttons:
            button = QPushButton(text)
            buttons_layout.addWidget(button, row, col)

            button.setFont(QFont('Monospace', 10, QFont.Weight.Normal, False))

            button.clicked.connect(self.on_button_pressed)

        return buttons_layout


    def set_model(self, model):
        self.calc_model = model
        self.result_label.setText(self.calc_model.get_display())
