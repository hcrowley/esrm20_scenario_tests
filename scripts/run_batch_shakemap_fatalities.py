#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:01:39 2020

Batch run shakemap risk calculations (fatalities)
After running 'run_shakemap_prep.py' for fatalities, record the hazard calculation numbers for each country and time and replace here
@author: helencrowley
"""

import os
import pandas as pd

jobs = os.listdir('../shakemaps/OQ-engine_jobs_run')


events = pd.read_excel('../testing_scenarios.xlsx',header=1,engine='openpyxl')
event_ids = events.Scenario_ID

        
for job in jobs:
  if 'job' in job:
    if 'Albania' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3884'.format(job)) 
      elif 'night' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3896'.format(job))
      else:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3908'.format(job))
    elif 'Croatia' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3885 '.format(job)) 
      elif 'night' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3897 '.format(job)) 
      else: 
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3909 '.format(job)) 
    elif 'Cyprus' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('.././../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3886'.format(job))  
      elif 'night' in time:
        os.system('.././../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3898'.format(job))  
      else:
        os.system('.././../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3910'.format(job))  
    elif 'Germany' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3887'.format(job)) 
      elif 'night' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3899'.format(job)) 
      else:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3911'.format(job))  
    elif 'Greece' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3888'.format(job)) 
      elif 'night' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3900'.format(job)) 
      else:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3912'.format(job))  
    elif 'Iceland' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3889'.format(job)) 
      elif 'night' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3901'.format(job)) 
      else:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3913'.format(job))  
    elif 'Italy' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:  
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3890'.format(job)) 
      elif 'night' in time:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3902'.format(job)) 
      else:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3914'.format(job))   
    elif 'Netherlands' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3891'.format(job)) 
      elif 'night' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3903'.format(job)) 
      else:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3915'.format(job))  
    elif 'Romania' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3892'.format(job))  
      elif 'night' in time:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3904'.format(job))
      else:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3916'.format(job))
    elif 'Serbia' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3893'.format(job)) 
      elif 'night' in time:  
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3905'.format(job)) 
      else: 
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3917'.format(job))  
    elif 'Spain' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:  
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3894'.format(job)) 
      elif 'night' in time:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3906'.format(job)) 
      else:
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3918'.format(job))  
    elif 'Turkey' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3895'.format(job)) 
      elif 'night' in time:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3907'.format(job)) 
      else:   
        os.system('../../../../../openquake/oqenv/bin/oq engine --run ../shakemaps/OQ-engine_jobs_run/{} --hc 3919'.format(job))  

