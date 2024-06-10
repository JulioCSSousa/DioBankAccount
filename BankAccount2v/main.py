from utilities.operations import *

balance = 0
LIMIT_WITHDRAW: float = 500
limit_withdraw_count: int = 2
end: bool = False
choose: int = 0
clients = []
accounts = []
statement = list()
account_num: int = 1


print("\033[0;36m=============Bank===============\033[m")
while True:
    screen()
    choose = int(input("Choose the option: "))
    if choose == 0:
        print("Bye")
        break
    if choose == 1:
        withdraw(clients)
    if choose == 2:
        deposit(clients)
    if choose == 3:
        statement_display(clients)
    if choose == 4:
        user = user_create(clients)
    if choose == 5:
        account = account_create(clients, accounts)






