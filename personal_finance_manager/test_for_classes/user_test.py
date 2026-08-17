from unittest import TestCase, main

from personal_finance_manager.user import User


class UserTest(TestCase):
    def setUp(self):
        self.user = User("TestUser", "LastNameUser", 20, "UserCity", "Address12", 100)

    def test_init(self):
        self.assertEqual("TestUser", self.user.first_name)
        self.assertEqual("LastNameUser", self.user.last_name)
        self.assertEqual(20, self.user.age)
        self.assertEqual("UserCity", self.user.city)
        self.assertEqual("Address12", self.user.address)
        self.assertEqual(100, self.user.budget)

    def test_first_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.user.first_name = " "
        self.assertEqual("First name cannot be an empty string and must be more than 1 character", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.user.first_name = "E"
        self.assertEqual("First name cannot be an empty string and must be more than 1 character", str(ex.exception))

    def test_last_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.user.last_name = " "
        self.assertEqual("Last name cannot be an empty string and must be more than 1 character", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.user.last_name = "E"
        self.assertEqual("Last name cannot be an empty string and must be more than 1 character", str(ex.exception))

    def test_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.user.age = 14
        self.assertEqual("Age must be at least 16", str(ex.exception))

    def test_address_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.user.address = "SOFIA12B"
        self.assertEqual("The address is not correct. The address must start with a capital letter and end with a number, with no space between them.", str(ex.exception))


if __name__ == '__main__':
    main()