

class Rectangulo:
    def __init__(self, punto1=(0, 0), punto2=(0, 0)):
        self.punto1 = punto1
        self.punto2 = punto2
    
    def base(self):
        return abs(self.punto2[0] - self.punto1[0])
    
    def altura(self):
        return abs(self.punto2[1] - self.punto1[1])
    
    def area(self):
        return self.base() * self.altura()