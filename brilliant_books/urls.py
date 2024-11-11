from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("books/", include("book_browser.urls")),
    path('admin/', admin.site.urls),
]
