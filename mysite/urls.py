from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from translator import views


urlpatterns = [
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("translator/", include("translator.urls")),
    path("admin/", admin.site.urls),
]

