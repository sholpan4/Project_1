import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont



class SimpleCalcView(QWidget):
    calc_model = None

    def on_button_pressed(self):
        btn = self.sender()
        key_text = btn.text()
        self.calc_model.command(key_text)
        self.result_label.setText(self.calc_model.get_display())

    def keyPressEvent(self, event):
        key_text = event.text()
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

        buttons_layout = QGridLayout()
        main_layout.addLayout(buttons_layout)

        buttons = [
            ('AC', 0, 0), ('C', 0, 1), ('%', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            if text != '0':
                buttons_layout.addWidget(button, row, col)
            else:
                buttons_layout.addWidget(button,row,col,1,2)

            button.setFont(QFont('Monospace', 10, QFont.Weight.Normal, False))

            button.clicked.connect(self.on_button_pressed)
        self.setLayout(main_layout)

    def set_model(self, model):
        self.calc_model = model
        self.result_label.setText(self.calc_model.get_display())


class AccountCalcViev(SimpleCalcView):
    def __init__(self):
        super().__init__()
        keys_layout = QGridLayout()
        self.layout().addLayout(keys_layout)
        
        keys = ('(', ')', '%', '')

        for c in range(len(keys)):
            key = keys[c]
            if key:
                btn = QPushButton(text=key)
                btn.clicked.connect(self.on_button_pressed)
                if key != '%':
                    keys_layout.addWidget(btn, 0, c)
                else:
                    keys_layout.addWidget(btn, 0, c, 1, 2)