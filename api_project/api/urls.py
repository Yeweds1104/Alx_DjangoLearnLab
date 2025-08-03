from django.urls import path, include
from rest_framework import routers
from .views import BookList

#router = routers.DefaultRouter()
#router.register(r'books', BookList)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    #path('api/', include(router.urls)),
]