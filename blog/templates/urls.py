from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/', views.create_author, name='create_author'),
    path('category/', views.create_category, name='create_category'),
    path('post/', views.create_post, name='create_post'),
    path('search/', views.search_post, name='search_post'),
]
