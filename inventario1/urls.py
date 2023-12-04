from django.contrib import admin
from django import views
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(url='/inicial/', permanent=False), name='inicio'),
    path('inicial/', views.inicial, name='inicial'),
    path('crear-pro', views.crear_producto, name='crear-pro'),
    path('modificar-producto', views.modificar_producto, name='modificar-producto'),
    path('eliminar-producto', views.eliminar_producto, name='eliminar-producto'),
    path('consultar-producto', views.consultar_producto, name='consultar-producto'),
    # Other URL patterns
]