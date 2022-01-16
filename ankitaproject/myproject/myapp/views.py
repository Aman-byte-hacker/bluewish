from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")

def products(request):
    product = Product.objects.filter(status="arrived")
    context = {
        'product' : product
    }
    return render(request, "products.html",context=context)

def arrivingproducts(request):
    product = Product.objects.filter(status="arriving")
    context = {
        'product' : product
    }
    return render(request, "arrivingproducts.html",context=context)

def see(request,product_id):
    product = Product.objects.filter(id=product_id)
    context = {
        'product' : product
    }
    return render(request,"see.html",context=context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name,email=email,mobilenumber=phone,message=message)
        contact.save()
        messages.success(request,"Your message has been sent successfully")
    return render(request,"contact.html")