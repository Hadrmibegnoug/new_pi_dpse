from django.urls import path
from . import views

urlpatterns = [
    path('Hi/',views.hello)
]