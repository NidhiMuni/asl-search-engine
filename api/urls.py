from django.urls import path
from .  import views

urlpatterns = [
    path('getData/', views.getData),
   #  path('add/', views.addData),
    path("vote/", views.vote),
]