import tkinter as tk
import customtkinter as ctk
import Calculator
from NumberSystemConverter import NumberSystemConverter
from IpPlanner import IPPlanner
from Login import Login

class PageManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title ="Computer Science Calculator"
        self.geometry("800x500")
        self.minsize(800 , 500)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # the Container
        self.container = ctk.CTkFrame(self, corner_radius=0)
        self.container.pack(fill="both", expand=True)

        # frames Dictionary
        self.frames = {}

        # Initialize pages
        for F in (
                LoginPage, MainMenuPage, IPPlannerPage, NumberSystemConverterPage, CalculatorPage):  # Include CalculatorPage
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

        # Set a consistent style for all pages
        self.configure(fg_color="#FFFFFF")  # White background
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

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.login_manager = Login()

        # responsive layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # LEFT SECTION : gradient background
        self.left_frame = tk.Frame(self, bg="#FFFFFF")
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.create_gradient_canvas(self.left_frame).pack(fill="both", expand=True)

        # RIGHT SECTION : Login page
        self.right_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#FFFFFF")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Welcome Text
        ctk.CTkLabel(self.right_frame, text="Welcome Back!", font=("Helvetica", 24, "bold"), text_color="#4682B4").pack(pady=10)
        ctk.CTkLabel(self.right_frame, text="Sign in to your account", font=("Helvetica", 16), text_color="#A9A9A9").pack(pady=5)

        # Username Input
        ctk.CTkLabel(self.right_frame, text="Username:", font=("Helvetica", 12), text_color="#A9A9A9").pack(anchor="w", padx=20, pady=5)
        self.username_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Enter your username", corner_radius=10)
        self.username_entry.pack(fill="x", padx=20, pady=5)

        # Password Input
        ctk.CTkLabel(self.right_frame, text="Password:", font=("Helvetica", 12), text_color="#A9A9A9").pack(anchor="w", padx=20, pady=5)
        self.password_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Enter your password", corner_radius=10, show="*")
        self.password_entry.pack(fill="x", padx=20, pady=5)

        # Login Button
        ctk.CTkButton(self.right_frame, text="Login", command=self.authenticate, corner_radius=10, font=("Helvetica", 14),fg_color="#7F00FF", hover_color="#B83AF3").pack(fill="x", padx=20, pady=15)

        # Register Button
        ctk.CTkButton(self.right_frame, text="Register", command=self.register, corner_radius=10, font=("Helvetica", 14), fg_color="#E0E0E0", hover_color="#B8B8B8", text_color="#000000").pack(fill="x", padx=20, pady=5)

        # down Message Label
        self.message_label = ctk.CTkLabel(self.right_frame, text="", font=("Helvetica", 12), text_color="red")
        self.message_label.pack(pady=10)

    def create_gradient_canvas(self, parent):
        #Create a gradient canvas
        canvas = tk.Canvas(parent, bg="#FFFFFF", highlightthickness=0)
        canvas.bind("<Configure>", lambda e: self.draw_gradient(canvas))
        return canvas

    @staticmethod
    def draw_gradient(canvas):
        canvas.delete("gradient")
        colors = ["#abb2b9" , "#abb2b9" , "#abb2b9"  , "#abb2b9" ]
        width = canvas.winfo_width()
        step = 200

        for i, color in enumerate(colors):
            canvas.create_rectangle(0, i * step, width, (i + 1) * step, fill=color, outline="", tags="gradient")

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        result = self.login_manager.authenticate(username, password)
        if result is True:
            self.message_label.configure(text="Login Successful!", text_color="green")
            self.controller.show_frame(MainMenuPage)
        else:
            self.message_label.configure(text=result, text_color="red")

    def register(self, **kwargs):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.login_manager.register(username, password)
        self.message_label.configure(text=result, text_color="green" if "successful" in result else "red")

class MainMenuPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.gradient_canvas = self.create_gradient_canvas(self)
        self.gradient_canvas.pack(fill="x")  # Fill horizontally

        # Use place to set the height of the gradient canvas
        self.gradient_canvas.place(x=0, y=0, relwidth=1, height=170)  # Set the fixed height

        # Menu Frame (centered below the gradient)
        menu_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="transparent")
        menu_frame.pack(expand=True, padx=10, pady=(10, 10))  # Add bottom padding if needed
        self.create_label("Main Menu", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(in_=menu_frame, pady=20)
        #Style the buttons to match the gradient theme
        self.create_button("IP Planner", lambda: controller.show_frame(IPPlannerPage), fg="#FFFFFF", bg="#7F00FF").pack(in_=menu_frame, pady=10)
        self.create_button("Number System Converter", lambda: controller.show_frame(NumberSystemConverterPage), fg="#FFFFFF", bg="#7F00FF").pack(in_=menu_frame, pady=10),
        self.create_button("Calculator", lambda: controller.show_frame(CalculatorPage), fg="#FFFFFF", bg="#7F00FF").pack(in_=menu_frame, pady=10)
        self.create_button("Exit", controller.quit, bg="#cb4335", fg="#FFFFFF").pack(in_=menu_frame, pady=20) # Style the Exit button

    def create_gradient_canvas(self, parent):
       # Create an abstract gradient canvas
        canvas = tk.Canvas(parent, bg="#FFFFFF", highlightthickness=0)
        canvas.bind("<Configure>", lambda e: self.draw_gradient(canvas))
        return canvas

    @staticmethod
    def draw_gradient(canvas):
        canvas.delete("gradient")  # Remove old gradient
        width = canvas.winfo_width()
        # Define your gradient colors
        colors = ["#abb2b9" , "#d5d8dc" , "#eaecee" ]

        # Calculate the height of each color band
        step = 50

        # Create gradient rectangles
        for i, color in enumerate(colors):
            canvas.create_rectangle(
                0, i * step, width, (i + 1) * step, fill=color, outline="", tags="gradient"
            )

class IPPlannerPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.planner = IPPlanner()

        # Responsive frame
        planner_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="white")
        planner_frame.pack(fill="both", expand=True,  pady=20)

        self.create_label("IP Planner", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(in_=planner_frame, pady=20)

        self.network_entry = self.create_entry(placeholder="Network Address")
        self.network_entry.pack(in_=planner_frame, pady=10)

        self.subnet_entry = self.create_entry(placeholder="Subnet Mask")
        self.subnet_entry.pack(in_=planner_frame, pady=10)

        self.create_button("Calculate", self.calculate,bg="#7F00FF").pack(in_=planner_frame, pady=20)
        self.result_label = self.create_label("", font=("Helvetica", 14))
        self.result_label.pack(in_=planner_frame, pady=10)

        self.create_button("Back to Main Menu", lambda: controller.show_frame(MainMenuPage),bg="#7F00FF").pack(in_=planner_frame, pady=20)

    def calculate(self):
        network = self.network_entry.get()
        subnet = self.subnet_entry.get()
        result = self.planner.compute_ip_details(network, subnet)

        if isinstance(result, dict):
            self.result_label.configure(
                text=(
                    f"Network Address: {result['Network Address']}\n"
                    f"Broadcast Address: {result['Broadcast Address']}\n"
                    f"Available Hosts: {result['Number of available Hosts']}"
                )
            )
        else:
            self.result_label.configure(text=f"Error: {result}")



class NumberSystemConverterPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.converter = NumberSystemConverter()

        # Responsive frame
        converter_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="white")
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

        self.create_button("Convert", self.convert,bg="#7F00FF").pack(in_=converter_frame, pady=20)
        self.result_label = self.create_label("", font=("Helvetica", 14))
        self.result_label.pack(in_=converter_frame, pady=10)

        self.create_button("Back to Main Menu", lambda: controller.show_frame(MainMenuPage),bg="#7F00FF").pack(
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


class CalculatorPage(StyledPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)  # Pass controller to StyledPage

        # Responsive frame
        calculator_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="white")
        calculator_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_label("Simple Calculator", font=("Helvetica", 28, "bold"), fg="#4682B4").pack(
            in_=calculator_frame, pady=20
        )

        self.num1_entry = self.create_entry(placeholder="Enter first number")
        self.num1_entry.pack(in_=calculator_frame, pady=10)

        # Frame for operation buttons (row 1)
        operation_frame_row1 = ctk.CTkFrame(calculator_frame)
        operation_frame_row1.pack(pady=10)

        # First row of operation buttons
        operations_row1 = ["+", "-", "*", "/", "**"]
        for op in operations_row1:
            self.create_button(op, lambda o=op: self.calculate(o),bg="#7F00FF").pack(
                in_=operation_frame_row1, side="left", padx=5
            )

        # Frame for operation buttons (row 2)
        operation_frame_row2 = ctk.CTkFrame(calculator_frame)
        operation_frame_row2.pack(pady=10)

        # Second row of operation buttons
        operations_row2 = ["//", "%", "root"]
        for op in operations_row2:
            self.create_button(op, lambda o=op: self.calculate(o),bg="#7F00FF").pack(
                in_=operation_frame_row2, side="left", padx=5
            )

        self.num2_entry = self.create_entry(placeholder="Enter second number (optional for root)")
        self.num2_entry.pack(in_=calculator_frame, pady=10)

        self.result_label = self.create_label("", font=("Helvetica", 14))  # Use create_label from StyledPage
        self.result_label.pack(in_=calculator_frame, pady=10)

        self.create_button("Back to Main Menu", lambda: controller.show_frame(MainMenuPage),bg="#7F00FF").pack(
            in_=calculator_frame, pady=20
        )

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            if operation != "root":
                try:
                    num2 = float(self.num2_entry.get())
                except ValueError:
                    self.result_label.configure(text="Error: Invalid input for second number.")
                    return
            else:
                num2 = None  # No second number needed for "root"

            # Call the calculate method from the Calculator class
            result = Calculator.Calculator.calculate(num1, num2, operation)
            self.result_label.configure(text=f"Result: {result}")
        except ValueError:
            self.result_label.configure(text="Error: Invalid input for first number.")
        except Exception as e:  # Catch other potential errors from Calculator.calculate
            self.result_label.configure(text=f"Error: {e}")



if __name__ == "__main__":
    app = PageManager()
    app.mainloop()
