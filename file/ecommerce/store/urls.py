from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('product/<int:pk>/', views.store_detail, name='store_detail'),
    path('master/', views.master, name='master'),
]