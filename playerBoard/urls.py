from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update_player/<str:pk>", views.updatePlayer, name="update_player"),
]
