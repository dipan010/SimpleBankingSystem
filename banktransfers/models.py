from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    balance = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name 

class Transactions(models.Model):
    from_field = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='from_name')
    to_field = models.ForeignKey(Customer,max_length=30,related_name='to_name',on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now_add=True)