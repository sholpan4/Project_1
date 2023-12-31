from calc_model import SimpleCalcModel
import math
class MathCalcModel(SimpleCalcModel):

    def command(self, key: str):
        if key == "ctg":
            current_value = eval(self._display)
            if math.sin(math.radians(current_value)) != 0:
                    result = 1 / math.tan(math.radians(current_value))
                    self._display = str(result)
            else:
                    print("Котангенс от нуля не определен")
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
        elif key == "log":
            current_value = eval(self._display)
            if current_value > 0:
                result = math.log10(current_value)
                self._display = str(result)
            else:
                print("Логарифм от нуля не определен")
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