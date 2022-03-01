from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base'),
    path('lista_cuadros', views.listaCuadros, name='lista_cuadros'),
    path('cuadros/insertar', views.insertarCuadro, name='insertar_cuadro'),
    path('cuadros/modificar/<str:pk>', views.modificarCuadro, name='modificar_cuadro'),
    path('cuadros/eliminar/<str:pk>', views.eliminarCuadro, name='eliminar_cuadro'),
    path('lista_galerias', views.listaGalerias, name='lista_galerias'),
    path('galerias/insertar', views.insertarGaleria, name='insertar_galeria'),
    path('galerias/modificar/<str:pk>', views.modificarGaleria, name='modificar_galeria'),
    path('galerias/eliminar/<str:pk>', views.eliminarGaleria, name='eliminar_galeria')
]