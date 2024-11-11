from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("popularity", views.browse, name="popularity", kwargs={'sort_by': 'popularity'}),
    path("author", views.browse, name="author", kwargs={'sort_by': 'author'}),
    path("genre", views.browse, name="genre", kwargs={'sort_by': 'genre'}),
]