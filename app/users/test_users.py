import unittest

from app.users.models import User


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(email='moses@gmail.com', firstname='Moses',
                         lastname='Ongwenyi', password='Password')

    def tearDown(self):
        self.user = None

    def test_password_setter(self):
        self.assertTrue(self.user.password_hash is not None)

    def test_no_password_getter(self):
        with self.assertRaises(AttributeError):
            self.user.password

    def test_password_verification(self):
        self.assertTrue(self.user.verify_password('Password'))
        self.assertFalse(self.user.verify_password('password'))

    def test_password_salts_are_random(self):
        user = User(email='moses@gmail.com', firstname='Moses',
                    lastname='Ongwenyi', password='Password')
        self.assertTrue(self.user.password_hash != user.password_hash)
