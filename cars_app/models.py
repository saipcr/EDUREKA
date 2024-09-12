from django.db import models

# Create your models here.
class Message(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    MessageText=models.TextField()

class Product(models.Model):
    Name=models.CharField(max_length=20)
    Description=models.TextField()
    price=models.IntegerField()