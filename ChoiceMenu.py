class ChoiceMenu:
    def __init__(self):
        self.choices = ["xxxxx", "Number System Converter"]

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
