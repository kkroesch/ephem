#!/usr/bin/python
from datetime import date
from math import radians as rad,degrees as deg

import ephem

j = ephem.city('Tel Aviv')
v = ephem.Venus()

j.date = ephem.Date('1/12/1')

for i in range(24): # compute position for every 15 minutes
    v.compute(j)
    print("%s\t%s\t%s") % (ephem.localtime(j.date).time().strftime("%H:%M:%S"), deg(v.alt),deg(v.az))
    j.date += ephem.hour*24
