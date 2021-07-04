from django.http import HttpResponse

from django.shortcuts import render,redirect


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_delivery_staff:
                    return redirect('delivery')
            else:
                    return redirect('products')
        else:    
            return view_func(request,*args,**kwargs)
    return wrapper_func    

def delivery_users(view_func):
        def wrapper_func(request,*args,**kwargs):
            if request.user.is_delivery_staff:
                return view_func(request,*args,**kwargs)
            else:
                return redirect('sign')  
        return wrapper_func

