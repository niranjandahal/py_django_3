from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import HttpResponse, response

def index(request):
    return HttpResponse("<h1> this is a homepage"),


  