#!/usr/bin/python
from datetime import date
from math import radians as rad,degrees as deg

import ephem
g = ephem.Observer()
g.name='Somewhere'
g.lat=rad(47.35)  # lat/long in decimal degrees
g.long=rad(7.94)

m = ephem.Mars()
j = ephem.Jupiter()
g.date = date.today()
g.date -= ephem.hour

azimuths = []
heights = []

for i in range(24*4): # compute position for every 15 minutes
	j.compute(g)
	azimuths.append(deg(j.az))
	heights.append(deg(j.alt))
	g.date += ephem.minute*15
	print "%s:\t%.2f\t%.2f" % (ephem.localtime(g.date).time().strftime("%H:%M"), deg(j.alt), deg(j.az))

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

plt.plot(azimuths, heights)
plt.xlabel('Azimuth')
plt.ylabel('Altitude')
plt.grid(True)
plt.savefig('mars.svg')
