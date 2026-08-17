from personal_finance_manager.user import User


class BudgetManagement:

    @staticmethod
    def income(income_budget, user: User):
        if income_budget > 0:
            user.budget += income_budget
            return f"Income budget: {income_budget} and the current budget: {user.budget}"
        return "There is no income budget"

    @staticmethod
    def expense(expense_budget, user: User):
        if user.budget <= 0 or expense_budget > user.budget:
            return "You do not have enough budget to cover this expense."

        if expense_budget > 0:
            user.budget -= expense_budget
            return f"Expense budget: {expense_budget} and the current budget: {user.budget}"
        return "There is no expense budget"



