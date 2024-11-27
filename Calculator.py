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
    def run(self):
        while True:
            try:
                num1 = float(input("Enter first number: "))
                operation = input("Enter operation (+, -, *, /, **, //, %, root): ")
                if operation != "root":
                    num2 = float(input("Enter second number: "))
                else:
                    num2 = None
                result = self.calculate(num1, num2, operation)
                print(f"Result: {result}")
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except Exception as e:
                print(f"Error: {e}")