import sys
from PyQt6.QtWidgets import *
from calc_main_window import CalcMainWindow
from calc_view import *
from calc_model import *
from calc_control import CalcControlWidget

options = {
    "Простой": {"model": SimpleCalcModel, "view": SimpleCalcView},
    "Бухгалтерский": {"model": AccountCalcModel, "view": AccountCalcView},
    # "Математический": {"model": MathCalcModel, "view": MathCalcView}
}

def swich_mode(name):
    if name in options:
        model = options[name]["model"]()
        view = options[name]["view"]()
        view.set_model(model)
        window.set_view(view)
        

# def swich_mode(name):
#     if name == 'Простой':
#         model = SimpleCalcModel()
#         view = SimpleCalcView()
#         view.set_model(model)
#         window.set_view(view)
        
#     if name == 'Бухгалтерский':
#         model = AccountCalcModel()
#         view = AccountCalcViev()
#         view.set_model(model)
#         window.set_view(view)
        
#     if name == 'Математический':
#         model = MathCalcModel()
#         view = MathCalcView()
#         view.set_model(model)
#         window.set_view(view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalcMainWindow('Qalculus v. 1.0')
    
    fb = open("style.css", encoding="utf-8")
    style = fb.read()
    fb.close()

    switch = CalcControlWidget()
    switch.switched.connect(swich_mode)
    window.set_switcher(switch)

    swich_mode("Простой")
    # view = SimpleCalcView()
    # model = SimpleCalcModel()
    # view.set_model(model)
    # window.set_view(view)
    
    window.show()
    app.setStyleSheet(style)
    app.exec()