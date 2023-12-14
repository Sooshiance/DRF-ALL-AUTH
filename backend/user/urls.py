from django.urls import path 

from rest_framework_simplejwt.views import TokenRefreshView

from .views import *


urlpatterns = [
    path('', UserLoginAPIView.as_view(), name='LOGIN'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path('logout/', UserLogoutAPIView.as_view(), name='LOGOUT'),
    path('register/', UserRegisterationAPIView.as_view(), name='REGISTER'),
]
