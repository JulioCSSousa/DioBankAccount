class Client:
    def __init__(self, address: str) -> None:
        self._address = address
        self._account_list = list()

    @property
    def account_list(self):
        return self._account_list

    def make_transaction(self, account, transaction) -> None:
        transaction.register(account)
    
    def add_account(self, account: object) -> None:
        self._account_list.append(account)


    def __str__(self):
        return f"{self._account_list}"