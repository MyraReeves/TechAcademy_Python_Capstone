from django.urls import path
from . import views


urlpatterns = [
    path('comicbooks', views.collection, name='collection'),
    path('add_issue/', views.add_to_collection, name='add_comic'),
    path('<int:pk>/edit_comic/', views.edit_collection, name='edit_comic'),
    path('<int:pk>/delete_comic/', views.delete, name='delete'),
    path('delete_confirmation/', views.confirmed, name='confirmed'),
]
