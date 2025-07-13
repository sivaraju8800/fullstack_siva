from django.shortcuts import render

def master(request):
    return render(request,'master.html')

def home(request):
    return render(request,'home.html')

# subject 01
def dms(request):
    return render(request,'dms.html')

def afm(request):
    return render(request,'afm.html')

def co(request):
    return render(request,'co.html')

def java(request):
    return render(request,'java.html')

def os(request):
    return render(request,'os.html')

# subject 02
def adbms(request):
    return render(request,'adbms.html')

def coor(request):
    return render(request,'coor.html')

def dccn(request):
    return render(request,'dccn.html')

def ds_java(request):
    return render(request,'ds_java.html')

def e_commerce(request):
    return render(request,'e_commerce.html')
