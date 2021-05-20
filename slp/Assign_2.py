"""
GEOG5003M - Assignment 2 - Site Location Problem
-------------------------------------------------

The below code develops a piece of software that extracts three lots of raster
data being used in the decision making process in locating a rock aggregate 
factory in the UK. 

The three .csv files are read in to the program before being turned into numpy
arrays to increase the speed of processing; during development it was found that
running operators on a list of lists proved to be slow.

Upon running the program will display a series of three interactive sliders in 
a GUI that can be utilised in determining a weighting - i.e. a level of importance
which should be placed on each of the three critera based on the initial raster 
data - geology, population, and transport - in order to calculate a weighted linear
combination. 
"""

import csv                  # for reading in .csv files
import tkinter              # for developing and displaying GUI
import matplotlib           # for plotting raster data
matplotlib.use('TkAgg')
import matplotlib.pyplot    
import numpy                # for manipulating raster data in program
from MapData import MapData # attempt at creating a class to display OOP though not fully completed


# set the parameters to display GUI
fig = matplotlib.pyplot.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1])



# import the csv data to form initial geology raster data
# code adapted from lecture materials and assignment 1 (Evans, n.d.)
# https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/part7/index.html
with open ('geology.csv', newline='') as f:
    geo_env = []
    # Establish an empty list to store incoming data
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        geo_env.append(rowlist)
        for value in row:
           rowlist.append(value)
           #print(geo_env)

with open ('population.csv', newline='') as g:
    pop_env = []
    reader = csv.reader(g, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        pop_env.append(rowlist)
        for value in row:
            rowlist.append(value)
            #print(pop_env)

with open ('transport.csv', newline='') as h:
    trans_env = []
    reader = csv.reader(h, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        trans_env.append(rowlist)
        for value in row:
            rowlist.append(value)
            #print(trans_env)

f.close()
g.close()
h.close()

# convert csv imported list of lists into numpy array
# this was decided due to slow processing speed when applying operators to a list of lists. 
# Willems (2019)
# https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python#question16
geo_array = numpy.array(geo_env)
pop_array = numpy.array(pop_env)
trans_array = numpy.array(trans_env)

# create an empty numpy array as a global variable which can be used in create_output function
final = numpy.empty([530, 335])

# build canvas to display sliders and maps
root = tkinter.Tk()
root.wm_title("Site location")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# create sliders to determine importance weighting for each set of data 
# Anshuman Biswal (2020)
# https://www.youtube.com/watch?v=ieLE9F_RLsg
geo_slider = tkinter.Scale(root, from_ = 0, to = 100, orient='horizontal', label='Geology:')
geo_slider.pack(padx=5, pady=15, side='left')

pop_slider = tkinter.Scale(root, from_ = 0, to = 100, orient='horizontal', label='Population:')
pop_slider.pack(padx=5, pady=20, side='left')

trans_slider = tkinter.Scale(root, from_ = 0, to = 100, orient='horizontal', label ='Transport:')
trans_slider.pack(padx=5, pady=25, side='left')


def get_values():
# Extract weightings from sliders and apply to final map display
    """
    Function to extract weightings from the sliders and apply to final map display. 
    Operators used are based on the numpy library which take two arrays, hence having
    to combine two initial arrays before constructing the final array. 

    In this instance the array multiplication is simple as the shape of the data is consistent
    across all data sets. 

    https://numpy.org/doc/stable/reference/generated/numpy.multiply.html


    Parameters 
    ----------
    geo_array : ndarray (n dimensional numpy array)
        an initial numpy array that contains the raster data from 'geology.csv'.
        The value of the user input slider data, divided by 100, is then applied to this. 
    
    pop_array : ndarray
        an initial numpy array that contains the raster data from 'population.csv'.
        The value of the user input slider data, divided by 100, is then applied to this.
    
    trans_array : ndarray
        an initial numpy array that contains the raster data from 'transport.csv'.
        The value of the user input slider data, divided by 100, is then applied to this.
        
    combine : ndarray
        The combined values of the geology and population arrays following multiplication. 
        
    final : ndarray
        The overall weighted linear combination that will be displayed in the GUI.
    """
    global geo_array
    global pop_array
    global trans_array
    global final
    geo_array = numpy.multiply((geo_slider.get()/100), geo_array)
    pop_array = numpy.multiply((pop_slider.get()/100), pop_array)
    trans_array = numpy.multiply((trans_slider.get()/100), trans_array)
    combine = numpy.add(geo_array, pop_array)
    final = numpy.add(trans_array, combine)
    if (geo_slider.get() + pop_slider.get() + trans_slider.get()) > 100:
    # maintains decision making to 100% 
        tkinter.messagebox.showerror(title = 'Error', message = 'weight value totals cannot exceed 100')
        # https://docs.python.org/3/library/tkinter.messagebox.html
    else:
        matplotlib.pyplot.imshow(final, cmap='gray')
        canvas.draw()
        #print(final) - test application of operators
    #print(geo_slider.get(), pop_slider.get(), trans_slider.get())

# Button to execute application of weights and display map
# https://www.datacamp.com/community/tutorials/gui-tkinter-python
extract = tkinter.Button(root, text = 'Submit', command=get_values)
extract.pack()  

def reset_values():
# Reset numpy arrays to initial settings after button click
# Without this approach the final numpy array was reverting to all zeroes. 
    """
    A function that resets the data to the initial values read in from the three
    .csv files. 
    
    Note that the GUI map display does not change when using the associated button, 
    however, by adjusting the sliders a new map output will be produced.
    
    The global variables are used here as these will be reset to initial values
    after having operators applied using the get_values function above. 
    
    Parameters 
    ----------
    geo_array : ndarray 
        an initial numpy array that contains the raster data from 'geology.csv'.
    
    pop_array : ndarray
        an initial numpy array that contains the raster data from 'population.csv'.
    
    trans_array : ndarray
        an initial numpy array that contains the raster data from 'transport.csv'.
    """
    global geo_array
    global pop_array
    global trans_array
    geo_array = numpy.array(geo_env)
    pop_array = numpy.array(pop_env)
    trans_array = numpy.array(trans_env)
    
# Click to reset original values.     
reset = tkinter.Button(root, text = 'Reset', command = reset_values)
reset.pack()

def create_output():
# Save to file location as 'output.csv'
    global final
    numpy.savetxt('output.csv', final, delimiter=',')
    # https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy.savetxt
    tkinter.messagebox.showinfo(title = 'Saved', message = 'File saved as output.csv')
    # https://docs.python.org/3/library/tkinter.messagebox.html

# Create menu to give save option
# https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/part10/key.html
menu = tkinter.Menu(root)
root.config(menu=menu)
program_menu = tkinter.Menu(menu)
menu.add_cascade(label="Functions", menu=program_menu)
program_menu.add_command(label="Save as .csv", command=create_output)
program_menu.add_command(label = "Exit", command = root.destroy)

tkinter.mainloop()