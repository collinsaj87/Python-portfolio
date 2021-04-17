# model.py

import random
import operator
import matplotlib.pyplot
import agentframework           # See agentframework.py
import csv


num_of_agents = 10              # Dictates the number of agents in the environment
num_of_iterations = 100         # Determines the number of times agent moves position
agents = []                     # Empty list for storing agents
environment = []                # Empty list for the environment data to be read in to
neighbourhood = 20


# Calculates distance between two agents

# This will be transferred into a method in agentframework.py

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.y - agents_row_b.y)**2) + 
            ((agents_row_a.x - agents_row_b.x)**2))**0.5




# Imports the csv data as the environment and compiles list
with open('in.csv', newline='') as f:
    environment = [] # Establishes a list containing the file data
    # Reads in the csv data and appends to the created lists
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        environment.append(rowlist)
        for value in row:
            rowlist.append(value)
            
f.close()



# Displays plot of initial environment
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
         

# Move the agents and consume from environment.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()



for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)







