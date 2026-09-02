class Bank:
    def __init__(self, database):
        self.database = database
    def create_account(self, account):
        query = """
            INSERT INTO accounts
            (account_no, customer_name, email, phone,
             account_type, balance)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.database.cursor.execute(
            query,
            (
                account.account_no,
                account.customer_name,
                account.email,
                account.phone,
                account.account_type,
                account.balance
            )
        )
        self.database.connection.commit()
        print("Account created successfully.")

    def deposit(self, account_no, amount):
        query = """
            UPDATE accounts
            SET balance = balance + ?
            WHERE account_no = ?
            AND status = 'Active'
        """
        self.database.cursor.execute(
            query,
            (amount, account_no)
        )
        if self.database.cursor.rowcount == 0:
            print("Account not found.")
            return
        self.database.cursor.execute("""
            INSERT INTO transactions
            (account_no, transaction_type, amount, description)
            VALUES (?, ?, ?, ?)
        """, (
            account_no,
            "DEPOSIT",
            amount,
            "Money deposited"
        ))
        self.database.connection.commit()
        print("Deposit successful.")

    def withdraw(self, account_no, amount):

        self.database.cursor.execute("""
            SELECT balance
            FROM accounts
            WHERE account_no = ?
            AND status = 'Active'
        """, (account_no,))

        result = self.database.cursor.fetchone()

        if result is None:
            print("Account not found.")
            return

        balance = result[0]

        if amount > balance:
            print("Insufficient balance.")
            return

        self.database.cursor.execute("""
            UPDATE accounts
            SET balance = balance - ?
            WHERE account_no = ?
        """, (amount, account_no))

        self.database.cursor.execute("""
            INSERT INTO transactions
            (account_no, transaction_type, amount, description)
            VALUES (?, ?, ?, ?)
        """, (
            account_no,
            "WITHDRAW",
            amount,
            "Money withdrawn"
        ))

        self.database.connection.commit()

        print("Withdrawal successful.")

    def check_balance(self, account_no):

        self.database.cursor.execute("""
            SELECT customer_name, balance
            FROM accounts
            WHERE account_no = ?
        """, (account_no,))

        result = self.database.cursor.fetchone()

        if result:
            print("\nCustomer :", result[0])
            print("Balance  :", result[1])
        else:
            print("Account not found.")


    def view_account(self, account_no):
        self.database.cursor.execute("""
            SELECT account_no,
                customer_name,
                email,
                phone,
                account_type,
                balance,
                status
            FROM accounts
            WHERE account_no = ?
        """, (account_no,))
        account = self.database.cursor.fetchone()
        if account:
            print("\n-----------------------------")
            print("       ACCOUNT DETAILS")
            print("-----------------------------")
            print("Account No   :", account[0])
            print("Name         :", account[1])
            print("Email        :", account[2])
            print("Phone        :", account[3])
            print("Account Type :", account[4])
            print("Balance      :", account[5])
            print("Status       :", account[6])
        else:
            print("Account not found.")


    def transaction_history(self, account_no):
        self.database.cursor.execute("""
            SELECT transaction_id,
                transaction_type,
                amount,
                transaction_date,
                description
            FROM transactions
            WHERE account_no = ?
            ORDER BY transaction_id DESC
        """, (account_no,))

        transactions = self.database.cursor.fetchall()
        print("\nTransaction History")
        print("-" * 70)
        for transaction in transactions:
            print(
                transaction[0],
                transaction[1],
                transaction[2],
                transaction[3],
                transaction[4]
            )