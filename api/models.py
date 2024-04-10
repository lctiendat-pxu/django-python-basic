from django.db import models
import uuid


class Category (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    createdAt =  models.DateTimeField(auto_now_add=True )
    updatedAt =  models.DateTimeField(auto_now=True )
    def __str__(self):
        return self.name
     
class Product (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description =  models.CharField(max_length= 500, blank=True )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdAt =  models.DateTimeField(auto_now_add=True )
    updatedAt =  models.DateTimeField(auto_now=True )
    def __str__(self):
        return self.name 
    
    

    
