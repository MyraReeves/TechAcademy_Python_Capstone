from django.urls import path
from . import views


urlpatterns = [
    path('Washington/', views.home, name='Washington'),

]