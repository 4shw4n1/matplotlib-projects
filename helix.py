# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:06:31 2019

@author: 4shw4n1
"""

"""
============
Helix in 3D
============
    parametric equation of a helix:
        x = r * sin(theta)
        y = r * cos(theta)
        z = theta
        
"""

# import the required modules
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# generate the figure
fig = plt.figure()

# generate axes
ax = fig.add_subplot(111, projection = '3d')

# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, 1000)
x = theta
z = np.sin(theta)
y = np.cos(theta)
ax.plot(x, y, z, 'b', lw=2)

# A line through the centre of the helix
ax.plot((-theta_max*0.2, theta_max * 1.2), (0,0), (0,0), color='k', lw=2)

# sin/cos components of the helix (e.g. electric and magnetic field
# components of a circularly-polarized electromagnetic wave
ax.plot(x, y, 0, color='r', lw=1, alpha=0.5)
ax.plot(x, [0]*(1000), z, color='m', lw=1, alpha=0.5)

# show plot
plt.show()
