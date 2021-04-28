import time
import random

class Enemy:
    def __init__(self, x, y, skin, index):
        self.x = x
        self.y = y
        self.health = 100
        self.easing = 0.06
        self.speed = 0.8
        self.img = skin
        self.index = index
        self.angle = None
        self.damage = 10
        
    def display(self, p_x, p_y):
        if self.index == 2:
            self.speed = 1.5
        elif self.index == 0:
            self.speed = 0.5
        fill(255, 0, 0)
        # color based on health ???

        
        # seeking algorithm using PVector
        enemy = PVector(self.x, self.y)
        angle = atan2(p_y - self.y, p_x-self.x)
        new_x = cos(angle) * self.speed + self.x
        new_y = sin(angle) * self.speed + self.y
        enemy.set(new_x, new_y)
        self.x = enemy.x
        self.y = enemy.y
        #look
        pushMatrix()
        self.angle = atan2(self.x - p_x, self.y - p_y)
        translate(self.x, self.y)
        rotate(-self.angle - QUARTER_PI+1)
        
        image(self.img, 0, 0)
        popMatrix()
    
        


    def bullet_intersection(self, bullet):
        distance = dist(self.x, self.y, bullet.location.x, bullet.location.y)
        if distance < 20:
            return True
        else:
            return False
