from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import HomeAPIView, LoginAPIView, LoginOTPVerifyAPIView, ProfileAPIView, RegisterAPIView


urlpatterns = [
    path('home/', HomeAPIView.as_view()),
    path("user/token/", LoginAPIView.as_view()),
    path("user/token/otp/", LoginOTPVerifyAPIView.as_view()),
    path("user/token/refresh/", TokenRefreshView.as_view()),
    path("user/profile/", ProfileAPIView.as_view()),
    path("user/register/", RegisterAPIView.as_view()),
]
