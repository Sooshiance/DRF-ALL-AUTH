from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import User, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("id", "phone", "email", "first_name", "last_name", "image", "role")


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['phone', 'email', 'first_name', 'last_name', 'id', 'image', 'password', 'role']
        
    def create(self, **validated_data):
        return super().create(validated_data)


class LoginUserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
