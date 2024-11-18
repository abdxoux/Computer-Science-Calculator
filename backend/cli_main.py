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
