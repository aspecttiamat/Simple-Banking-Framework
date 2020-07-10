from account_classes import BankAccount, User

user_accounts = []
bank_accounts = []


def create_user_account(name, email, username, password, bank_account=None):
    """
    Allows the creation of the new user account. Later will integrate withe login system.
    Note: Bank Account is not required at creation of User Account.
    """

    if bank_account:
        ph_account = bank_account
    else:
        ph_account = None

    new_account = User(name, email, username, password, ph_account)
    user_accounts.append(new_account)
    print("New user account created: " + name)


def create_bank_account(interest, type, amount):
    '''
    Allows the creation of the new bank account. Checks over all argument's to see if they're valid entries.
    '''

    account_types = ["Basic Checking", "Basic Savings", "Premiere Checking", "Premiere Savings"]
    interest_rates = [0.02, 0.05]
    i_rate = None
    a_type = None

    # Setting the Interest Rate for account
    if not interest or interest == "Default":
        i_rate = interest_rates[0]
    elif interest == interest_rates[0] or interest == interest_rates[1]:
        i_rate = interest
    else:
        print("Please Enter a Valid Interest Rate.")

    # Setting the Account Type
    if type in account_types:
        a_type = type
        print("Account created with type: " + type)
    else:
        print("Please enter a valid Account Type.")

    new_account = BankAccount(i_rate, a_type, amount)
    bank_accounts.append(new_account)