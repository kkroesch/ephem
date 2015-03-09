#!/usr/bin/python
from datetime import date
from math import radians as rad,degrees as deg

import ephem

dulliken = ephem.Observer()
dulliken.name='Dulliken'
dulliken.lat=rad(47.35)  # lat/long in decimal degrees
dulliken.long=rad(7.94)

s = ephem.Sun()

dulliken.date = date.today()# local time zone, I'm in UTC+1
dulliken.date -= ephem.hour # always everything in UTC

for i in range(24*4): # compute position for every 15 minutes
    s.compute(dulliken)

    print("%s\t%s\t%s") % (ephem.localtime(dulliken.date).time().strftime("%H:%M:%S"), deg(s.alt),deg(s.az))
    dulliken.date += ephem.minute*15
