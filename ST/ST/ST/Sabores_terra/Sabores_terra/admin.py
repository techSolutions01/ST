from django.contrib import admin
# Register your models here.
from  Sabores_terra.models import Categoria, Produto, Cliente

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('cid', 'titulo')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'preco',
                    'product_status')
    list_filter = ('product_status', 'em_estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome_do_cliente','senha')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)