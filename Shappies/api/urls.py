
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from api import views

router = routers.DefaultRouter()  # allows us to have the standard rest routing urls (put, post, get, delete)

router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('current_user', views.current_user)
]
