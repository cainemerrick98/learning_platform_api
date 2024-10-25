from rest_framework import serializers
from .models import Textbook, Exercise

class TextbookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook
        fields = ['id', 'user', 'title']

class TextbookRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'