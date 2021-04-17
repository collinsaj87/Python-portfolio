#agentframework.py

#This creates a module that moves agents in a given model.

import random

class Agent():
    def __init__(self, environment, agents):
    #Gives agents the labels x and y and sets the random start location
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        # determines intial position of y and x
        self.environment = environment     
        self.agents = agents
        self.store = 0
        
            
    #Property get and set
    def gety(self):
        return self._y
        
    def sety(self, value):
        self._y = value 
            
    def dely(self):
        del self._y
            
    y = property(gety, sety, dely, "I'm the 'y' property.")
        
    def getx(self):
        return self._x
        
    def setx(self, value):
        self._x = value 
            
    def delx(self):
        del self._x
            
    x = property(getx, setx, delx, "I'm the 'x' property.")
    
    def move(self):
    #Moves the x and y agents based on the result of a random float
    #corrected for torus environment
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100 
        else:
            self._y = (self._y - 1) % 100
            
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100 
        else:
            self._x = (self._x - 1) % 100
            
    
    def eat(self):                                 
    # Creates a method to eat 10 units of the environment
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        self.neighbourhood = neighbourhood
        

            
            
    
        
            
       
            
            
        
        
        