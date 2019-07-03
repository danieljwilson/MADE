#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on January 24, 2018, at 09:37
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'test02_TestSegment'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\lab\\Dropbox\\LabSharedFolder\\MADE01\\CODE\\v3_FractionalWeights\\Part2_Test.psyexp',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "TestInstr_1"
TestInstr_1Clock = core.Clock()
instructions_9 = visual.TextStim(win=win, name='instructions_9',
    text='Congratulations on completing the learning phase of the experiment.\n\nNext we will show you how the actual trials work.',
    font='Helvetica',
    pos=(0, .6), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continue9_14 = visual.TextStim(win=win, name='continue9_14',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
import random
from random import randint
import pandas as pd
import itertools
inputText = ""

earnings = 0
earningsUpdate = 0

mult1 = 1
mult2 = 1
switchMult = 1 #for image switch version

exp2Trial = 0
counter = 0

flipVersion = 1
posNeg = 1

# Create House and Face Distributions
import glob
face_list = glob.glob('images/morphs/face/*.jpg')
house_list = glob.glob('images/morphs/house/*.jpg')

# create values to match to stimuli
values = np.arange(-1.,1.01,0.02)

# Get rid of extra digits
for i in range(len(values)):
    values[i] = round(values[i], 2)

# Create Data Frames
house_df = pd.DataFrame(
    {'value': values,
     'exemplar': house_list
    })

face_df = pd.DataFrame(
    {'value': values,
     'exemplar': face_list
    })

# Create mult value list
multipliers = [0.1, 0.5, 1,2,3, 10]
# Create mult vals distribution
mult_vals = list(itertools.product(multipliers, multipliers))
mult_vals = np.repeat(mult_vals, 8, axis=0) # duplicate values * simsPerVal
extra_base_val = np.repeat([[1,1]], 112, axis=0) # extra instances of base val [1,1] to add up to 120 total

# append extra 112 base value instances. Result = 30% base value, 70% with multipliers
# Of those with multipliers: 1/36 of each permutation
mult_vals_dist = np.append(mult_vals, extra_base_val, axis=0)
# shuffle the elements
np.random.shuffle(mult_vals_dist)

# create mult val counter
mult_val_counter = 25   # this is just for the test trials
                        # it is reset to 0 after the test trials

#For alternating the image
trialImage = '/Users/djw/Dropbox/PHD/CENDRI/Project/Code/LabSharedFolder/MADE01/CODE/v3_FractionalWeights/images/morphs/face/faceMorph000.jpg' # this just initializes an image
imageSelector = randint(1,2)

# Initialize components for Routine "TestInstr_2"
TestInstr_2Clock = core.Clock()
faceMorph_50 = visual.ImageStim(
    win=win, name='faceMorph_50',units='pix', 
    image=face_df.exemplar[75], mask=None,
    ori=0, pos=(-250, 0), size=(300,300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
houseMorph_neg25 = visual.ImageStim(
    win=win, name='houseMorph_neg25',units='pix', 
    image=house_df.exemplar[37], mask=None,
    ori=0, pos=(250, 0), size=[300,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='You will need to consider the SUM of the two values in order to decide whether you ACCEPT or REJECT the combination.\n\nIn this case the combined value of the two images is: $0.50 - $0.26 = $0.24.',
    font='Helvetica',
    pos=(0, .65), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
faceValueText_2 = visual.TextStim(win=win, name='faceValueText_2',
    text='default text',
    font='Helvetica',
    pos=(-0.4, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
houseValue_2 = visual.TextStim(win=win, name='houseValue_2',
    text='default text',
    font='Helvetica',
    pos=(0.4, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
compValues_2 = visual.TextStim(win=win, name='compValues_2',
    text='Therefore it would make sense to ACCEPT this combination.',
    font='Helvetica',
    pos=(0, -.65), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
continue9_3 = visual.TextStim(win=win, name='continue9_3',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);

# Initialize components for Routine "TestInstr_3"
TestInstr_3Clock = core.Clock()
faceMorph05 = visual.ImageStim(
    win=win, name='faceMorph05',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(300,300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instructions_5 = visual.TextStim(win=win, name='instructions_5',
    text='However you will only see one image at a time.\n\nLook at the first image (in this case the face), calculate the value, then press the SPACE BAR to view the other image.',
    font='Helvetica',
    pos=(0, .65), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
faceValueText = visual.TextStim(win=win, name='faceValueText',
    text='default text',
    font='Helvetica',
    pos=(0, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
continue9_6 = visual.TextStim(win=win, name='continue9_6',
    text='press the SPACE BAR to see the second image',
    font='Helvetica',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "TestInstr_4"
TestInstr_4Clock = core.Clock()
houseMorph07_3 = visual.ImageStim(
    win=win, name='houseMorph07_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=[300,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instructions_6 = visual.TextStim(win=win, name='instructions_6',
    text="Each time you PRESS the space bar you will SWAP between the two images until you decide to ACCEPT (press 'f') or REJECT (press 'j') the combination.",
    font='Helvetica',
    pos=(0, .6), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
houseValue_3 = visual.TextStim(win=win, name='houseValue_3',
    text='default text',
    font='Helvetica',
    pos=(0, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
continue9_7 = visual.TextStim(win=win, name='continue9_7',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "one_more_thing"
one_more_thingClock = core.Clock()
instructions_17 = visual.TextStim(win=win, name='instructions_17',
    text='ONE MORE THING!',
    font='Helvetica',
    pos=(0, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continue9_24 = visual.TextStim(win=win, name='continue9_24',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
multipliers = visual.TextStim(win=win, name='multipliers',
    text='MULTIPLIERS',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "mult_instructions"
mult_instructionsClock = core.Clock()
faceMorph = visual.ImageStim(
    win=win, name='faceMorph',units='pix', 
    image=face_df.exemplar[75], mask=None,
    ori=0, pos=(-250, 0), size=(300,300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
house_neg25_2 = visual.ImageStim(
    win=win, name='house_neg25_2',units='pix', 
    image=house_df.exemplar[37], mask=None,
    ori=0, pos=(250, 0), size=[300,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instructions_16 = visual.TextStim(win=win, name='instructions_16',
    text='Multipliers can change the value of the image on a trial-by-trial basis.\n\nIn this example the HOUSE image has a multiplier of 3 and the FACE image has a multiplier of 1.',
    font='Helvetica',
    pos=(0, .7), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
faceValueText_3 = visual.TextStim(win=win, name='faceValueText_3',
    text='default text',
    font='Helvetica',
    pos=(-0.35, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
houseValue = visual.TextStim(win=win, name='houseValue',
    text='default text',
    font='Helvetica',
    pos=(0.35, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
compValues = visual.TextStim(win=win, name='compValues',
    text='Because of the MULTIPLIERS it would make sense to REJECT this combination as the SUMMED VALUE ($0.50 - $0.26 * 3) is -$0.28.',
    font='Helvetica',
    pos=(0, -.7), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
continue9_23 = visual.TextStim(win=win, name='continue9_23',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
x_1 = visual.TextStim(win=win, name='x_1',
    text='x 1',
    font='Arial',
    pos=(-0.33, 0.43), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-8.0);
x_3 = visual.TextStim(win=win, name='x_3',
    text='x 3',
    font='Arial',
    pos=(0.33, 0.43), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "test_run_10"
test_run_10Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='You will now complete 10 example trials.',
    font='Helvetica',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continue9_4 = visual.TextStim(win=win, name='continue9_4',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
FixationCrossJitter = visual.TextStim(win=win, name='FixationCrossJitter',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
import random


# Initialize components for Routine "trial_run_test"
trial_run_testClock = core.Clock()

square_entry = visual.Rect(
    win=win, name='square_entry',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
Accept_Reject_3 = visual.TextStim(win=win, name='Accept_Reject_3',
    text='Do you accept or reject this combination?',
    font='Helvetica',
    pos=(0, 0.82), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
nextTrialTest = visual.TextStim(win=win, name='nextTrialTest',
    text="enter 'f' for accept, and 'j' for reject",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
earnings__4 = visual.TextStim(win=win, name='earnings__4',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
SWITCH_Image2_2 = visual.ImageStim(
    win=win, name='SWITCH_Image2_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 20), size=(450, 450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
EarningsLabel_3 = visual.TextStim(win=win, name='EarningsLabel_3',
    text='total earnings',
    font='Helvetica',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
SWITCH_Mult_2 = visual.TextStim(win=win, name='SWITCH_Mult_2',
    text='default text',
    font='Helvetica',
    pos=(0, 0.64), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-8.0);
press_space = visual.TextStim(win=win, name='press_space',
    text='Press SPACE to see\nthe OTHER IMAGE.',
    font='Arial',
    pos=(0.6, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "Test1_WinLoss"
Test1_WinLossClock = core.Clock()
amount = visual.TextStim(win=win, name='amount',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

text_12 = visual.TextStim(win=win, name='text_12',
    text='Trial Earnings:',
    font='Helvetica',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
correct_wrong = visual.TextStim(win=win, name='correct_wrong',
    text='default text',
    font='Helvetica',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "Block02_a"
Block02_aClock = core.Clock()

continue4_2 = visual.TextStim(win=win, name='continue4_2',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
FinishedPart1 = visual.TextStim(win=win, name='FinishedPart1',
    text='This is the end of the example trials.\n\nIf you do not understand how the experiment works that is okay - just please LET THE RA KNOW.\n',
    font='Helvetica',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Block02_b"
Block02_bClock = core.Clock()

multInstr_5 = visual.TextStim(win=win, name='multInstr_5',
    text='We will now begin the REAL TRIALS.\n\nThere will be FOUR sets of 100 trials.\n\nWe will SHOW you the HOUSE and FACE VALUES before each block of trials.\n\nCONCENTRATE: the more accurate you are, the more money you earn.',
    font='Helvetica',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
continue4_6 = visual.TextStim(win=win, name='continue4_6',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "block_number"
block_numberClock = core.Clock()
multInstr = visual.TextStim(win=win, name='multInstr',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.18, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continue4_7 = visual.TextStim(win=win, name='continue4_7',
    text='press any key to continue (when ready)',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
FixationCrossJitter = visual.TextStim(win=win, name='FixationCrossJitter',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
import random


# Initialize components for Routine "FullTest_01_Mult"
FullTest_01_MultClock = core.Clock()

square_entry_4 = visual.Rect(
    win=win, name='square_entry_4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
Accept_Reject_2 = visual.TextStim(win=win, name='Accept_Reject_2',
    text='Do you accept or reject this combination?',
    font='Helvetica',
    pos=(0, 0.82), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
nextTrialTest_4 = visual.TextStim(win=win, name='nextTrialTest_4',
    text="enter 'f' for accept, and 'j' for reject",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
earnings__2 = visual.TextStim(win=win, name='earnings__2',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
SWITCH_Image2 = visual.ImageStim(
    win=win, name='SWITCH_Image2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 20), size=(450, 450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
EarningsLabel_2 = visual.TextStim(win=win, name='EarningsLabel_2',
    text='total earnings',
    font='Helvetica',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
SWITCH_Mult = visual.TextStim(win=win, name='SWITCH_Mult',
    text='default text',
    font='Helvetica',
    pos=(0, 0.64), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Initialize components for Routine "Feedback_Block2"
Feedback_Block2Clock = core.Clock()
amount_2 = visual.TextStim(win=win, name='amount_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

text_13 = visual.TextStim(win=win, name='text_13',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='Trial Earnings',
    font='Helvetica',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
Correct_wrong2 = visual.TextStim(win=win, name='Correct_wrong2',
    text='default text',
    font='Helvetica',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "FinalScore"
FinalScoreClock = core.Clock()

FinalEarnings = visual.TextStim(win=win, name='FinalEarnings',
    text='FINAL EARNINGS',
    font='Helvetica',
    pos=(0, 0.75), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
square_entry_5 = visual.Rect(
    win=win, name='square_entry_5',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
earnings__3 = visual.TextStim(win=win, name='earnings__3',
    text='default text',
    font='Helvetica',
    pos=(0, -0.4), height=0.25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
test_earnings = visual.TextStim(win=win, name='test_earnings',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0);
total_earnings = visual.TextStim(win=win, name='total_earnings',
    text='TOTAL',
    font='Arial',
    pos=(0, -0.1), height=0.13, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0);
continue4 = visual.TextStim(win=win, name='continue4',
    text='TELL THE EXPERIMENTER YOU HAVE FINISHED',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TestInstr_1"-------
t = 0
TestInstr_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_14 = event.BuilderKeyResponse()

# keep track of which components have finished
TestInstr_1Components = [exitKeys_14, instructions_9, continue9_14]
for thisComponent in TestInstr_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "TestInstr_1"-------
while continueRoutine:
    # get current time
    t = TestInstr_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_14* updates
    if t >= 0.0 and exitKeys_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_14.tStart = t
        exitKeys_14.frameNStart = frameN  # exact frame index
        exitKeys_14.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exitKeys_14.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *instructions_9* updates
    if t >= 0.0 and instructions_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_9.tStart = t
        instructions_9.frameNStart = frameN  # exact frame index
        instructions_9.setAutoDraw(True)
    
    # *continue9_14* updates
    if t >= 0.5 and continue9_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_14.tStart = t
        continue9_14.frameNStart = frameN  # exact frame index
        continue9_14.setAutoDraw(True)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TestInstr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TestInstr_1"-------
for thisComponent in TestInstr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "TestInstr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TestInstr_2"-------
t = 0
TestInstr_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_2 = event.BuilderKeyResponse()
faceValueText_2.setText("$%0.2f" % face_df.value[75])
houseValue_2.setText("$%0.2f" % house_df.value[37])
# keep track of which components have finished
TestInstr_2Components = [exitKeys_2, faceMorph_50, houseMorph_neg25, instructions_2, faceValueText_2, houseValue_2, compValues_2, continue9_3]
for thisComponent in TestInstr_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "TestInstr_2"-------
while continueRoutine:
    # get current time
    t = TestInstr_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_2* updates
    if t >= 0.0 and exitKeys_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_2.tStart = t
        exitKeys_2.frameNStart = frameN  # exact frame index
        exitKeys_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exitKeys_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *faceMorph_50* updates
    if t >= 0.0 and faceMorph_50.status == NOT_STARTED:
        # keep track of start time/frame for later
        faceMorph_50.tStart = t
        faceMorph_50.frameNStart = frameN  # exact frame index
        faceMorph_50.setAutoDraw(True)
    
    # *houseMorph_neg25* updates
    if t >= 0.0 and houseMorph_neg25.status == NOT_STARTED:
        # keep track of start time/frame for later
        houseMorph_neg25.tStart = t
        houseMorph_neg25.frameNStart = frameN  # exact frame index
        houseMorph_neg25.setAutoDraw(True)
    
    # *instructions_2* updates
    if t >= 0.0 and instructions_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_2.tStart = t
        instructions_2.frameNStart = frameN  # exact frame index
        instructions_2.setAutoDraw(True)
    
    # *faceValueText_2* updates
    if t >= 0 and faceValueText_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        faceValueText_2.tStart = t
        faceValueText_2.frameNStart = frameN  # exact frame index
        faceValueText_2.setAutoDraw(True)
    
    # *houseValue_2* updates
    if t >= 0 and houseValue_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        houseValue_2.tStart = t
        houseValue_2.frameNStart = frameN  # exact frame index
        houseValue_2.setAutoDraw(True)
    
    # *compValues_2* updates
    if t >= 0 and compValues_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        compValues_2.tStart = t
        compValues_2.frameNStart = frameN  # exact frame index
        compValues_2.setAutoDraw(True)
    
    # *continue9_3* updates
    if t >= 0.5 and continue9_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_3.tStart = t
        continue9_3.frameNStart = frameN  # exact frame index
        continue9_3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TestInstr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TestInstr_2"-------
for thisComponent in TestInstr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "TestInstr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TestInstr_3"-------
t = 0
TestInstr_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_5 = event.BuilderKeyResponse()
faceMorph05.setImage(face_df.exemplar[75])
faceValueText.setText("Face Value = $%0.2f" % face_df.value[75])
# keep track of which components have finished
TestInstr_3Components = [exitKeys_5, faceMorph05, instructions_5, faceValueText, continue9_6]
for thisComponent in TestInstr_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "TestInstr_3"-------
while continueRoutine:
    # get current time
    t = TestInstr_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_5* updates
    if t >= 0.0 and exitKeys_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_5.tStart = t
        exitKeys_5.frameNStart = frameN  # exact frame index
        exitKeys_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exitKeys_5.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *faceMorph05* updates
    if t >= 0.0 and faceMorph05.status == NOT_STARTED:
        # keep track of start time/frame for later
        faceMorph05.tStart = t
        faceMorph05.frameNStart = frameN  # exact frame index
        faceMorph05.setAutoDraw(True)
    
    # *instructions_5* updates
    if t >= 0.0 and instructions_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_5.tStart = t
        instructions_5.frameNStart = frameN  # exact frame index
        instructions_5.setAutoDraw(True)
    
    # *faceValueText* updates
    if t >= 0 and faceValueText.status == NOT_STARTED:
        # keep track of start time/frame for later
        faceValueText.tStart = t
        faceValueText.frameNStart = frameN  # exact frame index
        faceValueText.setAutoDraw(True)
    
    # *continue9_6* updates
    if t >= 0.5 and continue9_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_6.tStart = t
        continue9_6.frameNStart = frameN  # exact frame index
        continue9_6.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TestInstr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TestInstr_3"-------
for thisComponent in TestInstr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "TestInstr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TestInstr_4"-------
t = 0
TestInstr_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_6 = event.BuilderKeyResponse()
houseMorph07_3.setImage(house_df.exemplar[37])
houseValue_3.setText("House Value = $%0.2f" % house_df.value[37])
# keep track of which components have finished
TestInstr_4Components = [exitKeys_6, houseMorph07_3, instructions_6, houseValue_3, continue9_7]
for thisComponent in TestInstr_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "TestInstr_4"-------
while continueRoutine:
    # get current time
    t = TestInstr_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_6* updates
    if t >= 0.0 and exitKeys_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_6.tStart = t
        exitKeys_6.frameNStart = frameN  # exact frame index
        exitKeys_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exitKeys_6.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *houseMorph07_3* updates
    if t >= 0.0 and houseMorph07_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        houseMorph07_3.tStart = t
        houseMorph07_3.frameNStart = frameN  # exact frame index
        houseMorph07_3.setAutoDraw(True)
    
    # *instructions_6* updates
    if t >= 0.0 and instructions_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_6.tStart = t
        instructions_6.frameNStart = frameN  # exact frame index
        instructions_6.setAutoDraw(True)
    
    # *houseValue_3* updates
    if t >= 0 and houseValue_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        houseValue_3.tStart = t
        houseValue_3.frameNStart = frameN  # exact frame index
        houseValue_3.setAutoDraw(True)
    
    # *continue9_7* updates
    if t >= 0.5 and continue9_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_7.tStart = t
        continue9_7.frameNStart = frameN  # exact frame index
        continue9_7.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TestInstr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TestInstr_4"-------
for thisComponent in TestInstr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "TestInstr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "one_more_thing"-------
t = 0
one_more_thingClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_24 = event.BuilderKeyResponse()
# keep track of which components have finished
one_more_thingComponents = [exitKeys_24, instructions_17, continue9_24, multipliers]
for thisComponent in one_more_thingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "one_more_thing"-------
while continueRoutine:
    # get current time
    t = one_more_thingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_24* updates
    if t >= 0.5 and exitKeys_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_24.tStart = t
        exitKeys_24.frameNStart = frameN  # exact frame index
        exitKeys_24.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exitKeys_24.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *instructions_17* updates
    if t >= 0.0 and instructions_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_17.tStart = t
        instructions_17.frameNStart = frameN  # exact frame index
        instructions_17.setAutoDraw(True)
    
    # *continue9_24* updates
    if t >= 0.5 and continue9_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_24.tStart = t
        continue9_24.frameNStart = frameN  # exact frame index
        continue9_24.setAutoDraw(True)
    
    # *multipliers* updates
    if t >= 1 and multipliers.status == NOT_STARTED:
        # keep track of start time/frame for later
        multipliers.tStart = t
        multipliers.frameNStart = frameN  # exact frame index
        multipliers.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in one_more_thingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "one_more_thing"-------
for thisComponent in one_more_thingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "one_more_thing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mult_instructions"-------
t = 0
mult_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_23 = event.BuilderKeyResponse()
faceValueText_3.setText("${0}\nValue with Mult. = ${1}".format(face_df.value[75], face_df.value[75]))
houseValue.setText("${0}\nValue with Mult. = ${1}".format(house_df.value[37], house_df.value[37] * 3))
# keep track of which components have finished
mult_instructionsComponents = [exitKeys_23, faceMorph, house_neg25_2, instructions_16, faceValueText_3, houseValue, compValues, continue9_23, x_1, x_3]
for thisComponent in mult_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mult_instructions"-------
while continueRoutine:
    # get current time
    t = mult_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_23* updates
    if t >= 0.0 and exitKeys_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_23.tStart = t
        exitKeys_23.frameNStart = frameN  # exact frame index
        exitKeys_23.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exitKeys_23.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *faceMorph* updates
    if t >= 0.0 and faceMorph.status == NOT_STARTED:
        # keep track of start time/frame for later
        faceMorph.tStart = t
        faceMorph.frameNStart = frameN  # exact frame index
        faceMorph.setAutoDraw(True)
    
    # *house_neg25_2* updates
    if t >= 0.0 and house_neg25_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        house_neg25_2.tStart = t
        house_neg25_2.frameNStart = frameN  # exact frame index
        house_neg25_2.setAutoDraw(True)
    
    # *instructions_16* updates
    if t >= 0.0 and instructions_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_16.tStart = t
        instructions_16.frameNStart = frameN  # exact frame index
        instructions_16.setAutoDraw(True)
    
    # *faceValueText_3* updates
    if t >= 0 and faceValueText_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        faceValueText_3.tStart = t
        faceValueText_3.frameNStart = frameN  # exact frame index
        faceValueText_3.setAutoDraw(True)
    
    # *houseValue* updates
    if t >= 0 and houseValue.status == NOT_STARTED:
        # keep track of start time/frame for later
        houseValue.tStart = t
        houseValue.frameNStart = frameN  # exact frame index
        houseValue.setAutoDraw(True)
    
    # *compValues* updates
    if t >= 0 and compValues.status == NOT_STARTED:
        # keep track of start time/frame for later
        compValues.tStart = t
        compValues.frameNStart = frameN  # exact frame index
        compValues.setAutoDraw(True)
    
    # *continue9_23* updates
    if t >= 0.5 and continue9_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_23.tStart = t
        continue9_23.frameNStart = frameN  # exact frame index
        continue9_23.setAutoDraw(True)
    
    # *x_1* updates
    if t >= 0.0 and x_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        x_1.tStart = t
        x_1.frameNStart = frameN  # exact frame index
        x_1.setAutoDraw(True)
    
    # *x_3* updates
    if t >= 0.0 and x_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        x_3.tStart = t
        x_3.frameNStart = frameN  # exact frame index
        x_3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mult_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mult_instructions"-------
for thisComponent in mult_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "mult_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test_run_10"-------
t = 0
test_run_10Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_3 = event.BuilderKeyResponse()
# keep track of which components have finished
test_run_10Components = [exitKeys_3, instructions_3, continue9_4]
for thisComponent in test_run_10Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test_run_10"-------
while continueRoutine:
    # get current time
    t = test_run_10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_3* updates
    if t >= 0.5 and exitKeys_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_3.tStart = t
        exitKeys_3.frameNStart = frameN  # exact frame index
        exitKeys_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exitKeys_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *instructions_3* updates
    if t >= 0.0 and instructions_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_3.tStart = t
        instructions_3.frameNStart = frameN  # exact frame index
        instructions_3.setAutoDraw(True)
    
    # *continue9_4* updates
    if t >= 0.5 and continue9_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_4.tStart = t
        continue9_4.frameNStart = frameN  # exact frame index
        continue9_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_run_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_run_10"-------
for thisComponent in test_run_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test_run_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=20, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='test')
thisExp.addLoop(test)  # add the loop to the experiment
thisTest = test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest.keys():
        exec(paramName + '= thisTest.' + paramName)

for thisTest in test:
    currentLoop = test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest.keys():
            exec(paramName + '= thisTest.' + paramName)
    
    # ------Prepare to start Routine "FixationCross"-------
    t = 0
    FixationCrossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    FixationCrossComponents = [FixationCrossJitter]
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCrossJitter* updates
        if t >= 0.0 and FixationCrossJitter.status == NOT_STARTED:
            # keep track of start time/frame for later
            FixationCrossJitter.tStart = t
            FixationCrossJitter.frameNStart = frameN  # exact frame index
            FixationCrossJitter.setAutoDraw(True)
        frameRemains = 3 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if FixationCrossJitter.status == STARTED and t >= frameRemains:
            FixationCrossJitter.setAutoDraw(False)
        core.wait(random.uniform(0.0, 0.8))
        break
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "trial_run_test"-------
    t = 0
    trial_run_testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    theseKeys=""
    shift_flag = False
    #inputTextValue.alignHoriz = 'center'
    
    #Count Trials
    counter = counter + 1
    
    #For alternating the image
    imageSelector = randint(1,2)
    #Save the image that we start with
    viewedImage = imageSelector%2
    imageList = [viewedImage]
    
    #flipChoice OFF
    flip = False
    
    #Pick random value for House and Face morph
    #This means the trials are randomized WITH replacement
    randFace = random.randint(0,100) # this INCLUDES 100
    randHouse = random.randint(0,100)
    
    #Create filepath for image
    trialFace = face_df.exemplar[randFace]
    trialHouse = house_df.exemplar[randHouse]
    
    #Calculate monetary value based on morph value
    actFaceVal = face_df.value[randFace]
    actHouseVal = house_df.value[randHouse]
    
    # Take value from mult distribution based on counter
    mult1 = mult_vals_dist[mult_val_counter][0]
    mult2 = mult_vals_dist[mult_val_counter][1]
    
    mult_val_counter = mult_val_counter + 1
    numberEntry = event.BuilderKeyResponse()
    square_entry.setOpacity(1)
    square_entry.setPos((0, -.75))
    square_entry.setLineWidth(1)
    square_entry.setOri(0)
    square_entry.setSize((0.25, 0.15))
    earnings__4.setText(('$%0.2f' %(earnings)))
    # keep track of which components have finished
    trial_run_testComponents = [numberEntry, square_entry, Accept_Reject_3, nextTrialTest, earnings__4, SWITCH_Image2_2, EarningsLabel_3, SWITCH_Mult_2, press_space]
    for thisComponent in trial_run_testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_run_test"-------
    while continueRoutine:
        # get current time
        t = trial_run_testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n = len(theseKeys)
        i = 0
        
        #For alternating the image & multiplier
        if imageSelector%2==0:
            trialImage = face_df.exemplar[randFace]
            switchMult = str(mult2)
        if imageSelector%2==1:
            trialImage = house_df.exemplar[randHouse]
            switchMult = str(mult1)
        
        ####################
        # KEY STROKE INPUT #
        ####################
        while i < n:
            if theseKeys[i] == 'space':
                imageSelector +=1
                viewedImage = imageSelector%2
                imageList.append(viewedImage)
        
            #for ACCEPTING and starting a new loop
            if theseKeys[i] == 'f':
                earningsUpdate = actHouseVal*mult1 + actFaceVal*mult2
                if earningsUpdate >=0:
                    correct=1
                else:
                    correct=0
                earnings = earnings + earningsUpdate
                winLoss=earningsUpdate
                continueRoutine = False
                break
            
            #for REJECTING and starting a new loop
            elif theseKeys[i] == 'j':
                earningsUpdate = actHouseVal*mult1 + actFaceVal*mult2
                if earningsUpdate >0:
                    correct=0
                    winLoss= -1*earningsUpdate
                    earnings = earnings - earningsUpdate
                    continueRoutine = False
                else:
                    correct=1
                    winLoss= 0.00
                    continueRoutine = False
                break
        
            elif theseKeys[i] in ['lshift', 'rshift']:
                shift_flag = True
                i = i+1
        
            else:
                if len(theseKeys[i]) ==1:
                    #we only have 1 char so should be a normal key
                    #otherwise it might be 'ctrl' or similar so ignore it
                    if shift_flag:
                        inputText += chr( ord(theseKeys[i]) - ord(' '))
                        shift_flag = False
                    else:
                        inputText += theseKeys[i]
                i = i + 1
        
        # *numberEntry* updates
        if t >= 0.1 and numberEntry.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry.tStart = t
            numberEntry.frameNStart = frameN  # exact frame index
            numberEntry.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numberEntry.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numberEntry.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numberEntry.keys.extend(theseKeys)  # storing all keys
                numberEntry.rt.append(numberEntry.clock.getTime())
        
        # *square_entry* updates
        if t >= 0 and square_entry.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry.tStart = t
            square_entry.frameNStart = frameN  # exact frame index
            square_entry.setAutoDraw(True)
        
        # *Accept_Reject_3* updates
        if t >= 0 and Accept_Reject_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Accept_Reject_3.tStart = t
            Accept_Reject_3.frameNStart = frameN  # exact frame index
            Accept_Reject_3.setAutoDraw(True)
        
        # *nextTrialTest* updates
        if t >= 0 and nextTrialTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest.tStart = t
            nextTrialTest.frameNStart = frameN  # exact frame index
            nextTrialTest.setAutoDraw(True)
        
        # *earnings__4* updates
        if t >= 0 and earnings__4.status == NOT_STARTED:
            # keep track of start time/frame for later
            earnings__4.tStart = t
            earnings__4.frameNStart = frameN  # exact frame index
            earnings__4.setAutoDraw(True)
        
        # *SWITCH_Image2_2* updates
        if t >= 0 and SWITCH_Image2_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            SWITCH_Image2_2.tStart = t
            SWITCH_Image2_2.frameNStart = frameN  # exact frame index
            SWITCH_Image2_2.setAutoDraw(True)
        if SWITCH_Image2_2.status == STARTED:  # only update if drawing
            SWITCH_Image2_2.setImage(trialImage, log=False)
        
        # *EarningsLabel_3* updates
        if t >= 0 and EarningsLabel_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            EarningsLabel_3.tStart = t
            EarningsLabel_3.frameNStart = frameN  # exact frame index
            EarningsLabel_3.setAutoDraw(True)
        
        # *SWITCH_Mult_2* updates
        if t >= 0 and SWITCH_Mult_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            SWITCH_Mult_2.tStart = t
            SWITCH_Mult_2.frameNStart = frameN  # exact frame index
            SWITCH_Mult_2.setAutoDraw(True)
        if SWITCH_Mult_2.status == STARTED:  # only update if drawing
            SWITCH_Mult_2.setText("x {0}".format(switchMult), log=False)
        
        # *press_space* updates
        if t >= 0.0 and press_space.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_space.tStart = t
            press_space.frameNStart = frameN  # exact frame index
            press_space.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_run_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_run_test"-------
    for thisComponent in trial_run_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #let's store the final text string into the results final...
    thisExp.addData('Trial', counter)
    thisExp.addData('correct', correct) 
    thisExp.addData('faceVal', actFaceVal)
    thisExp.addData('houseVal', actHouseVal)
    thisExp.addData('mult1House', mult1)
    thisExp.addData('mult2Face', mult2)
    thisExp.addData('summedVal', earningsUpdate)
    thisExp.addData('earnings', earnings)
    thisExp.addData('imageList', imageList) 
    
    inputText=""
    
    #done with the next routine
    #if exp2Trial>=200:
    #    trials_2.finished=1
    # check responses
    if numberEntry.keys in ['', [], None]:  # No response was made
        numberEntry.keys=None
    test.addData('numberEntry.keys',numberEntry.keys)
    if numberEntry.keys != None:  # we had a response
        test.addData('numberEntry.rt', numberEntry.rt)
    # the Routine "trial_run_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Test1_WinLoss"-------
    t = 0
    Test1_WinLossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    amount.setText(('$%0.2f' %(winLoss)))
    if winLoss >= 0.0:
        correct = "CORRECT"
        correctColor = "green"
    else:
        correct = "INCORRECT"
        correctColor = "red"
    correct_wrong.setColor(correctColor, colorSpace='rgb')
    correct_wrong.setText(correct)
    # keep track of which components have finished
    Test1_WinLossComponents = [amount, text_12, text_10, correct_wrong]
    for thisComponent in Test1_WinLossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Test1_WinLoss"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Test1_WinLossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *amount* updates
        if t >= 0.0 and amount.status == NOT_STARTED:
            # keep track of start time/frame for later
            amount.tStart = t
            amount.frameNStart = frameN  # exact frame index
            amount.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if amount.status == STARTED and t >= frameRemains:
            amount.setAutoDraw(False)
        
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_12.status == STARTED and t >= frameRemains:
            text_12.setAutoDraw(False)
        
        # *text_10* updates
        if t >= 1.5 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        frameRemains = 1.5 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_10.status == STARTED and t >= frameRemains:
            text_10.setAutoDraw(False)
        
        # *correct_wrong* updates
        if t >= 0.0 and correct_wrong.status == NOT_STARTED:
            # keep track of start time/frame for later
            correct_wrong.tStart = t
            correct_wrong.frameNStart = frameN  # exact frame index
            correct_wrong.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if correct_wrong.status == STARTED and t >= frameRemains:
            correct_wrong.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test1_WinLossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test1_WinLoss"-------
    for thisComponent in Test1_WinLossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if counter>=10:  # number of demo trials
        counter = 0
        earnings = 0
        mult_val_counter = 0
        test.finished=1
    thisExp.nextEntry()
    
# completed 20 repeats of 'test'

# get names of stimulus parameters
if test.trialList in ([], [None], None):
    params = []
else:
    params = test.trialList[0].keys()
# save data for this loop
test.saveAsText(filename + 'test.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Block02_a"-------
t = 0
Block02_aClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

numberEntry_6 = event.BuilderKeyResponse()
# keep track of which components have finished
Block02_aComponents = [numberEntry_6, continue4_2, FinishedPart1]
for thisComponent in Block02_aComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block02_a"-------
while continueRoutine:
    # get current time
    t = Block02_aClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *numberEntry_6* updates
    if t >= 2. and numberEntry_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_6.tStart = t
        numberEntry_6.frameNStart = frameN  # exact frame index
        numberEntry_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if numberEntry_6.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *continue4_2* updates
    if t >= 0.5 and continue4_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4_2.tStart = t
        continue4_2.frameNStart = frameN  # exact frame index
        continue4_2.setAutoDraw(True)
    
    # *FinishedPart1* updates
    if t >= 0.5 and FinishedPart1.status == NOT_STARTED:
        # keep track of start time/frame for later
        FinishedPart1.tStart = t
        FinishedPart1.frameNStart = frameN  # exact frame index
        FinishedPart1.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block02_aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block02_a"-------
for thisComponent in Block02_aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Block02_a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Block02_b"-------
t = 0
Block02_bClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
loop_num = 1
numberEntry_10 = event.BuilderKeyResponse()
# keep track of which components have finished
Block02_bComponents = [numberEntry_10, multInstr_5, continue4_6]
for thisComponent in Block02_bComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block02_b"-------
while continueRoutine:
    # get current time
    t = Block02_bClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *numberEntry_10* updates
    if t >= 2. and numberEntry_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_10.tStart = t
        numberEntry_10.frameNStart = frameN  # exact frame index
        numberEntry_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if numberEntry_10.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *multInstr_5* updates
    if t >= 0.5 and multInstr_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        multInstr_5.tStart = t
        multInstr_5.frameNStart = frameN  # exact frame index
        multInstr_5.setAutoDraw(True)
    
    # *continue4_6* updates
    if t >= 0.5 and continue4_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4_6.tStart = t
        continue4_6.frameNStart = frameN  # exact frame index
        continue4_6.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block02_bComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block02_b"-------
for thisComponent in Block02_bComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# the Routine "Block02_b" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_blocks = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_blocks')
thisExp.addLoop(trial_blocks)  # add the loop to the experiment
thisTrial_block = trial_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_block.rgb)
if thisTrial_block != None:
    for paramName in thisTrial_block.keys():
        exec(paramName + '= thisTrial_block.' + paramName)

for thisTrial_block in trial_blocks:
    currentLoop = trial_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_block.rgb)
    if thisTrial_block != None:
        for paramName in thisTrial_block.keys():
            exec(paramName + '= thisTrial_block.' + paramName)
    
    # ------Prepare to start Routine "block_number"-------
    t = 0
    block_numberClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    numberEntry_11 = event.BuilderKeyResponse()
    multInstr.setText("BLOCK #{0}".format(loop_num))
    # keep track of which components have finished
    block_numberComponents = [numberEntry_11, multInstr, continue4_7]
    for thisComponent in block_numberComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "block_number"-------
    while continueRoutine:
        # get current time
        t = block_numberClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *numberEntry_11* updates
        if t >= 2. and numberEntry_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry_11.tStart = t
            numberEntry_11.frameNStart = frameN  # exact frame index
            numberEntry_11.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if numberEntry_11.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *multInstr* updates
        if t >= 0 and multInstr.status == NOT_STARTED:
            # keep track of start time/frame for later
            multInstr.tStart = t
            multInstr.frameNStart = frameN  # exact frame index
            multInstr.setAutoDraw(True)
        
        # *continue4_7* updates
        if t >= 0.5 and continue4_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            continue4_7.tStart = t
            continue4_7.frameNStart = frameN  # exact frame index
            continue4_7.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_numberComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_number"-------
    for thisComponent in block_numberComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_number" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=200, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2.keys():
                exec(paramName + '= thisTrial_2.' + paramName)
        
        # ------Prepare to start Routine "FixationCross"-------
        t = 0
        FixationCrossClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        FixationCrossComponents = [FixationCrossJitter]
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "FixationCross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FixationCrossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixationCrossJitter* updates
            if t >= 0.0 and FixationCrossJitter.status == NOT_STARTED:
                # keep track of start time/frame for later
                FixationCrossJitter.tStart = t
                FixationCrossJitter.frameNStart = frameN  # exact frame index
                FixationCrossJitter.setAutoDraw(True)
            frameRemains = 3 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if FixationCrossJitter.status == STARTED and t >= frameRemains:
                FixationCrossJitter.setAutoDraw(False)
            core.wait(random.uniform(0.0, 0.8))
            break
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixationCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FixationCross"-------
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "FullTest_01_Mult"-------
        t = 0
        FullTest_01_MultClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        theseKeys=""
        shift_flag = False
        #inputTextValue.alignHoriz = 'center'
        
        #Count Trials
        counter = counter + 1
        
        #For alternating the image
        imageSelector = randint(1,2)
        #Save the image that we start with
        viewedImage = imageSelector%2
        imageList = [viewedImage]
        
        #flipChoice OFF
        flip = False
        
        #Pick random value for House and Face morph
        #This means the trials are randomized WITH replacement
        randFace = random.randint(0,100) # this INCLUDES 100
        randHouse = random.randint(0,100)
        
        #Create filepath for image
        trialFace = face_df.exemplar[randFace]
        trialHouse = house_df.exemplar[randHouse]
        
        #Calculate monetary value based on morph value
        actFaceVal = face_df.value[randFace]
        actHouseVal = house_df.value[randHouse]
        
        # Take value from mult distribution based on counter
        mult1 = mult_vals_dist[mult_val_counter][0]
        mult2 = mult_vals_dist[mult_val_counter][1]
        
        mult_val_counter = mult_val_counter + 1
        
        numberEntry_4 = event.BuilderKeyResponse()
        square_entry_4.setOpacity(1)
        square_entry_4.setPos((0, -.75))
        square_entry_4.setLineWidth(1)
        square_entry_4.setOri(0)
        square_entry_4.setSize((0.25, 0.15))
        earnings__2.setText(('$%0.2f' %(earnings)))
        # keep track of which components have finished
        FullTest_01_MultComponents = [numberEntry_4, square_entry_4, Accept_Reject_2, nextTrialTest_4, earnings__2, SWITCH_Image2, EarningsLabel_2, SWITCH_Mult]
        for thisComponent in FullTest_01_MultComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "FullTest_01_Mult"-------
        while continueRoutine:
            # get current time
            t = FullTest_01_MultClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            n = len(theseKeys)
            i = 0
            
            #For alternating the image & multiplier
            if imageSelector%2==0:
                trialImage = face_df.exemplar[randFace]
                switchMult = str(mult2)
            if imageSelector%2==1:
                trialImage = house_df.exemplar[randHouse]
                switchMult = str(mult1)
            
            ####################
            # KEY STROKE INPUT #
            ####################
            while i < n:
                if theseKeys[i] == 'space':
                    imageSelector +=1
                    viewedImage = imageSelector%2
                    imageList.append(viewedImage)
            
                #for ACCEPTING and starting a new loop
                if theseKeys[i] == 'f':
                    earningsUpdate = actHouseVal*mult1 + actFaceVal*mult2
                    if earningsUpdate >=0:
                        correct=1
                    else:
                        correct=0
                    earnings = earnings + earningsUpdate
                    winLoss=earningsUpdate
                    continueRoutine = False
                    break
                
                #for REJECTING and starting a new loop
                elif theseKeys[i] == 'j':
                    earningsUpdate = actHouseVal*mult1 + actFaceVal*mult2
                    if earningsUpdate >0:
                        correct=0
                        winLoss= -1*earningsUpdate
                        earnings = earnings - earningsUpdate
                        continueRoutine = False
                    else:
                        correct=1
                        winLoss= 0.00
                        continueRoutine = False
                    break
            
                elif theseKeys[i] in ['lshift', 'rshift']:
                    shift_flag = True
                    i = i+1
            
                else:
                    if len(theseKeys[i]) ==1:
                        #we only have 1 char so should be a normal key
                        #otherwise it might be 'ctrl' or similar so ignore it
                        if shift_flag:
                            inputText += chr( ord(theseKeys[i]) - ord(' '))
                            shift_flag = False
                        else:
                            inputText += theseKeys[i]
                    i = i + 1
            
            # *numberEntry_4* updates
            if t >= 0.1 and numberEntry_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                numberEntry_4.tStart = t
                numberEntry_4.frameNStart = frameN  # exact frame index
                numberEntry_4.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(numberEntry_4.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if numberEntry_4.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    numberEntry_4.keys.extend(theseKeys)  # storing all keys
                    numberEntry_4.rt.append(numberEntry_4.clock.getTime())
            
            # *square_entry_4* updates
            if t >= 0 and square_entry_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                square_entry_4.tStart = t
                square_entry_4.frameNStart = frameN  # exact frame index
                square_entry_4.setAutoDraw(True)
            
            # *Accept_Reject_2* updates
            if t >= 0 and Accept_Reject_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Accept_Reject_2.tStart = t
                Accept_Reject_2.frameNStart = frameN  # exact frame index
                Accept_Reject_2.setAutoDraw(True)
            
            # *nextTrialTest_4* updates
            if t >= 0 and nextTrialTest_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                nextTrialTest_4.tStart = t
                nextTrialTest_4.frameNStart = frameN  # exact frame index
                nextTrialTest_4.setAutoDraw(True)
            
            # *earnings__2* updates
            if t >= 0 and earnings__2.status == NOT_STARTED:
                # keep track of start time/frame for later
                earnings__2.tStart = t
                earnings__2.frameNStart = frameN  # exact frame index
                earnings__2.setAutoDraw(True)
            
            # *SWITCH_Image2* updates
            if t >= 0 and SWITCH_Image2.status == NOT_STARTED:
                # keep track of start time/frame for later
                SWITCH_Image2.tStart = t
                SWITCH_Image2.frameNStart = frameN  # exact frame index
                SWITCH_Image2.setAutoDraw(True)
            if SWITCH_Image2.status == STARTED:  # only update if drawing
                SWITCH_Image2.setImage(trialImage, log=False)
            
            # *EarningsLabel_2* updates
            if t >= 0 and EarningsLabel_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                EarningsLabel_2.tStart = t
                EarningsLabel_2.frameNStart = frameN  # exact frame index
                EarningsLabel_2.setAutoDraw(True)
            
            # *SWITCH_Mult* updates
            if t >= 0 and SWITCH_Mult.status == NOT_STARTED:
                # keep track of start time/frame for later
                SWITCH_Mult.tStart = t
                SWITCH_Mult.frameNStart = frameN  # exact frame index
                SWITCH_Mult.setAutoDraw(True)
            if SWITCH_Mult.status == STARTED:  # only update if drawing
                SWITCH_Mult.setText("x {0}".format(switchMult), log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FullTest_01_MultComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FullTest_01_Mult"-------
        for thisComponent in FullTest_01_MultComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #let's store the final text string into the results final...
        thisExp.addData('Trial', counter)
        thisExp.addData('correct', correct) 
        thisExp.addData('faceVal', actFaceVal)
        thisExp.addData('houseVal', actHouseVal)
        thisExp.addData('mult1House', mult1)
        thisExp.addData('mult2Face', mult2)
        thisExp.addData('summedVal', earningsUpdate)
        thisExp.addData('earnings', earnings)
        thisExp.addData('imageList', imageList) 
        
        inputText=""
        
        #done with the next routine
        #if exp2Trial>=200:
        #    trials_2.finished=1
        # check responses
        if numberEntry_4.keys in ['', [], None]:  # No response was made
            numberEntry_4.keys=None
        trials_2.addData('numberEntry_4.keys',numberEntry_4.keys)
        if numberEntry_4.keys != None:  # we had a response
            trials_2.addData('numberEntry_4.rt', numberEntry_4.rt)
        # the Routine "FullTest_01_Mult" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback_Block2"-------
        t = 0
        Feedback_Block2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.700000)
        # update component parameters for each repeat
        amount_2.setText(('$%0.2f' %(winLoss)))
        if winLoss >= 0.0:
            correct = "CORRECT"
            correctColor = "green"
        else:
            correct = "INCORRECT"
            correctColor = "red"
        Correct_wrong2.setColor(correctColor, colorSpace='rgb')
        Correct_wrong2.setText(correct)
        # keep track of which components have finished
        Feedback_Block2Components = [amount_2, text_13, text_14, Correct_wrong2]
        for thisComponent in Feedback_Block2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Feedback_Block2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Feedback_Block2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *amount_2* updates
            if t >= 0.0 and amount_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                amount_2.tStart = t
                amount_2.frameNStart = frameN  # exact frame index
                amount_2.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if amount_2.status == STARTED and t >= frameRemains:
                amount_2.setAutoDraw(False)
            
            
            # *text_13* updates
            if t >= 1.5 and text_13.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_13.tStart = t
                text_13.frameNStart = frameN  # exact frame index
                text_13.setAutoDraw(True)
            frameRemains = 1.5 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_13.status == STARTED and t >= frameRemains:
                text_13.setAutoDraw(False)
            
            # *text_14* updates
            if t >= 0.0 and text_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_14.tStart = t
                text_14.frameNStart = frameN  # exact frame index
                text_14.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_14.status == STARTED and t >= frameRemains:
                text_14.setAutoDraw(False)
            
            # *Correct_wrong2* updates
            if t >= 0.0 and Correct_wrong2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Correct_wrong2.tStart = t
                Correct_wrong2.frameNStart = frameN  # exact frame index
                Correct_wrong2.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Correct_wrong2.status == STARTED and t >= frameRemains:
                Correct_wrong2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_Block2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback_Block2"-------
        for thisComponent in Feedback_Block2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run trial blocks of 100
        if counter>=100 and loop_num == 4: # change to 100
            counter = 0
            trials_2.finished=1
            trial_blocks.finished=1
        
        elif counter>=100: #change to 100
            counter =0
            loop_num = loop_num + 1
            trials_2.finished=1
        thisExp.nextEntry()
        
    # completed 200 repeats of 'trials_2'
    
    # get names of stimulus parameters
    if trials_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_2.trialList[0].keys()
    # save data for this loop
    trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 5 repeats of 'trial_blocks'

# get names of stimulus parameters
if trial_blocks.trialList in ([], [None], None):
    params = []
else:
    params = trial_blocks.trialList[0].keys()
# save data for this loop
trial_blocks.saveAsText(filename + 'trial_blocks.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "FinalScore"-------
t = 0
FinalScoreClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

numberEntry_5 = event.BuilderKeyResponse()
square_entry_5.setOpacity(1)
square_entry_5.setPos((0, -0.4))
square_entry_5.setLineWidth(1)
square_entry_5.setOri(0)
square_entry_5.setSize((0.7, 0.3))
earnings__3.setText(('$%0.2f' %(earnings)))
test_earnings.setText("Test Earnings: ${0}".format(earnings))
# keep track of which components have finished
FinalScoreComponents = [numberEntry_5, FinalEarnings, square_entry_5, earnings__3, test_earnings, total_earnings, continue4]
for thisComponent in FinalScoreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "FinalScore"-------
while continueRoutine:
    # get current time
    t = FinalScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *numberEntry_5* updates
    if t >= 0.7 and numberEntry_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_5.tStart = t
        numberEntry_5.frameNStart = frameN  # exact frame index
        numberEntry_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if numberEntry_5.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *FinalEarnings* updates
    if t >= 0.5 and FinalEarnings.status == NOT_STARTED:
        # keep track of start time/frame for later
        FinalEarnings.tStart = t
        FinalEarnings.frameNStart = frameN  # exact frame index
        FinalEarnings.setAutoDraw(True)
    
    # *square_entry_5* updates
    if t >= 0.5 and square_entry_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_entry_5.tStart = t
        square_entry_5.frameNStart = frameN  # exact frame index
        square_entry_5.setAutoDraw(True)
    
    # *earnings__3* updates
    if t >= 0.5 and earnings__3.status == NOT_STARTED:
        # keep track of start time/frame for later
        earnings__3.tStart = t
        earnings__3.frameNStart = frameN  # exact frame index
        earnings__3.setAutoDraw(True)
    
    # *test_earnings* updates
    if t >= 0.5 and test_earnings.status == NOT_STARTED:
        # keep track of start time/frame for later
        test_earnings.tStart = t
        test_earnings.frameNStart = frameN  # exact frame index
        test_earnings.setAutoDraw(True)
    
    # *total_earnings* updates
    if t >= 0.5 and total_earnings.status == NOT_STARTED:
        # keep track of start time/frame for later
        total_earnings.tStart = t
        total_earnings.frameNStart = frameN  # exact frame index
        total_earnings.setAutoDraw(True)
    
    # *continue4* updates
    if t >= 0.5 and continue4.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4.tStart = t
        continue4.frameNStart = frameN  # exact frame index
        continue4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FinalScore"-------
for thisComponent in FinalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "FinalScore" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()










# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
