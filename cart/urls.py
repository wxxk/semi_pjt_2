"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('delete/<int:product_id>/<str:product_color>/<str:product_size>/', views.delete_cart, name='delete_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('revise_cart/<int:product_id>/<str:product_color>/<str:product_size>/', views.revise_cart, name='revise_cart'),
]