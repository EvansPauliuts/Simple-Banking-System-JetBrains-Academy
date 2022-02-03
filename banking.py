# Write your code here
from random import randint

from db import DBManager
from transacion import Transaction


db = DBManager('card.s3db')
db.create_table()

transaction_account = Transaction()


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

    @staticmethod
    def check_algorithm_luhn(card_number):
        n_digits = len(card_number)
        n_sum = 0
        is_second = False

        for i in range(n_digits - 1, -1, -1):
            d = ord(card_number[i]) - ord('0')

            if is_second:
                d = d * 2

            n_sum += d // 10
            n_sum += d % 10

            is_second = not is_second

        if n_sum % 10 == 0:
            return n_sum

        return False


class BankingSystem:
    def __init__(self):
        self.card_number = ''
        self.card_pin = ''

    def card_pin_account(self):
        account_bnk = GenerateAccount()
        card_number, card_pin = account_bnk.generate_card_number()

        self.card_number = card_number
        self.card_pin = card_pin

        db.insert_card(card_number, card_pin)

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

        if db.get_pin_and_number(card_number_input) == card_pin_input:
            print('\nYou have successfully logged in!\n')
            flag = True
        else:
            print('\nWrong card number or PIN!\n')

        while flag:
            name_input = self.menu_balance()

            if name_input == 1:
                balance = db.get_balance(card_number_input)
                print(f'Balance: {balance}\n')
            elif name_input == 2:
                transaction_account.add_balance()
                db.update_balance(card_number_input, transaction_account.balance)
            elif name_input == 3:
                print('Transfer')
                card_number_check = input('Enter card number:\n')

                check_alg = GenerateAccount.check_algorithm_luhn(card_number_check)

                if check_alg:
                    check_card = db.get_card_number_check(card_number_check)

                    if check_card == -1:
                        print('Such a card does not exist.')
                    if check_card == card_number_input:
                        print('You can\'t transfer money to the same account!\n')
                    else:
                        self.do_transactions(db.get_balance(card_number_input), card_number_input, card_number_check)
                else:
                    print('Probably you made a mistake in the card number. Please try again!\n')
            elif name_input == 4:
                db.delete_account_card(card_number_input)
                print('The account has been closed!\n')
                break
            elif name_input == 5:
                print('You have successfully logged out!\n')
                break
            elif name_input == 0:
                db.close_cursor()
                self.exit()

    @staticmethod
    def do_transactions(balance_db, card_number, card_transfer):
        money_transfer = int(input('Enter how much money you want to transfer:\n'))

        if balance_db >= money_transfer:
            subtraction_money = balance_db - money_transfer
            db.update_balance(card_number, subtraction_money)
            db.update_balance(card_transfer, money_transfer)
            print('Success!\n')
        else:
            print('Not enough money!\n')


    @staticmethod
    def menu_balance():
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
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
