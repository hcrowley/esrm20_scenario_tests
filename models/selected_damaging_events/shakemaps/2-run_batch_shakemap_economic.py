#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:01:39 2020

Batch run shakemap risk calculations (economic loss)
After running 'run_shakemap_prep.py' for economic losses, record the hazard calculation numbers for Albania and replace here
@author: helencrowley
"""

import os

jobs = os.listdir('OQ-engine_jobs_run')
hc = 1 #input here the hazard calculation for Albania
        
for job in jobs:
    if 'job' in job:
    	if 'Albania' in job:
        	os.system('oq engine --run .OQ-engine_jobs_run/{} --hc {}'.format(job,hc))   
        elif 'Croatia' in job:
            os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {} '.format(job,hc+1))  
        elif 'Cyprus' in job:
        	os.system('.././../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+2))  
        elif 'Germany' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+3))  
        elif 'Greece' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+4))  
        elif 'Iceland' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+5))  
        elif 'Italy' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+6))   
        elif 'Netherlands' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+7))  
        elif 'Romania' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+8))  
        elif 'Serbia' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+9))  
        elif 'Spain' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+10))  
        elif 'Turkey' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc {}'.format(job, hc+11))  

