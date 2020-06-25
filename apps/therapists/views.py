from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import Therapist
from .permissions import IsOwnerProfileOrReadOnly
from .serializer import TherapistSerializer

# Create your views here.

class TherapistListCreateView(ListCreateAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class TherapistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer
    permission_classes = [IsOwnerProfileOrReadOnly,IsAuthenticated]

class TherapistsDetailView(ListCreateAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer
