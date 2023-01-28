#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:01:39 2020

Batch run shakemap risk calculations (fatalities)
After running 'run_shakemap_prep.py' for fatalities, record the first hazard calculation number (for Albania) and replace here
@author: helencrowley
"""

import os
import pandas as pd

jobs = os.listdir('OQ-engine_jobs_run')
hc = 1 #replace with hazard calculation for Albania

events = pd.read_excel('../summary_selected_damaging_events.xlsx',header=1,engine='openpyxl')
event_ids = events.Scenario_ID

        
for job in jobs:
  if 'job' in job:
    if 'Albania' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc)) 
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+12))
      else:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+24))
    elif 'Croatia' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {} '.format(job, hc+1)) 
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {} '.format(job, hc+13)) 
      else: 
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {} '.format(job, hc+25)) 
    elif 'Cyprus' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+2))  
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+14))  
      else:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+26))  
    elif 'Germany' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+3)) 
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+15)) 
      else:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+27))  
    elif 'Greece' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+4)) 
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+16)) 
      else:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+28))  
    elif 'Iceland' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+5)) 
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+17)) 
      else:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+29))  
    elif 'Italy' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:  
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+6)) 
      elif 'night' in time:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+18)) 
      else:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+30))   
    elif 'Netherlands' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+7)) 
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+19)) 
      else:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+31))  
    elif 'Romania' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+8))  
      elif 'night' in time:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+20))
      else:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+32))
    elif 'Serbia' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+9)) 
      elif 'night' in time:  
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+21)) 
      else: 
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+33))  
    elif 'Spain' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:  
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+10)) 
      elif 'night' in time:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+22)) 
      else:
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+34))  
    elif 'Turkey' in job:
      name = str(job)
      scenario_id = name.partition('job_run_shakemap_')[2][:-4]
      time = events[events.Scenario_ID==scenario_id]['Exposure_Time']
      if 'day' in time:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+11)) 
      elif 'night' in time:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+23)) 
      else:   
        os.system('oq engine --run OQ-engine_jobs_run/{} --hc {}'.format(job, hc+35))  

