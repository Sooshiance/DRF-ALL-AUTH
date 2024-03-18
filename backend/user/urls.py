from django.urls import path

from .views import HomeAPIView, LoginAPIView


urlpatterns = [
    path('home/', HomeAPIView.as_view()),
    path("user/token/", LoginAPIView.as_view()),
]
