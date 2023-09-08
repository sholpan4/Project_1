from calc_model import SimpleCalcModel
import math
class MathCalcModel(SimpleCalcModel):

    def command(self, key: str):
        if key in "()":
            self._display += key
        # elif key == "%":
        #     expression = self._display.replace('%', '/ 100')
        #     result = eval(expression)
        #     self.__display = str(result)
        elif key == "ctg":
            current_value = eval(self._display)
            result = 1 / math.tan(math.radians(current_value))
            self._display = str(result)
        elif key == "tg":
            current_value = eval(self._display)
            result = math.tan(math.radians(current_value))
            self._display = str(result)
        elif key == "cos":
            current_value = eval(self._display)
            result = math.cos(math.radians(current_value))
            self._display = str(result)
        elif key == "sin":
            current_value = eval(self._display)
            result = math.sin(math.radians(current_value))
            self._display = str(result)
        elif key == "x²":
            som = eval(self._display)
            result = som ** 2
            self._display = str(result)
        elif key == "|x|":
            current_value = eval(self._display)
            result = abs(current_value)
            self._display = str(result)
        elif key == "log":
            current_value = eval(self._display)
            result = math.log10(current_value)
            self._display = str(result)
        elif key == "x!":
            current_value = eval(self._display)
            if current_value < 0:
                print("Факториал определен только для неотрицательных целых чисел")
            else:
                result = math.factorial(current_value)
                self._display = str(result)
        elif key == "√x":
            current_value = eval(self._display)
            if current_value >= 0:
                result = math.sqrt(current_value)
                self._display = str(result)
        else:
            super().command(key)