from rest_framework import serializers
from .models import FunctionalIndependenceMeasure

class FunctionalIndependenceMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionalIndependenceMeasure
        fields = '__all__'