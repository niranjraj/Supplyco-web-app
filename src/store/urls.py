from django.urls import path
from .import views


urlpatterns =[
    path('',views.store,name="store"),
    path('sign/',views.sign,name="sign"),
     path('help/',views.help,name="help"),
]