
class Setting:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (255, 212, 71)
        self.blue = (106, 165, 225)
        self.color1 = (248, 239, 197)
        self.color2 = (0, 129, 138)
        self.cyan = (145, 255, 204)
        self.orange = (255, 171, 140)
        self.fps = 30
        self.PI = 3.14159265359
        self.TAU = self.PI * 2

    def get_resolution(self):
        return (self.width, self.height)

def Translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2) * ((value-min1)/(max1-min1))
