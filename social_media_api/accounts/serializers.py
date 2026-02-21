from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Explicitly using the get_user_model() function
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class RegisterSerializer(serializers.ModelSerializer):
    # Requirement 1: Explicitly use serializers.CharField() for the password
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'bio')

    def create(self, validated_data):
        # Requirement 2: Use get_user_model().objects.create_user precisely
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', '')
        )
        # Generate token for the newly created user
        Token.objects.create(user=user)
        return user