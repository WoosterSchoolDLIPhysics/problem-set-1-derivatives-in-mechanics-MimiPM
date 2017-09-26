# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:17:04 2017

@author: Mimi PM
"""
from pylab import *

t0 = 0.0 #initial time
tf = 30.0 #how long I fall
dt = 0.5 #time step size

t = arange(t0,tf,dt)
v = zeros(len(t))
v0 = 0
v[0] = v0

#define constants
b = .05
g = 10 #meters per second sqr of course.
m = 1.0 #kg

for i in arange(1,len(t)):
    dv = (-b/m*v[i-1]-g)*dt
    v[i] = v[i-1] + dv


figure(1)
clf()
plot (t,v,'bo')
vt = m*g/b
plot(t,vt*(exp(-b*t/m)-1))