from django.shortcuts import render
import random
import math
# Create your views here.
from django.http import HttpResponse
from . import periodicElement

#Constant
gravity = 9.81

class Particle: 
    def __init__(self, element_name, x ,y):
        self.element_name = element_name
        self.x = x
        self.y = y
        self.mass = periodicElement.get_elementMass(element_name)
        self.charge = periodicElement.get_electronegativity(element_name)


def generate_particles(num_simulations):
    colors = ['blue', 'red', 'yellow', 'blue', 'purple']
    #Testing random elements
    elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron'] 
    all_particles = []

    for i in range(num_simulations):
        element = random.choice(elements)  # Randomly choose an element
        color = random.choice(colors)      # Randomly choose a color
        x = random.uniform(50, 450)
        y = random.uniform(50, 450)
        particle = Particle(element, x, y)
        particle.color = color  # Assign color as an additional attribute
        all_particles.append(particle)
    
    return all_particles


def particle_simulator(request):
    particles = generate_particles(100)
    return render(request, 'index.html', {'particles': particles})


def particle_interaction(particle1, particle2, g):
    dx = particle1.x - particle2.x
    dy = particle1.y - particle2.y 
    distance = math.sqrt(dx**2 + dy**2)

    if distance > 0: 
        #Gravitational Force: F = G(m1m2)/r^2
        force = g * (particle1.mass * particle2.mass)/ distance**2
        return force
    else: 
        return None


#Testing:
particle_interaction("Hydrogen", "Helium", gravity)

#-=-=---=-=-=-
def home(request):
    return render(request, 'index.html')

def welcome(request):
    return HttpResponse("Welcome to Particle Simulator")

