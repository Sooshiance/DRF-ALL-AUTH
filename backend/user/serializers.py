from rest_framework import serializers

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('is_active',
                            'is_staff',
                            'is_admin',
                            'last_login',
                            'created_at',
                            'pk',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('pk',)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"
        read_only_fields = ('is_active',
                            'is_staff',
                            'is_admin',
                            'last_login',
                            'created_at',
                            'pk',)


class LoginSerializer(serializers.Serializer):
    phone   = serializers.CharField(required=True)
    pasword = serializers.CharField(required=True, write_only=True)


class OTPSerializer(serializers.Serializer):
    phone = serializers.CharField(required=False)
    otp   = serializers.CharField(required=True)
