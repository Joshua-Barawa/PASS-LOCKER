
class Password:
    def __init__(self, page, password):
        self.page = page
        self.password = password

    user_passwords = []

    def create_password(self):
        Password.user_passwords.append(self)


    def delete_password(self, page):
        for password in Password.user_passwords:
            if password.page == page:
                Password.user_passwords.remove(password)