from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status, permissions
import re
from django.contrib.auth import authenticate
import jwt
from django.conf import settings
from .models import User
# Create your views here.


class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return response.Response({'user': serializer.data}, status=status.HTTP_200_OK)


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializers = self.get_serializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return response.Response(serializers.data, status=status.HTTP_201_CREATED)
        return response.Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)
        
        user = authenticate(username=username, password=password)
        print(user, email, password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(email=email)
        if user:
            if user.check_password(password):
                serializer = self.serializer_class(user)
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            return response.Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)