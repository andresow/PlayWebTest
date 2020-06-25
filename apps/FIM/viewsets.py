from rest_framework import viewsets
from .models import FunctionalIndependenceMeasure
from .serializer import FunctionalIndependenceMeasureSerializer

class FunctionalIndependenceMeasuretViewSet(viewsets.ModelViewSet):
    queryset = FunctionalIndependenceMeasure.objects.all()
    serializer_class = FunctionalIndependenceMeasureSerializer