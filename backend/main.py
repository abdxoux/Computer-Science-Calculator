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


class StyledPage(tk.Frame):
    """Base class for consistent styling across pages."""
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller

    def create_label(self, text, font=("Helvetica", 16), fg="#A9A9A9"):
        """Create a styled label."""
        return tk.Label(self, text=text, font=font, fg=fg, bg="#FFFFFF")

    def create_entry(self, font=("Helvetica", 14), width=30):
        """Create a styled entry."""
        return tk.Entry(self, font=font, width=width, bg="#F5F5F5", relief="solid")

    def create_button(self, text, command, bg="#ADD8E6", fg="#FFFFFF", width=20):
        """Create a styled button."""
        return tk.Button(self, text=text, command=command, bg=bg, fg=fg, font=("Helvetica", 14), width=width, relief="flat")


class LoginPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.create_label("Login", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(pady=30)

        self.create_label("Username").pack(pady=5)
        self.username_entry = self.create_entry()
        self.username_entry.pack(pady=10)

        self.create_label("Password").pack(pady=5)
        self.password_entry = self.create_entry()
        self.password_entry.config(show="*")
        self.password_entry.pack(pady=10)

        self.create_button("Login", self.authenticate, bg="#4682B4").pack(pady=20)
        self.message_label = self.create_label("", fg="red")
        self.message_label.pack()

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            self.controller.show_frame(MainMenuPage)
        else:
            self.message_label.config(text="Invalid username or password!")


class MainMenuPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.create_label("Main Menu", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(pady=30)

        self.create_button("IP Planner", lambda: controller.show_frame(IPPlannerPage)).pack(pady=20)
        self.create_button("Number System Converter", lambda: controller.show_frame(NumberSystemConverterPage)).pack(pady=20)
        self.create_button("Exit", controller.quit, bg="#FF6666", fg="#FFFFFF").pack(pady=20)


class IPPlannerPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.planner = IPPlanner()

        self.create_label("IP Planner", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(pady=30)

        self.create_label("Network Address").pack(pady=5)
        self.network_entry = self.create_entry()
        self.network_entry.pack(pady=10)

        self.create_label("Subnet Mask").pack(pady=5)
        self.subnet_entry = self.create_entry()
        self.subnet_entry.pack(pady=10)

        self.create_button("Calculate", self.calculate, bg="#4682B4").pack(pady=20)

        self.result_label = self.create_label("", font=("Helvetica", 14), fg="#4682B4")
        self.result_label.pack(pady=10)

        self.create_button("Back to Main Menu", lambda: controller.show_frame(MainMenuPage), bg="#ADD8E6").pack(pady=20)

    def calculate(self):
        network = self.network_entry.get()
        subnet = self.subnet_entry.get()
        result = self.planner.compute_ip_details(network, subnet)

        if isinstance(result, dict):
            self.result_label.config(
                text=(
                    f"Network Address: {result['Network Address']}\n"
                    f"Broadcast Address: {result['Broadcast Address']}\n"
                    f"Available Hosts: {len(result['Available Hosts'])}"
                )
            )
        else:
            self.result_label.config(text=f"Error: {result}")


class NumberSystemConverterPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.converter = NumberSystemConverter()

        self.create_label("Number System Converter", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(pady=30)

        self.create_label("Number").pack(pady=5)
        self.number_entry = self.create_entry()
        self.number_entry.pack(pady=10)

        self.create_label("From Base").pack(pady=5)
        self.from_base_entry = self.create_entry()
        self.from_base_entry.pack(pady=10)

        self.create_label("To Base").pack(pady=5)
        self.to_base_entry = self.create_entry()
        self.to_base_entry.pack(pady=10)

        self.create_button("Convert", self.convert, bg="#4682B4").pack(pady=20)

        self.result_label = self.create_label("", font=("Helvetica", 14), fg="#4682B4")
        self.result_label.pack(pady=10)

        self.create_button("Back to Main Menu", lambda: controller.show_frame(MainMenuPage), bg="#ADD8E6").pack(pady=20)

    def convert(self):
        number = self.number_entry.get()
        try:
            from_base = int(self.from_base_entry.get())
            to_base = int(self.to_base_entry.get())
            result = self.converter.convert_number(number, from_base, to_base)
            self.result_label.config(text=f"Converted Result: {result}")
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter valid bases and a number.")


if __name__ == "__main__":
    app = PageManager()
    app.mainloop()
