import sys
from PyQt6.QtWidgets import *
from calc_main_window import CalcMainWindow
from calc_view import *
from calc_model import *
from calc_control import CalcControlWidget
from math_calc_view import *
from math_calc_model import *
from account_calc_view import *
from account_calc_model import *


options = {
    "Простой": {"model": SimpleCalcModel, "view": SimpleCalcView},
    "Бухгалтерский": {"model": AccountCalcModel, "view": AccountCalcView},
    "Математический": {"model": MathCalcModel, "view": MathCalcView}
}


def swich_mode(name):
    if name in options:
        model = options[name]["model"]()
        view = options[name]["view"]()
        view.set_model(model)
        window.set_view(view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalcMainWindow('Qalculus v. 1.0')
    
    fb = open("Calculator/style.css", 'r', encoding="utf-8")
    style = fb.read()
    fb.close()


    switch = CalcControlWidget(tuple(options.keys()))
    switch.switched.connect(swich_mode)
    window.set_switcher(switch)

    swich_mode("Простой")
    
    window.show()
    app.setStyleSheet(style)
    app.exec()