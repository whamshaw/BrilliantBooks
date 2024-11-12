from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('browse/', views.browse, name='browse'),
    path('add_to_reading_list/<int:book_id>/', views.add_to_reading_list, name='add_to_reading_list'),
    path('remove_from_reading_list/<int:book_id>/', views.remove_from_reading_list, name='remove_from_reading_list'),
    path('search_results/', views.search_results, name='search_results'),
]