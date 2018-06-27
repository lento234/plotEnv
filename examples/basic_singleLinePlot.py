"""
Basic: Simple plotting
======================
"""

import matplotlib.pyplot as plt
import numpy as np

# Plotting wrapper
import plotenv as pen

palette = pen.initialize()

colors = palette['mpl']

# Generate data
x = np.linspace(-1,1,100)
y = np.cos(3*x)*np.sin(2*x)

# Plot - CMB DIV cmap
fig,ax = pen.figure(figsize=(8,4))
ax.plot(x,y,c=colors['orange'],label='orange')
ax.set(xlabel='$x$',ylabel='$y$')

# Custom plot wrapper
pen.cleanupFigure()

ax.legend()
