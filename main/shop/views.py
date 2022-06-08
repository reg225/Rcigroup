from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    Products = Product.objects.all
    return render(request, 'product.html', {'Product': Products} )

def product1(request):
    return render(request, 'product1.html')

def andex(request):
    return render(request, 'andex.html')

def tile(request):
    return render(request, 'tile.html')

def b12(request):
    return render(request, 'b12.html')

def white(request):
    return render(request, 'white.html')

def grout(request):
    return render(request, 'grout.html')

def polish(request):
    return render(request, 'polish.html')
