class Transaction:
    def __init__(self):
        self.balance = 0

    def add_balance(self):
        add_num = int(input('Enter income:\n'))
        self.balance += add_num
        print('Income was added!\n')
