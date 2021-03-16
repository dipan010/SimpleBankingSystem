from django import forms 
from .models import Transactions,Customer

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transactions
        fields=['from_field','to_field','amount']

class BalanceForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['balance']