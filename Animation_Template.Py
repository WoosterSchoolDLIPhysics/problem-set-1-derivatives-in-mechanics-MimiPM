# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:09:12 2017

@author: Mimi PM
"""

from pylab import *

t = linspace(0,1,100)

x = 3*sin(2*pi*t)
y = 2*cos(2*pi*t)

vx =3*cos(2*pi*t)*2*pi
vy =2*-sin(2*pi*t)*2*pi

ax =3*-sin(2*pi*t)*2*pi
ay =2*-cos(2*pi*t)*2*pi

figure(1)

for it in arange(len(t)):
    clf()
    #subplot(131)
    plot(x,y)
    plot([0,x[it]],[0,y[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)

    text(1.1*x[it]/10,1.1*y[it]/10,r'$\vec{x}$',color='red',size=15)
    grid()
    #savefig('frame_%03d.png' % it)
    
    plot(vx,vy)
    plot([0,vx[it]],[0,vy[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*vx[it],1.2*vy[it],r'$\vec{v}$',color='green',size=15)

    text(1.1*vx[it]/10,1.1*vy[it]/10,r'$\vec{v}$',color='black',size=15)
    grid()
    #savefig('frame_%03d.png' % it)

    plot(ax,ay)
    plot([0,ax[it]],[0,ay[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*ax[it],1.2*ay[it],r'$\vec{a}$',color='purple',size=15)

    text(1.1*ax[it]/10,1.1*ay[it]/10,r'$\vec{a}$',color='skyblue',size=15)
    grid()
    #savefig('frame_%03d.png' % it)
    
    
    pause(.001)

speed = sqrt(vx**2+vy**2)
maxit = argmax(speed)
tmax = t[maxit]
print(tmax)