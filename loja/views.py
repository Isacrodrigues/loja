from django.shortcuts import render
def products_list(request):
    return render(request, 'loja/products_list.html', {})
# Create your views here.
