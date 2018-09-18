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
  	path('products_page.html', views.products_page, name='products_page.html') 

] 
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
