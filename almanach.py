import datetime
from datetime import date
from math import radians as rad, degrees as deg
import ephem

def last_day_of_month(dt):
	next_month = (dt.month % 12) + 1
	end_date = datetime.date(dt.year, next_month, 1) - datetime.timedelta(days=1)
	return end_date

obs = ephem.Observer()
obs.name='Windhoek'
obs.lat=rad(22.34)  # lat/long in decimal degrees
obs.long=rad(17.5)

moon = ephem.Moon()
sun = ephem.Sun()

today = datetime.date(2013,4,19) #date.today()
start = datetime.date(today.year, today.month, 1)
end = last_day_of_month(today)

events = []
while start < end:
	obs.date = start
	sunrise = obs.next_rising(sun).datetime().strftime('%H:%M')
	sunset = obs.next_setting(sun).datetime().strftime('%H:%M')
	moonrise = obs.next_rising(moon).datetime().strftime('%H:%M')
	moonset = obs.next_setting(moon).datetime().strftime('%H:%M')

	print "%s | Sunrise: %s\tSunset: %s\tMoonrise: %s\tMoonset: %s" % (start.strftime('%d.%m.%Y'), sunrise, sunset, moonrise, moonset)
	
	events.append([start.strftime('%d.%m.%Y'), sunrise, sunset, moonrise, moonset])
	start = start + datetime.timedelta(days=1)
	

#print events
