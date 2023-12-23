from django.urls import path
from .views import *

app_name = 'apps.posts'


urlpatterns = [
    #path('', views.mi_vista, name='mi_vista'),
    path('posts/', PostListView.as_views(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_individual"),
    path('post/', PostCreateView.as_view(), name='crear_post'),
    path('post/categoria', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/', CategoriaListlView.as_view(), name='categoria_list'),
    path('categoria/<inte:pk>/delete/', CategoriaListlView.as_view(), name='categoria_delete'),
    path('post/<int:pk>/modificar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
    
    
]
