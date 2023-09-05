from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class CalcControlWidget(QWidget):
    switched = pyqtSignal(str)

    def calc_mode_switch(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            text = radiobtn.text()
            self.switched.emit(text)

    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setLayout(main_layout)

        label = QLabel('Выберите вид: ')
        
        rb_simple = QRadioButton(text='Простой')
        rb_simple.setChecked(True)
        rb_simple.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(rb_simple)

        rb_account = QRadioButton(text='Бухгалтерский')
        rb_account.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(rb_account)