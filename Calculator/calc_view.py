from PyQt6.QtWidgets import *


class SimpleCalcView(QWidget):
    main_display: QLabel = None

    def __init__(self):
        super().__init__()
        central_widget = QWidget()

        main_layout = QVBoxLayout(central_widget)

        result_label = QLabel("0")
        main_layout.addWidget(result_label)

        buttons_layout = QGridLayout()
        main_layout.addLayout(buttons_layout)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            buttons_layout.addWidget(button, row, col)

        self.setLayout(main_layout)