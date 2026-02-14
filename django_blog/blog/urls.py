from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='posts'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/update/', views.post_edit, name='post-edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
]