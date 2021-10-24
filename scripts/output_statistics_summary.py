#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 08:52:43 2021

@author: helencrowley
"""


import os
import pandas as pd
import numpy as np


# rupture files

output_files = os.listdir('../ruptures/outputs')

ruptures_out = pd.DataFrame(columns=['event','eco_mean','eco_median','eco_5',
                                     'eco_95','fatality_mean','fatality_median',
                                     'fatality_5','fatality_95'])

str_loss_mean = np.zeros(shape=0)
str_loss_median = np.zeros(shape=0)
str_loss_5 = np.zeros(shape=0)
str_loss_95 = np.zeros(shape=0)
occ_loss_mean = np.zeros(shape=0)
occ_loss_median = np.zeros(shape=0)
occ_loss_5 = np.zeros(shape=0)
occ_loss_95 = np.zeros(shape=0)


for file in output_files:
    data = pd.read_csv('../ruptures/outputs/{}'.format(file), header =1)
    data_str = data[data.loss_type=='structural']
    data_occ = data[data.loss_type=='occupants']
    str_loss_mean = np.append(str_loss_mean,np.mean(data_str.loss))
    str_loss_median = np.append(str_loss_median,np.percentile(data_str.loss,50))
    str_loss_5 = np.append(str_loss_5,np.percentile(data_str.loss,5))
    str_loss_95 = np.append(str_loss_95,np.percentile(data_str.loss,95))
    occ_loss_mean = np.append(occ_loss_mean,np.mean(data_occ.loss))
    occ_loss_median = np.append(occ_loss_median,np.percentile(data_occ.loss,50))
    occ_loss_5 = np.append(occ_loss_5,np.percentile(data_occ.loss,5))
    occ_loss_95 = np.append(occ_loss_95,np.percentile(data_occ.loss,95))
    
    
ruptures_out.event = [z[14:-4] for z in output_files]
ruptures_out.eco_mean = str_loss_mean/1000000 
ruptures_out.eco_median = str_loss_median/1000000
ruptures_out.eco_5 = str_loss_5/1000000
ruptures_out.eco_95 = str_loss_95/1000000 
ruptures_out.fatality_mean = occ_loss_mean
ruptures_out.fatality_median = occ_loss_median
ruptures_out.fatality_5 = occ_loss_5
ruptures_out.fatality_95 = occ_loss_95


ruptures_out.to_csv('../scenario_ruptures_output_summary.csv', index= False)


#%% shakemap files

output_files = os.listdir('../shakemaps/outputs/fatalities')

shakemaps_out = pd.DataFrame(columns=['event','eco_mean','eco_median','eco_5',
                                     'eco_95','fatality_mean','fatality_median',
                                     'fatality_5','fatality_95'])

str_loss_mean = np.zeros(shape=0)
str_loss_median = np.zeros(shape=0)
str_loss_5 = np.zeros(shape=0)
str_loss_95 = np.zeros(shape=0)
occ_loss_mean = np.zeros(shape=0)
occ_loss_median = np.zeros(shape=0)
occ_loss_5 = np.zeros(shape=0)
occ_loss_95 = np.zeros(shape=0)


for file in output_files:
    data_str = pd.read_csv('../shakemaps/outputs/economic/{}'.format(file), header =1)
    data_occ = pd.read_csv('../shakemaps/outputs/fatalities/{}'.format(file), header =1)
    str_loss_mean = np.append(str_loss_mean,np.mean(data_str.loss))
    str_loss_median = np.append(str_loss_median,np.percentile(data_str.loss,50))
    str_loss_5 = np.append(str_loss_5,np.percentile(data_str.loss,5))
    str_loss_95 = np.append(str_loss_95,np.percentile(data_str.loss,95))
    occ_loss_mean = np.append(occ_loss_mean,np.mean(data_occ.loss))
    occ_loss_median = np.append(occ_loss_median,np.percentile(data_occ.loss,50))
    occ_loss_5 = np.append(occ_loss_5,np.percentile(data_occ.loss,5))
    occ_loss_95 = np.append(occ_loss_95,np.percentile(data_occ.loss,95))
    
    
shakemaps_out.event = [z[14:-4] for z in output_files]
shakemaps_out.eco_mean = str_loss_mean/1000000 
shakemaps_out.eco_median = str_loss_median/1000000
shakemaps_out.eco_5 = str_loss_5/1000000
shakemaps_out.eco_95 = str_loss_95/1000000 
shakemaps_out.fatality_mean = occ_loss_mean
shakemaps_out.fatality_median = occ_loss_median
shakemaps_out.fatality_5 = occ_loss_5
shakemaps_out.fatality_95 = occ_loss_95


shakemaps_out.to_csv('../scenario_shakemaps_output_summary.csv', index= False)