from django.urls import path
from Sabores_terra import views


urlpatterns = [
    path('', views.index, name='product-cebola'),
]