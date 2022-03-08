from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('productos/<int:pk>/', views.descripcion, name='descripcion'),
]