from django.urls import path
from .  import views

urlpatterns = [
    path('getData/', views.getData),
   #  path('add/', views.addData),
    path("<int:question_id>/vote/", views.vote),
]