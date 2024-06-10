from BankAccount2v.models.transaction import Transaction

class Withdraw(Transaction):
    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self) -> float:
        return self._value
    
    def register(self, account) -> None:
        transaction_success = account.withdraw(self.value)
        if transaction_success:
            account.historic.add_transaction(self)
            
            