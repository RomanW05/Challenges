from abc import ABC, abstractmethod
from typing import Optional


class IValidator(ABC):
   
    @abstractmethod
    def integers(self):
        pass

    @abstractmethod
    def boundries(self):
        pass

