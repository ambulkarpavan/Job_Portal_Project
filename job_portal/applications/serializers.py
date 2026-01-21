from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    candidate = serializers.ReadOnlyField(source='candidate.username')

    class Meta:
        model = Application
        fields = '__all__'
