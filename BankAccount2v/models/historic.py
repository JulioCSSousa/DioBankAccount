from datetime import datetime
from BankAccount2v.models.transaction import Transaction

class Historic:
    def __init__(self) -> None:
        self.transaction_list = []
    
    def add_transaction(self, transaction: Transaction) -> None:
        transact = \
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now()
            }
        self.transaction_list.append(transact)
        