"""
Basic: Simple plotting
======================
"""

import numpy as np

# Plotting wrapper
import plotenv as pen

# Setting up plotting environment
palette = pen.initialize(numColors=9)

# Generate data
x = np.linspace(-1,1,100)
y = [np.cos(i*x/10)*np.sin(i*x/10) for i in range(9)]

# labels
colors = palette['colors']

# Plot
fig,ax = pen.figure(figsize=(8,4))
for i in range(9):
    ax.plot(x,y[i],c=colors[i],label='line {}'.format(i))
ax.set(xlabel=r'$x$', ylabel=r'$y$')

# Custom plot wrapper
pen.cleanupFigure()

# Legend after despine / cleanup
pen.legend(outside=True)
