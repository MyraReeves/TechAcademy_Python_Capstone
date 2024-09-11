from django.urls import path
from . import views


urlpatterns = [
    path('Washington/', views.home, name='Washington'),
    path('<int:pk>/park_details/', views.park_details, name='park_info'),
]