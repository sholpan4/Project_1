from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class CalcControlWidget(QWidget):
    switched = pyqtSignal(str)

    def calc_mode_switch(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            text = radiobtn.text()
            self.switched.emit(text)

    def __init__(self, options):
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        for i in range(len(options)):
            radiobutton = QRadioButton(text=options[i])
            radiobutton.toggled.connect(self.calc_mode_switch)
            main_layout.addWidget(radiobutton)

            if i == 0:
                radiobutton.setChecked(True)