from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('NTR/',views.NTR,name='NTR'),
    path('pk/',views.pk,name='pk'),
    path('prabhas/',views.prabhas,name='prabhas'),
    path('RC/',views.RC,name='RC'),
    path('siva/',views.siva,name='siva'),
]










# def home(request):
#     return render(request,'home.html')
# def NTR(request):
#     return render(request,'NTR.html')
# def pk(request):
#     return render(request,'pk.html')
# def prabhas(request):
#     return render(request,'prabhas.html')
# def RC(request):
#     return render(request,'Rc.html')
# def siva(request):
#      return render(request,'siva.html')