from django.shortcuts import render
from .models import Product,Contact
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
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



    return render(request,"signup.html")

