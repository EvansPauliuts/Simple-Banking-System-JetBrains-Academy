import sqlite3


class DBManager:
    def __init__(self, db_conn):
        self.conn = sqlite3.connect(db_conn)
        self.cur = self.conn.cursor()
        self.CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY,
            number TEXT UNIQUE,
            pin TEXT,
            balance INTEGER DEFAULT 0
        );
        """
        self.INSERT_ACCOUNT_CARD = "INSERT INTO card (number, pin) VALUES (?, ?);"
        self.GET_PIN_AND_NUMBER = "SELECT pin FROM card WHERE number = ?;"
        self.GET_BALANCE = "SELECT balance FROM card WHERE number = ?;"
        self.UPDATE_BALANCE = "UPDATE card SET balance = ? WHERE number = ?;"
        self.DELETE_ACCOUNT_CARD = "DELETE FROM card WHERE number = ?;"

    def close_cursor(self):
        self.conn.close()

    def create_table(self):
        self.cur.execute(self.CREATE_TABLE)

    def insert_card(self, number, pin):
        self.cur.execute(self.INSERT_ACCOUNT_CARD, (number, pin))
        self.conn.commit()

    def get_pin_and_number(self, number):
        pin = self.cur.execute(self.GET_PIN_AND_NUMBER, (number, )).fetchone()
        return -1 if pin is None else pin[0]

    def get_balance(self, number):
        balance = self.cur.execute(self.GET_BALANCE, (number, )).fetchone()
        return -1 if balance is None else balance[0]

    def update_balance(self, card_num, add_balance):
        self.cur.execute(self.UPDATE_BALANCE, (add_balance, card_num))
        self.conn.commit()

    def delete_account_card(self, account_id):
        self.cur.execute(self.DELETE_ACCOUNT_CARD, (account_id, ))
        self.conn.commit()
