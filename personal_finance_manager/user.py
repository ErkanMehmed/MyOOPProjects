import re

class User:
    def __init__(self, first_name: str, last_name: str, age: int, city: str, address: str, budget: float | int=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.address = address
        self.budget = budget

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value.strip() == "" or len(value.strip()) <= 1:
            raise ValueError("First name cannot be an empty string and must be more than 1 character")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value.strip() == "" or len(value.strip()) <= 1:
            raise ValueError("Last name cannot be an empty string and must be more than 1 character")
        self.__last_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Age must be at least 16")
        self.__age = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        pattern = r"^[A-Z][a-z]+\d+$"
        if not re.fullmatch(pattern, value):
            raise ValueError("The address is not correct. The address must start with a capital letter and end with a number, with no space between them.")
        self.__address = value
    
