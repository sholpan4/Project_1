from PyQt6 import *
from calc_view import SimpleCalcView

class MathCalcView(SimpleCalcView):
    buttons = [
        ('AC', 0, 0), ('C', 0, 1), ('|x|', 0, 2), ('√x', 0, 3),
        ('sin', 1, 0), ('cos', 1, 1), ('tg', 1, 2), ('ctg', 1, 3),
        ('log', 2, 0), ('x!', 2, 1), ('x²', 2, 2), ('/', 2, 3),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
        ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
        ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
        ('0', 6, 0), ('.', 6, 2), ('=', 6, 3)
    ]

    def __init__(self):
        super().__init__()

        self.create_buttons(self.buttons)
