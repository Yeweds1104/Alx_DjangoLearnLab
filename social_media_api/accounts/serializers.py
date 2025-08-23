from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        
class RegisterSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password = serializers.CharField()
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'email']
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user