# make the weight inputs a function that can be used in the development

import csv
import tkinter
import ipywidgets
from IPython.display import display
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot

geo_env = []
pop_env = []
trans_env = []
geo_w = []
pop_w = []
trans_w = []
weight1 = 0.4
weight2 = 0.3
weight3 = 0.3

# importing the csv data from the geology map

with open ('geology.csv', newline='') as f:
    geo_env = []
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        geo_env.append(rowlist)
        for value in row:
           rowlist.append(value)



with open ('population.csv', newline='') as g:
    pop_env = []
    reader = csv.reader(g, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        pop_env.append(rowlist)
        for value in row:
            rowlist.append(value)


with open ('transport.csv', newline='') as h:
    trans_env = []
    reader = csv.reader(h, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        trans_env.append(rowlist)
        for value in row:
            rowlist.append(value)

f.close()
g.close()
h.close()

geo_slider = ipywidgets.IntSlider(value = 0, min = 0, max = 100, step = 1, description = 'Geology:')
pop_slider = ipywidgets.IntSlider(value = 0, min = 0, max = 100, step = 1, description = 'Population:')
trans_slider = ipywidgets.IntSlider(value = 0, min = 0, max = 100, step = 1, description = 'Transport:')

display(geo_slider)
