from personal_finance_manager.budget_management import BudgetManagement
from personal_finance_manager.user import User
from datetime import datetime

class Transaction:
    def __init__(self, amount: float | int, category: str, merchant: str, transaction_type: str, user: User):
        self.amount = amount
        self.category = category
        self.merchant = merchant
        self.transaction_type = transaction_type
        self.user = user
        self.date = datetime.now()

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("Amount must be larger than 0")
        self.__amount = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if value.strip() == "":
            raise ValueError("Category must not be empty")

        self.__category = value

    @property
    def merchant(self):
        return self.__merchant

    @merchant.setter
    def merchant(self, value):
        if not isinstance(value, str):
            raise ValueError("Merchant must be a string")
        if value.strip() == "":
            raise ValueError("Merchant must not be empty")

        self.__merchant = value

    def process(self):
        if self.transaction_type == "Income":
            return BudgetManagement.income(self.amount, self.user)

        elif self.transaction_type == "Expense":
            return BudgetManagement.expense(self.amount, self.user)

        return "Invalid transaction type"

    def __str__(self):
        return(f"{self.transaction_type}: {self.amount:.2f}лв. | "
               f"Category: {self.category} | "
               f"Description: {self.merchant} | "
               f"Date: {self.date.strftime('%d.%m.%Y %H:%M')}")