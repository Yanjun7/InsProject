from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloWord.as_view())
]