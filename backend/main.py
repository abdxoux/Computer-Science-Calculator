import customtkinter as ctk
from NumberSystemConverter import NumberSystemConverter
from IpPlanner import IPPlanner


class PageManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Utility Application")
        self.geometry("400x600")
        self.minsize(400, 600)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # the Container
        self.container = ctk.CTkFrame(self, corner_radius=0)
        self.container.pack(fill="both", expand=True)

        # frames Dictionary
        self.frames = {}

        # Initialize pages
        for F in (LoginPage, MainMenuPage, IPPlannerPage, NumberSystemConverterPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Show Login Page at first
        self.show_frame(LoginPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()


class StyledPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_label(self, text, font=("Helvetica", 16), fg="#4682B4"):
        return ctk.CTkLabel(self, text=text, font=ctk.CTkFont(*font), text_color=fg)

    def create_entry(self, font=("Helvetica", 14), placeholder=""):
        return ctk.CTkEntry(self, placeholder_text=placeholder, font=ctk.CTkFont(*font))

    def create_button(self, text, command, fg="#FFFFFF", bg="#4682B4"):
        return ctk.CTkButton(
            self, text=text, command=command, fg_color=bg, text_color=fg, font=ctk.CTkFont("Helvetica", 14)
        )


class LoginPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Responsive frame
        login_frame = ctk.CTkFrame(self, corner_radius=10)
        login_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_label("Login", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(in_=login_frame, pady=20)

        self.username_entry = self.create_entry(placeholder="Username")
        self.username_entry.pack(in_=login_frame, pady=10)

        self.password_entry = self.create_entry(placeholder="Password")
        self.password_entry.configure(show="*")
        self.password_entry.pack(in_=login_frame, pady=10)

        self.create_button("Login", self.authenticate).pack(in_=login_frame, pady=20)
        self.message_label = self.create_label("", fg="red")
        self.message_label.pack(in_=login_frame)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            self.controller.show_frame(MainMenuPage)
        else:
            self.message_label.configure(text="Invalid username or password!")


class MainMenuPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Responsive frame
        menu_frame = ctk.CTkFrame(self, corner_radius=10)
        menu_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_label("Main Menu", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(in_=menu_frame, pady=20)
        self.create_button("IP Planner", lambda: controller.show_frame(IPPlannerPage)).pack(in_=menu_frame, pady=10)
        self.create_button("Number System Converter", lambda: controller.show_frame(NumberSystemConverterPage)).pack(
            in_=menu_frame, pady=10
        )
        self.create_button("Exit", controller.quit, bg="#FF6666").pack(in_=menu_frame, pady=20)


class IPPlannerPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.planner = IPPlanner()

        # Responsive frame
        planner_frame = ctk.CTkFrame(self, corner_radius=10)
        planner_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_label("IP Planner", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(in_=planner_frame, pady=20)

        self.network_entry = self.create_entry(placeholder="Network Address")
        self.network_entry.pack(in_=planner_frame, pady=10)

        self.subnet_entry = self.create_entry(placeholder="Subnet Mask")
        self.subnet_entry.pack(in_=planner_frame, pady=10)

        self.create_button("Calculate", self.calculate).pack(in_=planner_frame, pady=20)
        self.result_label = self.create_label("", font=("Helvetica", 14))
        self.result_label.pack(in_=planner_frame, pady=10)

        self.create_button("Back to Main Menu", lambda: controller.show_frame(MainMenuPage)).pack(in_=planner_frame, pady=20)

    def calculate(self):
        network = self.network_entry.get()
        subnet = self.subnet_entry.get()
        result = self.planner.compute_ip_details(network, subnet)

        if isinstance(result, dict):
            self.result_label.configure(
                text=(
                    f"Network Address: {result['Network Address']}\n"
                    f"Broadcast Address: {result['Broadcast Address']}\n"
                    f"Available Hosts: {len(result['Available Hosts'])}"
                )
            )
        else:
            self.result_label.configure(text=f"Error: {result}")


class NumberSystemConverterPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.converter = NumberSystemConverter()

        # Responsive frame
        converter_frame = ctk.CTkFrame(self, corner_radius=10)
        converter_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_label("Number System Converter", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(
            in_=converter_frame, pady=20
        )

        self.number_entry = self.create_entry(placeholder="Number")
        self.number_entry.pack(in_=converter_frame, pady=10)

        self.from_base_entry = self.create_entry(placeholder="From Base")
        self.from_base_entry.pack(in_=converter_frame, pady=10)

        self.to_base_entry = self.create_entry(placeholder="To Base")
        self.to_base_entry.pack(in_=converter_frame, pady=10)

        self.create_button("Convert", self.convert).pack(in_=converter_frame, pady=20)
        self.result_label = self.create_label("", font=("Helvetica", 14))
        self.result_label.pack(in_=converter_frame, pady=10)

        self.create_button("Back to Main Menu", lambda: controller.show_frame(MainMenuPage)).pack(
            in_=converter_frame, pady=20
        )

    def convert(self):
        number = self.number_entry.get()
        try:
            from_base = int(self.from_base_entry.get())
            to_base = int(self.to_base_entry.get())
            result = self.converter.convert_number(number, from_base, to_base)
            self.result_label.configure(text=f"Converted Result: {result}")
        except ValueError:
            self.result_label.configure(text="Invalid input ! Please enter valid base or number.")


if __name__ == "__main__":
    app = PageManager()
    app.mainloop()
