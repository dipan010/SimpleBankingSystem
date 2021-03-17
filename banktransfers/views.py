from django.shortcuts import render,redirect
from .models import Customer,Transactions
from .forms import TransactionForm,BalanceForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def customers(request):
    customers = Customer.objects.all().order_by('id')
    return render(request,'customers.html',context={'customers':customers})
    

def transactions(request):
    transactions = Transactions.objects.all().order_by('-id')
    return render(request,'transactions.html',context={'transactions':transactions})

