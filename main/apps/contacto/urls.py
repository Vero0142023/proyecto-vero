from django.urls import path
from .import views


from django.contrib.auth import views as auth_views

app_name = 'app.contacto'

urlpatterns = [
    path('contacto/', views.ContactoUsuario.as_view(), name='contacto')
    #path('registrar/', RegistrarUsuario.as_view(), name='registrar'),
]