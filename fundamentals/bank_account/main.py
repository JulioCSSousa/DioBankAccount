
balance = 0
LIMIT_WITHDRAW = 500
LIMIT_WITHDRAW_COUNT = 3
statement = []
end: bool = False
choose: int = 0
def deposit(amount):
    if amount > 0:
        global  balance 
        balance += amount
        action = {"Deposit": amount}
        statement.append(action)
    else:
        print('invalid Operation')
    
def withdraw(amount):
    global balance
    global LIMIT_WITHDRAW
    global LIMIT_WITHDRAW_COUNT
    if amount < 0:
        print("\033[0;33m Invalid Operation \033[m")
    elif amount >= LIMIT_WITHDRAW:
        print(F"\033[0;33m You can't withdraw more than your limit \033[m {LIMIT_WITHDRAW}")
    elif LIMIT_WITHDRAW_COUNT == 0:
        print(f"\033[0;33m You cannot make more withdraw today, you exceeded your limit \033[m ")
    else:
        if balance >= amount:
            balance -= amount
            LIMIT_WITHDRAW_COUNT -= 1
            action = {"Withdraw":amount}
            statement.append(action)
            print(F"\033[0;32m You can make more {LIMIT_WITHDRAW_COUNT} withdraws \033[m")
        else:
            print("\033[0;33m Not enough cash! \033[m")

print("\033[0;36m=============Bank===============\033[m")  
while end == False:
    print("\033[0;31m[1] - Withdraw\033[m")
    print("\033[0;32m[2] - Deposit\033[m ")
    print("\033[0;34m[3] - Show Statement\033[m")
    print("\033[0;33m[4] - Finish\033[m")
    choose = int(input("Choose the option: "))
    if choose == 1:
        withdraw_value = round(float(input("Enter the amount you want to withdraw ")), 2)
        withdraw(withdraw_value)
    elif choose == 2:
        deposit_value = round(float(input("Enter the amount you want to add to your balance ")), 2)
        deposit(deposit_value)
    elif choose == 3:
        print("*****Bank Statement*****")
        print("==========================")
        print(f"\033[0;36m Balance: {balance}R$\033[m")
        print("==========================")
        for item in statement:
            if "Deposit" in item.keys():
                print(f"\033[0;34m +R$", item["Deposit"], "\033[m")
            if "Withdraw" in item.keys():
                print(f"\033[0;31m -R$", item["Withdraw"], "\033[m")
        print("===========================")     
    if choose == 4:
        print("Bye")
        end = True


