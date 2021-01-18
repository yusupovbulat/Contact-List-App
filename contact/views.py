from django.shortcuts import render, redirect

from .models import Contact

# Create your views here.


def index(request):
    return render(request, "index.html")


def add_contact(request):
    if request.method == "POST":
        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address']
        )
        new_contact.save()
        return redirect("/")
    return render(request, "new.html")
