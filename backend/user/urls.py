from django.urls import path

from .views import HomeAPIView


urlpatterns = [
    path('home/', HomeAPIView.as_view()),
]
