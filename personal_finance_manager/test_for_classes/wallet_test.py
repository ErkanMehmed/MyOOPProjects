from unittest import TestCase, main

from personal_finance_manager.data_base_manager import DataBaseManager
from personal_finance_manager.goal import Goal
from personal_finance_manager.user import User
from personal_finance_manager.wallet import Wallet
from datetime import datetime


class WalletTest(TestCase):
    def setUp(self):
        self.user = User("TestUser", "LastNameUser", 20, "UserCity", "Address12", 100)
        self.wallet = Wallet(self.user, 50)
        self.goal = Goal("Target", 20)

    def test_init(self):
        self.assertEqual(self.user, self.wallet.user)
        self.assertEqual(50, self.wallet.monthly_limit)
        self.assertEqual([], self.wallet.transactions)
        self.assertEqual([], self.wallet.goals)

    def test_get_current_month_expenses(self):
        result = self.wallet.get_current_month_expenses()
        self.assertEqual(0, result)

    def test_add_transaction_income(self):
        result = self.wallet.add_transaction(10, "Category", "Merchant", "Income")
        self.assertEqual(1, len(self.wallet.transactions))
        self.assertEqual("Income budget: 10 and the current budget: 110", result)

    def test_add_transaction_expenses_over_limit(self):
        result = self.wallet.add_transaction(60, "Category", "Merchant", "Expense")
        self.assertEqual("You are exceeding your monthly limit by 10.00лв.! (Limit: 50лв.)", result)

    def test_add_transaction_expense(self):
        result = self.wallet.add_transaction(10, "Category", "Merchant", "Expense")
        self.assertEqual(1, len(self.wallet.transactions))
        self.assertEqual("Expense budget: 10 and the current budget: 90", result)

    def test_add_transaction_invalid_type(self):
        result = self.wallet.add_transaction(60, "Category", "Merchant", "Expenses")
        self.assertEqual("Invalid transaction type", result)

    def test_get_current_budget(self):
        result = self.wallet.get_current_budget()
        self.assertEqual(100, result)

    def test_get_history_transactions_without_transactions(self):
        result = self.wallet.get_history_transactions()
        self.assertEqual("There is no transactions", result)

    def test_get_history_transactions_with_transactions(self):
        self.wallet.add_transaction(10, "Category", "Merchant", "Expense")

        tx = self.wallet.transactions[0]
        formatted_date = tx.date.strftime('%d.%m.%Y %H:%M')

        result = self.wallet.get_history_transactions()
        self.assertEqual("Expense: 10.00лв. | "
               f"Category: Category | "
               f"Description: Merchant | "
               f"Date: {formatted_date}", result)

    def test_add_goal(self):
        result = self.wallet.add_goal(self.goal)
        self.assertEqual(1, len(self.wallet.goals))
        self.assertEqual("Goal Target has been added", result)

    def test_fund_goal_does_not_exist(self):
        result = self.wallet.fund_goal("Name", 10)
        self.assertEqual("Goal Name does not exist", result)

    def test_fund_goal_do_not_have_enough_budget(self):
        self.wallet.add_goal(self.goal)
        result = self.wallet.fund_goal("Target", 1000)
        self.assertEqual("You do not have enough budget to cover this goal.", result)

    def test_fund_goal_success(self):
        self.wallet.add_goal(self.goal)
        result = self.wallet.fund_goal("Target", 1)
        self.assertEqual(99, self.user.budget)
        self.assertEqual("The funds 1лв. have been allocated for Target.", result)

    def test_get_goals_without_goals(self):
        result = self.wallet.get_goals()
        self.assertEqual("There is no goals", result)
if __name__ == '__main__':
    main()