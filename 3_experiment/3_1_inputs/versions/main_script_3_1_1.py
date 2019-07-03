"""
Multi Attribute Decision Making Task v3.1.1
Time Pressure Version 2
    - accuracy incentive
    - multipliers: 0.1, 0.5, 1, 2, 3, 10
    - three condition (low/hi/no time pressure)
    - time starts from first stimulation selection
    
2019.06.06

Author: Daniel J Wilson
Contact: daniel.j.wilson@gmail.com
Github: danieljwilson
"""

#------------------#
# PsychoPy Imports #
#------------------#
from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile

#----------------#
# Python Imports #
#----------------#
import numpy as np
import random
from collections import namedtuple
from collections import Counter
from itertools import permutations 
import webbrowser as wb
import os

# MAKE SURE THE UTILS VERSION MATCHES THE EXPERIMENT VERSION
import utils_v3_1_1 as utils    # file with custom experiment functions


###########
# 0 SETUP #
###########

#---------------------#
# 0.1 Load parameters #
#---------------------#

# experiment details
expInfo = {'subject':999, 'exp_version': '3.1.1', 'psychopy_version': '3.0.2', 'start_section': 1, 'monitor': 'testMonitor'}
expInfo['dateStr'] = data.getDateStr()  # add the current time
qualtricsLink = 'https://utorontopsych.az1.qualtrics.com/jfe/form/SV_e8nqiYUuDWJ8P7T'

#-----------------------#
# 0.2 Update parameters #
#-----------------------#

# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='MADE v3', fixed=['dateStr', 'exp_version', 'psychopy_version'], order=['subject', 'monitor', 'start_section', 'exp_version', 'psychopy_version'])
if dlg.OK:
    filename = 'subject_data/' + str(expInfo['subject']) + '/' + 'Params.pickle'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    toFile(filename, expInfo)  # save params to file (unnecessary)
else:
    core.quit()  # the user hit cancel so exit

# set current monitor
currentMonitor = expInfo['monitor']

# set number of each type of trials
# debug
if expInfo['subject']==999 or expInfo['subject']==998:
	learn_trial_num = 3
	practice_trial_num = 3
	practice_tp_trial_num = 3
	task_trial_num = 42
	recall_trial_num = 3
# experiment
else:
	learn_trial_num = 25
	practice_trial_num = 25
	practice_tp_trial_num = 15
	task_trial_num = 420 # 60 calibration + 30 trials * 3 conditions * 4 times each 
	recall_trial_num = 50

# counterbalance house/face sides and good/bad houses/faces.
if expInfo['subject']%2 == 0:
    expInfo['left'] = 'house'
    expInfo['house_version'] = 0
else:
    expInfo['left'] = 'face'
    expInfo['house_version'] = 1

if (expInfo['subject']%3 == 0) or (expInfo['subject']%4 == 0):
    expInfo['face_version'] = 0
else:
    expInfo['face_version'] = 1

# indicate which segments to run
start_section = expInfo['start_section']

# Print exp params to Output Log
print('Subject: {}, Face version: {}, House version: {}, Left side: {}'.format(expInfo['subject'], expInfo['face_version'], expInfo['house_version'], expInfo['left']))

#-------------------------------------------#
# 0.3 Initialize Stimuli Values and Weights #
#-------------------------------------------#

# returns 505 trials
Stimuli, Rand_Stimuli = utils.init_stims_weights(expInfo)
# conditions ordering
conditions = utils.init_conds()

#-------------------#
# 0.4 Create Window #
#-------------------#

# small for debug (subject 999), otherwise fullscreen
if expInfo['subject'] == 999:
    win = visual.Window([800,600],allowGUI=True,
                    monitor=currentMonitor, units='deg')
else:
    win = visual.Window([800,600],allowGUI=False, fullscr=True,
                    monitor=currentMonitor, units='deg')

#-----------------#
# 0.5 Start Clock #
#-----------------#

globalClock = core.Clock()

#--------------#
# 0.6 Kill Key #
#--------------#

from psychopy import event
event.globalKeys.clear()
modifiers = ['ctrl']
    core.quit()


##################
# 1 LEARN VALUES #
##################

if start_section ==1:
    
    #---------------------#
    # 1.1 Instructions    #
    #---------------------#

    utils.instructions_1(win, Stimuli)

    #-------------------#
    # 1.2 Stim Val Test #
    #-------------------#

    utils.test_vals(win, expInfo, Rand_Stimuli, task_trial_num, trial_num=learn_trial_num, max_blocks=5, min_accuracy = 70, trial_type='learn')
    start_section+=1

