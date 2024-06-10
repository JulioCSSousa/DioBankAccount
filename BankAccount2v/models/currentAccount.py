from BankAccount2v.models.account import Account


class CurrentAccount(Account):
    def __init__(self, client, account_number: int, limit:float = 500.0,  withdraw_limit:int=3):
        super().__init__(client, account_number)
        self.limit = limit
        self.withdraw_limit = withdraw_limit

    def withdraw(self, value: float) -> bool:
        withdraws_num = len([transaction for transaction in self.historic.transaction_list if transaction["type"] == "Withdraw"])
        if value >= self.limit:
            print(F"\033[0;31m You can't withdraw more than your limit \033[m {self.limit}")
            return False
        if withdraws_num >= self.withdraw_limit:
            print(f"\033[0;31m You cannot make more withdraw today, you exceeded your limit \033[m ")
            return False
        return super().withdraw(value)
        
        
    def __str__(self) -> str:
        return f"Agency: {self.agency}, Account: {self.account_number}, Client: {self.client}"
            
        