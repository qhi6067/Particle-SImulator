from django.shortcuts import render
import random
import json
from . import periodicElement

class Particle:
    def __init__(self, element_name, x, y):
        self.element_name = element_name
        self.x = x
        self.y = y
        self.vx = 0  # Initial velocity x
        self.vy = 0  # Initial velocity y
        self.mass = float(periodicElement.get_elementMass(element_name))
        self.charge = float(periodicElement.get_electronegativity(element_name))

def generate_particles(num_simulations):
    colors = ['blue', 'red', 'yellow', 'blue', 'purple']
    elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
    all_particles = []
    for i in range(num_simulations):
        element = random.choice(elements)
        color = random.choice(colors)
        x = random.uniform(50, 450)
        y = random.uniform(50, 450)
        particle = Particle(element, x, y)
        particle.color = color
        all_particles.append(particle)
    return all_particles

def particle_simulator(request):
    particles = generate_particles(100)
    particles_data = [
        {'element_name': p.element_name, 'x': p.x, 'y': p.y, 'mass': p.mass, 'charge': p.charge, 'color': p.color}
        for p in particles
    ]
    particles_json = json.dumps(particles_data)
    return render(request, 'index.html', {'particles': particles_json})

# Optional views
def home(request):
    return render(request, 'index.html')

