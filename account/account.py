class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    user_accounts = []

    def create_account(self):
        Account.user_accounts.append(self)

    def login(self, username, password):
        for account in Account.user_accounts:
            if account.username == username and account.password == password:
                return True
            else:
                return False

    def delete_account(self):
        for account in Account.user_accounts:
            if account.username == self.username:
                Account.user_accounts.remove(account)
            else:
                return False

