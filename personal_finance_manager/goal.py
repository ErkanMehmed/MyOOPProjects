from datetime import datetime

class Goal:
    def __init__(self, target_name: str, target_amount: float | int, month: int=None, year: int=None):
        self.target_name = target_name
        self.target_amount = target_amount
        self.current_amount = 0.0

        now = datetime.now()
        self.month = month if month is not None else now.month
        self.year = year if year is not None else now.year

    @property
    def target_name(self):
        return self.__target_name

    @target_name.setter
    def target_name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Goal name must be a non-empty string")
        self.__target_name = value
    
    @property
    def target_amount(self):
        return self.__target_amount
    
    @target_amount.setter
    def target_amount(self, value):
        if value <= 0:
            raise ValueError("Target amount must be greater than 0")
        self.__target_amount = value

    def add_savings(self, amount: float | int):
        if amount <= 0:
            raise ValueError("Amount to save must be greater than 0")
        self.current_amount += amount
        return f"The funds {amount}лв. have been allocated for {self.target_name}."

    def is_achieved(self):
        return self.current_amount >= self.target_amount

    def get_progress_percentage(self):
        if self.target_amount == 0:
            return 0.0
        return min(100.0, (self.current_amount / self.target_amount) * 100)

    def __str__(self):
        status = "Goal successfully reached" if self.is_achieved() else f"{self.get_progress_percentage():.1f}% is achieved."
        return (f"Goal: {self.target_name} | Month: {self.month:02d}.{self.year} | "
                f"Collected: {self.current_amount:.2f} / {self.target_amount:.2f} лв. "
                f"({status})")