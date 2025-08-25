from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, RegisterSerializer
from .models import CustomUser

# Create your views here.
class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user': response.data, 'token': token.key})
    
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, username):
        target_user = get_object_or_404(CustomUser, username=username)
        if target_user == request.user:
            return Response({'error': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user in target_user.followers.all():
            target_user.followers.remove(request.user)
            action = 'unfollowed'
        else:
            target_user.followers.add(request.user)
            action = 'followed'
        
        return Response({'status': f'Successfully {action} {target_user.username}.'}, status=status.HTTP_200_OK)
    
class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, username):
        target_user = get_object_or_404(CustomUser, username=username)
        if target_user == request.user:
            return Response({'error': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user in target_user.followers.all():
            target_user.followers.remove(request.user)
            return Response({'status': f'Successfully unfollowed {target_user.username}.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': f'You are not following {target_user.username}.'}, status=status.HTTP_400_BAD_REQUEST)