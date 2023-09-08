class SimpleCalcModel:
    _display = ''

    def calculate(self):
        try:
            expression = self._display
            result = eval(expression)
            self._display = str(result)
        except SyntaxError:
            print("Некоректное выражение")
        self.get_display()

    def command(self, key: str):
        if key == "C":
            if len(self._display) > 1:
                self._display = self._display[:-1]
            else:
                self._display = ""
        elif key != "=":
            if key.isdigit():
                if self._display == "0":
                    self._display = key
                else:
                    self._display += key
            else:
                if self._display[-1] not in "+-*/":
                    self._display += key


        if key == "AC":
            self._display = ""
        if key == "=":
            print(self._display)
            self.calculate()

    def get_display(self):
        return self._display



