#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:09:01 2021

@author: helencrowley
"""


import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# read estimated loss statistics versus emdat 

eco_loss_comp = pd.read_csv('../plots/scenario_vs_emdat_eco-loss.csv')
fatalities_comp = pd.read_csv('../plots/scenario_vs_emdat_fatalities.csv')

conv = 1.16


# rupture plot eco loss

fig,ax = plt.subplots(figsize=(6,4)) 
plt.loglog(eco_loss_comp['EM-DAT']*conv,eco_loss_comp['eco-loss_mean-rupture'],'o',color='grey')

# linear fit to model
x = eco_loss_comp['EM-DAT']*conv*eco_loss_comp['CPI']/100
y = eco_loss_comp['eco-loss_mean-rupture']
def f(x, a):
    return a*x
popt,pcov=curve_fit(f, x, y)
power_y = popt[0]*x
plt.loglog(x, power_y, color='k',linewidth = 0.7)

for i in range(0,len(eco_loss_comp['EM-DAT'])):
    plt.plot([(eco_loss_comp['EM-DAT'].iloc[i])*conv,(eco_loss_comp['EM-DAT'].iloc[i])*conv],[eco_loss_comp['eco-loss_5-rupture'].iloc[i],eco_loss_comp['eco-loss_95-rupture'].iloc[i]],'-k', linewidth = 0.5)
plt.plot([10**-2,10**6],[10**-2,10**6],'--k',linewidth = 0.7)
plt.xlim(10**0, 10**6)
plt.ylim(10**0, 10**6)
ax.set_xlabel('EM-DAT Total Damage [M EUR]',fontsize=10, fontweight='bold')
ax.set_ylabel('Rupture model losses [M EUR]',fontsize=10, fontweight='bold')
plt.savefig('../plots/Observed_vs_model_scenario_eco-loss_curve_rupture.png', dpi=300)

# shakemap plot eco loss

fig,ax = plt.subplots(figsize=(6,4)) 
plt.loglog(eco_loss_comp['EM-DAT']*conv,eco_loss_comp['eco-loss_mean-shakemap'],'o',color='grey')

# linear fit to model
x = eco_loss_comp['EM-DAT']*conv*eco_loss_comp['CPI']/100
y = eco_loss_comp['eco-loss_mean-shakemap']
def f(x, a):
    return a*x
popt,pcov=curve_fit(f, x, y)
power_y = popt[0]*x
plt.loglog(x, power_y,color='k',linewidth = 0.7)

for i in range(0,len(eco_loss_comp['EM-DAT'])):
    plt.plot([(eco_loss_comp['EM-DAT'].iloc[i])*conv,(eco_loss_comp['EM-DAT'].iloc[i])*conv],[eco_loss_comp['eco-loss_5-shakemap'].iloc[i],eco_loss_comp['eco-loss_95-shakemap'].iloc[i]],'-k', linewidth = 0.5)
plt.plot([10**-2,10**6],[10**-2,10**6],'--k',linewidth = 0.7)
plt.xlim(10**0, 10**6)
plt.ylim(10**0, 10**6)
ax.set_xlabel('EM-DAT Total Damage [M EUR]',fontsize=10, fontweight='bold')
ax.set_ylabel('ShakeMap model losses [M EUR]',fontsize=10, fontweight='bold')
plt.savefig('../plots/Observed_vs_model_scenario_eco-loss_curve_shakemap.png', dpi=300)

# rupture plot fatalities

fig,ax = plt.subplots(figsize=(6,4)) 
plt.loglog(fatalities_comp['EM-DAT']*conv,fatalities_comp['fatality_mean-rupture'],'o',color='grey')

# linear fit to model
x = fatalities_comp['EM-DAT']*conv
y = fatalities_comp['fatality_mean-rupture']
def f(x, a):
    return a*x
popt,pcov=curve_fit(f, x, y)
power_y = popt[0]*x
plt.loglog(x, power_y,color='k',linewidth = 0.7)

for i in range(0,len(fatalities_comp['EM-DAT'])):
    plt.plot([(fatalities_comp['EM-DAT'].iloc[i])*conv,(fatalities_comp['EM-DAT'].iloc[i])*conv],[fatalities_comp['fatality_5-rupture'].iloc[i],fatalities_comp['fatality_95-rupture'].iloc[i]],'-k', linewidth = 0.5)
plt.plot([10**-2,10**6],[10**-2,10**6],'--k',linewidth = 0.7)
plt.xlim(10**-1, 10**6)
plt.ylim(10**-1, 10**6)
ax.set_xlabel('EM-DAT Total fatalities',fontsize=10, fontweight='bold')
ax.set_ylabel('Rupture model fatalities',fontsize=10, fontweight='bold')
plt.savefig('../plots/Observed_vs_model_scenario_fatalities_curve_rupture.png', dpi=300)

# shakemap plot fatalities

fig,ax = plt.subplots(figsize=(6,4)) 
plt.loglog(fatalities_comp['EM-DAT']*conv,fatalities_comp['fatality_mean-shakemap'],'o',color='grey')

# linear fit to model
x = fatalities_comp['EM-DAT']*conv
y = fatalities_comp['fatality_mean-shakemap']
def f(x, a):
    return a*x
popt,pcov=curve_fit(f, x, y)
power_y = popt[0]*x
plt.loglog(x, power_y,color='k',linewidth = 0.7)

for i in range(0,len(fatalities_comp['EM-DAT'])):
    plt.plot([(fatalities_comp['EM-DAT'].iloc[i])*conv,(fatalities_comp['EM-DAT'].iloc[i])*conv],[fatalities_comp['fatality_5-shakemap'].iloc[i],fatalities_comp['fatality_95-shakemap'].iloc[i]],'-k', linewidth = 0.5)
plt.plot([10**-2,10**6],[10**-2,10**6],'--k',linewidth = 0.7)
plt.xlim(10**-1, 10**6)
plt.ylim(10**-1, 10**6)
ax.set_xlabel('EM-DAT Total fatalities',fontsize=10, fontweight='bold')
ax.set_ylabel('ShakeMap model fatalities',fontsize=10, fontweight='bold')
plt.savefig('../plots/Observed_vs_model_scenario_fatalities_curve_shakemap.png', dpi=300)

