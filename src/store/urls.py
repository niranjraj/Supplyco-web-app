from django.urls import path
from .import views


urlpatterns =[
    path('',views.store,name="store"),
    path('help/',views.help,name="help"),
    path('delivery/',views.delivery,name="delivery"),
]