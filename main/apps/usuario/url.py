from django.urls import path
from .import views
from .views import LoginUsuario
from django.contrib.auth import views as auth_views

app_name = 'app.usuario'

urlpatterns = [
    path('regitrar/', view.RegistrarUsuario.as_view(), name='registrar'),
    path('login/', Login.Usuario.as_view(), name='login'),
    path('logout/', view.LogoutUsuario.as_view(), name='logout')
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='passwoerd_reset_done'),
    path('reset/done/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_view.PaswordResetCompleteView.as_view(), name='pasword_reset_complete')

]