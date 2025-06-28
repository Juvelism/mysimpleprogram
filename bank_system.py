from unittest import addModuleCleanup


def deposit(bal):

    depo = int(input('Amount to deposit: '))
    return bal + depo


def main():
    is_atm_open = True
    amount_balance = 0

    while is_atm_open:
        transaction = input('1. Balance \n2. Deposit \n3. Exit \n>> ')

        if transaction == '1':
            print(f'Your account balance is [ {amount_balance:,.2f} ] Php')
        elif transaction == '2':
            amount_balance = (deposit(amount_balance))
        elif transaction == '3':
            is_atm_open = False
            print('Thank you')
        else:
            print('Invalid Input')
main()