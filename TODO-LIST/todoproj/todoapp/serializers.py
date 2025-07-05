from .models import TODOAPP
from rest_framework import serializers

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODOAPP
        fields = '__all__'