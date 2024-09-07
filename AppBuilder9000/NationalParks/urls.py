from django.urls import path
from . import views


urlpatterns = [
    # path(url name, name of the function being called, name=nickname)
    path('National_Parks/', views.states, name='parks'),
    path('comments/', views.comments, name='comments'),
    path('new_comment/', views.create_comment, name='visitor_entry'),
]
