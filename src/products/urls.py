from django.urls import path
from .import views


urlpatterns =[
    path('',views.products,name="products"),
    path('logout',views.logout,name='logout'),
    path('cart',views.cart,name='cart'),
    path('update_item',views.updateItem,name='update_item'),
  
]