# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('posts', views.index),
    path('posts', views.group_list)
]
