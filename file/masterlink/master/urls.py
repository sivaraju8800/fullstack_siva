from django.urls import path
from . import views
urlpatterns=[
    path('master/',views.master,name='master'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
]