# model.py

import random
import operator
import matplotlib.pyplot
import agentframework           # See agentframework.py
import csv
import matplotlib.animation
    

num_of_agents = 10              # Dictates the number of agents in the environment
num_of_iterations = 100         # Determines the number of times agent moves position
agents = []                     # Empty list for storing agents
environment = []                # Empty list for the environment data to be read in to
neighbourhood = 20


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

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

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

carry_on = True
       
# Move the agents and consume from environment.  # Wk7 'update' is added prior to the call to move for animating

def update(frame_number):
    fig.clear()                         # Wk7 addition, animating the plot
    global carry_on
    
   # for j in range(num_of_iterations):      # Wk7 - commenting this out results in animation displaying 10 agents rather than all iterations!
       # random.shuffle(agents)              # Changes the order of agents each iteration
    for i in range(num_of_agents):              
           agents[i].move()
           agents[i].eat()
           agents[i].share_with_neighbours(neighbourhood)
           #print(agents[i].store)
      
    # Sets a stopping condition for the model to cease when each agent has eaten the input number. 
    if agents[i].store >= 1000:
          carry_on = False
          print("Stopping condition")
 
      
    for i in range(num_of_agents):
           matplotlib.pyplot.xlim(0, 99)
           matplotlib.pyplot.ylim(0, 99)
           matplotlib.pyplot.imshow(environment)
           matplotlib.pyplot.scatter(agents[i].x,agents[i].y)   # Creates the update function running in the animation variable
           # print(agents[i].x,agents[i].y)
         
    
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1           
           
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat = False, frames = num_of_agents)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()

 
'''
a=agentframework.Agent(environment, agents)
print(a.x, a.y)
a.move()
print(a.x, a.y)
'''




