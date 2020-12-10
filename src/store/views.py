from django.shortcuts import render

# Create your views here.
def store(request):
    context={}
    return render(request,'store/store.html',context)

def help(request):
    context={}
    return render(request,'store/help.html',context)   


def delivery (request):
    context={}
    return render(request,'store/delivery.html',context)


