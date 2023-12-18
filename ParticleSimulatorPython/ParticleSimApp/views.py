from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to the Particle Simulator!")

def welcome(request):
    return HttpResponse("Welcome to Particle Simulator\n Made by Jaime Perez and Arjun Daya")
