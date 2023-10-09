from User import *


class Customer(User):
    def __init__(self, name, email, phone, location, age, password, role, initial_balance) -> None:
        self.__walet = initial_balance
        self.cart = []
        super().__init__(name, email, phone, location, age, password, role)

    def display_profile(self):
        return super().display_profile()

    def create_account(self, email, password):
        pass
