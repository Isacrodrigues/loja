from django.shortcuts import render
def products_list(request):
    return render(request, 'loja/products_list.html', {})
'''def Pagina_produto(request):
	return render(request'loja/Pagina_produto', {})
