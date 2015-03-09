#!/usr/bin/python

#This source code is public domain 
#Author: Christian Schirm

# This fixes complains about missing DISPLAY variable on server
import matplotlib
matplotlib.use('Agg')

import numpy, pylab
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
 
G=1
k=1
f0=0.5
 
x=numpy.linspace(-8,8,16)[1:-1]
numpy.random.seed(50)
y=numpy.random.normal(G/(1+numpy.exp(-k*G*x)*(G/f0-1)),0.1)
#numpy.random.seed(int(time.time()))
 
err=1E8
err=numpy.mean(numpy.square(y-G/(1+numpy.exp(-k*G*x)*(G/f0-1))))
print err,G,k,f0
numpy.random.seed(2)
for i in range(5000):
    faktor=1+0.01*(numpy.random.rand()-.5)
    for ivar in 1,2,3:
        backup=[err,G,k,f0]
        var=backup[:]
        var[ivar]=var[ivar]*faktor
        err,G,k,f0=var
 
        err_neu=numpy.mean(numpy.square(y-G/(1+numpy.exp(-k*G*x)*(G/f0-1))))
        if err_neu<err:
            err=err_neu
        else:
            var[ivar]=backup[ivar]
            err,G,k,f0=var
print err,G,k,f0,"(Fehlerquadrat minimiert)"
 
xneu=numpy.linspace(-8,8,50)
yneu=G/(1+numpy.exp(-k*G*xneu)*(G/f0-1))
 
xr=x
yr=G/(1+numpy.exp(-k*G*xr)*(G/f0-1))
residuen=[]
for i in range(len(x)): residuen+=[[x[i]+8,x[i]+8],[y[i]*10,yr[i]*10],'g-']
 
plt.clf()
fig=plt.figure(figsize=(4.5, 3.5))
fig.subplotpars.bottom=0.15
y0=plt.plot(*residuen[:-3])
plt.setp(y0, color='#60c060', linewidth=1.5)
y0=plt.plot(*residuen[-3:],label='Residuum')
plt.setp(y0, color='#60c060', linewidth=1.5)
y2=plt.plot(xneu+8,yneu*10,'r-',label='Modellfunktion')
plt.setp(y2, linewidth=1.5)
y1=plt.plot(x+8,y*10,'o',label='Messungen')
plt.xlabel('x')
plt.ylabel('y')
font = FontProperties()
font.set_size('medium')
leg = plt.legend([y1,y2,y0],['Messpunkte','Modellfunktion','Residuen'],loc='lower right',labelspacing=0.3,prop=font)
plt.grid(True)
#plt.show()
plt.savefig('MDKQ1.svg')
