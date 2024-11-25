import math

class Calculator:
    @staticmethod
    def calculate(num1, num2=None, operation="+"):

        try:
            num1 = float(num1)
            if operation != "root":
                num2 = float(num2) if num2 is not None else 0

            if operation == "+":
                return num1 + num2
            elif operation == "-":
                return num1 - num2
            elif operation == "*":
                return num1 * num2
            elif operation == "/":
                if num2 == 0:
                    return "Error: Division by zero!"
                return num1 / num2
            elif operation == "**":
                return num1 ** num2
            elif operation == "//":
                if num2 == 0:
                    return "Error: Division by zero!"
                return num1 // num2
            elif operation == "%":
                if num2 == 0:
                    return "Error: Division by zero!"
                return num1 % num2
            elif operation == "root":
                if num1 < 0:
                    return "Error: Negative number!"
                return math.sqrt(num1)
            else:
                return "Error: Invalid operation!"
        except ValueError:
            return "Error: Invalid input ! Please enter numbers only."
