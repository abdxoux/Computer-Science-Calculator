import bcrypt

class Login:
    def __init__(self):
        self.user_data = {"admin": bcrypt.hashpw("admin".encode(), bcrypt.gensalt())}

    def register(self, username, password):
        if username in self.user_data:
            return "User already exists!"
        elif username == "" or password == "":
            return "Username or password cannot be empty!"
        else:

            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            self.user_data[username] = hashed_password
            return "Registration successful!"

    def authenticate(self, username, password):
        if username not in self.user_data:
            return "User does not exist!"

        else:

            stored_hash = self.user_data[username]
            if bcrypt.checkpw(password.encode(), stored_hash):
                return True
            else:
                return "Invalid username or password!"

