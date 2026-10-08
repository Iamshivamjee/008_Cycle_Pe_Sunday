from django.urls import path
from . import views

app_name = 'drives'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('impact/', views.impact_archive_view, name='impact'),
    path('about/', views.about_view, name='about'),
    path('join/', views.join_view, name='join'),
]