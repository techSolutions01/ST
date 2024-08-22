from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

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
   
@csrf_exempt
def cadastro(request):
     if request.method == 'GET':
        return render(request, 'cadastro.html')
     else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        

        user = User.objects.filter(username=username).first()
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return render(request, "index.html")
        
@csrf_exempt
def Login(request):
    if(request.method=="GET"):
        return render(request, "Login.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        usuario = authenticate(username=username, password=senha)
        if usuario:
            login(request,usuario)
            return HttpResponse("foi")
        else:
            return HttpResponse("Merda")
            

       