#from django.shortcuts import render
#from .models import Post
#from .forms import ContactoForm, PostForm
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.models import Group
# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        return redirect('apps.usuario:registrar')
    
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')

        return reverse('apps.usuario:login')
    
class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')

        return reverse('apps.usuario:logout')




def home(request):
    posts = Post.objects.all()
    data= {
        'posts': posts
    }
    return render(request, 'apps/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'contacto enviado'
        else:
            data['form'] = formulario
    return render(request, 'apps/contacto.html', data)

def regaleria(request):
    return render(request, 'apps/regaleria.html')


def agregar_noticia(request):
    data = {
        'form': PostForm()
    }

    if request.method == 'POST':
        formulario = PostForm(data = request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'guardado correctamente'
        else: 
            data['form'] = formulario
    return render(request, 'apps/noticias/agregar.html', data)

def listar_noticia(request):

    return render(request, 'apps/noticias/listar.html')