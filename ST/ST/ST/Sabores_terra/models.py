# Create your models here.
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    ("rascunho", "Rascunho"),
    ("desabilitado", "Desabilitado"),
    ("publicado", "Publicado")
)

class Categoria(models.Model):
    cid = ShortUUIDField(unique=True, length=5, 
                         max_length=10, 
                         alphabet="abcdef12345")
    titulo = models.CharField(max_length=50,
                              help_text="Categoria do Produto")
    
    class Meta:
        verbose_name_plural = "Categorias"
   
    def __str__(self):
        return self.titulo

class Produto(models.Model):
    pid = ShortUUIDField(unique=True, length=5, 
                         max_length=10, alphabet="abcd1234")
    categoria = models.ForeignKey('Categoria', 
                                  on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=20, default="Titulo")

    descricao = models.TextField(null=True, blank=True)
    
    preco = models.DecimalField(max_digits=6,
                                decimal_places=2)
    product_status = models.CharField(choices=STATUS,
                                      max_length=12)
    em_estoque = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return self.titulo
class Cliente(models.Model):
    Nome_do_cliente =models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=20)
    def __str__(self):
        return self.Nome_do_cliente

