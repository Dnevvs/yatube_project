# urls.py
from django.urls import path

from . import views

app_name = 'group_list'

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.group_list, name='group_list')
    # path('posts/<slug:slug>', views.group_list, name='group_list')
]
