from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('second_app/', views.second_app)
]
