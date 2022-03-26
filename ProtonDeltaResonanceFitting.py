# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:56:54 2020

@author: osjac
"""



from PDTF_modules import discrepancy
from PDTF_modules import read
from PDTF_modules import func1
from PDTF_modules import theory
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#================================DATALOADING===================================
f= open('data1.txt','r')
energy , pionNum , pionNumError = read(f)
f. close ()

f= open('data2.txt','r')
energy2 , pionNum2 , pionNumError2 = read(f)
f. close ()

f= open('data3.txt','r')
energy3 , pionNum3 , pionNumError3 = read(f)
f. close () 
#================================DATALOADING===================================   


#=================================FITTING======================================  
ans, cov = curve_fit(func1,energy,pionNum,sigma=pionNumError,absolute_sigma=True,p0=100)
w = ans[0] ; werr = cov[0][0]

ans2, cov2 = curve_fit(func1,energy2,pionNum2,sigma=pionNumError2,absolute_sigma=True,p0=100)
w2 = ans2[0] ; werr2 = cov2[0][0]

ans3, cov3 = curve_fit(func1,energy3,pionNum3,sigma=pionNumError3,absolute_sigma=True,p0=100)
w3 = ans3[0] ; werr3 = cov3[0][0]
#=================================FITTING====================================== 

print("w Vaules (using curve fit):")
print("Set 1:            Error:")
print(w,werr)
print("Set 2:            Error:")
print(w2,werr2)
print("Set 3:            Error:")
print(w3,werr3)


energyTH, pionNumTH = theory(energy,w)
energyTH2, pionNumTH2 = theory(energy2,w2)
energyTH3, pionNumTH3 = theory(energy3,w3)

#================================PLOTTING======================================
fig, axs = plt.subplots(3,sharex=True,figsize=(20, 10))

t = 1
for ax in axs:
    ax.set_ylabel('''Number of scattered 
Pions''' + ' Data set: ' + str(t),fontsize=10)
    t = t + 1
    
wPa = mpatches.Patch(color='green', label=('w = '+ str(round(w,3)) + ' ± '  + str(round(werr,3))))
axs[0].legend(handles=[wPa])
wPa2 = mpatches.Patch(color='green', label=('w = '+ str(round(w2,3)) + ' ± ' + str(round(werr2,3))))
axs[1].legend(handles=[wPa2])
wPa3 = mpatches.Patch(color='green', label=('w = '+ str(round(w3,3)) + ' ± ' + str(round(werr3,3))))
axs[2].legend(handles=[wPa3])


plt.xlabel('Energy of incident Pions (MeV)')
axs[0].set_title('Delta resonance of the Proton')
axs[0].plot(energy,pionNum,'x',linestyle='-', markersize=5)
axs[0].errorbar(energy,pionNum,yerr = pionNumError, fmt =' ')
axs[1].plot(energy2,pionNum2,'x',linestyle='-', markersize=5)
axs[1].errorbar(energy2,pionNum2,yerr = pionNumError2, fmt =' ')
axs[2].plot(energy3,pionNum3,'x',linestyle='-', markersize=5)
axs[2].errorbar(energy3,pionNum3,yerr = pionNumError3, fmt =' ')


axs[0].plot(energyTH,pionNumTH)
axs[1].plot(energyTH2,pionNumTH2)
axs[2].plot(energyTH2,pionNumTH2)

plt.savefig('Delta resonance of the Proton (2).png')
#================================PLOTTING======================================


