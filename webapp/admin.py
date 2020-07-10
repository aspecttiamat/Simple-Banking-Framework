from django.contrib import admin
from .models import UserAccount, BankAccount


admin.site.register(UserAccount)
admin.site.register(BankAccount)