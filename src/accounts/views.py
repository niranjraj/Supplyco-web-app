from django.shortcuts import render

# Create your views here.

def sign(request):
    context={}
    return render(request,'accounts/sign.html',context)