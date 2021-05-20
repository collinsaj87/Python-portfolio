"""
Output Test
------------
This code is taken from the code used in assignment2 for reading in the .csv files. 
In this instance it is used to test that the create_output function has worked and 
that the saved 'output.csv' matches that which is displayed on the GUI in the main
program.

"""

import csv
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
   
        
with open ('output.csv', newline='') as f:
    env = []
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        env.append(rowlist)
        for value in row:
            rowlist.append(value)
           
f.close()
matplotlib.pyplot.imshow(env)
tkinter.mainloop()