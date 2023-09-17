class SimpleCalcModel:
    _display = '0'

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
                self._display = "0"
        elif key != "=":
            if key.isdigit():
                if self._display == "0":
                    self._display = key
                else:
                    self._display += key
            elif key == ".":
                if "." not in self._display:
                    self._display += key
            elif key in '()+-*/':
                if key == '(':
                    if self._display == '0':
                        self._display = key
                    elif self._display[-1] == '.':
                        self._display = self._display[:-1] + "*" + key
                    elif self._display[-1].isdigit() or self._display[-1] == ')':
                        self._display += "*" + key
                    else:
                        self._display += key
                elif key == ')':
                    if self._display[-1] == '(':
                        self._display += '0' + key
                    if self._display.count('(') > self._display.count(')'):
                        self._display += key
                elif self._display[-1] not in "+-*/":
                    self._display += key


        if key == "AC":
            self._display = "0"
        if key == "=":
            print(self._display)
            self.calculate()

    def get_display(self):
        return self._display


