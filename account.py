class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    user_accounts = []

    def create_account(self):
        Account.user_accounts.append(self)

    def login(self, username):
        for user in Account.user_accounts:
            if user.username == username:
                return True
            else:
                return False

    def delete_account(self):
        for account in Account.user_accounts:
            if account.username == self.username:
                Account.user_accounts.remove(account)
            else:
                return False

