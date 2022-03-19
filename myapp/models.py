from email import message
from unicodedata import category
from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    remarks = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)
    address = models.TextField()
    usertype=models.CharField(max_length=100,default="user")

    def __str__(self):
        return self.fname+" - "+self.usertype

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)

class Books(models.Model):
    bookid = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_image = models.ImageField()
    book_description = models.TextField()
    book_price = models.IntegerField()
    publisher = models.CharField(max_length=100)
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)



    
