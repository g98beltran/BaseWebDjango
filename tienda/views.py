from django.shortcuts import render
from .models import Producto

# Create your views here.
def products_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/products_list.html', {'productos': productos})