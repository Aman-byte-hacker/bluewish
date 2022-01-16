from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200);
    description = models.TextField(max_length=5000)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="uploads/images")
    discount = models.PositiveIntegerField(default=0)
    productstatus = [
        ('arriving','arriving'),
        ('arrived','arrived')
    ]
    status = models.CharField(choices=productstatus,max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    mobilenumber = models.PositiveIntegerField(default=0)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return self.name        

          