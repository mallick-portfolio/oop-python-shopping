
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, email, phone, location, age, password, role) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location
        self.age = age
        self.__password = password
        self.__role = role
        super().__init__()

    @abstractmethod
    def display_profile(self):
        return f"{self.name} with email {self.email}"

    def __repr__(self) -> str:
        return f"{self.name}, {self.email}, {self.phone}, {self.location}"
