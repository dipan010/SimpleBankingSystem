from django.contrib import admin
from .models import Customer,Transactions

# Register your models here.
admin.site.register(Customer)
admin.site.register(Transactions)