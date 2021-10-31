from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contacts = contact(name=name,email=email,message=message)
        contacts.save()
    return render(request, 'index.html')
