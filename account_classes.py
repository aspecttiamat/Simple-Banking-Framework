class User:
    '''
    The base User class. This will be used during account creation as well as login.
    Can be linked up with bank accounts.
    '''

    def __init__(self, name, username, password, email, bank_account):
        self.name = name
        self.user = username
        self.pswd = password
        self.email = email
        self.account = bank_account
        if bank_account:
            self.account = bank_account
        else:
            self.account = None

    def user_info(self):
        # Returns the base user info, nothing personal though.

        return self.name, self.user, self.email

    def connect_account(self, account):
        # Later on, will be used for linking the User's new bank account to the User Account.

        if account:
            self.account = account
            print("Account linked.")
        else:
            print("Invalid Account.")


class BankAccount:
    '''
    The base Bank Account class. Later will be tied into the user account, and will be used to handle
    the transferring and processing of user funds.
    '''

    def __init__(self, interest, type, balance):
        self.i_rate = interest
        self.type = type
        self.balance = balance

    def deposit(self, amt):
        # Simple Deposit method.

        self.balance += amt

    def withdrawal(self, amt):
        # Simple Withdrawal.

        self.balance -= amt

    def transfer(self, usr, amt):
        # Simple user2user transfer.

        if usr and self.balance >= amt:
            self.balance -= amt
            usr.balance += amt

    def check_balance(self):
        # Returns the current balance of the bank account.

        return self.balance

    def accrue_interest(self):
        # Used to accredit the bank account interest based off of the interest rate.

        if self.balance > 0:
            self.balance += (self.balance * self.i_rate)