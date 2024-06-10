from BankAccount2v.models.transaction import Transaction

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    def register(self, account) -> None:
        transaction_success = account.deposit(self.value)
        if transaction_success:
            account.historic.add_transaction(self)
        return transaction_success
