from rest_framework import generics, response, status, permissions

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
