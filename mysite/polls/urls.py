from django.urls import path
from . import views

urlpatterns = [
    # Path to '/' to function views.index() with name "index"
    path("", views.index, name="index"),
]