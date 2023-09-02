import sys
from PyQt6.QtWidgets import QApplication
from calc_main_window import CalcMainWindow
from calc_view import SimpleCalcView
from calc_model import SimpleCalcModel


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CalcMainWindow('Qalculus v. 1.0')
    view = SimpleCalcView()
    model = SimpleCalcModel()
    view.set_model(model)
    window.set_view(view)
    window.show()
    app.exec()

