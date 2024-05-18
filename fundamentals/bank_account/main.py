from time import sleep
balance = 0
LIMIT_WITHDRAW: float = 500
limit_withdraw_count: int = 2
end: bool = False
choose: int = 0
users = list()
statement = list()
account_num: int = 1

def screen():
    print("\033[0;32m [0] - Finish\033[m")
    print("\033[0;32m [1] - Withdraw\033[m")
    print("\033[0;32m [2] - Deposit\033[m ")
    print("\033[0;32m [3] - Show Statement\033[m")
    print("\033[0;32m [4] - Create a new User")
    print("\033[0;32m [5] - Show users\033[m")
    print("\033[0;32m [6] - Create new account\033[m")

def deposit(amount):
    if amount > 0:
        global  balance
        balance += amount
        action = {"Deposit": amount}
        statement.append(action)
    else:
        print('invalid Operation')
    
def withdraw(amount, balance, limit_withdraw_count):
        balance -= amount
        action = {"Withdraw":amount}
        statement.append(action)
        print(F"\033[0;32m You can make more {limit_withdraw_count} withdraws \033[m")

def withdraw_validations(amount, balance, limit_withdraw, limit_withdraw_count):
    if amount < 0:
        return "\033[0;31m Invalid Operation \033[m"
    elif amount >= limit_withdraw:
        return F"\033[0;31m You can't withdraw more than your limit \033[m {limit_withdraw}"
    elif limit_withdraw_count < 0:
        return f"\033[0;31m You cannot make more withdraw today, you exceeded your limit \033[m "
    elif balance < amount:
        return f"\033[0;31m Not enough cash! \033[m "

def statement_display():
    print("*****Bank Statement*****")
    print("==========================")
    print(f"\033[0;36m Balance: {balance}R$\033[m")
    print("==========================")
    for item in statement:
        if "Deposit" in item.keys():
            print(f"\033[0;34m +R$", item["Deposit"], "\033[m")
        if "Withdraw" in item.keys():
            print(f"\033[0;31m -R$", item["Withdraw"], "\033[m")
def user_create(name, birthdate, cpf, street, num, district, city, state):
    new = {cpf: {"Name": name, "Birthdate":birthdate, "Address": {"Street": street, "Num": num, "District": district, "City": city, "State": state},
     "Accounts" : []}}
    users.append(new)
def create_user_validation(cpf):
    for item in users:
        if cpf in item.keys():
            return "CPF alread exists"
def account_create(cpf):
    global account_num
    for new_account in users:
        if cpf in new_account.keys():
            account = {"Agency": "0001", "account number": account_num}
            new_account[cpf]["Accounts"].append(account)
            account_num += 1

print("\033[0;36m=============Bank===============\033[m")  
while True:
    screen()
    choose = int(input("Choose the option: "))
    if choose == 0:
        print("Bye")
        break
    if choose == 1:
        withdraw_value = round(float(input("Enter the amount you want to withdraw ")), 2)
        valid = withdraw_validations(withdraw_value, balance, LIMIT_WITHDRAW, limit_withdraw_count)
        if valid:
            print(valid)
            sleep(1)
            print()
        else:
            withdraw(withdraw_value, balance, limit_withdraw_count)
            limit_withdraw_count -= 1
    if choose == 2:
        deposit_value = round(float(input("Enter the amount you want to add to your balance ")), 2)
        deposit(deposit_value)
    if choose == 3:
        statement_display()
    if choose == 4:
        name = input("Write your name ")
        birthdate = input("Tip you birthday [yyyy/mm/dd] ")
        cpf = input("Tip your CPF ")
        uservalid = create_user_validation(cpf)
        if uservalid:
            print(uservalid)
            account_create(cpf)
            print(users)
        else:
            street, num, district, city, state = input("Tip your address: [street - number - distric - city - state] ").split('-')
            user_create(name, birthdate,cpf, street, num, district,city, state)
            account_create(cpf)
            print(users)
    if choose == 5:
        for i in users:
            print(i)
    if choose == 6:
        cpf = input("Tip your CPF ")
        account_create(cpf)
        print("Bounding you new account to your cpf....")
        sleep(2)
        for user in users:
            print(user)





