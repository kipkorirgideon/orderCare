import django
import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import viewsets, permissions, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from orderCare.serializers import UserSerializer


# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [OAuth2Authentication]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        protocol = 'https' if django.conf.settings.SECURE_SSL_REDIRECT else 'http'
        url = f'{protocol}://{request.get_host()}/o/token/'
        response = requests.post(url,
                                 data={
                                     'grant_type': 'password',
                                     'username': user.username,
                                     'password': request.data['password'],
                                     'client_id': django.conf.settings.OAUTH2_CLIENT_ID,
                                     'client_secret': django.conf.settings.OAUTH2_CLIENT_SECRET,
                                     'scope': 'read write openid',
                                 },
                                 )
        return Response(response.json())