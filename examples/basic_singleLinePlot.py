"""
Basic: Simple plotting
======================
"""

import matplotlib.pyplot as plt
import numpy as np

# Plotting wrapper
import plotenv

# Setting up plotting environment - default options
# palette = plotenv.set(plotType='line', # 
#                       numColors=1, # 
#                       interactive=True) # returns palette
palette = plotenv.set()                      

# Generate data
x = np.linspace(-1,1,100)
y = np.cos(3*x)*np.sin(2*x)

# Plot - CMB DIV cmap
plt.figure()
plt.plot(x,y,c=palette[0],label='Midnight blue')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
# Custom plot wrapper
plotenv.cleanupFigure()
