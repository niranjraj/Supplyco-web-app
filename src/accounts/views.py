from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from  django.contrib import messages
from django.contrib.auth import authenticate, login



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