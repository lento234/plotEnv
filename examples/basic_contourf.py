"""
Basic: Simple plotting
======================
"""

import matplotlib.pyplot as plt
import numpy as np

# Plotting wrapper
import plotenv

# Setting up plotting environment
palette = plotenv.set(plotType='surface',
                      interactive=True) # returns palette
                      

# Generate data
xi = np.linspace(-1,1,100)
X,Y = np.meshgrid(xi,xi)
Z = np.cos(3*X)*np.sin(2*Y)

# Levels and ticks
levels = np.linspace(xi.min(),xi.max(),22)
ticks  = np.linspace(xi.min(),xi.max(),11)

# Plot - CMB DIV cmap
plt.figure()
plt.contourf(X,Y,Z,cmap=palette['CMB']['DIV'],levels=levels)
plt.axis('scaled')
plt.axis('scaled')

# Customization
plotenv.colorbar(ticks=ticks,
                 orientation='v',
                 format='%.2f',label=r'$z=\cos(3x)\ \sin(2y)$')
plotenv.cleanupFigure(despine=False)


# Plot - CMB HOT cmap
plt.figure()
plt.contourf(X,Y,Z,cmap=palette['CMB']['HOT'],levels=levels)
plt.axis('scaled')
plt.axis('scaled')

# Customization
plotenv.colorbar(ticks=ticks,
                 orientation='v',
                 format='%.2f',label=r'$z=\cos(3x)\ \sin(2y)$')
plotenv.cleanupFigure(despine=False)

# Plot - CMB COLD cmap
plt.figure()
plt.contourf(X,Y,Z,cmap=palette['CMB']['COLD'],levels=levels)
plt.axis('scaled')
plt.axis('scaled')

# Customization
plotenv.colorbar(ticks=ticks,
                 orientation='v',
                 format='%.2f',label=r'$z=\cos(3x)\ \sin(2y)$')
plotenv.cleanupFigure(despine=False)

# Plot - SPECTRAL DIV cmap
plt.figure()
plt.contourf(X,Y,Z,cmap=palette['SPECTRAL']['DIV'],levels=levels)
plt.axis('scaled')
plt.axis('scaled')

# Customization
plotenv.colorbar(ticks=ticks,
                 orientation='v',
                 format='%.2f',label=r'$z=\cos(3x)\ \sin(2y)$')
plotenv.cleanupFigure(despine=False)


# Plot - SPECTRAL HOT cmap
plt.figure()
plt.contourf(X,Y,Z,cmap=palette['SPECTRAL']['HOT'],levels=levels)
plt.axis('scaled')
plt.axis('scaled')

# Customization
plotenv.colorbar(ticks=ticks,
                 orientation='v',
                 format='%.2f',label=r'$z=\cos(3x)\ \sin(2y)$')
plotenv.cleanupFigure(despine=False)

# Plot - SPECTRAL COLD cmap
plt.figure()
plt.contourf(X,Y,Z,cmap=palette['SPECTRAL']['COLD'],levels=levels)
plt.axis('scaled')
plt.axis('scaled')

# Customization
plotenv.colorbar(ticks=ticks,
                 orientation='v',
                 format='%.2f',label=r'$z=\cos(3x)\ \sin(2y)$')
plotenv.cleanupFigure(despine=False)