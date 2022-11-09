class Polygon:
    def __init__(self):
        self.vertices = []
    
    def getSize(self):
        return len(self.vertices)
    
    def __repr__(self):
        return f"polygon - [{self.vertices}]"