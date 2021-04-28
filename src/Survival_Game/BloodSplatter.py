
class BloodSplatter:
    def __init__(self, img, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.img = img
        self.show_blood = False
        
    def display(self):
            
            # face direction
        pushMatrix()
        translate(self.x, self.y)
        rotate(-self.angle + HALF_PI)
        image(self.img, 0, 0)
        popMatrix()

        
