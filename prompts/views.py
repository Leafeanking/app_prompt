from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from prompts.serializers import PromptSerializer, UserSerializer
from prompts.permissions import IsOwnerOrReadOnly
from prompts.models import Prompt, get_random_item
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )

    def random(self, request):
        queryset = get_random_item(Prompt)
        serializer = PromptSerializer(queryset)
        return Response(serializer.data)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class getAuthTokenUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})
