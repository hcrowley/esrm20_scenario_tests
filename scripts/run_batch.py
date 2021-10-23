#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:01:39 2020

Batch run scenario risk calculations

@author: helencrowley
"""

import os

jobs = os.listdir('../ruptures/OQ-engine_jobs')

        
for job in jobs:
    if 'job' in job:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../ruptures/OQ-engine_jobs/{}'.format(job))        
        
        