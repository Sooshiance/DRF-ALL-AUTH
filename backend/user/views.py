from django.contrib.auth import authenticate

from rest_framework import generics, response, status, permissions
from rest_framework_simplejwt import tokens

from .models import User, UserOTP, Profile
from .serializers import UserSerializer, ProfileSerializer, RegisterSerializer, LoginSerializer, OTPSerializer
from .permissions import VendorPermission, CustomerPermission


class HomeAPIView(generics.GenericAPIView):
    """
    Home endpoint
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return response.Response(data=request.data, status=status.HTTP_200_OK)


class LoginAPIView(generics.GenericAPIView):
    """"""
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        s = LoginSerializer(data=request.data)
        if s.is_valid():
            phone = s.validated_data["phone"]
            password = s.validated_data["password"]
            if authenticate(request=request, phone=phone, password=password):
                user = User.objects.get(phone=phone)
                token = tokens.RefreshToken.for_user(user)
                data = s.data
                data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
                return response.Response(data, status=status.HTTP_200_OK)
            else:
                return response.Response(data=s.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return response.Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
