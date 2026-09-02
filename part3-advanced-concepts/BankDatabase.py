import sqlite3
class BankDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("bank.db")
        self.cursor = self.connection.cursor()
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_no INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                account_type TEXT,
                balance REAL DEFAULT 0,
                status TEXT DEFAULT 'Active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_no INTEGER,
                transaction_type TEXT,
                amount REAL,
                transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                description TEXT,
                FOREIGN KEY(account_no)
                REFERENCES accounts(account_no)
            )
        """)
        self.connection.commit()