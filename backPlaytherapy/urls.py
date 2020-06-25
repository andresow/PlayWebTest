"""backPlaytherapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.config import settings
from django.config.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('apps.patients.urls')),
    path('api/v1.0/', include('apps.FIM.urls')),
    path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.jwt')),
	path('api/v1.0/therapists/', include('apps.therapists.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)