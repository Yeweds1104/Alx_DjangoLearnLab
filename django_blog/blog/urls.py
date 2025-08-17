from django.urls import path
from .views import (
    CustomLoginView, CustomLogoutView, RegisterView, profile, PostListView,
    PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    
    #path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post=list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
