from tkinter import Y
import pygame as py
import math
py.init()
WIDTH , HEIGHT  = 800, 800
WIN = py.display.set_mode((WIDTH , HEIGHT))
py.display.set_caption("gravity simulator")
#colors

YELLOW = (255,255,0)
BLUE = (100,149,237)
class Planet:
    AU = 149.6e6 * 1000 # dist from sun to earth in m 
    G = 6.67e-11
    SCALE = 250/AU
    TIMESTEP = 3600 * 24 

    def __init__(self , x, y , color , mass , radius):
        self.x = x
        self.y = y
        self.color = color
        self.mass = mass
        self.radius = radius
        
        self.distanceTOSun = 0
        self.orbit = []
        self.is_sun = False

        self.xsp = 0 
        self.ysp = 0

    def draw(self , win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        py.draw.circle(win, self.color , (x, y) , self.radius)




def main():
    run = True
    clock = py.time.Clock()
    sun = Planet(0 , 0 , YELLOW , 1.98892*10**30 , 30)
    sun.is_sun = True

    earth = Planet(-1*Planet.AU , 0 , BLUE , 5.9742*10**24 , 16)

    planets = [sun, earth]
    while(run):
        clock.tick(17)
        WIN.fill()
        py.display.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                run  = False 
        
        for planet in planets:
            planet.draw(WIN)

        py.display.update()

    py.quit()

main()