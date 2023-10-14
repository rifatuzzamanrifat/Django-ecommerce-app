from django.shortcuts import render
from .models import *


# Create your views here.

def product(request, id):
    cat = category.objects.get(id=id)
    prod = product_all.objects.filter(category=cat)
    return render(request, 'product/product.html', locals())
