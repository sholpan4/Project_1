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
    "Математический": {"model": MathCalcModel, "view": MathCalcView},
    "Математический Стиль": {"style": "Calculator/MathStyle.css"},
    "Бухгалтерский Стиль": {"style": "Calculator/AccStyle.css"}
}


def swich_mode(name):
    if "Стиль" in name:
        with open(options[name]["style"], "r", encoding='utf-8') as file:
            app.setStyleSheet(file.read())
    else:
        if name in options:
            model = options[name]["model"]()
            view = options[name]["view"]()
            view.set_model(model)
            window.set_view(view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalcMainWindow('Qalculus v. 1.0')

    switch = CalcControlWidget(tuple(options.keys()))
    switch.switched.connect(swich_mode)
    window.set_switcher(switch)

    swich_mode("Простой")
    
    window.show()
    app.exec()