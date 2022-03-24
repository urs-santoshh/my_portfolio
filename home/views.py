from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        description = request.POST["description"]
        contact = Contact(name=name,email=email,phone=phone,description=description)
        contact.save()
    return render(request,"contact.html")
