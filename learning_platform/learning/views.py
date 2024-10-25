from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions, authentication
from . import models, serializers

# Create your views here.
class TextbookViewset(ListAPIView, RetrieveAPIView, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    queryset = models.Textbook.objects.all()

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return serializers.TextbookRetrieveSerializer
        else:
            return serializers.TextbookListSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class ExerciseViewset(ListAPIView, CreateAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    queryset = models.Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer


