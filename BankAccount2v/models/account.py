from random import randint
from BankAccount2v.models.historic import Historic

class Account:
    def __init__(self, client: object, account_number) -> None:
        self._balance: float = 0
        self._account_number = account_number
        self.agency: str = '0001'
        self._client = client
        self._historic = Historic()
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def account_number(self) -> int:
        return self._account_number
    
    @property
    def client(self):
        return self._client
    
    @property
    def historic(self):
        return self._historic
    
    @classmethod
    def new_account(cls, client, account_num: int) -> object:
        return cls(client, account_num)
    
    def deposit(self, value) -> bool:
        invalid = value <= 0
        if invalid:
            print("\033[0;31m Invalid Operation \033[m")
            return False
        self._balance += value
        print("\033[0;32m successful deposit \033[m")
        return True
    
    def withdraw(self, value) -> bool:
        invalid = value <= 0 
        balance_exceed = value >= self._balance
        if invalid:
            print("\033[0;31m Invalid Operation \033[m")
            return False
        if balance_exceed:
            print(f"\033[0;31m Not enough cash! \033[m")
            return False
        self._balance += value
        print("\033[0;32m successful withdraw \033[m")
        return True
    