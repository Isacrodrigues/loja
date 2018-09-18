from django.shortcuts import render
from django.db import transaction
from django.db import models
from .models import Produto

def products_consult(request):
    return render(request, 'loja/products_consult.html', {})
def products_consult_camisas(request):
    return render(request,'loja/products_consult_camisas.html',{})

def products_consult_bones(request):
    return render(request,'loja/products_consult_bones.html',{})

def products_consult_bermudas(request):
    return render(request,'loja/products_consult_bermudas.html',{})

def products_consult_sapatos(request):
    return render(request,'loja/products_consult_sapatos.html',{})



def products_page(request):
    return render(request, 'loja/products_page.html', {})


    

def products_list(request):
    return render(request, 'loja/products_list.html', {})


 		
	
