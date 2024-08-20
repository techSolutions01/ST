from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def urls(request):
    return render(request, "Login.html")

def monitorshop(request):
    return render(request, "monitorshop.html")

def product_alface(request):
    return render(request, "product-alface.html")

def product_banana(request):
    return render(request, "product-banana.html")

def product_cebola(request):
    return render(request, "product-cebola.html")

def product_cominho(request):
    return render(request, "product-cominho.html")

def product_maça(request):
    return render(request, "product-maça.html")

def product_tomate(request):
    return render(request, "product-tomate.html")

def shopnow1(request):
    return render(request, "shop-now1.html")

def shopnow1(request):
    return render(request, "shop-now1.html")

def sobre(request):
    return render(request, "sobre.html")

def category_frutas(request):
    return render(request, "category-frutas.html")

def category_temperos(request):
    return render(request, "category-temperos.html")

def category_verduras(request):
    return render(request, "category-verduras.html")

def coleção(request):
    return render(request, "coleção.html")

def contate_nos(request):
    return render(request, "contate-nos.html")

def feed(request):
    return render(request, "38feed.html")
