from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("popularity", views.browse_by_popularity, name="popularity"),
]