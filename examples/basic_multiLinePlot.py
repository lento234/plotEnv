"""
Basic: Simple plotting
======================
"""

import matplotlib.pyplot as plt
import numpy as np

# Plotting wrapper
import plotenv

# Setting up plotting environment
palette = plotenv.set(plotType='line',
                      numColors=9,
                      interactive=True) # returns palette
                      

# Generate data
x = np.linspace(-1,1,100)
y = [np.cos(i*x/10)*np.sin(i*x/10) for i in range(9)]

# labels
labels = ['Alizarin', 'Peter river', 'Emerald', 
          'Sun Flower', 'Wisteria', 'Midnight blue',
          'Asbestos', 'Green sea', 'Pumpkin']

# Plot
plt.figure()
for i in range(9):
    plt.plot(x,y[i],c=palette[i], label=labels[i])
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()

# Custom plot wrapper
plotenv.cleanupFigure()
