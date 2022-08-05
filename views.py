from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse('This is our Homepage')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def skills(request):
    return render(request,'skills.html')
