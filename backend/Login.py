class Login:

    def __init__(self):
        self.username = "admin"  # Default username
        self.password = "1234"  # Default password

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
