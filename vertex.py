import setting

class Vertex:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def translatetoScreen(self, min1, max1, min2, max2):
        x = setting.Translate(self.x, min1, max1, min2, max2)
        y = setting.Translate(self.y, min1, max1, min2, max2)
        z = setting.Translate(self.z, min1, max1, min2, max2)
        return Vertex(x, y, z)

    def ToMatrix(self):
        return [[self.x], [self.y], [self.z]]

    def __add__(self, vertex):
        return Vertex(self.x + vertex.x , self.y + vertex.y, self.z + vertex.z)

    def __sub__(self, vertex):
        return Vertex(self.x - vertex.x , self.y - vertex.y, self.z - vertex.z)

    def __mul__(self, vertex):
        return Vertex(self.x * vertex.x , self.y * vertex.y, self.z * vertex.z)

    def __truediv__(self, vertex):
        return Vertex(self.x / vertex.x , self.y / vertex.y, self.z / vertex.z)

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.z}]"
