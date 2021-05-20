'''
MapData Class
-------------
In this instance there was an attempt at reading in and manipulating the data 
within this class and applying this to buttons created in main program. 
However, issues were encountered in trying to get the map 
data to display in the GUI once this method had been called. See README. 
'''

import numpy
import matplotlib
import matplotlib.pyplot

class MapData():
    
    
    def __init__(self, geo_array, pop_array, trans_array): #geo_slider, pop_slider, trans_slider):
        self.geo_array = geo_array
        self.pop_array = pop_array
        self.trans_array = trans_array
        #self.geo_slider = geo_slider.get() / 100
        #self.pop_slider = pop_slider.get() / 100
        #self.trans_slider = trans_slider.get() / 100
        #self.final = numpy.empty([530, 335])
      
    
    def weight_combine(self):
        self.geo_array =  numpy.multiply(self.geo_slider, self.geo_array)
        self.pop_array = numpy.multiply(self.pop_slider, self.pop_array)
        self.trans_array = numpy.multiply(self.trans_slider, self.trans_array)
        self.combine = numpy.add(self.geo_array, self.pop_array)
        
        self.final =numpy.add(self.trans_array, self.combine)
        print(self.final)
        
        
    def get_values(self):
    # Function to extract weightings from sliders and apply to final map display
        matplotlib.pyplot.imshow(self.final, cmap='gray')
        #matplotlib.pyplot.show()
        #canvas.draw()
        #print(self.final)
        #tkinter.mainloop()
        
    def reset_values(self, geo_env, pop_env, trans_env):
    # Function resets numpy arrays to initial settings
    # Without this approach the final numpy array was reverting to all zeroes. 
        self.geo_array = geo_env
        self.pop_array = pop_env
        self.trans_array = trans_env
        
    def create_output(self):
        self.final
        numpy.savetxt('output.csv', self.final, delimiter=',')