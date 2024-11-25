class NumberSystemConverter:
    def __init__(self):
        self.choose = {
            "1": (10, 2), "2": (10, 8), "3": (10, 16),
            "4": (2, 10), "5": (2, 8), "6": (2, 16),
            "7": (8, 10), "8": (8, 2), "9": (8, 16),
            "10": (16, 10), "11": (16, 2), "12": (16, 8)
        }
    @staticmethod
    def convert_number( value, from_base,to_base):

        decimal_value = int(value, from_base)
        if to_base == 2:
            return bin(decimal_value)[2:]
        elif to_base == 8:
            return oct(decimal_value)[2:]
        elif to_base == 16:
            return hex(decimal_value)[2:]
        elif to_base == 10:
            return str(decimal_value)
        else:
            raise ValueError("Invalid base.")
    @staticmethod
    def menu():
        options = ["Number System Converter", "1. Decimal to Binary", "2. Decimal to Octal",
            "3. Decimal to Hexadecimal", "4. Binary to Decimal", "5. Binary to Octal", "6. Binary to Hexadecimal",
            "7. Octal to Decimal", "8. Octal to Binary", "9. Octal to Hexadecimal", "10. Hexadecimal to Decimal",
            "11. Hexadecimal to Binary", "12. Hexadecimal to Octal", "0. Back to Main Menu"]
        for option in options:
            print(option)

    def run(self):
        while True:
            self.menu()
            choice = input("Choose an option: ")
            if choice == "0":
                print("Returning to Main Menu...")
                break
            if choice in self.choose:
                from_base, to_base = self.choose[choice]
                number = input(f"Enter a number in base {from_base}: ")
                try:
                    result = self.convert_number(number, from_base, to_base)
                    print(f"Converted result (base {to_base}): {result}")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            else:
                print("Invalid choice! Please try again.")
