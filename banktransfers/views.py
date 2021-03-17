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

def transfer(request,cust_id):
    if request.method =='POST':
        cust_info = Customer.objects.get(pk=cust_id)
        customers = Customer.objects.all()
        
        form = TransactionForm(request.POST or None)
        if cust_info.balance > int(form.data['amount']):
            cust1 = Customer.objects.get(id=form.data['to_field'])
            c = cust_info.balance - int(form.data['amount'])
            d = cust1.balance + int(form.data['amount'])
            cust_info.balance = c
            cust_info.save(update_fields=['balance'])
            cust1.balance = d
            cust1.save(update_fields=['balance'])
            if form.is_valid():
                form.save(commit=True)
            
            messages.success(request,"Transaction Successfull!")
            return redirect('transactions')
        else:
            messages.error(request,"Insufficient balance!")
            return render(request,'transfer.html',context={'cust_info':cust_info,'customers':customers,'form':form})
    else:
        cust_info = Customer.objects.get(pk=cust_id)
        customers = Customer.objects.all()
        
        form = TransactionForm(initial={'from_field':cust_info})
        
        
        return render(request,'transfer.html',context={'cust_info':cust_info,'customers':customers,'form':form})
    #return render(request,'banktransfers/transfer.html')