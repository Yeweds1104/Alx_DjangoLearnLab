from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, register
from .views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login')),
    path('logout/', LogoutView.as_view(template_name='logout')),
    path('admin-panel/', views.admin_view, name='admin_view'),
    path('librarian-panel/', views.librarian_view, name='librarian_view'),
    path('member-panel/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]