from Login import Login
from ChoiceMenu import ChoiceMenu
from NumberSystemConverter import NumberSystemConverter
from IpPlanner import IPPlanner
from Calculator import Calculator


def main():
    login = Login()
    while True:
        print("\n1. Login")
        print("2. Register")
        print("0. Exit") # Add exit option

        login_choice = input("Choose an option: ")

        if login_choice == "0":
            print("Exiting the program...")
            return  # Exit the entire program

        if login_choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            result = login.authenticate(username, password)
            if result is True:
                print("Login successful!")
                break
            else:
                print(result)

        elif login_choice == "2":
            username = input("Enter username for registration: ")
            password = input("Enter password for registration: ")
            result = login.register(username, password)
            print(result)  # Print registration success/failure message

        else:
            print("Invalid login choice. Please try again.")



    menu = ChoiceMenu()
    converter = NumberSystemConverter()
    ip_planner = IPPlanner()
    calculator = Calculator()

    while True:
        choice = menu.get_choice()

        if choice == "0":
            print("Exiting the program...")
            break
        elif choice == "1":
            ip_planner.run()
        elif choice == "2":
            converter.run()
        elif choice == "3":
            calculator.run()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
