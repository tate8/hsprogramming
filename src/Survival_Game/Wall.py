

class Wall:
    def __init__(self, x_1, y_1, x_2, y_2, p_x, p_y, p_x_speed, p_y_speed):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.p_x = p_x
        self.p_y = p_y
        self.p_x_speed = p_x_speed
        self.p_y_speed = p_y_speed
        self.is_colliding = False

        
    def display(self):
        fill(100)
        rect(self.x_1, self.y_1, self.x_2, self.y_2)
        
    def collision_detection_y(self):
        if self.p_x + 0 > self.x_1 and self.p_x < self.x_1 + self.x_2 and self.p_y + 20 + self.p_x_speed > self.y_1 and self.p_y + self.p_y_speed < self.y_1 + self.y_2:
            return True
        else:
            return False
    def collision_detection_x(self):
        if self.p_x + 20 + self.p_x_speed > self.x_1 and self.p_x + self.p_x_speed < self.x_1 + self.x_2 and self.p_y + 20 > self.y_1 and self.p_y < self.y_1 + self.y_2:
            return True
        else:
            return False
        
