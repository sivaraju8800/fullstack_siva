from django.shortcuts import render, get_object_or_404
from .models import store
def store_list(request):
    ob_products = store.objects.all()
    return render(request, 'product_list.html', {'products': ob_products})

def store_detail(request, pk):
    ob_product = get_object_or_404(store, pk=pk)
    return render(request, 'product_detail.html', {'product': ob_product})

def master(request):
    return render(request,'master.html')