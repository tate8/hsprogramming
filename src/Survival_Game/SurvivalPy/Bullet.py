


class Bullet:
    def __init__(self, x, y):
        self.speed = 25
        self.x = x
        self.y = y
        self.can_shoot = False
        self.location = PVector(self.x, self.y)
        self.rotation = atan2(mouseY - self.location.y, mouseX - self.location.x) / PI * 180 + random(-2, 2)
        self.x_speed = 0
        self.y_speed = 0


    def fire(self):
        self.x_speed = cos(self.rotation/180*PI)*self.speed
        self.y_speed = sin(self.rotation/180*PI)*self.speed
        self.location.x = self.location.x + self.x_speed
        self.location.y = self.location.y + self.y_speed
        fill(0)
        rect(self.location.x, self.location.y, 3, 3)
        
        
    
    def reached_an_edge(self):
        if self.location.y < 0 or self.location.y > height or self.location.x < 0 or self.location.x > width:
            return True
        else:
            return False
