#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:07:09 2020

Batch extract scenario risk results

@author: helencrowley
"""

import os
import subprocess as sp


#%%
start_id = 4020#manually input by user
for i in range(0,1):
     
    lrc = sp.getoutput('../../../../../openquake/oqenv/bin/oq engine --lrc')

    for line in lrc.splitlines():
    	if str(start_id+i) in line:
    		text = line.partition('Scenario ')[2].partition(' with')[0]
            

    output = sp.getoutput('../../../../../openquake/oqenv/bin/oq engine --list-outputs {}'.format(start_id+i))
    
    # for line in output.splitlines():
    #     if 'Risk By Event' in line:
    #         out_id = line[0:5]
    #         os.system('../../../../../openquake/oqenv/bin/oq engine --export-output {} ../ruptures/outputs/'.format(out_id))
    #         os.rename('../ruptures/outputs/risk_by_event_{}.csv'.format(start_id+i),'../ruptures/outputs/risk_by_event_{}.csv'.format(text))

    for line in output.splitlines():
        if 'Risk By Event' in line:
            out_id = line[0:5]
            os.system('../../../../../openquake/oqenv/bin/oq engine --export-output {} ../shakemaps/outputs/fatalities'.format(out_id))
            os.rename('../shakemaps/outputs/fatalities/risk_by_event_{}.csv'.format(start_id+i),'../shakemaps/outputs/fatalities/risk_by_event_{}.csv'.format(text))


            
