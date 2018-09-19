from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.products_list, name='products_list.html'),
    path('products_consult.html', views.products_consult, name='products_consult.html'),
    path('products_consult_camisas.html', views.products_consult_camisas, name='products_consult_camisas.html'),
    path('products_consult_bones.html', views.products_consult_bones, name='products_consult_bones.html'),
    path('products_consult_bermudas.html', views.products_consult_bermudas, name='products_consult_bermudas.html'),
    path('products_consult_sapatos.html', views.products_consult_sapatos, name='products_consult_sapatos.html'), 
  	path('products_page.html', views.products_page, name='products_page.html'),
  	path('paginas_produtos/products_page_camisa_rosa.html', views.products_page_camisa_rosa, name='products_page_camisa_rosa.html'),
  	path('paginas_produtos/products_page_camisa_vermelha.html', views.products_page_camisa_vermelha, name='products_page_camisa_vermelha.html'),
  	path('paginas_produtos/products_page_camisa_verde.html', views.products_page_camisa_verde, name='products_page_camisa_verde.html'),
    path('paginas_produtos/products_page_bone_vermelho.html', views.products_page_bone_vermelho, name='products_page_bone_vermelho.html'),
    path('paginas_produtos/products_page_bone_verde.html', views.products_page_bone_verde, name='products_page_bone_verde.html'),
    path('paginas_produtos/products_page_bone_cinza.html', views.products_page_bone_cinza, name='products_page_bone_cinza.html'),
    path('paginas_produtos/products_page_bermuda_bege.html', views.products_page_bermuda_bege, name='products_page_bermuda_bege.html'),
    path('paginas_produtos/products_page_bermuda_cinza.html', views.products_page_bermuda_cinza, name='products_page_bermuda_cinza.html'),
    path('paginas_produtos/products_page_bermuda_jeans.html', views.products_page_bermuda_jeans, name='products_page_bermuda_jeans.html'),
    path('paginas_produtos/products_page_sapato_bege.html', views.products_page_sapato_bege, name='products_page_sapato_bege.html'),
    path('paginas_produtos/products_page_sapato_marrom.html', views.products_page_sapato_marrom, name='products_page_sapato_marrom.html'),
    path('paginas_produtos/products_page_tenis_preto.html', views.products_page_tenis_preto, name='products_page_tenis_preto.html')

] 
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
