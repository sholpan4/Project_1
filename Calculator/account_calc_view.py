from PyQt6 import *
from calc_view import SimpleCalcView

class AccountCalcView(SimpleCalcView):
    buttons = [
            ('MS', 0, 0), ('MR', 0, 1), ('M+', 0, 2), ('M-', 0, 3),
            ('AC', 1, 0), ('MC', 1, 1), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
    ]


    def __init__(self):
        super().__init__()


        self.create_buttons(self.buttons)