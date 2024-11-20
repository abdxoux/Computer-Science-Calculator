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
