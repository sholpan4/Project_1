from PyQt6 import *
from calc_view import SimpleCalcView

class AccountCalcView(SimpleCalcView):
    buttons = [
        ('MC', 0, 0), ('MR', 0, 1), ("M+", 0, 2), ('/', 0, 3),
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
        ('0', 4, 0), ('.', 4, 2), ('=', 4, 3)
    ]


    def __init__(self):
        super().__init__()


        self.create_buttons(self.buttons)