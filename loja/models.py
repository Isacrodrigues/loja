from django.db import models
from django.db import transaction


class Produto(models.Model):
   nome = models.CharField(max_length=200)
   descricao = models.TextField(max_length=400)
   estoque = models.DecimalField( max_digits=100, decimal_places=0, default=0)
   tamanho = models.CharField(max_length=10, blank=True)
   cor = models.CharField(max_length=20, blank=True)
   preco = models.DecimalField( max_digits=1000, decimal_places=2, default=0)
	

   




	   

		
		