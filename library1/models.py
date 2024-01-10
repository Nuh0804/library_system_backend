from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings 
from uuid import uuid4
from datetime import date
# Create your models here.

class Collection(models.Model):
    Title = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)
    Author = models.CharField(max_length=250)
    count = models.IntegerField()
    def __str__(self):
        return self.Title
    

class Book(models.Model):
    ISBN = models.AutoField(primary_key=True, editable=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ISBN}'
    
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    date_taken = models.DateField(default=date.today)
    date_to_return = models.DateField(auto_now_add=False)
    is_returned = models.BooleanField(default=False)

    def clean(self):
        if self.date_to_return < self.date_taken:
            raise ValidationError('The return date cannot be earlier than the taken date.')
        
    def __str__(self):
        return f'{self.collection.Title}'



class Returned(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_returned = models.DateField(default=date.today)
    punctuality = models.BooleanField(default=False)

    def clean(self):
        if self.order.date_to_return<self.date_returned:
            return self.punctuality == True
        
