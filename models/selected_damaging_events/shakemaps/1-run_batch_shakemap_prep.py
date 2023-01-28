#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:01:39 2020

Batch run shakemap prep calculations
Run this script before running the ShakeMap scenario losses, store the resulting hazard calculation numbers
@author: helencrowley
"""

import os

jobs1 = os.listdir('shakemaps/OQ-engine_jobs_prep/economic')
jobs2 = os.listdir('shakemaps/OQ-engine_jobs_prep/fatalities_day')
jobs3 = os.listdir('shakemaps/OQ-engine_jobs_prep/fatalities_night')
jobs4 = os.listdir('shakemaps/OQ-engine_jobs_prep/fatalities_transit')

        
for job in jobs1:
    if 'job' in job:
        os.system('oq engine --run OQ-engine_jobs_prep/economic/{}'.format(job))     

for job in jobs2:
    if 'job' in job:
        os.system('oq engine --run .OQ-engine_jobs_prep/fatalities_day/{}'.format(job))     

for job in jobs3:
    if 'job' in job:
        os.system('oq engine --run OQ-engine_jobs_prep/fatalities_night/{}'.format(job))     

for job in jobs4:
    if 'job' in job:
        os.system('oq engine --run OQ-engine_jobs_prep/fatalities_transit/{}'.format(job))        
        
        