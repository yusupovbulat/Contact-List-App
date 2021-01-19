from django.shortcuts import render, redirect

from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(request, "index.html", {'contacts': contacts})


def add_contact(request):
    if request.method == "POST":
        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone'],
            address=request.POST['address']
        )
        new_contact.save()
        return redirect("/")
    return render(request, "new.html")
