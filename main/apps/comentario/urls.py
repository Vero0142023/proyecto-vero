from django.urls import path
from .views import *

app_name = 'apps.comentario'

urlpatterns = [
    path('comentar/<int:id>/', ComentarPostView.as_view(), name='comentar_articulo'),
    path('listado_comentario/', ListadoComentarioView.as_view(), name='listado_comentario'),
    path('agregar_comentario/', AgregarComentarioView.as_view(), name='agregar_comentario'),
    path('eliminar_comentario/<int:pk>/', DeleteComentario.as_view(), name='eliminarComentario'),
    path('detalle_post/<int:post_id>/', DetallePostView.as_view(), name='detalle_post'),
]