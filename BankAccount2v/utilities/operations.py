from random import randint
from BankAccount2v.models.currentAccount import CurrentAccount
from BankAccount2v.models.deposit import Deposit
from BankAccount2v.models.withdraw import Withdraw
from BankAccount2v.models.client import Client
from BankAccount2v.models.naturalPersonClient import NPClient

def screen():
    print("\033[0;32m [0] - Finish\033[m")
    print("\033[0;32m [1] - Withdraw\033[m")
    print("\033[0;32m [2] - Deposit\033[m ")
    print("\033[0;32m [3] - Show Statement\033[m")
    print("\033[0;32m [4] - Create a new User")
    print("\033[0;32m [5] - Create new account\033[m")


def client_filter(cpf: str, clients: list) -> NPClient:
    obj = None
    for client in clients:
        if client.cpf == cpf:
            obj = client
    return obj



def account_recover(client: Client):
    if not client.account_list:
        print('\033[0;31 Client not exists\033[m')
        return
    return client.account_list[0]

def deposit(clients: list):
    cpf: str = input("Enter client's CPF ")
    client: Client = client_filter(cpf, clients)
    if not client:
        print("\033[0;31m Client not found\033[m")
        return 
    value: float = (float(input("Enter deposit value ")))
    transaction = Deposit(value)
    account = account_recover(client)
    if not account:
        return
    client.make_transaction(account, transaction)


def withdraw(clients):
    cpf: str = input("Tip client's CPF ")
    client = client_filter(cpf, clients)
    if not client:
        print("\033[0;31m Client not found\033[m")
        return
    value: float = (float(input("Enter withdraw value ")))
    transaction = Withdraw(value)
    account = account_recover(client)
    if not account:
        return
    client.make_transaction(account, transaction)

def statement_display(clients):
    cpf: str = input("Tip client's CPF ")
    client: Client = client_filter(cpf, clients)
    if not client:
        print("\033[0;31m Client not found\033[m")
        return
    account = account_recover(client)
    if not account:
        return
    print("*****Bank Statement*****")
    print("==========================")
    transact = account.historic.transaction_list
    print(transact)
    statement = ""
    if not transact:
        statement = "\033[0;31m Has no transaction yet\033[m"
    else:
        for items in transact:
            statement += f"\n{items['type']}:\n\tR${items['value']:.2f}"
    print(statement)
    print(f"Balance: {account.balance}")
    

def user_create(clients: list):
    cpf: str = input("Tip client's CPF ")
    client: NPClient = client_filter(cpf, clients)
    if not client:
        name = input("Enter clients name ")
        birthDate = input("Enter client's birth date [dd/mm/yyyy] ")
        address = input("Enter client's address ")
        client: NPClient = NPClient(name=name, birth_date=birthDate, cpf=cpf, address=address)
        clients.append(client)
        print("\033[0;33mClient successfully created\033[m")
    else:
        print("\033[0;31 user alread exists\033[m")
    return clients


def account_create(clients: list, accounts: list):
    account_number = randint(1000, 10000)
    cpf: str = input("Tip client's CPF ")
    client = client_filter(cpf, clients)
    if not client:
        print("client not found")
        return
    account: object = CurrentAccount.new_account(client, account_number)
    accounts.append(account)
    client.account_list.append(account)
    print(account)
    print(f"\033[0;32m Account successfully created\033[m")