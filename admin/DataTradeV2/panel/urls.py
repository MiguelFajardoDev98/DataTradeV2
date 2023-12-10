from django.contrib import admin
from django.urls import path
from django import views
from . import views

from django.conf.urls import include

urlpatterns = [
    path('',views.index, name='index'),
    path('listar',views.listar,name="listar"),
    path('agregar',views.agregar,name="agregar"),
    path('actualizar',views.actualizar,name="actualizar"),
    path('eliminar',views.eliminar,name="eliminar"),
    

    

]