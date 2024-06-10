from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def value(self):
        pass
    
    @abstractmethod
    def register(self, account):
        pass
    
    