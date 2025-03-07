from authentication import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('user/', views.AuthUserAPIView.as_view()),
]