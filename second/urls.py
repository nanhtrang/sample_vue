from django.contrib import admin
from django.urls import re_path, include
from second import views

urlpatterns = [
    re_path(r'^$', views.get_sampple)
]
