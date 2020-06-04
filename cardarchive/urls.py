from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('backup/', views.create_backup, name='create backup'),
    path('purge/', views.purge, name='purge'),
    path('search/', views.search, name='search')
]