from django.urls import path
from . import views

urlpatterns = [
    path('',views.say_hi),
    path('up',views.insert)
]