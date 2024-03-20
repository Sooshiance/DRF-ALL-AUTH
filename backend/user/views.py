from django.contrib.auth import authenticate

from rest_framework import generics, response, status, permissions
from rest_framework_simplejwt import tokens

from .models import User, UserOTP, Profile
from .serializers import UserSerializer, ProfileSerializer, RegisterSerializer, LoginSerializer, OTPSerializer
from .permissions import VendorPermission, CustomerPermission
from .otp import otpToken

class HomeAPIView(generics.GenericAPIView):
    """
    Home endpoint
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return response.Response(data=request.data, status=status.HTTP_200_OK)


class LoginAPIView(generics.GenericAPIView):
    """
    Login API View page
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        s = LoginSerializer(data=request.data)
        if s.is_valid():
            phone = s.validated_data["phone"]
            password = s.validated_data["password"]
            if authenticate(request=request, phone=phone, password=password):
                user = User.objects.get(phone=phone)
                # token = tokens.RefreshToken.for_user(user)
                data = s.data
                otp = otpToken()
                str_otp = str(otp) + "1"
                print(str_otp)
                UserOTP.objects.create(user=user,otp=str_otp,otp_type=1).save()
                # data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
                return response.Response(data=data, status=status.HTTP_200_OK)
            else:
                return response.Response(data=s.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return response.Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginOTPVerifyAPIView(generics.GenericAPIView):
    serializer_class = OTPSerializer

    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.data)
        if s.is_valid():
            otp = s.validated_data["otp"]
            if UserOTP.objects.get(otp=otp):
                user = UserOTP.objects.get(otp=otp)
                user = User.objects.get(phone=user)
                token = tokens.RefreshToken.for_user(user)
                data = s.data 
                data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
                return response.Response(data=data, status=status.HTTP_200_OK)
            else:
                return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ProfileAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(phone=request.user)
        prof = Profile.objects.get(user=user.pk)
        serializer = ProfileSerializer(instance=prof)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return response.Response(data=request.data, status=status.HTTP_201_CREATED)
