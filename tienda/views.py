from django.shortcuts import render

# Create your views here.
def products_list(request):
    return render(request, 'tienda/products_list.html', {})