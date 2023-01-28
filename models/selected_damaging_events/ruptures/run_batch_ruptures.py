#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:01:39 2020

Batch run scenario risk calculations
Make sure you activate the OQ virtual environment before running this script

@author: helencrowley
"""

import os

jobs = os.listdir('OQ-engine_jobs')

        
for job in jobs:
    if 'job' in job:
        os.system('oq engine --run ../ruptures/OQ-engine_jobs/{}'.format(job))        
        
        