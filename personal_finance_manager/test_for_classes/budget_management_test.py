from unittest import TestCase, main

from personal_finance_manager.budget_management import BudgetManagement
from personal_finance_manager.user import User


class BudgetManagementTest(TestCase):
    def setUp(self):
        self.user = User("TestUser", "LastUser", 20, "UserCity", "Address12", 100)
        self.budget_management = BudgetManagement

    def test_income_zero_income_budget(self):
        result = self.budget_management.income(0, self.user)
        self.assertEqual("There is no income budget", result)

    def test_income_success(self):
        result = self.budget_management.income(10, self.user)
        self.assertEqual("Income budget: 10 and the current budget: 110", result)

    def test_expense_no_budget(self):
        self.user.budget = 0
        result = self.budget_management.expense(10, self.user)

        self.assertEqual("You do not have enough budget to cover this expense.", result)

    def test_expense_larger_than_budget(self):
        result = self.budget_management.expense(110, self.user)
        self.assertEqual("You do not have enough budget to cover this expense.", result)

    def test_expense_with_zero_expense(self):
        result = self.budget_management.expense(0, self.user)
        self.assertEqual("There is no expense budget", result)

    def test_expense_success(self):
        result = self.budget_management.expense(10, self.user)
        self.assertEqual("Expense budget: 10 and the current budget: 90", result)


if __name__ == '__main__':
    main()