from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt #importing matplotlib

def main():
    x = np.arange(0, radians(1800), radians(12)) # a range between 0 t0 1800rads at a 12 step interval
    plt.plot(x, np.cos(x), 'b') # plots the result
    plt.show() # displays the result

main()
