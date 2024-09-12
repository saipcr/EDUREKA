from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.response import Response

global cart_box
cart_box=[]
# Create your views here.
def home(request):
    return render(request,"base.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("Name")
        email=request.POST.get("Email")
        message1=request.POST.get("Message")
        
        if name !=None or name!="":
            message=models.Message(Name=name,Email=email,MessageText=message1)

            message.save()
        
            print("Created User")
            print(contact)
    return render(request,"contacts.html")


@api_view(['GET'])
def getProduct(request):
    
    products=models.Product.objects.all()
    productSerializer=ProductSerializer(products,many=True)
    
    return render(request,"product.html",{"data":productSerializer.data})

@api_view(['POST'])
def cart(request,product):
    if request.method=="POST":    
        products=models.Product.objects.all()
        productSerializer=ProductSerializer(products,many=True)
        for prod in productSerializer.data:
            if prod["Name"]==product:
                globals()['cart_box'].append(prod)
    return render(request,"product.html",{"data":productSerializer.data})

def checkout(request):
    if globals()['cart_box']==[]:
        products=models.Product.objects.all()
        productSerializer=ProductSerializer(products,many=True)
        return render(request,"product.html",{"data":productSerializer.data})
    else:
        bought=[]
        total=0
        for s in globals()['cart_box']:
            print(s)
            total+=s["price"]
            bought.append(s)
        globals()['cart_box']=[]
        return render(request,"cart.html",{"Total":total,'cart':bought})
    