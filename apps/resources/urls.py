from django.urls import path
from .views import ResourceListAPI

urlpatterns = [
    path('resources/', ResourceListAPI.as_view(), name='resources')
]
