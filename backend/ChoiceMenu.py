class ChoiceMenu:
    def __init__(self):
        self.choices = ["IP Planner", "Number System Converter", "Calculator"]

    def display_choices(self):
        print("\nMain Menu:")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"{idx}. {choice}")
        print("0. Exit")

    def get_choice(self):
        while True:
            self.display_choices()
            try:
                choice = input("Choose an option: ")
                if 0 <= int(choice) <= len(self.choices):  # Validate input as integer within range
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")