import sys
from PyQt6.QtWidgets import QApplication
from calc_main_window import CalcMainWindow
from calc_view import *
from calc_model import *
from calc_control import CalcControlWidget


def swich_mode(name):
    if name == "Account":
        model = AccountCalcModel()
        view = AccountCalcViev()
        view.set_model(model)
        window.set_view(view)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CalcMainWindow('Qalculus v. 1.0')
    view = SimpleCalcView()
    model = SimpleCalcModel()

    switch = CalcControlWidget()
    switch.switched.connect(swich_mode)
    window.set_switcher(switch)

    view.set_model(model)
    window.set_view(view)
    window.show()
    app.exec()