################################
# 2 PRACTICE: NO TIME PRESSURE #
################################

if start_section ==2:

    #------------------#
    # 2.1 Instructions #
    #------------------#

    utils.instructions_2(win, Stimuli)

    #-------------------#
    # 2.2 Practice Task #
    #-------------------#
    
    utils.task_trials(win, expInfo, Rand_Stimuli, practice_trial_num, task_trial_num, conditions, blocks=1, block_run=1, trial_type='practice')
    start_section+=1
    
############################
# 3 TASK: NO TIME PRESSURE #
############################

if start_section ==3:

    #-------------------#
    # 3.1 Instructions  #
    #-------------------#
    
    utils.instructions_3(win, task_trial_num, blocks=14)    

    #-------------------#
    # 3.2 Task Trials   #
    #-------------------#

    tp_low_rt, payout_1 = utils.task_trials(win, expInfo, Rand_Stimuli, practice_trial_num, task_trial_num, conditions, blocks=14, block_run=2, trial_type='task')
    start_section+=1
    
#############################
# 4 PRACTICE: TIME PRESSURE #
#############################

if start_section ==4:
    # test if tp_rt exists(in case we are starting in this section)
    try:
        tp_low_rt
    except NameError:
        tp_low_rt = 3.5
    tp_high_rt = tp_low_rt/2
    
    #------------------#
    # 4.1 Instructions #
    #------------------#

    utils.instructions_4_low(win, Stimuli, tp_low_rt)

    #--------------------------#
    # 4.2 Low TP Practice Task #
    #--------------------------#

    utils.task_tp_trials(win, expInfo, Rand_Stimuli, practice_tp_trial_num, task_trial_num, conditions, tp_low_rt, blocks=1, trial_type='practice')
    
    #------------------#
    # 4.3 Instructions #
    #------------------#

    utils.instructions_4_high(win, Stimuli, tp_high_rt)

    #------------------------#
    # 4.4 High Practice Task #
    #------------------------#

    utils.task_tp_trials(win, expInfo, Rand_Stimuli, practice_tp_trial_num, task_trial_num, conditions, tp_high_rt, blocks=1, trial_type='practice')
    start_section+=1 


#########################
# 5 TASK: TIME PRESSURE #
#########################

if start_section ==5:

    #-------------------#
    # 5.1 Instructions  #
    #-------------------#
    
    utils.instructions_5(win, task_trial_num, tp_low_rt, blocks=14)

    #-------------------#
    # 5.2 Task Trials   #
    #-------------------#

    payout_2 = utils.task_tp_trials(win, expInfo, Rand_Stimuli, practice_tp_trial_num, task_trial_num, conditions, tp_low_rt, blocks=14, trial_type='task')
    start_section+=1

############
# 6 RECALL #
############

if start_section ==6:
    
    # need to pull final earnings from csv in case we start from this section
    #------------------#
    # 6.1 Instructions #
    #------------------#

    utils.instructions_6(win, recall_trial_num)

    #-------------------#
    # 6.2 Stim Val Test #
    #-------------------#

    utils.test_vals(win, expInfo, Rand_Stimuli, task_trial_num, trial_num=recall_trial_num, max_blocks=1, min_accuracy=1, trial_type='recall')
    start_section+=1

############
# 7 Rating #
############

if start_section ==7:
    
    #------------------#
    # 7.1 Instructions #
    #------------------#

    utils.instructions_7(win)

    #-------------------------#
    # 7.2 Rate Attractiveness #
    #-------------------------#

    utils.face_eval(win, expInfo, Stimuli)
    start_section+=1
    

##############
# 8 FEEDBACK #
##############

if start_section ==8:
    
    try:
        payout_1
    except NameError:
        payout_1 = 0
    try:
        payout_2
    except NameError:
        payout_2 = 0
    
    utils.instructions_8(win, payout_1, payout_2)

event.waitKeys()
# wait for participant to respond
# info on usage: https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser

print('Subject {} earnings: {}'.format(expInfo['subject'], payout_1*(1/7) + payout_2*(6/7)))

# Open questionnaire in browser 
if qualtricsLink is not None:
    import webbrowser
    webURL = qualtricsLink + "?participant=" + str(expInfo['subject']) # open using default web browser
    webbrowser.open_new(webURL)
win.close()
core.quit()