from django.shortcuts import render
from .serializers import RegisterSerializer , UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics , permissions
from rest_framework.response import Response
from django.contrib.auth.models import User



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileViews (generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user