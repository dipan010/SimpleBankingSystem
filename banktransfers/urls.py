from django.urls import path
from . import views

urlpatterns = [
     path('',views.index,name='index'),
     path('customers',views.customers,name='customers'),
     path('transactions',views.transactions,name='transactions'),
]
