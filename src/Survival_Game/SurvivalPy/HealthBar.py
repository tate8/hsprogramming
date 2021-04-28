class HealthBar:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        
    def display(self, x, y, w, h, health):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        fill(22, 198, 41)
        if health < 100:
            self.w -= 35
        if health < 90:
            self.w -= 35
        if health < 80:
            self.w -= 35
        if health < 70:
            self.w -= 35
        if health < 60:
            fill(240, 211, 46)
            self.w -= 35
        if health < 50:
            self.w -= 35
        if health < 40:
            self.w -= 35
            fill(185, 13, 33)
        if health < 30:
            self.w -= 35
        if health < 20:
            self.w -= 35
        if health < 10:
            self.w = 10
        
        rect(self.x, self.y, self.w, self.h, 3)
