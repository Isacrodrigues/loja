from django.db import models
from django.utils import timezone
from django.db import transaction
class Produto(models.Model):
   nome = models.CharField(max_length=200)
   descricao = models.TextField(max_length=600)
   #tamanho = models.CharField(max_length=10)
   #estoque = models.TextField(int)
   #cor = models.CharField(max_length=10)

		
		