class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    user_accounts = []

    def create_account(self):
        Account.user_account.append(self)

    def login(self, username):
        for account in Account.user_accounts:
            if account.username == username:
                return True
            else:
                return False

    def delete_account(self):
        for account in Account.user_accounts:
            if account.username == self.username:
                return True
            else:
                return False

