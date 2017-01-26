from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from prompts.serializers import PromptSerializer
from prompts.models import Prompt, get_random_item


class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def random(self, request):
        queryset = get_random_item(Prompt)
        serializer = PromptSerializer(queryset)
        return Response(serializer.data)
