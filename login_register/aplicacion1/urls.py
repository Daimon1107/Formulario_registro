from django.urls import path
from . import views
from .views import Registro

urlpatterns = [
    path('inicio/',views.inicio,name='inicio'),
    path('',Registro.as_view(),name='registro'),
    
]