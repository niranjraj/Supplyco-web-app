from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from  django.contrib import messages
from django.contrib.auth import authenticate, login
from store.models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User=get_user_model()

# Create your views here.

def sign(request):
    form=SignUpForm(request.POST or None)
    form2=LoginForm(request.POST or None)
    if request.POST.get('SignUp'):
        if form.is_valid():
            form.save()
            return redirect('sign')
    elif request.POST.get('Login'):
        if form2.is_valid():
            email=form2.cleaned_data.get("email")
            password=form2.cleaned_data.get("password") 
            user= authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('products')
            else:
                return redirect('sign')    
            
    context={'form':form,'form2':form2}            
    return render(request,'accounts/sign.html',context)

@receiver(post_save)
def  checkUser(sender,**kwargs):
    if sender is User:
        if kwargs["created"]:
               data=kwargs["instance"].aadhaar
               checkingData=Customer.objects.filter(aadhaar__contains=data)
               if checkingData:
                   checkingData.update(user_id=kwargs["instance"].id)    