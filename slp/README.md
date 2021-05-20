Assignment 2 - Site Location Problem
=====================================

Site Location Decision Support Software
---------------------------------------

The software (assignment2.py) is designed to help assess likely locations for a rock aggregate factory in the United Kingdom.
When run the software will display a GUI with three sliders which take in information from three .csv files that contain raster
data on ideal locations based on geology, population, and transport. 

In order to operate the program the user should decide on a weighted linear combination of the three factors which totals to 100, 
essentially placing relative importance on each of the three factors based upon agreed values. When these values are confirmed the 
user should click 'submit' in order to produce a grayscale map of the United Kingdom in which lighter values represent 'better' conditions 
based on the weightings applied to the slider bars. The 'reset' button on the GUI should be used before resubmitting slider values as 
this will revert the data back to original settings prior to readjusting the sliders and submitting again. 

Output data can be saved. In order to do this click the functions tab and then 'Save as .csv'. This will create a file in the filetree 
in which the program is being run called 'output.csv'. Please ensure that you save this to your own directory before saving another output 
file if you wish to have comparisons. 

printoutput.py
--------------

There is a program included to display the saved output.csv, although initially used to test that the output is saving to the program file
it may be used to open a separate window and compare maps being considered. 
