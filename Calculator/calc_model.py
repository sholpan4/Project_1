class SimpleCalcModel:
    __display = ''

    def calculate(self):
        try:
            expression = self.__display.replace('%', '/ 100')
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
