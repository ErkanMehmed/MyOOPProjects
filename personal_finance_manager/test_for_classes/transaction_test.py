from unittest import TestCase, main

from personal_finance_manager.budget_management import BudgetManagement
from personal_finance_manager.transactions import Transaction
from personal_finance_manager.user import User


class TransactionTest(TestCase):
    def setUp(self):
        self.user = User("TestUser", "LastUser", 20, "UserCity", "Address12", 100)
        self.transaction = Transaction(5.5, "Category", "Merchant", "Income", self.user)

    def test_init(self):
        self.assertEqual(5.5, self.transaction.amount)
        self.assertEqual("Category", self.transaction.category)
        self.assertEqual("Merchant", self.transaction.merchant)
        self.assertEqual("Income", self.transaction.transaction_type)
        self.assertEqual(self.user, self.transaction.user)

    def test_amount_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.transaction.amount = -1
        self.assertEqual("Amount must be larger than 0", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.transaction.amount = 0
        self.assertEqual("Amount must be larger than 0", str(ex.exception))

    def test_category_raises_non_string(self):
        with self.assertRaises(ValueError) as ex:
            self.transaction.category = 23
        self.assertEqual("Category must be a string", str(ex.exception))

    def test_category_raises_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.transaction.category = ""
        self.assertEqual("Category must not be empty", str(ex.exception))

    def test_merchant_raises_non_string(self):
        with self.assertRaises(ValueError) as ex:
            self.transaction.merchant = 23
        self.assertEqual("Merchant must be a string", str(ex.exception))

    def test_merchant_raises_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.transaction.merchant = ""
        self.assertEqual("Merchant must not be empty", str(ex.exception))

    def test_process_invalid_transaction_type(self):
        self.transaction.transaction_type = "Invalid"
        result = self.transaction.process()
        self.assertEqual("Invalid transaction type", result)

    def test_process_income(self):
        result = self.transaction.process()
        self.assertEqual("Income budget: 5.5 and the current budget: 105.5", result)

    def test_process_expense(self):
        self.transaction.transaction_type = "Expense"
        result = self.transaction.process()
        self.assertEqual("Expense budget: 5.5 and the current budget: 94.5", result)

if __name__ == '__main__':
    main()