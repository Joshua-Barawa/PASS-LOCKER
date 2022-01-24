import unittest
from account import Account


class TestAccount(unittest.TestCase):

    Account.user_accounts = []

    def setUp(self):
        '''test runs before every test occurs'''
        self.account = Account("joshua", "123j")

    def test_init(self):
        '''a test to assert whether the values entered would appear when the attribute is called'''
        self.assertEqual(self.account.username, 'joshua')
        self.assertEqual(self.account.password, '123j')

    def test_create_account(self):
        ''' a test to check whether the create account function works'''
        self.account.create_account()
        self.assertEqual(len(Account.user_accounts), 1)

    def test_login(self):
        ''' test to check whether login function works'''
        test_account = Account('joshua', '123j')
        test_account.create_account()
        exist_account = Account.login(self, 'joshua')
        self.assertTrue(exist_account)


if __name__ == '__main__':
    unittest.main()
