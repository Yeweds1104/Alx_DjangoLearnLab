from .models import Post, Comment
from rest_framework import viewsets, permissions, filters, generics
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly

# Create your views here.
User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'updated_at', 'author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')