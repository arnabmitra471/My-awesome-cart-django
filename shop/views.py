from django.shortcuts import render,redirect
from .models import Product,Contact
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request,"index.html",{'products': products})

def contact_us(request):
    # Checking if the request method is POST, if it is then gathering the data
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user_email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        
        print(request.POST)
        # Performing validation of input fields in the form and showing the corresponding messages
        if first_name and last_name and user_email and feedback:
            customer_feedback = Contact(first_name=first_name,last_name=last_name,email=user_email,feedback=feedback)
            customer_feedback.save()

            messages.success(request,"Your feedback has been submitted successfully")
            return HttpResponseRedirect("/shop/contact/")
        else:
            # If any field is empty then showing the error message
            messages.error(request,"All the fields are required")
        
    return render(request,"contact.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        signup_email = request.POST.get("user_signup_email")
        signup_password = request.POST.get("user_signup_password")
        conf_pass = request.POST.get("user_signup_conf_pass")

        context = {
            "first_name": first_name,
            "last_name" : last_name,
            "signup_email":signup_email
        }

        if signup_password != conf_pass:
            messages.error(request,"Passwords do not match")
            return render(request,"signup.html",context)
        
        if User.objects.filter(email=signup_email).exists():
            messages.error(request,"Email is already taken")
            return render(request,"signup.html",context)
        
        new_user = User.objects.create_user(username=signup_email,email=signup_email,password=signup_password,first_name=first_name,last_name=last_name)
        new_user.save()
        messages.success(request,"You have registered successfully")
        return redirect("login")
    return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        user_email = request.POST.get("user_email")
        user_password = request.POST.get("user_password")
        # Authenticating the user
        user = authenticate(request,username=user_email,password=user_password)


        if user is not None:
            # if the user gets authenticated and we get a user object then logging in the user
            auth_login(request,user)
            messages.success(request,"You have logged in successfully")
            return redirect("home")
        else:
            messages.error(request,"Invalid username or password")
            
    return render(request,"login.html")
