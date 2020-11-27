from django.shortcuts import render
from .models import *

# Create your views here.
def products(request):
    productItems= Product.objects.filter(active=True)
    context={'products':productItems}
    return render(request,'product/products.html',context)