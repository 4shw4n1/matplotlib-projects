# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:06:57 2019

@author: 4shw4n1
"""

"""
============
Spiral in 3D
============   
"""

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from math import exp,sin,cos
from pylab import *

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
n=100
a=0.5
b=0.20

th=np.linspace(0, 35, 1000)

x=a*exp(b*th)*cos(th)
y=a*exp(b*th)*sin(th)

z = np.linspace(0,2, 1000)

ax.plot(x, y, z, label = 'Spiral')
ax.legend(loc = 'best')

ax.set_axis_off()
plt.show()
