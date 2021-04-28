from Bullet import Bullet
import time

class Player:
    # len of cooldown
    COOLDOWN = 120
    def __init__(self):
        self.x = 300
        self.y = 300
        self.health = 100
        self.x_speed = 0
        self.y_speed = 0
        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False
        self.bullets = []
        self.is_colliding = False
        self.score = 0
        self.level = 0
        self.can_increase_level = True
        self.kill_count = 0
        self.bullets_left = 60
        self.can_shoot = True
        self.key_r = False
        self.pressed_r = False
        self.cool_down_counter = 0
        
        
        
    def display(self, p):
        fill(0, 155, 0)
        pushMatrix()
        angle = atan2(self.x - mouseX, self.y - mouseY)
        translate(self.x, self.y)
        rotate(-angle - HALF_PI)
        img = image(p,0,0)
        popMatrix()

        for bullet in self.bullets:
            bullet.fire()
            
    def count_down(self):
        if self.key_r == True and self.cool_down_counter == 0:
            self.bullets_left = 60
            self.can_shoot = True
            self.pressed_r = False
            self.cool_down_counter = 1
            
    def cool_down(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
        
        
    def shoot(self):
        bullet = Bullet(self.x, self.y)
        self.bullets.append(bullet)
                

    def count_speed(self):
        if self.key_up == True:
            self.y_speed -= 0.3

        if self.key_down == True:
            self.y_speed += 0.3

        if self.key_left == True:
            self.x_speed -= 0.3

        if self.key_right == True:
            self.x_speed += 0.3
    
    def change_pos(self):
        self.x += self.x_speed
        self.y += self.y_speed
