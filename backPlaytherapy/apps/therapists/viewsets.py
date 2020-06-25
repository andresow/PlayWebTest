from rest_framework import viewsets
from .models import Therapist
from .serializer import TherapistSerializer

class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer