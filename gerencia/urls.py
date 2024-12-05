from django.urls import path
from .views import*

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    path('categorias/', listar_categorias, name='listar_categorias'),  
    path('categorias/cadastro', criar_categoria, name='criar_categoria'), 
    path('categorias/editar/<int:pk>', editar_categoria, name='editar_categoria'),  
    path('categorias/excluir/<int:pk>', excluir_categoria, name='excluir_categoria'), 
    # Add your URL patterns here
]