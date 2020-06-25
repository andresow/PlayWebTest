from rest_framework import serializers
from .models import Therapist

class TherapistSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Therapist
        fields='__all__'
