from django.db import models
from django.utils.translation import gettext_lazy as _


class UserAccount(models.Model):
    """
    This class is the base model for the User's Account. All relevant information is stored in
    objects of this class.
    """
    name = models.CharField("Name", max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=30, default="")

    def __str__(self):
        return 'User: {}'.format(self.name)


class BankAccount(models.Model):
    """
    This is the baes model for the Bank Accounts. All related data is stored within objects of this class.
    """
    class AccountType(models.TextChoices):
        """
        Account type class, simple.
        """
        SIMPLECHECKING = 'SC', _('Simple Checking')
        PREMIERECHECKING = 'PC', _('Premiere Checking')
        SIMPLESAVINGS = 'SS', _('Simple Savings')
        PREMIERESAVINGS = 'PS', _('Premiere Savings')

    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=AccountType.choices, default=AccountType.SIMPLECHECKING)
    account_balance = models.DecimalField("Balance", max_digits=1000000000, decimal_places=2, default=0.00)

    def deposit(self, amt):
        # Self explanatory, a method to deposit into the account.
        self.account_balance += amt

    def withdrawal(self, amt):
        # As above, but for taking money out.
        self.account_balance -= amt
