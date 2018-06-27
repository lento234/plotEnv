"""
Basic: Simple plotting
======================
"""

import numpy as np

# Plotting wrapper
import plotenv as pen

# Setting up plotting environment
palette = pen.initialize()
cmap = palette['CMB']['DIV']


# Generate data
xi = np.linspace(-1,1,100)
X,Y = np.meshgrid(xi,xi)
Z = np.cos(3*X)*np.sin(2*Y)

# Levels and ticks
levels = np.linspace(xi.min(),xi.max(),22)
ticks  = levels[::2]

# Plot - SPECTRAL DIV cmap
fig, ax = pen.figure(figsize=(8,5))
im = ax.contourf(X,Y,Z,cmap=cmap,levels=levels)
ax.axis('scaled')
ax.set(xlabel='$x$ (unit)',ylabel='$y$ (unit)')
pen.colorbar(im,ax,drawEdges=True)

# Cleanup
pen.cleanupFigure(despine=False)
