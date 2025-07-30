from rest_framework import serializers
from .models import todoapp

class todoserializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = todoapp