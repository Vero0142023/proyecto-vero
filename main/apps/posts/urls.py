from django.urls import path
from .views import *

app_name = 'apps.posts'


urlpatterns = [
    #path('', views.mi_vista, name='mi_vista'),
    path('posts/', PostListView.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_detalle"),
    path('post/crear/', PostCreateView.as_view(), name='crear_post'),
    path('post/categoria', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/', CategoriaListView.as_view(), name='categoria_lista'),
    path('post/<int:pk>/actualizar/', PostUpdateView.as_view(), name='post_actualizar'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_eliminar'),
    path('categoria/<int:pk>/posts/', PostsPorCategoriaView.as_view(), name= 'posts_por_categoria'),
    #path('comentario/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='comentario_editar'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    
]
