from django.db import models
from django.shortcuts import render,redirect
from .models import User,Product,Wishlist,Cart
import random
from django.conf import settings
from django.core.mail import send_mail

# models
class User(models.Modesl):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    address=models.TextField()
    password=models.CharField(max_lenght=100)
    profile_pic=models.ImageField(upload_to='profile_pic/',default='')
    usertype=models.CharField(max_length=100,default='buyer')

    def __str__(self):
        return self.fname+''+self.lname



# views
def signup(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg='Email Already Registered'
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    address=request.POST['address'],
                    profile_pic=request.FILES['profile_pic'],
                    usertype=request.POST['usertype'],
                )
                msg='User Sign Up Successfully'
                return render(request,'signup.html',{'msg':msg})
            else:
                msg='Password & Confirm Password Does Not Matched'
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')
    
def login(request):
    