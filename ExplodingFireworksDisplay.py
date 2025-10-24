import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("#050510")
screen.tracer(0)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 8)
        self.lifetime = 100
        self.size = random.randint(3, 7)
        
    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.speed *= 0.95
        self.lifetime -= 1
        self.size = max(1, self.size * 0.98)
        
    def is_alive(self):
        return self.lifetime > 0

particles = []
colors = ["#ff006e", "#fb5607", "#ffbe0b", "#06ffa5", "#3a86ff", "#8338ec", "#ff0080", "#00ff80"]
frame_count = 0

def create_explosion(x, y):
    color = random.choice(colors)
    for _ in range(50):
        particles.append(Particle(x, y, color))

def draw_frame():
    global frame_count
    
    screen.clear()
    screen.bgcolor("#050510")
    
    # Create new explosions randomly
    if random.random() > 0.92:
        x = random.randint(-300, 300)
        y = random.randint(-100, 300)
        create_explosion(x, y)
    
    # Update and draw particles
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    
    for particle in particles[:]:
        if not particle.is_alive():
            particles.remove(particle)
            continue
            
        particle.update()
        drawer.penup()
        drawer.goto(particle.x, particle.y)
        
        # Fade effect
        opacity = particle.lifetime / 100
        drawer.dot(int(particle.size), particle.color)
        
        # Add trails
        if random.random() > 0.7:
            drawer.pensize(1)
            drawer.pencolor(particle.color)
            drawer.goto(particle.x - math.cos(particle.angle) * 5, 
                       particle.y - math.sin(particle.angle) * 5)
    
    frame_count += 1
    
    screen.update()
    screen.ontimer(draw_frame, 30)

# Create initial explosions
for _ in range(3):
    create_explosion(random.randint(-200, 200), random.randint(0, 200))

draw_frame()
turtle.done()