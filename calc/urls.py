from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('add',views.add, name='add'),
    path('customer/<str:pk_test>/',views.customer, name='customer'),
    path('create_order/',views.createOrder, name='create_order'),
    path('update_order/<str:pk>/',views.updateOrder, name='update_order'),
]