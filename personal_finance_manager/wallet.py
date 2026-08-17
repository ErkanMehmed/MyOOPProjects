from datetime import datetime

from personal_finance_manager.data_base_manager import DataBaseManager
from personal_finance_manager.goal import Goal
from personal_finance_manager.transactions import Transaction
from personal_finance_manager.user import User


class Wallet:
    def __init__(self, user: User, monthly_limit: float | int=0):
        self.user = user
        self.monthly_limit = monthly_limit
        self.transactions: list[Transaction] = []
        self.goals: list[Goal] = []

        self.db = DataBaseManager()
        self.db.save_wallet_state(self)

    def get_current_month_expenses(self):
        now = datetime.now()
        total_expenses = 0

        for transaction in self.transactions:
            if transaction.transaction_type == "Expense" and transaction.date.month == now.month and transaction.date.year == now.year:
                total_expenses += transaction.amount

        return total_expenses

    def add_transaction(self, amount, category, merchant, trans_type):
        if trans_type == "Income":
            new_transaction = Transaction(amount, category, merchant, trans_type, self.user)
            result = new_transaction.process()
            if result != "There is no income budget":
                self.transactions.append(new_transaction)
                self.db.save_wallet_state(self)
                self.db.save_transaction(new_transaction)
            return result

        elif trans_type == "Expense":

            if self.monthly_limit > 0:
                current_monthly_expenses = self.get_current_month_expenses()
                if current_monthly_expenses + amount > self.monthly_limit:
                    excess = (current_monthly_expenses + amount) - self.monthly_limit
                    return f"You are exceeding your monthly limit by {excess:.2f}лв.! (Limit: {self.monthly_limit}лв.)"

            new_transaction = Transaction(amount, category, merchant, trans_type, self.user)
            result = new_transaction.process()
            if result != "You do not have enough budget to cover this expense." and result != "There is no expense budget":
                self.transactions.append(new_transaction)
                self.db.save_wallet_state(self)
                self.db.save_transaction(new_transaction)

            return result
        else:
            return "Invalid transaction type"

    def get_current_budget(self):
        return self.user.budget

    def get_history_transactions(self):
        if not self.transactions:
            return "There is no transactions"

        history_transactions = [str(t) for t in self.transactions]
        return "\n".join(history_transactions)

    def get_summary(self):
        income_transaction = []
        expense_transaction = []

        total_income = 0
        total_expenses = 0

        for transaction in self.transactions:
            if transaction.transaction_type == "Income":
                total_income += transaction.amount
                income_transaction.append(str(transaction))
            elif transaction.transaction_type == "Expense":
                total_expenses += transaction.amount
                expense_transaction.append(str(transaction))

        return f"Total Income: {total_income}лв.\n{'\n'.join(income_transaction)}\nTotal Expense: {total_expenses}лв.\n{'\n'.join(expense_transaction)}"

    def add_goal(self, goal: Goal):
        self.goals.append(goal)
        return f"Goal {goal.target_name} has been added"

    def fund_goal(self, goal_name: str, goal_amount: float):

        target_goal = next((g for g in self.goals if g.target_name == goal_name), None)

        if target_goal is None:
            return f"Goal {goal_name} does not exist"

        if goal_amount > self.user.budget:
            return f"You do not have enough budget to cover this goal."

        self.user.budget -= goal_amount
        self.db.save_wallet_state(self)
        return target_goal.add_savings(goal_amount)

    def get_goals(self):

        if not self.goals:
            return "There is no goals"

        return '\n'.join([str(g) for g in self.goals])