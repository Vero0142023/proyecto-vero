from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Contacto, Post


class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'first_name','last_name', 'password', 'password2', 'email', 'imagen']  # 

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ['email']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' 
        widgets = {
            'fecha_creacion': forms.SelectDateWidget()
        }