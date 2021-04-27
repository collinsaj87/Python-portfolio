#agentframework.py

#This creates a module that moves agents in a given model.

import random

class Agent():
    def __init__(self, environment, agents, td_y, td_x):
    #Gives agents the labels x and y and sets the random start location
        # determines intial position of y and x using web scrape to initialise
        if (td_y == None):
            self._y = random.randint(0, 100)
        else:
            self._y = td_y
        if (td_x == None):
            self._x = random.randint(0, 100)
        else:
            self._x = td_x
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
    # Method to share information with each agent
        self.neighbourhood = neighbourhood
        for agent in self.agents:                   # Loops through created agents list
            distance = self.distance_between(agent)
            if distance <= self.neighbourhood:      # Evaluates the distance compared to hardwired neighbourhood variable
                sum = self.store + agent.store
                average = sum / 2
                self.store = average
                agent.store = average
               # print("sharing " + str(distance) + " " + str(average))
            
    def distance_between(self, agents):
        return (((self._x - agents._x)**2) +((self._y - agents._y)**2))**0.5
        
        
       
        

            
            
    
        
            
       
            
            
        
        
        