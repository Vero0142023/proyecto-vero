from .models import Post, Comentario, Categoria
from .forms import ComentarioForm, CrearPostForm, NuevaCategoriaForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Comentario

# Create your views here.
#def cambio(request):
    #return render(request, 'cambio.html')

#def mi_vista(request):
    #return render(request, 'mi_vista.html')

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_individual.html"
    context_objet_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


#class PostCreateView(LoginRequiredMixin, CreateView):

#class CategoriaCreateView(LoginRequiredMixin, CreateView):

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_objet_name = 'posts'

#class CategoriaDeleteView(LoginRequiredMixin, DeleteView):


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'posts/modificar_post.html'
    success_url = reverse_lazy('apps.posts:posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/eliminar_post.html'
    success_url = reverse_lazy('apps.posts:posts')


#class ComentarioCreateView(LoginRequiredMixin, CreateView):

#class PostDetailView(DeleteView):

#class PostCreateView(CreateView):

#class CategoriaCreateView(CreateView):




class CategoriaListView(ListView):
    model = Categoria
    template_name = "posts/categoria_list.html"
    context_objet_name = 'categorias'

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "posts/categoria_confirm_delete.html"
    context_objet_name = reverse_lazy('apps.posts:categoria_list')

class PostCreateView(CreateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'posts/crear_post.html'
    success_url = reverse_lazy('apps.posts:posts')


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'posts/crear_categoria.html'

class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html'
    success_url = 'comentario/comentarios/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['posts_id']
        return super().form_valid(form)
    


