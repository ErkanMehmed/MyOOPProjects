import sqlite3
from datetime import datetime

class DataBaseManager:
    def __init__(self, db_name: str="finance.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS wallet_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                city TEXT,
                address TEXT,
                budget REAL,
                monthly_limit REAL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                merchant TEXT,
                transaction_type TEXT,
                date TEXT
            )
        ''')

        self.conn.commit()

    def save_wallet_state(self, wallet):

        self.cursor.execute("DELETE FROM wallet_data")

        self.cursor.execute('''
            INSERT INTO wallet_data (first_name, last_name, age, city, address, budget, monthly_limit)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            wallet.user.first_name,
            wallet.user.last_name,
            wallet.user.age,
            wallet.user.city,
            wallet.user.address,
            wallet.user.budget,
            wallet.monthly_limit
        ))
        self.conn.commit()

    def save_transaction(self, transaction):

        self.cursor.execute('''
            INSERT INTO transactions (amount, category, merchant, transaction_type, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            transaction.amount,
            transaction.category,
            transaction.merchant,
            transaction.transaction_type,
            transaction.date.strftime('%Y-%m-%d %H:%M:%S')
        ))
        self.conn.commit()

    def close(self):
        self.conn.close()