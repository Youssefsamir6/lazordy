from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.select_related('category').all().order_by('name')
    return render(request, 'inventory/product_list.html', {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {"product": product})
