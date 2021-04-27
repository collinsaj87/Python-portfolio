# model.py

import tkinter                  # for displaying GUI
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework           # See agentframework.py
import csv                      # For reading in csv file
import matplotlib.animation     # generates animation with x and y axis
import requests                 # allows for import of html data
import bs4                      # allows html data to be parsed into the model

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_y = soup.find_all(attrs={"class" : "y"})
td_x = soup.find_all(attrs={"class" : "x"})
print(td_y)
print(td_x)


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
    y = int(td_y[i].text)
    x = int(td_x[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

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
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#matplotlib.pyplot.show()

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()



