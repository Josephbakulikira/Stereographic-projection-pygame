
class Setting:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (200, 150, 20)
        self.blue = (89, 120, 250)
        self.fps = 60
        self.PI = 3.14159265359
        self.TAU = self.PI * 2

    def get_resolution(self):
        return (self.width, self.height)

def Translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2) * ((value-min1)/(max1-min1))
