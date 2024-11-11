from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('book_browser.urls')),
    path("books/", include("book_browser.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
]
