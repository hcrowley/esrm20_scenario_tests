#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:01:39 2020

Batch run shakemap risk calculations

@author: helencrowley
"""

import os

jobs = os.listdir('../shakemaps/OQ-engine_jobs_run')

        
for job in jobs:
    if 'job' in job:
    	if 'Albania' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3872'.format(job))   
        elif 'Croatia' in job:
            os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3873 '.format(job))  
        elif 'Cyprus' in job:
        	os.system('.././../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3874'.format(job))  
        elif 'Germany' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3875'.format(job))  
        elif 'Greece' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3876'.format(job))  
        elif 'Iceland' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3877'.format(job))  
        elif 'Italy' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3878'.format(job))   
        elif 'Netherlands' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3879'.format(job))  
        elif 'Romania' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3880'.format(job))  
        elif 'Serbia' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3881'.format(job))  
        elif 'Spain' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3882'.format(job))  
        elif 'Turkey' in job:
        	os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3883'.format(job))  

