from django.urls import path, include
from . import views

urlpatterns = [
    path('lista/', views.listar, name='listar')
]