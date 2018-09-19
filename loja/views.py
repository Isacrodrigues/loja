from django.shortcuts import render
from django.db import transaction
from django.db import models
from .models import Produto




def products_list(request):
    return render(request, 'loja/products_list.html', {})

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

def products_page_camisa_verde(request):
    return render(request, 'loja/paginas_produtos/products_page_camisa_verde.html', {})

def products_page_camisa_vermelha(request):
    return render(request, 'loja/paginas_produtos/products_page_camisa_vermelha.html', {})

def products_page_camisa_rosa(request):
    return render(request, 'loja/paginas_produtos/products_page_camisa_rosa.html', {})

def products_page_bermuda_jeans(request):
    return render(request, 'loja/paginas_produtos/products_page_bermuda_jeans.html', {})

def products_page_bermuda_bege(request):
    return render(request, 'loja/paginas_produtos/products_page_bermuda_bege.html', {})

def products_page_bermuda_cinza(request):
    return render(request, 'loja/paginas_produtos/products_page_bermuda_cinza.html', {})

def products_page_sapato_bege(request):
    return render(request, 'loja/paginas_produtos/products_page_sapato_bege.html', {})

def products_page_sapato_marrom(request):
    return render(request, 'loja/paginas_produtos/products_page_sapato_marrom.html', {})    

def products_page_tenis_preto(request):
    return render(request, 'loja/paginas_produtos/products_page_tenis_preto.html', {})

def products_page_bone_vermelho(request):
    return render(request, 'loja/paginas_produtos/products_page_bone_vermelho.html', {})

def products_page_bone_cinza(request):
    return render(request, 'loja/paginas_produtos/products_page_bone_cinza.html', {})

def products_page_bone_verde(request):
    return render(request, 'loja/paginas_produtos/products_page_bone_verde.html', {})


 		
	
