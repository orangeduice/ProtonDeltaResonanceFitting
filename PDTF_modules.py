# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:48:49 2020

@author: osjac
"""

import numpy as np


def func1(E,w):
    return (1.467*10**7)/((((w**2)/4)+(E-1232)**2))


def discrepancy(x,y,yerr,w):
    temp = 0
    for i in range(0,len(x)):
        temp = temp + ((y[i]-func1(x[i],w))/(yerr[i]*x[i]))**2
    return temp


def theory(Ex,w):
    energyTH = np.linspace(min(Ex),max(Ex),100)
    pionNumTH = []
    for i in energyTH:
        pionNumTH.append(func1(i,w))
    return energyTH, pionNumTH


def read(f):
    c1 = [] ; c2 = [] ; c3 = []
    for line in f:
        r1 , r2 , r3 = line . split ()
        c1.append(float(r1))
        c2.append(float(r2))
        c3.append(float(r3))
    
    c1 = np.array(c1)
    c2 = np.array(c2)
    c3 = np.array(c3)
    return c1 , c2 , c3