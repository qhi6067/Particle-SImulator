from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse

def generate_particles(num_simulations):
    colors = ['blue', 'red', 'yellow', 'blue', 'purple']
    all_particles = [] #empty list to append all particles to be simlauted 
    for color in colors:
        for i in range(num_simulations):
            particle = {'x': random.uniform(50,450), 'y':random.uniform(50,450), 'color': color}
            all_particles.append(particle) #contains x y and color
    return all_particles

def particle_simulator(request):
    particles = generate_particles(100)
    return render(request, 'index.html', {'particles': particles})

def home(request):
    return render(request, 'index.html')

def welcome(request):
    return HttpResponse("Welcome to Particle Simulator\n Made by Jaime Perez, Frankie and Arjun Daya")

