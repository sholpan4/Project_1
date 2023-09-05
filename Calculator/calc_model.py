class SimpleCalcModel:
    __display = ''

    def calculate(self):
        try:
            expression = self.__display.replace('%', '/ 100') #будем убирать или оставим? для бухгалтерского отдельно нужно ли будет делать? ~
            result = eval(expression)
            self.__display = str(result)
        except SyntaxError:
            print("Некоректное выражение")
        self.get_display()

    def command(self, key: str):
        if key == "C":
            if len(self.__display) > 1:
                self.__display = self.__display[:-1]
            else:
                self.__display = "0"
        elif key != "=":
            if key.isdigit():
                if self.__display == "0":
                    self.__display = key
                else:
                    self.__display += key
            else:
                if self.__display[-1] not in "+-*/":
                    self.__display += key


        if key == "AC":
            self.__display = "0"
        if key == "=":
            print(self.__display)
            self.calculate()

    def get_display(self):
        return self.__display


class AccountCalcModel(SimpleCalcModel):
    def command(self, key: str):
        if key in "()":
            self._display += key
        elif key == "%":   #  3*7-1 => "3*7", "-100000000000.000"\
            last_value_index = max(self._display.rfind("-"),
                                   self._display.rfind("+"),
                                   self._display.rfind("*"),
                                   self._display.rfind("/"))
            if last_value_index < 0:
                return
            last_value = self._display[last_value_index:]
            self._display = self._display[:last_value_index]
            self.calculate()
            res1 = eval(f"{self._display}*{last_value}/100")
            self._display += str(res1)
        else:
            super().command(key)
            
            
class MathCalcModel(SimpleCalcModel):
    pass