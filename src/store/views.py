from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
def store(request):
    context={}
    return render(request,'store/store.html',context)

def help(request):
    context={}
    return render(request,'store/help.html',context)   


def delivery (request):
    deliveryItems=Delivery.objects.filter(active=True)
    currentUserName=request.user
    currentUser=request.user.id
    print(currentUser)
    # sending data of specific order
    if request.method=="POST":
        data=json.loads(request.body)
        if(data['action']=='check'):
              
                details=Delivery.objects.get(id=data['deliveryId'])
                address=details.deliverAddress.address
                zipcode=details.deliverAddress.zipcode
                city=details.deliverAddress.city
                phoneNumber=details.deliverAddress.phoneNumber
                orderItems=details.deliverAddress.order.orderitem_set.all()
                if details.user is None:
                    userCheck=True
                else:    
                    orderUser=details.user.id
                    if(orderUser==currentUser):
                         userCheck=True
                    else:
                        userCheck=False
                    print(orderUser)
                itemList=[]
                for item in orderItems:
                    itemName=item.product.title
                    itemQuanity=item.quantity
                    itemList.append({"itemName":itemName,"itemQuantity":itemQuanity})

                shippingInfo={
                    "address":address,
                    "city":city,
                    "zipcode":zipcode,
                    "phoneNumber":phoneNumber,
                }
                
                print(userCheck)
                return JsonResponse({"shippingInfo":shippingInfo,"itemList":itemList,"userCheck":userCheck},safe=False)   
        if(data['action']=='start'):
            user=request.user
            details=Delivery.objects.filter(id=data['startId'])
            details.update(status="Delivering")
            details.update(user=user)
            return JsonResponse("success",safe=False)   
        if(data['action']=='complete'):
            print("in complete")
            user=request.user
            details=Delivery.objects.filter(id=data['completeId'])
            details.update(status="Delivered")
            details.update(active=False)
            return JsonResponse("success",safe=False)   

    context={'deliveryItems':deliveryItems,'currentUser':currentUser,'currentUserName':currentUserName}
    return render(request,'store/delivery.html',context)


