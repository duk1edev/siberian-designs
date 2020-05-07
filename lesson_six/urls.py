from django.contrib import admin
from django.urls import path, include, re_path
from .views import List

urlpatterns = [
    path('', List.as_view(), name='list-view')
]
