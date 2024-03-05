import turtle as t
import math as m
t.hideturtle()
t.tracer(0)
tscreen = t.Screen()
tscreen.bgcolor("black")
planet_distance = {}
planet_data = {}
G = 0.5 #can change this later
M = 100
class Planet:
    def __init__(self, radius, mass, start_pos, start_velocity, color, name):
        self.radius = radius
        self.mass = mass * M #can change this later
        self.pos = start_pos
        self.velocity = start_velocity #vector
        self.color = color
        self.name = name
planet_x = Planet(50, 1500, (0, 0), (0, 0), "blue", "x") #must have different name (i kind of used it as an ID)
planet_y = Planet(10, 5, (250, 250), (3, -3), "green", "y")
#planet_z = Planet(15, 25, (-350, -250), (-3, 3), "red", "z")
list_planets = [planet_x, planet_y] 
list_turtles = []
for i in list_planets:
    turtle = t.Turtle()
    turtle.width(2)
    turtle.shape("circle")
    turtle.color(i.color, i.color)
    turtle.turtlesize(i.radius / 10)
    turtle.up()
    turtle.goto(i.pos)
    turtle.down()
    list_turtles.append(turtle)
def draw_planets():
    #for offsetting screen position by average planet position (unnecessary)
    """average_x = 0
    average_y = 0
    for i in list_planets:
        average_x += i.pos[0]
        average_y += i.pos[1]
    average_x /= len(list_planets)
    average_y /= len(list_planets)
    for i in list_planets:
        t.goto(i.pos[0], i.pos[1] - i.radius)
        #t.goto(i.pos[0], i.pos[1] - i.radius)
        t.down()
        t.color("white", i.color)
        t.begin_fill()
        t.circle(i.radius, 360)
        t.end_fill()
        t.up()
        t.goto(t.xcor() + i.radius, t.ycor() + i.radius)
        t.write(f"({m.floor(i.pos[0])}, {m.floor(i.pos[1])})")
        #t.goto(0, 0)
        #t.dot(5, "white")
        #t.write(f"({m.floor(average_x)}, {m.floor(average_y)})")
    """
    x_offset, y_offset = list_planets[0].pos
    for i in range(0, len(list_turtles)):
        turtle = list_turtles[i]
        #turtle.goto(list_planets[i].pos)
        turtle.goto(list_planets[i].pos[0] - x_offset, list_planets[i].pos[1] - y_offset)
        #turtle.goto(list_planets[i].pos[0] - average_x, list_planets[i].pos[1] - average_y)
    tscreen.update()
def animate():
    planet_data.clear()
    for i in list_planets: #loops through each planet 
        current_velocity = i.velocity
        for j in list_planets:
            if (j == i):
                continue
            if (not (i.name + j.name) in planet_distance):
                D = m.sqrt(pow(i.pos[0] - j.pos[0], 2) + pow(i.pos[1] - j.pos[1], 2))
                planet_distance[j.name + i.name] = D
            else:
                D = planet_distance[i.name + j.name] 
            V = [j.pos[0] - i.pos[0], j.pos[1] - i.pos[1]]
            F = (G * j.mass) / (pow(D, 2) * 1000) #offset the fps -> 1000
            current_velocity = [current_velocity[0] + V[0] * F, current_velocity[1] + V[1] * F]
        planet_data[i.name] = (current_velocity, [i.pos[0] + current_velocity[0], i.pos[1] + current_velocity[1]])
    for i in list_planets:
        velocity, position = planet_data[i.name]
        i.velocity = velocity
        i.pos = position
    planet_distance.clear()
    draw_planets()
    t.ontimer(animate, 5)
animate()
tscreen.mainloop()