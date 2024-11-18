class NumberSystemConverter:
    def __init__(self):
        self.choiz = {
            "1": (10, 2), "2": (10, 8), "3": (10, 16),
            "4": (2, 10), "5": (2, 8), "6": (2, 16),
            "7": (8, 10), "8": (8, 2), "9": (8, 16),
            "10": (16, 10), "11": (16, 2), "12": (16, 8)
        }
    @staticmethod
    def convert_number( value, from_base, to_base):

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
        print("\nNumber System Converter")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Binary to Octal")
        print("6. Binary to Hexadecimal")
        print("7. Octal to Decimal")
        print("8. Octal to Binary")
        print("9. Octal to Hexadecimal")
        print("10. Hexadecimal to Decimal")
        print("11. Hexadecimal to Binary")
        print("12. Hexadecimal to Octal")
        print("0. Back to Main Menu")

    def run(self):
        while True:
            self.menu()
            choice = input("Choose an option: ")
            if choice == "0":
                print("Returning to Main Menu...")
                break
            if choice in self.choiz:
                from_base, to_base = self.choiz[choice]
                number = input(f"Enter a number in base {from_base}: ")
                try:
                    result = self.convert_number(number, from_base, to_base)
                    print(f"Converted result (base {to_base}): {result}")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            else:
                print("Invalid choice! Please try again.")
