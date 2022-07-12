from django.urls import path
from . import views


urlpatterns = [

path('menu/',views.menu),
path('informacion/',views.informacion ,name='informacion'),  
path('registro/',views.registro, name='registro'),  
path('login',views.login, name='login'),
path('',views.registro, name='login'),
]
