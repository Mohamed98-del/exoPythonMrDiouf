import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getx(self):
        return self.x
    
    
    def gety(self):
        return self.y
    
    def getSurface(self):
        return self
    
    def afficher(self):
        return "(Point"+self.x+","+self.y+")"
    
class cercle:
    def __init__(self, centre, rayon):
        self.centre = centre
        self.rayon = rayon
    
    def getCentre(self):
        return Point(self.x,self.y)
    
    def getRayon(self):
        return self.rayon
    
    def getPerimetre(self):
        return 2*math.pi*self.rayon
    
    def getSurface(self):
        return 2*math.pi*self.rayon**2
    
    
    def appartient(self):
        x = math.sqrt(math.pow(self.centre - ))
        #je suis desole Mr de ne pas avoir implementer le reste du code a cause d'une manque de temps
        
        
class cylindre:
    def __init__(self, rayon, centre):
        self.rayon = rayon
        self.centre = centre
        
    
    

    
    
    
    
    