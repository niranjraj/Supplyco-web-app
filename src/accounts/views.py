from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from  django.contrib import messages
from django.contrib.auth import authenticate, login
from store.models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib  import sessions
from django.views.decorators.csrf import csrf_protect
import random
import http.client
import http
import ast
import json

conn=http.client.HTTPConnection("2factor.in")

User=get_user_model()

# Create your views here.
@csrf_protect
def sign(request):
    User.objects.filter(active=False).delete()
    form=SignUpForm(request.POST or None)
    form2=LoginForm(request.POST or None)
    if request.POST.get('SignUp'):
        if form.is_valid():
            aadhaar=form.cleaned_data['aadhaar']
            try:
                checkingAadhaar=Customer.objects.get(aadhaar=aadhaar)
                
            except Customer.DoesNotExist:
                checkingAadhaar=False   
            if checkingAadhaar:
                key= send_otp()
                old=checkingAadhaar.phoneOtp
                if(old > 10):
                    status="Sending Otp error"     
                checkingAadhaar.phoneOtp=old+1
                checkingAadhaar.save()
                phone=checkingAadhaar.phoneNumber
                conn.request("GET","https://2factor.in/API/V1/a8254471-352a-11eb-83d4-0200cd936042/SMS/"+str(phone)+"/"+str(key)+"/supplyco")
                res=conn.getresponse()
                data=res.read()
                data=data.decode("utf-8")
                data=ast.literal_eval(data)
                form.save()
                request.session['key']=key
                request.session['aadhaar']=aadhaar

                return redirect('otp')
        else:
            errormsg=form.errors.as_json()
            errormsg=json.loads(errormsg)
            for msg in errormsg:
                print(msg)
                if msg =="aadhaar":
                    messages.error(request,'Invalid Aadhaar or Aadhaar already in use')
                elif msg=="email":
                    messages.error(request,'Invalid Email or Email already in use')
                elif msg =="password2":
                    messages.error(request,"Passwords don't match")     
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


# @receiver(post_save)
# def  checkUser(sender,**kwargs):
#     if sender is User:
#         if kwargs["created"]:
#                data=kwargs["instance"].aadhaar
#                checkingData=Customer.objects.filter(aadhaar__contains=data)
#                if checkingData:
#                    checkingData.update(user_id=kwargs["instance"].id)   

def send_otp():
    key=random.randint(1000,10000)
    return key


def otp(request):
    
    key=request.session['key']
    aadhaar=request.session['aadhaar']
    keyFromFront=request.body.decode('utf-8')
    if keyFromFront == str(key):
        user=User.objects.get(aadhaar=aadhaar)
        customer=Customer.objects.filter(aadhaar=aadhaar)
        customer.update(user_id=user.id)
        user.active=True
        user.save()
        return redirect('')
    context={}    
 
    return render(request,'accounts/otp.html',context)
