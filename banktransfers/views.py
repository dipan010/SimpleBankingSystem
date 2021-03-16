from django.shortcuts import render,redirect
from .models import Customer,Transactions
from .forms import TransactionForm,BalanceForm
# Create your views here.

def index(request):
    return render(request,'banktransfers/index.html')

def customers(request):
    customers = Customer.objects.all().order_by('id')
    return render(request,'banktransfers/customers.html',context={'customers':customers})
    

def transactions(request):
    transactions = Transactions.objects.all().order_by('-id')
    #query_set = Transactions.objects.order_by('-id')
    
    return render(request,'banktransfers/transactions.html',context={'transactions':transactions})

