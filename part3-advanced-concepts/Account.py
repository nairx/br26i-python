class Account:
    def __init__(self, account_no, customer_name, email,
                 phone, account_type, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.email = email
        self.phone = phone
        self.account_type = account_type
        self.balance = balance
    def __str__(self):
        return f"{self.account_no}-{self.customer_name}"