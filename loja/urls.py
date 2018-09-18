from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.products_list, name='products_list.html'),
    path('products_consult.html', views.products_consult, name='products_consult.html'), 
  	path('products_page.html', views.products_page, name='products_page.html') 

] 
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
