from abc import ABC, abstractmethod
from typing import Optional


class IValidator(ABC):
    def __init__(self, user_input: str) -> None:
        self.user_input = user_input
    
    @abstractmethod
    def integers(self):
        pass

    @abstractmethod
    def boundries(self):
        pass

