from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),               # Listagem de posts
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Detalhe do post
    path('post/new/', views.post_create, name='post_create'),      # Criação de post
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),  # Edição de post
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),  # Remoção de post
]
