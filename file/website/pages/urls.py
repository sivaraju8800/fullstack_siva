from django.urls import path
from . import views
urlpatterns=[
    path('master/',views.master,name='master'),
    path('',views.home,name='home'),
    path('dms/',views.dms,name='dms'),
    path('afm/',views.afm,name='afm'),
    path('co/',views.co,name='co'),
    path('java/',views.java,name='java'),
    path('os/',views.os,name='os'),
    path('dccn/',views.dccn,name='dccn'),
    path('e_commerce/',views.e_commerce,name='e_commerce'),
    path('adbms/',views.adbms,name='adbms'),
    path('ds_java/',views.ds_java,name='ds_java'),
    path('coor/',views.coor,name='coor'),
]