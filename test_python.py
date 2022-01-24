import unittest
from password import Password


class TestPasswords(unittest.TestCase):

    Password.user_passwords = []

    def setUp(self):
        '''test runs before every test occurs'''
        self.password = Password("facebook", "123f")

    def test_init(self):
        '''a test to assert whether the values entered would appear when the attribute is called'''
        self.assertEqual(self.password.page, 'facebook')
        self.assertEqual(self.password.password, '123f')

    def test_add_password(self):
        ''' a test to check whether the create password function works'''
        self.password.create_password()
        self.assertEqual(len(Password.user_passwords), 1)

    def test_delete_password(self):
        ''' test to check whether login function works'''
        test_password = Password('facebook', '123f')
        test_password.create_password()
        exist_password = Password.delete_password(self, 'facebook')
        self.assertFalse(exist_password)


if __name__ == '__main__':
    unittest.main()
