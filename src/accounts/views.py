from django.shortcuts import render,redirect

from django.contrib.auth.hashers import check_password
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
from django.http import JsonResponse
import random
import http.client
import http
import ast
import json

conn=http.client.HTTPConnection("2factor.in")

User=get_user_model()

# Create your views here.

def sign(request):
    usererror=''
    User.objects.filter(active=False).delete()
    form2=LoginForm(request.POST or None)
    if request.POST.get('Login'):
        if form2.is_valid():
            email=form2.cleaned_data.get("email")
            password=form2.cleaned_data.get("password") 
            user= authenticate(request,username=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('products')
            else:
                
                passUser=request.user
                answer=passUser.check_password(password)
                if(not answer):
                    usererror="Invalid Password"
     
    context={'form2':form2,'usererror':usererror}            
    return render(request,'accounts/sign.html',context)

@csrf_protect
def createUser(request):
    errormsg=''
    if request.method =="POST":
        data=json.loads(request.body)
        email=data["userData"]["email"]
        aadhaar=data["userData"]["aadhaar"]
        password=data["userData"]["password"]
        confirmpassword=data["userData"]["confirmpassword"]
        newdata={
           'email':email,
            'aadhaar':aadhaar,
            'password1':password,
            'password2':confirmpassword,
            
        }
        form=SignUpForm(newdata)
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
                success=True
                
        else:
            errormsg=form.errors.as_json()
            errormsg=json.loads(errormsg)
            success=False
          
    return JsonResponse(json.dumps({'errormsg':errormsg,'success':success}),safe=False)    
    

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

@csrf_protect
def otp(request):
    if request.method=='POST':
        key=request.session['key']
        aadhaar=request.session['aadhaar']
        keyFromFront=request.body.decode('utf-8')
        if keyFromFront == str(key):
            user=User.objects.get(aadhaar=aadhaar)
            customer=Customer.objects.filter(aadhaar=aadhaar)
            customer.update(user_id=user.id)
            user.active=True
            user.save()
            success=True
        else:
            success=False    
        return JsonResponse(json.dumps(success),safe=False)     
    context={}    
    return render(request,'accounts/otp.html',context)
