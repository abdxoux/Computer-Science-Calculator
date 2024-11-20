## Project: Computer-Science-Calculator

### Overview
This project is a utility application that includes functionalities such as IP planning and number system conversion. It has both a graphical user interface (GUI) and a command-line interface (CLI).

### Files and Structure
- `main.py`: The main entry point for the GUI application.
- `backend/ChoiceMenu.py`: Handles the main menu choices for the CLI.
- `backend/cli_main.py`: The main entry point for the CLI application.
- `backend/IpPlanner.py`: Contains the logic for IP planning.
- `backend/Login.py`: Handles user authentication.
- `backend/NumberSystemConverter.py`: Contains the logic for number system conversion.

  ## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, and division.
- **Advanced Functions**: Trigonometric functions, logarithms, exponentiation.
- **Computer Science Utilities**: Binary, hexadecimal conversions, bitwise operations.
- **User-Friendly Interface**: Easy-to-use command-line interface for quick calculations.


## Installation

To run the calculator locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/abdxoux/Computer-Science-Calculator.git
    cd Computer-Science-Calculator
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the calculator, simply run:
```bash
python calculator.py
```


### Code Explanation

#### `main.py`
This file initializes the GUI application using `tkinter`. It manages different pages such as login, main menu, IP planner, and number system converter.

```python
import tkinter as tk
from tkinter import ttk
from Login import Login
from ChoiceMenu import ChoiceMenu
from NumberSystemConverter import NumberSystemConverter
from IpPlanner import IPPlanner

class PageManager(tk.Tk):
    """Manages all pages in the application."""
    def __init__(self):
        super().__init__()
        self.title("Utility Application")
        self.geometry("450x600")
        self.configure(bg="#FFFFFF")  # Set white background

        # Container for all frames
        self.container = tk.Frame(self, bg="#FFFFFF")
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Initialize all pages
        for F in (LoginPage, MainMenuPage, IPPlannerPage, NumberSystemConverterPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show Login Page first
        self.show_frame(LoginPage)

    def show_frame(self, page_class):
        """Show a frame for the given page class."""
        frame = self.frames[page_class]
        frame.tkraise()
```

#### `backend/ChoiceMenu.py`
This file handles the main menu choices for the CLI.

```python
class ChoiceMenu:
    def __init__(self):
        self.choices = ["IP planner", "Number System Converter"]

    def display_choices(self):
        print("\nMain Menu:")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"{idx}. {choice}")
        print("0. Exit")

    def get_choice(self):
        while True:
            self.display_choices()
            choice = input("Choose an option: ")
            if choice in {"1", "2", "0"}:
                return choice
            else:
                print("Invalid choice! Please try again.")
```

#### `backend/cli_main.py`
This file is the main entry point for the CLI application.

```python
from Login import Login
from ChoiceMenu import ChoiceMenu
from NumberSystemConverter import NumberSystemConverter
from IpPlanner import IPPlanner

def main():
    login = Login()
    if not login.authenticate():
        return

    menu = ChoiceMenu()
    converter = NumberSystemConverter()
    ip_planner = IPPlanner()

    while True:
        choice = menu.get_choice()
        if choice == "0":
            print("Exiting the program...")
            break
        elif choice == "1":
            ip_planner.run()
        elif choice == "2":
            converter.run()

if __name__ == "__main__":
    main()
```

#### `backend/IpPlanner.py`
This file contains the logic for IP planning.

```python
import ipaddress

class IPPlanner:
    @staticmethod
    def compute_ip_details(network, subnet_mask):
        try:
            network_address = ipaddress.IPv4Network(f"{network}/{subnet_mask}", strict=False)
            return {
                "Network Address": str(network_address.network_address),
                "Broadcast Address": str(network_address.broadcast_address),
                "Number of available Hosts": len(list(network_address.hosts())),
                "Available Hosts": list(network_address.hosts())
            }
        except ValueError as e:
            return str(e)

    @staticmethod
    def menu():
        print("\nIP Planner")
        print("Enter network address and subnet mask to calculate details.")

    def run(self):
        while True:
            self.menu()
            network = input("Enter Network Address (ex: 192.168.1.0): ")
            subnet_mask = input("Enter Subnet Mask (ex: 24): ")

            result = self.compute_ip_details(network, subnet_mask)
            if isinstance(result, dict):
                print("\n--- IP Details ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            else:
                print(f"Error: {result}")

            choice = input("Do you want to calculate again? (yes/no): ")
            if choice.lower() != 'yes':
                break
```

#### `backend/Login.py`
This file handles user authentication.

```python
import getpass

class Login:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def authenticate(self):
        print("Login Required")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == self.username and password == self.password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password!")
            return False
```

#### `backend/NumberSystemConverter.py`
This file contains the logic for number system conversion.

```python
class NumberSystemConverter:
    def __init__(self):
        self.choiz = {
            "1": (10, 2), "2": (10, 8), "3": (10, 16),
            "4": (2, 10), "5": (2, 8), "6": (2, 16),
            "7": (8, 10), "8": (8, 2), "9": (8, 16),
            "10": (16, 10), "11": (16, 2), "12": (16, 8)
        }

    @staticmethod
    def convert_number(value, from_base, to_base):
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
```

---

This structured representation should help you present your project to your teacher effectively.
## Contact

For questions or suggestions, feel free to open an issue or contact the repository owner.
