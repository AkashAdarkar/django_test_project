from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customers/<str:pk>',views.customers,name='customers'),
    path('about/',views.about) ,   

    path('create_order/<str:pk>',views.createOrder,name='create_order'),
    path('update_order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),

    path('create_customer/',views.createCustomer,name='create_customer'),
    path('update_customer/<str:pk>',views.updateCustomer,name='update_customer'),
    path('delete_customer/<str:pk>',views.deleteCustomer,name='delete_customer'),

]