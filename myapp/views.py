from asyncio.log import logger
import email
from unicodedata import name
from django.forms import PasswordInput
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            remarks=request.POST['remarks']
        )

        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Email Already Registered"
            return render(request, 'signup.html', {'msg': msg})

        except:
            if request.POST['password'] == request.POST['cpassword']:

                User.objects.create(
                    usertype=request.POST['usertype'],
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    cpassword=request.POST['cpassword'],
                    address=request.POST['address']
                )
                msg = "User Signup Successfully"
                print(msg)
                return render(request, 'signin.html', {'msg': msg})
            else:
                msg = "Password & Confirm Password Does Not Matched"
                return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method=="POST":
        try:
            user=User.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            if user.usertype == "user":
                request.session['fname']=user.fname
                request.session['email']=user.email
                return render(request,'index.html')
            elif user.usertype == "seller":
                request.session['fname']=user.fname
                request.session['email']=user.email
                return render(request,'upload_book.html')

        except:
            msg="Email or Password are Incorrect"
            return render(request,'signin.html',{'msg':msg})
    else:
        return render(request,'signin.html')


def signout(request):
    try:
        del request.session['fname']
        del request.session['email']
        return render(request,'signin.html')
    except:
        return render(request,'signin.html')
    
    
def categories(request):
    return render(request,'categories.html')


def upload_book(request):
    if request.method == "POST":
        Books.objects.create(
            book_name = request.POST['book_name'],
            book_image = request.POST['book_image'],
            category_id = request.POST['category_id'],
            book_description = request.POST['book_description'],
            book_price = request.POST['book_price'],
            publisher = request.POST['publisher']
        )
        return render(request,'upload_book.html')
    else:
        return render(request,'upload_book.html')

def managebooks(request):
    try:
        publishedBooks = Books.objects.all()
        books = {
            "allbooks": publishedBooks
           
        }
        
        return render(request,'managebooks.html', books)
    except: 
        return render(request,'managebooks.html')