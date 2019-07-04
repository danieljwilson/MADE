"""
Multi Attribute Decision Making Task v3.3.0
Attractive/Unattractive faces
2019.07.03

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
import utils_v3_3_0 as utils    # file with custom experiment functions


###########
# 0 SETUP #
###########

#---------------------#
# 0.1 Load parameters #
#---------------------#

# experiment details
expInfo = {'subject':999, 'exp_version': '3.3.0', 'psychopy_version': '3.0.2', 'start_section': 1, 'sex': 'enter', 'monitor': 'testMonitor'}
expInfo['dateStr'] = data.getDateStr()  # add the current time
qualtricsLink = 'https://utorontopsych.az1.qualtrics.com/jfe/form/SV_e8nqiYUuDWJ8P7T'

#-----------------------#
# 0.2 Update parameters #
#-----------------------#

# present a dialogue to change params
# sex needs to be entered as 'male' or 'female'
dlg = gui.DlgFromDict(expInfo, title='MADE v3', fixed=['dateStr', 'exp_version', 'psychopy_version'], order=['subject', 'monitor', 'start_section', 'sex', 'exp_version', 'psychopy_version'])
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
if expInfo['subject']>=900:
    learn_trial_num = 3
    practice_trial_num = 3
    task_trial_num = 16
    recall_trial_num = 3
# experiment
else:
    learn_trial_num = 25
    practice_trial_num = 25
    task_trial_num = 404
    recall_trial_num = 50


# counterbalance house/face sides and good/bad houses/faces.
if expInfo['subject']%2 == 0:
    expInfo['left'] = 'attractive'
    expInfo['attractive_version'] = 0
else:
    expInfo['left'] = 'unattractive'
    expInfo['attractive_version'] = 1

if (expInfo['subject']%3 == 0) or (expInfo['subject']%4 == 0):
    expInfo['unattractive_version'] = 0
else:
    expInfo['unattractive_version'] = 1

# indicate which segments to run
start_section = expInfo['start_section']

# Print exp params to Output Log
print('Subject: {}, Unattractive version: {}, Attractive version: {}, Left side: {}'.format(expInfo['subject'], expInfo['unattractive_version'], expInfo['attractive_version'], expInfo['left']))

#-------------------------------------------#
# 0.3 Initialize Stimuli Values and Weights #
#-------------------------------------------#

Stimuli, Rand_Stimuli = utils.init_stims_weights(expInfo)

#-------------------#
# 0.4 Create Window #
#-------------------#

# small for debug (subject 999), otherwise fullscreen
if expInfo['subject'] >= 950:
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
key = 'q'
modifiers = ['ctrl']
def myfunc():
    core.quit()
event.globalKeys.add(key=key, func=myfunc, modifiers=modifiers)


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

##############
# 2 PRACTICE #
##############

if start_section ==2:

    #------------------#
    # 2.1 Instructions #
    #------------------#

    utils.instructions_2(win, Stimuli)

    #-------------------#
    # 2.2 Practice Task #
    #-------------------#

    utils.task_trials(win, expInfo, Rand_Stimuli, practice_trial_num, task_trial_num, blocks=1, trial_type='practice')
    start_section+=1
    
##########
# 3 TASK #
##########

if start_section ==3:

    #-------------------#
    # 3.1 Instructions  #
    #-------------------#
    
    utils.instructions_3(win, task_trial_num, blocks=4)

    #-------------------#
    # 3.2 Task Trials   #
    #-------------------#

    earnings = utils.task_trials(win, expInfo, Rand_Stimuli, practice_trial_num, task_trial_num, blocks=4, trial_type='task')
    start_section+=1
    
############
# 4 Recall #
############

if start_section ==4:
    
    # need to pull final earnings from csv in case we start from this section
    #------------------#
    # 4.1 Instructions #
    #------------------#

    utils.instructions_4(win, recall_trial_num)

    #-------------------#
    # 4.2 Stim Val Test #
    #-------------------#

    utils.test_vals(win, expInfo, Rand_Stimuli, task_trial_num, trial_num=recall_trial_num, max_blocks=1, min_accuracy=1, trial_type='recall')
    start_section+=1

############
# 5 Rating #
############

if start_section ==5:
    
    # need to pull final earnings from csv in case we start from this section
    #------------------#
    # 5.1 Instructions #
    #------------------#

    utils.instructions_5(win)

    #-------------------------#
    # 5.2 Rate Attractiveness #
    #-------------------------#

    utils.face_eval(win, expInfo, Stimuli)
    start_section+=1

##############
# 6 Feedback #
##############

if start_section ==6:
    utils.instructions_6(win)

event.waitKeys()
# wait for participant to respond
# info on usage: https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser

# Open questionnaire in browser 
if qualtricsLink is not None:
    import webbrowser
    webURL = qualtricsLink + "?participant=" + str(expInfo['subject']) # open using default web browser
    webbrowser.open_new(webURL)
win.close()
core.quit()