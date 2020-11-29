from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import *

# Create your views here.
@login_required(login_url='sign')
def products(request):
    productItems= Product.objects.filter(active=True)
    context={'products':productItems}
    return render(request,'product/products.html',context)


def logout(request):
    auth.logout(request)
    return redirect('sign')
