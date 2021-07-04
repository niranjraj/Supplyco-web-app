from django.urls import path
from .import views


urlpatterns =[
    path('',views.sign,name="sign"),
    path('otp',views.otp,name="otp"),
    path('createUser',views.createUser,name="createUser"),
   
]