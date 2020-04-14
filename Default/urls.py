from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1,name="openpage"),
    path('contact.html/',views.index2,name="contact")
]