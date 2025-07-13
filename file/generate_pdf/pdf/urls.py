from django.urls import path
from . import views

urlpatterns = [
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
     path('', views.home, name='home'),
]