from django.urls import path
from Sabores_terra import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Login.html/', views.cadastro, name='Login'),
    path('index.html/',  views.index, name='index'),
    path('monitorshop.html/',  views.monitorshop, name='monitorshop'),
    path('product-alface.html/',  views.product_alface, name='product-alface'),
    path('product-banana.html/',  views.product_banana, name='product-banana'),
    path('product-cebola.html/',  views.product_cebola, name='product-cebola'),
    path('product-cominho.html/',  views.product_cominho, name='product-cominho'),
    path('product-maça.html/',  views.product_maça, name='product-maça'),
    path('product-tomate.html/',  views.product_tomate, name='product-tomate'),
    path('shop-now1.html/',  views.shopnow1, name='shop-now1'),
    path('sobre.html/',  views.sobre, name='sobre'),
    path('category-frutas.html/',  views.category_frutas, name='category-frutas'),
    path('category-temperos.html/',  views.category_temperos, name='category-temperos'),
    path('category-verduras.html/',  views.category_verduras, name='category-verduras'),
    path('coleção.html/',  views.coleção, name='coleção'),
    path('Contate-nos.html/',  views.contate_nos, name='contate-nos'),
    path('38feed.html/', views.feed, name='38feed'),
]
    
    
    