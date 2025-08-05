from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('products/', views.product_list, name='products'),
    path('order/<int:product_id>/', views.create_order, name='order'),
    path('home/',views.load,name='index'),
    path('location/',views.loadl,name='location'),
]
