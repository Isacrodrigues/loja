from django.shortcuts import render
from django.db import transaction
from django.db import models
from .models import Produto

def products_consult(request):
    return render(request, 'loja/products_consult.html', {})

def products_page(request):
    return render(request, 'loja/products_page.html', {})

def products_list(request):
    return render(request, 'loja/products_list.html', {})

def compra(self):
   	if Produto.estoque() > 0:
	    return(Produto.estoque(self -1), Produto.estoque.save())
 		
	
