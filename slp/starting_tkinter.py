# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter
import matplotlib
matplotlib.use('TkAgg')


fig = matplotlib.pyplot.figure(figsize=(9, 9))
ax = fig.add_axes([0, 0, 1, 1])


# importing the csv data from the geology map
import csv
with open ('geology.csv', newline='') as f:
    geo_env = []
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        geo_env.append(rowlist)
        for value in row:
            rowlist.append(value)
matplotlib.pyplot.imshow(geo_env)
#matplotlib.pyplot.show()
           
with open ('population.csv', newline='') as g:
    pop_env = []
    reader = csv.reader(g, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        pop_env.append(rowlist)
        for value in row:
            rowlist.append(value)
    matplotlib.pyplot.imshow(pop_env)
    #matplotlib.pyplot.show()

with open ('transport.csv', newline='') as h:
    trans_env = []
    reader = csv.reader(h, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        trans_env.append(rowlist)
        for value in row:
            rowlist.append(value)
    matplotlib.pyplot.imshow(trans_env)
    #matplotlib.pyplot.show()

  
root = tkinter.Tk()
root.wm_title("Site location")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
