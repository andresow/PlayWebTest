from rest_framework import routers
from .viewsets import FunctionalIndependenceMeasuretViewSet

router = routers.SimpleRouter()
router.register('FIM', FunctionalIndependenceMeasuretViewSet)

urlpatterns = router.urls
