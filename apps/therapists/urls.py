from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TherapistListCreateView, TherapistDetailView,TherapistsDetailView

urlpatterns = [
    #gets all user profiles and create a new profile
    path("all-profiles",TherapistListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("therapist/<int:pk>",TherapistDetailView.as_view(),name="therapist"),
    path("all-therapist",TherapistsDetailView.as_view(),name="all-profiles"),

]
