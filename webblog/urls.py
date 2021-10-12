from django.contrib import admin
from django.urls import path
from webblog import views



urlpatterns = [
    path('', views.index,name="webblog"),

]
