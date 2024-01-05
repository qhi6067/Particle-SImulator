from django.shortcuts import render
import random
<<<<<<< Updated upstream
=======
import math
>>>>>>> Stashed changes

# Create your views here.
from django.http import HttpResponse

<<<<<<< Updated upstream
=======
###################################################
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
=======
def particle_interaction(particle1, particle2, g): 
    fx = 0
    fy = 0
    #distance: 
    dx = particle1.x - particle2.x
    dy = particle1.y -particle2.y
    # calculate the distance between both particles using pytharogeom theorem
    distance = math.sqrt(dx*dx + dy*dy)
    if distance > 0: 
    #Force (F) = F1 = F2 = G (mass1 * mass2)/ Distance^2
        Force = g (particle1['Atomic_mass'], particle2['Atomic_mass'])/ distance**2


#-=-=-=-=-=-=-=-=-=-=-=-=-=
>>>>>>> Stashed changes
def home(request):
    return render(request, 'index.html')

def welcome(request):
    return HttpResponse("Welcome to Particle Simulator\n Made by Jaime Perez, Frankie and Arjun Daya")

