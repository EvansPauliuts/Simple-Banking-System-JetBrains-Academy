# Write your code here
from random import randint


class GenerateAccount:
    def generate_card_number(self):
        card_num = '400000'
        card_num += self.generate_account_number(9, 0, 9)
        card_numbers = [int(x) for x in card_num]
        processed_n = self.process_numbers(card_numbers)
        check_n = self.check_digit(processed_n)

        card_num += str(check_n)

        return card_num, self.generate_account_number(4, 0, 9)

    @staticmethod
    def generate_account_number(a, b, c):
        account_num = ''
        for _ in range(0, a):
            account_num += str(randint(b, c))
        return account_num

    @staticmethod
    def process_numbers(num):
        for i in range(0, len(num), 2):
            num[i] *= 2
        num = [x-9 if x > 9 else x for x in num]
        return num

    @staticmethod
    def check_digit(card_num):
        num_sum = sum(card_num)
        check_d = 0

        while True:
            if (num_sum + check_d) % 10 == 0:
                break
            check_d += 1

        return check_d


class BankingSystem:
    def __init__(self):
        self.card_number = ''
        self.card_pin = ''

    def card_pin_account(self):
        account_bnk = GenerateAccount()
        card_number, card_pin = account_bnk.generate_card_number()

        self.card_number = card_number
        self.card_pin = card_pin

        print('Your card has been created')
        print('Your card number:')
        print(self.card_number)

        print('Your card PIN:')
        print(self.card_pin)
        print()

    def log_info_account(self):
        flag = False
        card_number_input = input('Enter your card number:\n')
        card_pin_input = input('Enter your PIN:\n')

        if card_number_input == self.card_number and card_pin_input == self.card_pin:
            print('\nYou have successfully logged in!\n')
            flag = True
        else:
            print('\nWrong card number or PIN!\n')

        while flag:
            name_input = self.menu_balance()

            if name_input == 1:
                print('Balance: 0\n')
            elif name_input == 2:
                print('You have successfully logged out!\n')
                break
            elif name_input == 0:
                self.exit()

    @staticmethod
    def menu_balance():
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')

        user_input = int(input())
        print()

        return user_input

    @staticmethod
    def menu_card():
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')

        user_input = int(input())
        print()

        return user_input

    @staticmethod
    def exit():
        print('Bye!')
        exit()

    def run(self):
        while True:
            menu_card = self.menu_card()

            if menu_card == 1:
                self.card_pin_account()
            elif menu_card == 2:
                self.log_info_account()
            elif menu_card == 0:
                self.exit()


def main():
    banking_system = BankingSystem()
    banking_system.run()


if __name__ == '__main__':
    main()
