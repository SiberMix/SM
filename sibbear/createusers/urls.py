from django.urls import path
from .views import index, mantis
urlpatterns = [
    path('', index),
    path('create', mantis),
]
