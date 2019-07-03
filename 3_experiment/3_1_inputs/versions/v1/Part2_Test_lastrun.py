#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Sun Sep 17 13:26:58 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
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
expInfo = {'participant':'', 'session':'001'}
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
    originPath=u'/Users/djw/Dropbox/PHD/CENDRI/Project/Code/LabSharedFolder/MADE01/CODE/v1/Part2_Test.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "TestInstr"
TestInstrClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='During this part of the study, you will be presented with combinations of images (e.g. one face and one house image).\n\nYour task will be to decide whether you would like to accept or reject the combined outcome of the two images.',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continue9_2 = visual.TextStim(win=win, name='continue9_2',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
Part2 = visual.TextStim(win=win, name='Part2',
    text='Part 2: Test',
    font='Arial',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "TestInstr_2"
TestInstr_2Clock = core.Clock()
faceMorph05_2 = visual.ImageStim(
    win=win, name='faceMorph05_2',units='pix', 
    image='images/morphs/faceMorph21.jpg', mask=None,
    ori=0, pos=(-250, 0), size=(300,300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
houseMorph07_2 = visual.ImageStim(
    win=win, name='houseMorph07_2',units='pix', 
    image='images/morphs/houseMorph60.jpg', mask=None,
    ori=0, pos=(250, 0), size=[300,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='In this case the combined value of the two images is: $0.58 - $0.20 = $0.38.',
    font='Helvetica',
    pos=(0, .6), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
faceValueText_2 = visual.TextStim(win=win, name='faceValueText_2',
    text='$0.58',
    font='Helvetica',
    pos=(-0.4, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
houseValue_2 = visual.TextStim(win=win, name='houseValue_2',
    text='-$0.20',
    font='Helvetica',
    pos=(0.4, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
compValues_2 = visual.TextStim(win=win, name='compValues_2',
    text='Therefore it would make sense to accept this combination.',
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

# Initialize components for Routine "Block01"
Block01Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='The test will now begin.\n\nTry to accumulate as much money as possible.\n\nA running total of your earnings will be shown on screen.\n\nThere will be 100 trials in this first segment.',
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


# Initialize components for Routine "FullTest_01"
FullTest_01Clock = core.Clock()
#earnings = -100
#newValue = 0
inputText = ""

import random

earnings = 0
earningsUpdate = 0

exp1Trial = 0

fPosX = 250
fPosY = 0

mult1 = 1
mult2 = 1

correct =0
winLoss = 0
square_entry_3 = visual.Rect(
    win=win, name='square_entry_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
Accept_Reject = visual.TextStim(win=win, name='Accept_Reject',
    text='Accept or Reject?',
    font='Helvetica',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
nextTrialTest_3 = visual.TextStim(win=win, name='nextTrialTest_3',
    text="enter 'f' for accept, and 'j' for reject",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings_ = visual.TextStim(win=win, name='earnings_',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
face_test = visual.ImageStim(
    win=win, name='face_test',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(250,0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
houses_2 = visual.ImageStim(
    win=win, name='houses_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
EarningsLabel = visual.TextStim(win=win, name='EarningsLabel',
    text='total earnings',
    font='Helvetica',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
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
correctColor = "white"
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
#earnings = -100
#newValue = 0
inputText = ""
earnings = 0
earningsUpdate = 0
square_entry_6 = visual.Rect(
    win=win, name='square_entry_6',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
multInstr = visual.TextStim(win=win, name='multInstr',
    text='You have finished the first part of the test.\n\nSo far you have earned:\n\n\n\n\n\nThere is one other aspect of this task that you should be aware of. The test will now be modified so that there will be a multiplier over the image of the face and house that modifies the value.\n\nIf the multiplier is x1, then the value is the same as normal. But if the value is x2, for example, then the value (positive or negative) has doubled.\n\nContinue for an example.',
    font='Helvetica',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
continue4_2 = visual.TextStim(win=win, name='continue4_2',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings__4 = visual.TextStim(win=win, name='earnings__4',
    text='default text',
    font='Helvetica',
    pos=(0, .37), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "Block02_b"
Block02_bClock = core.Clock()
multInstr_4 = visual.TextStim(win=win, name='multInstr_4',
    text='In this case, without the multiplier, the value of the face is $0.58 and the value of the house is -$0.92. The correct response would be to reject the combination.\n\nHowever, since there is a multiplier of x2 on the face, the value is now $0.58 x 2 = $1.16. This means the correct response would now be to accept the combination.\n\n\nThere will be 3 blocks of 100 trials.\nYou can take a short break between blocks.',
    font='Helvetica',
    pos=(0, -0.22), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continue4_5 = visual.TextStim(win=win, name='continue4_5',
    text='press any key to begin your first block of trials',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
mult_example = visual.ImageStim(
    win=win, name='mult_example',units='pix', 
    image='images/mult_example.png', mask=None,
    ori=0, pos=(0, 250), size=[500,275],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

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
#earnings = -100
#newValue = 0
from random import randint
inputText = ""

earnings = 0
earningsUpdate = 0
mult1 = 1
mult2 = 1

earnings = 0
earningsUpdate = 0

exp2Trial = 0

flip = False

flipVersion = 1
posNeg = 1
square_entry_4 = visual.Rect(
    win=win, name='square_entry_4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
Accept_Reject_2 = visual.TextStim(win=win, name='Accept_Reject_2',
    text='Do you accept or reject this combination?',
    font='Helvetica',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
nextTrialTest_4 = visual.TextStim(win=win, name='nextTrialTest_4',
    text="enter 'f' for accept, and 'j' for reject",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings__2 = visual.TextStim(win=win, name='earnings__2',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
Fixation_4 = visual.TextStim(win=win, name='Fixation_4',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
face_test_2 = visual.ImageStim(
    win=win, name='face_test_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
houses_3 = visual.ImageStim(
    win=win, name='houses_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
EarningsLabel_2 = visual.TextStim(win=win, name='EarningsLabel_2',
    text='total earnings',
    font='Helvetica',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
Mult1 = visual.TextStim(win=win, name='Mult1',
    text='default text',
    font='Helvetica',
    pos=(-.4, 0.52), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-11.0);
Mult2 = visual.TextStim(win=win, name='Mult2',
    text='default text',
    font='Helvetica',
    pos=(0.4, 0.52), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-12.0);

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

# Initialize components for Routine "Block03"
Block03Clock = core.Clock()
square_entry_7 = visual.Rect(
    win=win, name='square_entry_7',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
multInstr_2 = visual.TextStim(win=win, name='multInstr_2',
    text='You have finished the block. So far you have earned:\n\n\n\n\n\nYou now have 2 more blocks of 100 trials remaining.\n\nTake a short break and then press any key to continue.',
    font='Helvetica',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
continue4_3 = visual.TextStim(win=win, name='continue4_3',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
earnings__5 = visual.TextStim(win=win, name='earnings__5',
    text='default text',
    font='Helvetica',
    pos=(0, .30), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

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
#earnings = -100
#newValue = 0
from random import randint
inputText = ""

earnings = 0
earningsUpdate = 0
mult1 = 1
mult2 = 1

earnings = 0
earningsUpdate = 0

exp2Trial = 0

flip = False

flipVersion = 1
posNeg = 1
square_entry_4 = visual.Rect(
    win=win, name='square_entry_4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
Accept_Reject_2 = visual.TextStim(win=win, name='Accept_Reject_2',
    text='Do you accept or reject this combination?',
    font='Helvetica',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
nextTrialTest_4 = visual.TextStim(win=win, name='nextTrialTest_4',
    text="enter 'f' for accept, and 'j' for reject",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings__2 = visual.TextStim(win=win, name='earnings__2',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
Fixation_4 = visual.TextStim(win=win, name='Fixation_4',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
face_test_2 = visual.ImageStim(
    win=win, name='face_test_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
houses_3 = visual.ImageStim(
    win=win, name='houses_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
EarningsLabel_2 = visual.TextStim(win=win, name='EarningsLabel_2',
    text='total earnings',
    font='Helvetica',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
Mult1 = visual.TextStim(win=win, name='Mult1',
    text='default text',
    font='Helvetica',
    pos=(-.4, 0.52), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-11.0);
Mult2 = visual.TextStim(win=win, name='Mult2',
    text='default text',
    font='Helvetica',
    pos=(0.4, 0.52), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-12.0);

# Initialize components for Routine "Feedback_Block3"
Feedback_Block3Clock = core.Clock()
amount_3 = visual.TextStim(win=win, name='amount_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

text_15 = visual.TextStim(win=win, name='text_15',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='Trial Earnings',
    font='Helvetica',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
Correct_wrong2_2 = visual.TextStim(win=win, name='Correct_wrong2_2',
    text='default text',
    font='Helvetica',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "Block04"
Block04Clock = core.Clock()
#earnings = -100
#newValue = 0
inputText = ""
earnings = 0
earningsUpdate = 0
square_entry_8 = visual.Rect(
    win=win, name='square_entry_8',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
multInstr_3 = visual.TextStim(win=win, name='multInstr_3',
    text='You have finished the block. So far you have earned:\n\n\n\n\n\nYou now have 1 more block of 100 trials remaining.\n\nTake a short break and then press any key to continue.',
    font='Helvetica',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
continue4_4 = visual.TextStim(win=win, name='continue4_4',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings__6 = visual.TextStim(win=win, name='earnings__6',
    text='default text',
    font='Helvetica',
    pos=(0, .30), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

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
#earnings = -100
#newValue = 0
from random import randint
inputText = ""

earnings = 0
earningsUpdate = 0
mult1 = 1
mult2 = 1

earnings = 0
earningsUpdate = 0

exp2Trial = 0

flip = False

flipVersion = 1
posNeg = 1
square_entry_4 = visual.Rect(
    win=win, name='square_entry_4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
Accept_Reject_2 = visual.TextStim(win=win, name='Accept_Reject_2',
    text='Do you accept or reject this combination?',
    font='Helvetica',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
nextTrialTest_4 = visual.TextStim(win=win, name='nextTrialTest_4',
    text="enter 'f' for accept, and 'j' for reject",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings__2 = visual.TextStim(win=win, name='earnings__2',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
Fixation_4 = visual.TextStim(win=win, name='Fixation_4',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
face_test_2 = visual.ImageStim(
    win=win, name='face_test_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
houses_3 = visual.ImageStim(
    win=win, name='houses_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
EarningsLabel_2 = visual.TextStim(win=win, name='EarningsLabel_2',
    text='total earnings',
    font='Helvetica',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
Mult1 = visual.TextStim(win=win, name='Mult1',
    text='default text',
    font='Helvetica',
    pos=(-.4, 0.52), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-11.0);
Mult2 = visual.TextStim(win=win, name='Mult2',
    text='default text',
    font='Helvetica',
    pos=(0.4, 0.52), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-12.0);

# Initialize components for Routine "Feedback_Block4"
Feedback_Block4Clock = core.Clock()
amount_4 = visual.TextStim(win=win, name='amount_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

text_17 = visual.TextStim(win=win, name='text_17',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Trial Earnings',
    font='Helvetica',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
Correct_wrong2_3 = visual.TextStim(win=win, name='Correct_wrong2_3',
    text='default text',
    font='Helvetica',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "FinalScore"
FinalScoreClock = core.Clock()
#earnings = -100
#newValue = 0
inputText = ""
earnings = 0
earningsUpdate = 0
square_entry_5 = visual.Rect(
    win=win, name='square_entry_5',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
FinalEarnings = visual.TextStim(win=win, name='FinalEarnings',
    text='FINAL EARNINGS',
    font='Helvetica',
    pos=(0, 0.75), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
continue4 = visual.TextStim(win=win, name='continue4',
    text='TELL THE EXPERIMENTER YOU HAVE FINISHED',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings__3 = visual.TextStim(win=win, name='earnings__3',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TestInstr"-------
t = 0
TestInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys = event.BuilderKeyResponse()
# keep track of which components have finished
TestInstrComponents = [exitKeys, instructions, continue9_2, Part2]
for thisComponent in TestInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "TestInstr"-------
while continueRoutine:
    # get current time
    t = TestInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys* updates
    if t >= 0.5 and exitKeys.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys.tStart = t
        exitKeys.frameNStart = frameN  # exact frame index
        exitKeys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(exitKeys.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if exitKeys.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            exitKeys.keys = theseKeys[-1]  # just the last key pressed
            exitKeys.rt = exitKeys.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
    # *continue9_2* updates
    if t >= 0.5 and continue9_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9_2.tStart = t
        continue9_2.frameNStart = frameN  # exact frame index
        continue9_2.setAutoDraw(True)
    
    # *Part2* updates
    if t >= 0.0 and Part2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Part2.tStart = t
        Part2.frameNStart = frameN  # exact frame index
        Part2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TestInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TestInstr"-------
for thisComponent in TestInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if exitKeys.keys in ['', [], None]:  # No response was made
    exitKeys.keys=None
thisExp.addData('exitKeys.keys',exitKeys.keys)
if exitKeys.keys != None:  # we had a response
    thisExp.addData('exitKeys.rt', exitKeys.rt)
thisExp.nextEntry()
# the Routine "TestInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TestInstr_2"-------
t = 0
TestInstr_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_2 = event.BuilderKeyResponse()
# keep track of which components have finished
TestInstr_2Components = [exitKeys_2, faceMorph05_2, houseMorph07_2, instructions_2, faceValueText_2, houseValue_2, compValues_2, continue9_3]
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
        win.callOnFlip(exitKeys_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if exitKeys_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            exitKeys_2.keys = theseKeys[-1]  # just the last key pressed
            exitKeys_2.rt = exitKeys_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *faceMorph05_2* updates
    if t >= 0.0 and faceMorph05_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        faceMorph05_2.tStart = t
        faceMorph05_2.frameNStart = frameN  # exact frame index
        faceMorph05_2.setAutoDraw(True)
    
    # *houseMorph07_2* updates
    if t >= 0.0 and houseMorph07_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        houseMorph07_2.tStart = t
        houseMorph07_2.frameNStart = frameN  # exact frame index
        houseMorph07_2.setAutoDraw(True)
    
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
# check responses
if exitKeys_2.keys in ['', [], None]:  # No response was made
    exitKeys_2.keys=None
thisExp.addData('exitKeys_2.keys',exitKeys_2.keys)
if exitKeys_2.keys != None:  # we had a response
    thisExp.addData('exitKeys_2.rt', exitKeys_2.rt)
thisExp.nextEntry()
# the Routine "TestInstr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Block01"-------
t = 0
Block01Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Block01Components = [exitKeys_3, instructions_3, continue9_4]
for thisComponent in Block01Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block01"-------
while continueRoutine:
    # get current time
    t = Block01Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitKeys_3* updates
    if t >= 0.5 and exitKeys_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        exitKeys_3.tStart = t
        exitKeys_3.frameNStart = frameN  # exact frame index
        exitKeys_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(exitKeys_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if exitKeys_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            exitKeys_3.keys = theseKeys[-1]  # just the last key pressed
            exitKeys_3.rt = exitKeys_3.clock.getTime()
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
    for thisComponent in Block01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block01"-------
for thisComponent in Block01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if exitKeys_3.keys in ['', [], None]:  # No response was made
    exitKeys_3.keys=None
thisExp.addData('exitKeys_3.keys',exitKeys_3.keys)
if exitKeys_3.keys != None:  # we had a response
    thisExp.addData('exitKeys_3.rt', exitKeys_3.rt)
thisExp.nextEntry()
# the Routine "Block01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=20, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part1.xlsx'),
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
    
    
    # ------Prepare to start Routine "FullTest_01"-------
    t = 0
    FullTest_01Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    #theseKeys=""
    #shift_flag = False
    
    #difference between the input value and the house value
    #currently using input from last frame for current house
    
    
    #earnings = abs(long(float(newValue)) - houseValue)
    theseKeys=""
    shift_flag = False
    #inputTextValue.alignHoriz = 'center'
    
    #Count Trials
    exp1Trial +=1
    
    #Pick random value for House and Face morph
    #This means the trials are randomized WITH replacement
    randFace = random.randint(0,100)
    randHouse = random.randint(0,100)
    
    #Create filepath for image
    trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
    trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
    
    #Calculate monetary value based on morph value
    actFaceVal = 1.00 - (2*randFace/100)
    actHouseVal = 1.00 - (2*randHouse/100)
    
    
    
    numberEntry_3 = event.BuilderKeyResponse()
    square_entry_3.setOpacity(1)
    square_entry_3.setPos((0, -.75))
    square_entry_3.setLineWidth(1)
    square_entry_3.setOri(0)
    square_entry_3.setSize((0.25, 0.15))
    face_test.setImage(trialFace)
    houses_2.setImage(trialHouse)
    # keep track of which components have finished
    FullTest_01Components = [numberEntry_3, square_entry_3, Accept_Reject, nextTrialTest_3, earnings_, face_test, houses_2, EarningsLabel]
    for thisComponent in FullTest_01Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "FullTest_01"-------
    while continueRoutine:
        # get current time
        t = FullTest_01Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        n = len(theseKeys)
        i = 0
        while i < n:
            #for ACCEPTING and starting a new loop
            if theseKeys[i] == 'f':
                earningsUpdate = actFaceVal + actHouseVal
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
                earningsUpdate = actFaceVal + actHouseVal
                if (earningsUpdate) > 0:
                    correct=0
                    earnings = earnings - earningsUpdate
                    winLoss= -1*earningsUpdate #subtract incorrect rejection
                    continueRoutine = False
                else:
                    correct=1
                    winLoss = 0.00
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
        
        # *numberEntry_3* updates
        if t >= 0 and numberEntry_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry_3.tStart = t
            numberEntry_3.frameNStart = frameN  # exact frame index
            numberEntry_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numberEntry_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numberEntry_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numberEntry_3.keys.extend(theseKeys)  # storing all keys
                numberEntry_3.rt.append(numberEntry_3.clock.getTime())
        
        # *square_entry_3* updates
        if t >= 0 and square_entry_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry_3.tStart = t
            square_entry_3.frameNStart = frameN  # exact frame index
            square_entry_3.setAutoDraw(True)
        
        # *Accept_Reject* updates
        if t >= 0 and Accept_Reject.status == NOT_STARTED:
            # keep track of start time/frame for later
            Accept_Reject.tStart = t
            Accept_Reject.frameNStart = frameN  # exact frame index
            Accept_Reject.setAutoDraw(True)
        
        # *nextTrialTest_3* updates
        if t >= 0 and nextTrialTest_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest_3.tStart = t
            nextTrialTest_3.frameNStart = frameN  # exact frame index
            nextTrialTest_3.setAutoDraw(True)
        
        # *earnings_* updates
        if t >= 0 and earnings_.status == NOT_STARTED:
            # keep track of start time/frame for later
            earnings_.tStart = t
            earnings_.frameNStart = frameN  # exact frame index
            earnings_.setAutoDraw(True)
        if earnings_.status == STARTED:  # only update if drawing
            earnings_.setText(('$%0.2f' %(earnings)), log=False)
        
        # *face_test* updates
        if t >= 0 and face_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            face_test.tStart = t
            face_test.frameNStart = frameN  # exact frame index
            face_test.setAutoDraw(True)
        
        # *houses_2* updates
        if t >= 0 and houses_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            houses_2.tStart = t
            houses_2.frameNStart = frameN  # exact frame index
            houses_2.setAutoDraw(True)
        
        # *EarningsLabel* updates
        if t >= 0 and EarningsLabel.status == NOT_STARTED:
            # keep track of start time/frame for later
            EarningsLabel.tStart = t
            EarningsLabel.frameNStart = frameN  # exact frame index
            EarningsLabel.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FullTest_01Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FullTest_01"-------
    for thisComponent in FullTest_01Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #let's store the final text string into the results final...
    thisExp.addData('Trial', exp1Trial) 
    thisExp.addData('correct', correct) 
    thisExp.addData('faceVal', actFaceVal)
    thisExp.addData('houseVal', actHouseVal) 
    thisExp.addData('mult1House', mult1)
    thisExp.addData('mult2Face', mult2)
    thisExp.addData('summedVal', earningsUpdate) 
    thisExp.addData('earnings', earnings)
    
    inputText=""
    
    #This is done with the next routine
    #if exp1Trial>=100:
    #    test.finished=1
    # check responses
    if numberEntry_3.keys in ['', [], None]:  # No response was made
        numberEntry_3.keys=None
    test.addData('numberEntry_3.keys',numberEntry_3.keys)
    if numberEntry_3.keys != None:  # we had a response
        test.addData('numberEntry_3.rt', numberEntry_3.rt)
    # the Routine "FullTest_01" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Test1_WinLoss"-------
    t = 0
    Test1_WinLossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    amount.setText(('$%0.2f' %(winLoss)))
    
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
        if winLoss >= 0.0:
            correct = "CORRECT"
            correctColor = "green"
        else:
            correct = "INCORRECT"
            correctColor = "red"
        
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
        if correct_wrong.status == STARTED:  # only update if drawing
            correct_wrong.setColor(correctColor, colorSpace='rgb', log=False)
            correct_wrong.setText(correct, log=False)
        
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
    if exp1Trial>=5:  #change to 100
        test.finished=1
    thisExp.nextEntry()
    
# completed 20 repeats of 'test'


# ------Prepare to start Routine "Block02_a"-------
t = 0
Block02_aClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
#theseKeys=""
#shift_flag = False

#difference between the input value and the house value
#currently using input from last frame for current house


#earnings = abs(long(float(newValue)) - houseValue)
theseKeys=""
shift_flag = False
#inputTextValue.alignHoriz = 'center'
numberEntry_6 = event.BuilderKeyResponse()
square_entry_6.setOpacity(1)
square_entry_6.setPos((0, .37))
square_entry_6.setLineWidth(1)
square_entry_6.setOri(0)
square_entry_6.setSize((0.25, 0.15))
# keep track of which components have finished
Block02_aComponents = [numberEntry_6, square_entry_6, multInstr, continue4_2, earnings__4]
for thisComponent in Block02_aComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block02_a"-------
while continueRoutine:
    # get current time
    t = Block02_aClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    n = len(theseKeys)
    i = 0
    while i < n:
        #for ACCEPTING and starting a new loop
        if theseKeys[i] == 'f':
            earningsUpdate = houseValue + faceValue
            earnings = earnings + earningsUpdate
            continueRoutine = False
            break
        
        #for REJECTING and starting a new loop
        elif theseKeys[i] == 'j':
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
    
    # *numberEntry_6* updates
    if t >= 0.7 and numberEntry_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_6.tStart = t
        numberEntry_6.frameNStart = frameN  # exact frame index
        numberEntry_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(numberEntry_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if numberEntry_6.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            numberEntry_6.keys.extend(theseKeys)  # storing all keys
            numberEntry_6.rt.append(numberEntry_6.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *square_entry_6* updates
    if t >= 0.5 and square_entry_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_entry_6.tStart = t
        square_entry_6.frameNStart = frameN  # exact frame index
        square_entry_6.setAutoDraw(True)
    
    # *multInstr* updates
    if t >= 0.5 and multInstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        multInstr.tStart = t
        multInstr.frameNStart = frameN  # exact frame index
        multInstr.setAutoDraw(True)
    
    # *continue4_2* updates
    if t >= 0.5 and continue4_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4_2.tStart = t
        continue4_2.frameNStart = frameN  # exact frame index
        continue4_2.setAutoDraw(True)
    
    # *earnings__4* updates
    if t >= 0.5 and earnings__4.status == NOT_STARTED:
        # keep track of start time/frame for later
        earnings__4.tStart = t
        earnings__4.frameNStart = frameN  # exact frame index
        earnings__4.setAutoDraw(True)
    if earnings__4.status == STARTED:  # only update if drawing
        earnings__4.setText(('$%0.2f' %(earnings)), log=False)
    
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

#let's store the final text string into the results final...
thisExp.addData('earnings', earnings)
inputText=""

# check responses
if numberEntry_6.keys in ['', [], None]:  # No response was made
    numberEntry_6.keys=None
thisExp.addData('numberEntry_6.keys',numberEntry_6.keys)
if numberEntry_6.keys != None:  # we had a response
    thisExp.addData('numberEntry_6.rt', numberEntry_6.rt)
thisExp.nextEntry()
# the Routine "Block02_a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Block02_b"-------
t = 0
Block02_bClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
numberEntry_9 = event.BuilderKeyResponse()
# keep track of which components have finished
Block02_bComponents = [numberEntry_9, multInstr_4, continue4_5, mult_example]
for thisComponent in Block02_bComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block02_b"-------
while continueRoutine:
    # get current time
    t = Block02_bClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *numberEntry_9* updates
    if t >= 0.7 and numberEntry_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_9.tStart = t
        numberEntry_9.frameNStart = frameN  # exact frame index
        numberEntry_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(numberEntry_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if numberEntry_9.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            numberEntry_9.keys.extend(theseKeys)  # storing all keys
            numberEntry_9.rt.append(numberEntry_9.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *multInstr_4* updates
    if t >= 0.5 and multInstr_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        multInstr_4.tStart = t
        multInstr_4.frameNStart = frameN  # exact frame index
        multInstr_4.setAutoDraw(True)
    
    # *continue4_5* updates
    if t >= 0.5 and continue4_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4_5.tStart = t
        continue4_5.frameNStart = frameN  # exact frame index
        continue4_5.setAutoDraw(True)
    
    # *mult_example* updates
    if t >= 0.5 and mult_example.status == NOT_STARTED:
        # keep track of start time/frame for later
        mult_example.tStart = t
        mult_example.frameNStart = frameN  # exact frame index
        mult_example.setAutoDraw(True)
    
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
# check responses
if numberEntry_9.keys in ['', [], None]:  # No response was made
    numberEntry_9.keys=None
thisExp.addData('numberEntry_9.keys',numberEntry_9.keys)
if numberEntry_9.keys != None:  # we had a response
    thisExp.addData('numberEntry_9.rt', numberEntry_9.rt)
thisExp.nextEntry()
# the Routine "Block02_b" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part1.xlsx'),
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
    #theseKeys=""
    #shift_flag = False
    
    #difference between the input value and the house value
    #currently using input from last frame for current house
    
    
    #earnings = abs(long(float(newValue)) - houseValue)
    theseKeys=""
    shift_flag = False
    #inputTextValue.alignHoriz = 'center'
    
    #Count Trials
    exp2Trial +=1
    
    #flipChoice OFF
    flip = False
    
    #Pick random value for House and Face morph
    #This means the trials are randomized WITH replacement
    randFace = random.randint(0,100)
    randHouse = random.randint(0,100)
    
    #Create filepath for image
    trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
    trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
    
    #Calculate monetary value based on morph value
    actFaceVal = 1.00 - (2*randFace/100)
    actHouseVal = 1.00 - (2*randHouse/100)
    
    #Set Flip Trials
    flipChoice = randint(1,3) 
    
    if flipChoice == 1:
        flipVersion = randint(1,6) 
        posNeg = randint(1,2)
        flip = True
    
    
        if flipVersion == 1:  # 1/2
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(10,40) #values from .20 to .80
                randHouse = 110-randFace #values opposite in sign and 0.20 higher
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,90) #values from -0.20 to -0.80
                randHouse = 90-randFace #values opposite in sign and 0.20 higher
    
            #Multiplier assignment
            mult1 = str(1)
            mult2 = str(2)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 2: # 2/1
    
            if posNeg == 1: #FACE positive, house negative
                randHouse = randint(10,40) #values from .20 to .80
                randFace = 110-randHouse #values opposite in sign and 0.20 higher
    
            if posNeg == 2: #FACE negative, house positive
                randHouse = randint(60,90) #values from -0.20 to -0.80
                randFace = 90-randHouse #values opposite in sign and 0.20 higher
    
            #Multiplier assignment
            mult1 = str(2)
            mult2 = str(1)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 3: # 1/3
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(30,40) #values from .20 to .40
                randHouse = 152-randFace*2 #values opposite in sign and double
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,70) #values from -0.20 to -0.40
                randHouse = 152-randFace*2 #values opposite in sign and double
    
            #Multiplier assignment
            mult1 = str(1)
            mult2 = str(3)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 4: # 3/1
    
            if posNeg == 1: #FACE positive, house negative
                randHouse = randint(30,40) #values from .20 to .40
                randFace = 152-randHouse*2 #values opposite in sign and double
    
            if posNeg == 2: #FACE negative, house positive
                randHouse = randint(60,70) #values from -0.20 to -0.40
                randFace = 152-randHouse*2 #values opposite in sign and double
    
            #Multiplier assignment
            mult1 = str(3)
            mult2 = str(1)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 5: #2/3 (face becomes larger value)
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(10,40) #
                randHouse = 105-randFace # Values end up being almost equal...
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,90) #values from -0.20 to -0.40
                randHouse = 95-randFace #values opposite in sign and higher
    
            #Multiplier assignment
            mult1 = str(2)
            mult2 = str(3)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 6: #3/2
    
            if posNeg == 1: #face positive, HOUSE negative
                randHouse = randint(10,40) #
                randFace = 105-randHouse # Values end up being almost equal...
    
            if posNeg == 2: #face negative, HOUSE positive
                randHouse = randint(60,90) #values from -0.20 to -0.40
                randFace = 95-randHouse #values opposite in sign and higher
    
            #Multiplier assignment
            mult1 = str(3)
            mult2 = str(2)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
    if flipChoice > 1:
        flip = False
    
        #Set value of first multiplier
        #House Mult
        mult1 = randint(2,8) #2/7 chance of multiplier
        if mult1 < 4:
            mult1 = str(mult1)
        else:
            mult1 = str(1)
    
        #Set value of second multiplier
        #Face Mult
        mult2 = randint(2,8) #2/7 chance of multiplier (therefore chance of no mult = 5/7 * 5/7 = 25/49)
        if mult2 < 4:
            mult2 = str(mult2)
        else:
            mult2 = str(1)
        
    
    numberEntry_4 = event.BuilderKeyResponse()
    square_entry_4.setOpacity(1)
    square_entry_4.setPos((0, -.75))
    square_entry_4.setLineWidth(1)
    square_entry_4.setOri(0)
    square_entry_4.setSize((0.25, 0.15))
    face_test_2.setImage(trialFace)
    houses_3.setImage(trialHouse)
    Mult1.setText(('x' + mult1))
    Mult2.setText(('x' + mult2))
    # keep track of which components have finished
    FullTest_01_MultComponents = [numberEntry_4, square_entry_4, Accept_Reject_2, nextTrialTest_4, earnings__2, Fixation_4, face_test_2, houses_3, EarningsLabel_2, Mult1, Mult2]
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
        while i < n:
            #for ACCEPTING and starting a new loop
            if theseKeys[i] == 'f':
                earningsUpdate = actHouseVal*long(mult1) + actFaceVal*long(mult2)
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
                earningsUpdate = actHouseVal*long(mult1) + actFaceVal*long(mult2)
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
        if t >= 0.7 and numberEntry_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry_4.tStart = t
            numberEntry_4.frameNStart = frameN  # exact frame index
            numberEntry_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numberEntry_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numberEntry_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numberEntry_4.keys.extend(theseKeys)  # storing all keys
                numberEntry_4.rt.append(numberEntry_4.clock.getTime())
        
        # *square_entry_4* updates
        if t >= 0.5 and square_entry_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry_4.tStart = t
            square_entry_4.frameNStart = frameN  # exact frame index
            square_entry_4.setAutoDraw(True)
        
        # *Accept_Reject_2* updates
        if t >= 0.5 and Accept_Reject_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Accept_Reject_2.tStart = t
            Accept_Reject_2.frameNStart = frameN  # exact frame index
            Accept_Reject_2.setAutoDraw(True)
        
        # *nextTrialTest_4* updates
        if t >= 0.5 and nextTrialTest_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest_4.tStart = t
            nextTrialTest_4.frameNStart = frameN  # exact frame index
            nextTrialTest_4.setAutoDraw(True)
        
        # *earnings__2* updates
        if t >= 0.5 and earnings__2.status == NOT_STARTED:
            # keep track of start time/frame for later
            earnings__2.tStart = t
            earnings__2.frameNStart = frameN  # exact frame index
            earnings__2.setAutoDraw(True)
        if earnings__2.status == STARTED:  # only update if drawing
            earnings__2.setText(('$%0.2f' %(earnings)), log=False)
        
        # *Fixation_4* updates
        if t >= 0.0 and Fixation_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_4.tStart = t
            Fixation_4.frameNStart = frameN  # exact frame index
            Fixation_4.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation_4.status == STARTED and t >= frameRemains:
            Fixation_4.setAutoDraw(False)
        
        # *face_test_2* updates
        if t >= 0.5 and face_test_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            face_test_2.tStart = t
            face_test_2.frameNStart = frameN  # exact frame index
            face_test_2.setAutoDraw(True)
        
        # *houses_3* updates
        if t >= 0.5 and houses_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            houses_3.tStart = t
            houses_3.frameNStart = frameN  # exact frame index
            houses_3.setAutoDraw(True)
        
        # *EarningsLabel_2* updates
        if t >= 0.5 and EarningsLabel_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            EarningsLabel_2.tStart = t
            EarningsLabel_2.frameNStart = frameN  # exact frame index
            EarningsLabel_2.setAutoDraw(True)
        
        # *Mult1* updates
        if t >= 0.5 and Mult1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Mult1.tStart = t
            Mult1.frameNStart = frameN  # exact frame index
            Mult1.setAutoDraw(True)
        
        # *Mult2* updates
        if t >= 0.5 and Mult2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Mult2.tStart = t
            Mult2.frameNStart = frameN  # exact frame index
            Mult2.setAutoDraw(True)
        
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
    thisExp.addData('Trial', exp2Trial)
    thisExp.addData('correct', correct) 
    thisExp.addData('faceVal', actFaceVal)
    thisExp.addData('houseVal', actHouseVal)
    thisExp.addData('mult1House', mult1)
    thisExp.addData('mult2Face', mult2)
    thisExp.addData('summedVal', earningsUpdate)
    thisExp.addData('earnings', earnings)
    thisExp.addData('flip', flipChoice)
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
        if winLoss >= 0.0:
            correct = "CORRECT"
            correctColor = "green"
        else:
            correct = "INCORRECT"
            correctColor = "red"
        
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
        if Correct_wrong2.status == STARTED:  # only update if drawing
            Correct_wrong2.setColor(correctColor, colorSpace='rgb', log=False)
            Correct_wrong2.setText(correct, log=False)
        
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
    if exp2Trial>=100: #change to 100
        exp2Trial =0
        trials_2.finished=1
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_2'


# ------Prepare to start Routine "Block03"-------
t = 0
Block03Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
numberEntry_7 = event.BuilderKeyResponse()
square_entry_7.setOpacity(1)
square_entry_7.setPos((0, .30))
square_entry_7.setLineWidth(1)
square_entry_7.setOri(0)
square_entry_7.setSize((0.25, 0.15))
# keep track of which components have finished
Block03Components = [numberEntry_7, square_entry_7, multInstr_2, continue4_3, earnings__5]
for thisComponent in Block03Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block03"-------
while continueRoutine:
    # get current time
    t = Block03Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *numberEntry_7* updates
    if t >= 0.7 and numberEntry_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_7.tStart = t
        numberEntry_7.frameNStart = frameN  # exact frame index
        numberEntry_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(numberEntry_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if numberEntry_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            numberEntry_7.keys.extend(theseKeys)  # storing all keys
            numberEntry_7.rt.append(numberEntry_7.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *square_entry_7* updates
    if t >= 0.5 and square_entry_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_entry_7.tStart = t
        square_entry_7.frameNStart = frameN  # exact frame index
        square_entry_7.setAutoDraw(True)
    
    # *multInstr_2* updates
    if t >= 0.5 and multInstr_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        multInstr_2.tStart = t
        multInstr_2.frameNStart = frameN  # exact frame index
        multInstr_2.setAutoDraw(True)
    
    # *continue4_3* updates
    if t >= 0.5 and continue4_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4_3.tStart = t
        continue4_3.frameNStart = frameN  # exact frame index
        continue4_3.setAutoDraw(True)
    
    # *earnings__5* updates
    if t >= 0.5 and earnings__5.status == NOT_STARTED:
        # keep track of start time/frame for later
        earnings__5.tStart = t
        earnings__5.frameNStart = frameN  # exact frame index
        earnings__5.setAutoDraw(True)
    if earnings__5.status == STARTED:  # only update if drawing
        earnings__5.setText(('$%0.2f' %(earnings)), log=False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block03Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block03"-------
for thisComponent in Block03Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if numberEntry_7.keys in ['', [], None]:  # No response was made
    numberEntry_7.keys=None
thisExp.addData('numberEntry_7.keys',numberEntry_7.keys)
if numberEntry_7.keys != None:  # we had a response
    thisExp.addData('numberEntry_7.rt', numberEntry_7.rt)
thisExp.nextEntry()
# the Routine "Block03" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
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
    #theseKeys=""
    #shift_flag = False
    
    #difference between the input value and the house value
    #currently using input from last frame for current house
    
    
    #earnings = abs(long(float(newValue)) - houseValue)
    theseKeys=""
    shift_flag = False
    #inputTextValue.alignHoriz = 'center'
    
    #Count Trials
    exp2Trial +=1
    
    #flipChoice OFF
    flip = False
    
    #Pick random value for House and Face morph
    #This means the trials are randomized WITH replacement
    randFace = random.randint(0,100)
    randHouse = random.randint(0,100)
    
    #Create filepath for image
    trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
    trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
    
    #Calculate monetary value based on morph value
    actFaceVal = 1.00 - (2*randFace/100)
    actHouseVal = 1.00 - (2*randHouse/100)
    
    #Set Flip Trials
    flipChoice = randint(1,3) 
    
    if flipChoice == 1:
        flipVersion = randint(1,6) 
        posNeg = randint(1,2)
        flip = True
    
    
        if flipVersion == 1:  # 1/2
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(10,40) #values from .20 to .80
                randHouse = 110-randFace #values opposite in sign and 0.20 higher
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,90) #values from -0.20 to -0.80
                randHouse = 90-randFace #values opposite in sign and 0.20 higher
    
            #Multiplier assignment
            mult1 = str(1)
            mult2 = str(2)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 2: # 2/1
    
            if posNeg == 1: #FACE positive, house negative
                randHouse = randint(10,40) #values from .20 to .80
                randFace = 110-randHouse #values opposite in sign and 0.20 higher
    
            if posNeg == 2: #FACE negative, house positive
                randHouse = randint(60,90) #values from -0.20 to -0.80
                randFace = 90-randHouse #values opposite in sign and 0.20 higher
    
            #Multiplier assignment
            mult1 = str(2)
            mult2 = str(1)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 3: # 1/3
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(30,40) #values from .20 to .40
                randHouse = 152-randFace*2 #values opposite in sign and double
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,70) #values from -0.20 to -0.40
                randHouse = 152-randFace*2 #values opposite in sign and double
    
            #Multiplier assignment
            mult1 = str(1)
            mult2 = str(3)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 4: # 3/1
    
            if posNeg == 1: #FACE positive, house negative
                randHouse = randint(30,40) #values from .20 to .40
                randFace = 152-randHouse*2 #values opposite in sign and double
    
            if posNeg == 2: #FACE negative, house positive
                randHouse = randint(60,70) #values from -0.20 to -0.40
                randFace = 152-randHouse*2 #values opposite in sign and double
    
            #Multiplier assignment
            mult1 = str(3)
            mult2 = str(1)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 5: #2/3 (face becomes larger value)
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(10,40) #
                randHouse = 105-randFace # Values end up being almost equal...
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,90) #values from -0.20 to -0.40
                randHouse = 95-randFace #values opposite in sign and higher
    
            #Multiplier assignment
            mult1 = str(2)
            mult2 = str(3)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 6: #3/2
    
            if posNeg == 1: #face positive, HOUSE negative
                randHouse = randint(10,40) #
                randFace = 105-randHouse # Values end up being almost equal...
    
            if posNeg == 2: #face negative, HOUSE positive
                randHouse = randint(60,90) #values from -0.20 to -0.40
                randFace = 95-randHouse #values opposite in sign and higher
    
            #Multiplier assignment
            mult1 = str(3)
            mult2 = str(2)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
    if flipChoice > 1:
        flip = False
    
        #Set value of first multiplier
        #House Mult
        mult1 = randint(2,8) #2/7 chance of multiplier
        if mult1 < 4:
            mult1 = str(mult1)
        else:
            mult1 = str(1)
    
        #Set value of second multiplier
        #Face Mult
        mult2 = randint(2,8) #2/7 chance of multiplier (therefore chance of no mult = 5/7 * 5/7 = 25/49)
        if mult2 < 4:
            mult2 = str(mult2)
        else:
            mult2 = str(1)
        
    
    numberEntry_4 = event.BuilderKeyResponse()
    square_entry_4.setOpacity(1)
    square_entry_4.setPos((0, -.75))
    square_entry_4.setLineWidth(1)
    square_entry_4.setOri(0)
    square_entry_4.setSize((0.25, 0.15))
    face_test_2.setImage(trialFace)
    houses_3.setImage(trialHouse)
    Mult1.setText(('x' + mult1))
    Mult2.setText(('x' + mult2))
    # keep track of which components have finished
    FullTest_01_MultComponents = [numberEntry_4, square_entry_4, Accept_Reject_2, nextTrialTest_4, earnings__2, Fixation_4, face_test_2, houses_3, EarningsLabel_2, Mult1, Mult2]
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
        while i < n:
            #for ACCEPTING and starting a new loop
            if theseKeys[i] == 'f':
                earningsUpdate = actHouseVal*long(mult1) + actFaceVal*long(mult2)
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
                earningsUpdate = actHouseVal*long(mult1) + actFaceVal*long(mult2)
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
        if t >= 0.7 and numberEntry_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry_4.tStart = t
            numberEntry_4.frameNStart = frameN  # exact frame index
            numberEntry_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numberEntry_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numberEntry_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numberEntry_4.keys.extend(theseKeys)  # storing all keys
                numberEntry_4.rt.append(numberEntry_4.clock.getTime())
        
        # *square_entry_4* updates
        if t >= 0.5 and square_entry_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry_4.tStart = t
            square_entry_4.frameNStart = frameN  # exact frame index
            square_entry_4.setAutoDraw(True)
        
        # *Accept_Reject_2* updates
        if t >= 0.5 and Accept_Reject_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Accept_Reject_2.tStart = t
            Accept_Reject_2.frameNStart = frameN  # exact frame index
            Accept_Reject_2.setAutoDraw(True)
        
        # *nextTrialTest_4* updates
        if t >= 0.5 and nextTrialTest_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest_4.tStart = t
            nextTrialTest_4.frameNStart = frameN  # exact frame index
            nextTrialTest_4.setAutoDraw(True)
        
        # *earnings__2* updates
        if t >= 0.5 and earnings__2.status == NOT_STARTED:
            # keep track of start time/frame for later
            earnings__2.tStart = t
            earnings__2.frameNStart = frameN  # exact frame index
            earnings__2.setAutoDraw(True)
        if earnings__2.status == STARTED:  # only update if drawing
            earnings__2.setText(('$%0.2f' %(earnings)), log=False)
        
        # *Fixation_4* updates
        if t >= 0.0 and Fixation_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_4.tStart = t
            Fixation_4.frameNStart = frameN  # exact frame index
            Fixation_4.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation_4.status == STARTED and t >= frameRemains:
            Fixation_4.setAutoDraw(False)
        
        # *face_test_2* updates
        if t >= 0.5 and face_test_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            face_test_2.tStart = t
            face_test_2.frameNStart = frameN  # exact frame index
            face_test_2.setAutoDraw(True)
        
        # *houses_3* updates
        if t >= 0.5 and houses_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            houses_3.tStart = t
            houses_3.frameNStart = frameN  # exact frame index
            houses_3.setAutoDraw(True)
        
        # *EarningsLabel_2* updates
        if t >= 0.5 and EarningsLabel_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            EarningsLabel_2.tStart = t
            EarningsLabel_2.frameNStart = frameN  # exact frame index
            EarningsLabel_2.setAutoDraw(True)
        
        # *Mult1* updates
        if t >= 0.5 and Mult1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Mult1.tStart = t
            Mult1.frameNStart = frameN  # exact frame index
            Mult1.setAutoDraw(True)
        
        # *Mult2* updates
        if t >= 0.5 and Mult2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Mult2.tStart = t
            Mult2.frameNStart = frameN  # exact frame index
            Mult2.setAutoDraw(True)
        
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
    thisExp.addData('Trial', exp2Trial)
    thisExp.addData('correct', correct) 
    thisExp.addData('faceVal', actFaceVal)
    thisExp.addData('houseVal', actHouseVal)
    thisExp.addData('mult1House', mult1)
    thisExp.addData('mult2Face', mult2)
    thisExp.addData('summedVal', earningsUpdate)
    thisExp.addData('earnings', earnings)
    thisExp.addData('flip', flipChoice)
    inputText=""
    
    #done with the next routine
    #if exp2Trial>=200:
    #    trials_2.finished=1
    # check responses
    if numberEntry_4.keys in ['', [], None]:  # No response was made
        numberEntry_4.keys=None
    trials.addData('numberEntry_4.keys',numberEntry_4.keys)
    if numberEntry_4.keys != None:  # we had a response
        trials.addData('numberEntry_4.rt', numberEntry_4.rt)
    # the Routine "FullTest_01_Mult" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback_Block3"-------
    t = 0
    Feedback_Block3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    amount_3.setText(('$%0.2f' %(winLoss)))
    
    # keep track of which components have finished
    Feedback_Block3Components = [amount_3, text_15, text_16, Correct_wrong2_2]
    for thisComponent in Feedback_Block3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback_Block3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback_Block3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *amount_3* updates
        if t >= 0.0 and amount_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            amount_3.tStart = t
            amount_3.frameNStart = frameN  # exact frame index
            amount_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if amount_3.status == STARTED and t >= frameRemains:
            amount_3.setAutoDraw(False)
        if winLoss >= 0.0:
            correct = "CORRECT"
            correctColor = "green"
        else:
            correct = "INCORRECT"
            correctColor = "red"
        
        # *text_15* updates
        if t >= 1.5 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        frameRemains = 1.5 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_15.status == STARTED and t >= frameRemains:
            text_15.setAutoDraw(False)
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_16.status == STARTED and t >= frameRemains:
            text_16.setAutoDraw(False)
        
        # *Correct_wrong2_2* updates
        if t >= 0.0 and Correct_wrong2_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Correct_wrong2_2.tStart = t
            Correct_wrong2_2.frameNStart = frameN  # exact frame index
            Correct_wrong2_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Correct_wrong2_2.status == STARTED and t >= frameRemains:
            Correct_wrong2_2.setAutoDraw(False)
        if Correct_wrong2_2.status == STARTED:  # only update if drawing
            Correct_wrong2_2.setColor(correctColor, colorSpace='rgb', log=False)
            Correct_wrong2_2.setText(correct, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback_Block3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback_Block3"-------
    for thisComponent in Feedback_Block3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if exp2Trial>=100: #change to 100
        exp2Trial = 0
        trials.finished=1
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials'


# ------Prepare to start Routine "Block04"-------
t = 0
Block04Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
#theseKeys=""
#shift_flag = False

#difference between the input value and the house value
#currently using input from last frame for current house


#earnings = abs(long(float(newValue)) - houseValue)
theseKeys=""
shift_flag = False
#inputTextValue.alignHoriz = 'center'
numberEntry_8 = event.BuilderKeyResponse()
square_entry_8.setOpacity(1)
square_entry_8.setPos((0, .30))
square_entry_8.setLineWidth(1)
square_entry_8.setOri(0)
square_entry_8.setSize((0.25, 0.15))
# keep track of which components have finished
Block04Components = [numberEntry_8, square_entry_8, multInstr_3, continue4_4, earnings__6]
for thisComponent in Block04Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block04"-------
while continueRoutine:
    # get current time
    t = Block04Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    n = len(theseKeys)
    i = 0
    while i < n:
        #for ACCEPTING and starting a new loop
        if theseKeys[i] == 'f':
            earningsUpdate = houseValue + faceValue
            earnings = earnings + earningsUpdate
            continueRoutine = False
            break
        
        #for REJECTING and starting a new loop
        elif theseKeys[i] == 'j':
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
    
    # *numberEntry_8* updates
    if t >= 0.7 and numberEntry_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_8.tStart = t
        numberEntry_8.frameNStart = frameN  # exact frame index
        numberEntry_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(numberEntry_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if numberEntry_8.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            numberEntry_8.keys.extend(theseKeys)  # storing all keys
            numberEntry_8.rt.append(numberEntry_8.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *square_entry_8* updates
    if t >= 0.5 and square_entry_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_entry_8.tStart = t
        square_entry_8.frameNStart = frameN  # exact frame index
        square_entry_8.setAutoDraw(True)
    
    # *multInstr_3* updates
    if t >= 0.5 and multInstr_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        multInstr_3.tStart = t
        multInstr_3.frameNStart = frameN  # exact frame index
        multInstr_3.setAutoDraw(True)
    
    # *continue4_4* updates
    if t >= 0.5 and continue4_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4_4.tStart = t
        continue4_4.frameNStart = frameN  # exact frame index
        continue4_4.setAutoDraw(True)
    
    # *earnings__6* updates
    if t >= 0.5 and earnings__6.status == NOT_STARTED:
        # keep track of start time/frame for later
        earnings__6.tStart = t
        earnings__6.frameNStart = frameN  # exact frame index
        earnings__6.setAutoDraw(True)
    if earnings__6.status == STARTED:  # only update if drawing
        earnings__6.setText(('$%0.2f' %(earnings)), log=False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block04Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block04"-------
for thisComponent in Block04Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#let's store the final text string into the results final...
thisExp.addData('earnings', earnings)
inputText=""

# check responses
if numberEntry_8.keys in ['', [], None]:  # No response was made
    numberEntry_8.keys=None
thisExp.addData('numberEntry_8.keys',numberEntry_8.keys)
if numberEntry_8.keys != None:  # we had a response
    thisExp.addData('numberEntry_8.rt', numberEntry_8.rt)
thisExp.nextEntry()
# the Routine "Block04" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=50, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part1.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
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
    #theseKeys=""
    #shift_flag = False
    
    #difference between the input value and the house value
    #currently using input from last frame for current house
    
    
    #earnings = abs(long(float(newValue)) - houseValue)
    theseKeys=""
    shift_flag = False
    #inputTextValue.alignHoriz = 'center'
    
    #Count Trials
    exp2Trial +=1
    
    #flipChoice OFF
    flip = False
    
    #Pick random value for House and Face morph
    #This means the trials are randomized WITH replacement
    randFace = random.randint(0,100)
    randHouse = random.randint(0,100)
    
    #Create filepath for image
    trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
    trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
    
    #Calculate monetary value based on morph value
    actFaceVal = 1.00 - (2*randFace/100)
    actHouseVal = 1.00 - (2*randHouse/100)
    
    #Set Flip Trials
    flipChoice = randint(1,3) 
    
    if flipChoice == 1:
        flipVersion = randint(1,6) 
        posNeg = randint(1,2)
        flip = True
    
    
        if flipVersion == 1:  # 1/2
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(10,40) #values from .20 to .80
                randHouse = 110-randFace #values opposite in sign and 0.20 higher
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,90) #values from -0.20 to -0.80
                randHouse = 90-randFace #values opposite in sign and 0.20 higher
    
            #Multiplier assignment
            mult1 = str(1)
            mult2 = str(2)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 2: # 2/1
    
            if posNeg == 1: #FACE positive, house negative
                randHouse = randint(10,40) #values from .20 to .80
                randFace = 110-randHouse #values opposite in sign and 0.20 higher
    
            if posNeg == 2: #FACE negative, house positive
                randHouse = randint(60,90) #values from -0.20 to -0.80
                randFace = 90-randHouse #values opposite in sign and 0.20 higher
    
            #Multiplier assignment
            mult1 = str(2)
            mult2 = str(1)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 3: # 1/3
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(30,40) #values from .20 to .40
                randHouse = 152-randFace*2 #values opposite in sign and double
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,70) #values from -0.20 to -0.40
                randHouse = 152-randFace*2 #values opposite in sign and double
    
            #Multiplier assignment
            mult1 = str(1)
            mult2 = str(3)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 4: # 3/1
    
            if posNeg == 1: #FACE positive, house negative
                randHouse = randint(30,40) #values from .20 to .40
                randFace = 152-randHouse*2 #values opposite in sign and double
    
            if posNeg == 2: #FACE negative, house positive
                randHouse = randint(60,70) #values from -0.20 to -0.40
                randFace = 152-randHouse*2 #values opposite in sign and double
    
            #Multiplier assignment
            mult1 = str(3)
            mult2 = str(1)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 5: #2/3 (face becomes larger value)
    
            if posNeg == 1: #face positive, HOUSE negative
                randFace = randint(10,40) #
                randHouse = 105-randFace # Values end up being almost equal...
    
            if posNeg == 2: #face negative, HOUSE positive
                randFace = randint(60,90) #values from -0.20 to -0.40
                randHouse = 95-randFace #values opposite in sign and higher
    
            #Multiplier assignment
            mult1 = str(2)
            mult2 = str(3)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
        if flipVersion == 6: #3/2
    
            if posNeg == 1: #face positive, HOUSE negative
                randHouse = randint(10,40) #
                randFace = 105-randHouse # Values end up being almost equal...
    
            if posNeg == 2: #face negative, HOUSE positive
                randHouse = randint(60,90) #values from -0.20 to -0.40
                randFace = 95-randHouse #values opposite in sign and higher
    
            #Multiplier assignment
            mult1 = str(3)
            mult2 = str(2)
            #Create filepath for image
            trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
            trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
            #Calculate monetary value based on morph value
            actFaceVal = 1.00 - (2*randFace/100)
            actHouseVal = 1.00 - (2*randHouse/100)
    
    
    if flipChoice > 1:
        flip = False
    
        #Set value of first multiplier
        #House Mult
        mult1 = randint(2,8) #2/7 chance of multiplier
        if mult1 < 4:
            mult1 = str(mult1)
        else:
            mult1 = str(1)
    
        #Set value of second multiplier
        #Face Mult
        mult2 = randint(2,8) #2/7 chance of multiplier (therefore chance of no mult = 5/7 * 5/7 = 25/49)
        if mult2 < 4:
            mult2 = str(mult2)
        else:
            mult2 = str(1)
        
    
    numberEntry_4 = event.BuilderKeyResponse()
    square_entry_4.setOpacity(1)
    square_entry_4.setPos((0, -.75))
    square_entry_4.setLineWidth(1)
    square_entry_4.setOri(0)
    square_entry_4.setSize((0.25, 0.15))
    face_test_2.setImage(trialFace)
    houses_3.setImage(trialHouse)
    Mult1.setText(('x' + mult1))
    Mult2.setText(('x' + mult2))
    # keep track of which components have finished
    FullTest_01_MultComponents = [numberEntry_4, square_entry_4, Accept_Reject_2, nextTrialTest_4, earnings__2, Fixation_4, face_test_2, houses_3, EarningsLabel_2, Mult1, Mult2]
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
        while i < n:
            #for ACCEPTING and starting a new loop
            if theseKeys[i] == 'f':
                earningsUpdate = actHouseVal*long(mult1) + actFaceVal*long(mult2)
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
                earningsUpdate = actHouseVal*long(mult1) + actFaceVal*long(mult2)
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
        if t >= 0.7 and numberEntry_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry_4.tStart = t
            numberEntry_4.frameNStart = frameN  # exact frame index
            numberEntry_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numberEntry_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numberEntry_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numberEntry_4.keys.extend(theseKeys)  # storing all keys
                numberEntry_4.rt.append(numberEntry_4.clock.getTime())
        
        # *square_entry_4* updates
        if t >= 0.5 and square_entry_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry_4.tStart = t
            square_entry_4.frameNStart = frameN  # exact frame index
            square_entry_4.setAutoDraw(True)
        
        # *Accept_Reject_2* updates
        if t >= 0.5 and Accept_Reject_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Accept_Reject_2.tStart = t
            Accept_Reject_2.frameNStart = frameN  # exact frame index
            Accept_Reject_2.setAutoDraw(True)
        
        # *nextTrialTest_4* updates
        if t >= 0.5 and nextTrialTest_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest_4.tStart = t
            nextTrialTest_4.frameNStart = frameN  # exact frame index
            nextTrialTest_4.setAutoDraw(True)
        
        # *earnings__2* updates
        if t >= 0.5 and earnings__2.status == NOT_STARTED:
            # keep track of start time/frame for later
            earnings__2.tStart = t
            earnings__2.frameNStart = frameN  # exact frame index
            earnings__2.setAutoDraw(True)
        if earnings__2.status == STARTED:  # only update if drawing
            earnings__2.setText(('$%0.2f' %(earnings)), log=False)
        
        # *Fixation_4* updates
        if t >= 0.0 and Fixation_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_4.tStart = t
            Fixation_4.frameNStart = frameN  # exact frame index
            Fixation_4.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation_4.status == STARTED and t >= frameRemains:
            Fixation_4.setAutoDraw(False)
        
        # *face_test_2* updates
        if t >= 0.5 and face_test_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            face_test_2.tStart = t
            face_test_2.frameNStart = frameN  # exact frame index
            face_test_2.setAutoDraw(True)
        
        # *houses_3* updates
        if t >= 0.5 and houses_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            houses_3.tStart = t
            houses_3.frameNStart = frameN  # exact frame index
            houses_3.setAutoDraw(True)
        
        # *EarningsLabel_2* updates
        if t >= 0.5 and EarningsLabel_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            EarningsLabel_2.tStart = t
            EarningsLabel_2.frameNStart = frameN  # exact frame index
            EarningsLabel_2.setAutoDraw(True)
        
        # *Mult1* updates
        if t >= 0.5 and Mult1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Mult1.tStart = t
            Mult1.frameNStart = frameN  # exact frame index
            Mult1.setAutoDraw(True)
        
        # *Mult2* updates
        if t >= 0.5 and Mult2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Mult2.tStart = t
            Mult2.frameNStart = frameN  # exact frame index
            Mult2.setAutoDraw(True)
        
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
    thisExp.addData('Trial', exp2Trial)
    thisExp.addData('correct', correct) 
    thisExp.addData('faceVal', actFaceVal)
    thisExp.addData('houseVal', actHouseVal)
    thisExp.addData('mult1House', mult1)
    thisExp.addData('mult2Face', mult2)
    thisExp.addData('summedVal', earningsUpdate)
    thisExp.addData('earnings', earnings)
    thisExp.addData('flip', flipChoice)
    inputText=""
    
    #done with the next routine
    #if exp2Trial>=200:
    #    trials_2.finished=1
    # check responses
    if numberEntry_4.keys in ['', [], None]:  # No response was made
        numberEntry_4.keys=None
    trials_3.addData('numberEntry_4.keys',numberEntry_4.keys)
    if numberEntry_4.keys != None:  # we had a response
        trials_3.addData('numberEntry_4.rt', numberEntry_4.rt)
    # the Routine "FullTest_01_Mult" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback_Block4"-------
    t = 0
    Feedback_Block4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    amount_4.setText(('$%0.2f' %(winLoss)))
    
    # keep track of which components have finished
    Feedback_Block4Components = [amount_4, text_17, text_18, Correct_wrong2_3]
    for thisComponent in Feedback_Block4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback_Block4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback_Block4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *amount_4* updates
        if t >= 0.0 and amount_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            amount_4.tStart = t
            amount_4.frameNStart = frameN  # exact frame index
            amount_4.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if amount_4.status == STARTED and t >= frameRemains:
            amount_4.setAutoDraw(False)
        if winLoss >= 0.0:
            correct = "CORRECT"
            correctColor = "green"
        else:
            correct = "INCORRECT"
            correctColor = "red"
        
        # *text_17* updates
        if t >= 1.5 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        frameRemains = 1.5 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_17.status == STARTED and t >= frameRemains:
            text_17.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 0.0 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_18.status == STARTED and t >= frameRemains:
            text_18.setAutoDraw(False)
        
        # *Correct_wrong2_3* updates
        if t >= 0.0 and Correct_wrong2_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Correct_wrong2_3.tStart = t
            Correct_wrong2_3.frameNStart = frameN  # exact frame index
            Correct_wrong2_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Correct_wrong2_3.status == STARTED and t >= frameRemains:
            Correct_wrong2_3.setAutoDraw(False)
        if Correct_wrong2_3.status == STARTED:  # only update if drawing
            Correct_wrong2_3.setColor(correctColor, colorSpace='rgb', log=False)
            Correct_wrong2_3.setText(correct, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback_Block4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback_Block4"-------
    for thisComponent in Feedback_Block4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if exp2Trial>=100: #change to 100
        trials_3.finished=1
    thisExp.nextEntry()
    
# completed 50 repeats of 'trials_3'


# ------Prepare to start Routine "FinalScore"-------
t = 0
FinalScoreClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
#theseKeys=""
#shift_flag = False

#difference between the input value and the house value
#currently using input from last frame for current house


#earnings = abs(long(float(newValue)) - houseValue)
theseKeys=""
shift_flag = False
#inputTextValue.alignHoriz = 'center'
numberEntry_5 = event.BuilderKeyResponse()
square_entry_5.setOpacity(1)
square_entry_5.setPos((0, 0))
square_entry_5.setLineWidth(1)
square_entry_5.setOri(0)
square_entry_5.setSize((0.5, 0.3))
# keep track of which components have finished
FinalScoreComponents = [numberEntry_5, square_entry_5, FinalEarnings, continue4, earnings__3]
for thisComponent in FinalScoreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "FinalScore"-------
while continueRoutine:
    # get current time
    t = FinalScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    n = len(theseKeys)
    i = 0
    while i < n:
        #for ACCEPTING and starting a new loop
        if theseKeys[i] == 'f':
            earningsUpdate = houseValue + faceValue
            earnings = earnings + earningsUpdate
            continueRoutine = False
            break
        
        #for REJECTING and starting a new loop
        elif theseKeys[i] == 'j':
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
    
    # *numberEntry_5* updates
    if t >= 0.7 and numberEntry_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        numberEntry_5.tStart = t
        numberEntry_5.frameNStart = frameN  # exact frame index
        numberEntry_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(numberEntry_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if numberEntry_5.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            numberEntry_5.keys.extend(theseKeys)  # storing all keys
            numberEntry_5.rt.append(numberEntry_5.clock.getTime())
            # a response ends the routine
            continueRoutine = False
    
    # *square_entry_5* updates
    if t >= 0.5 and square_entry_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_entry_5.tStart = t
        square_entry_5.frameNStart = frameN  # exact frame index
        square_entry_5.setAutoDraw(True)
    
    # *FinalEarnings* updates
    if t >= 0.5 and FinalEarnings.status == NOT_STARTED:
        # keep track of start time/frame for later
        FinalEarnings.tStart = t
        FinalEarnings.frameNStart = frameN  # exact frame index
        FinalEarnings.setAutoDraw(True)
    
    # *continue4* updates
    if t >= 0.5 and continue4.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue4.tStart = t
        continue4.frameNStart = frameN  # exact frame index
        continue4.setAutoDraw(True)
    
    # *earnings__3* updates
    if t >= 0.5 and earnings__3.status == NOT_STARTED:
        # keep track of start time/frame for later
        earnings__3.tStart = t
        earnings__3.frameNStart = frameN  # exact frame index
        earnings__3.setAutoDraw(True)
    if earnings__3.status == STARTED:  # only update if drawing
        earnings__3.setText(('$%0.2f' %(earnings)), log=False)
    
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

#let's store the final text string into the results final...
thisExp.addData('earnings', earnings)
inputText=""

# check responses
if numberEntry_5.keys in ['', [], None]:  # No response was made
    numberEntry_5.keys=None
thisExp.addData('numberEntry_5.keys',numberEntry_5.keys)
if numberEntry_5.keys != None:  # we had a response
    thisExp.addData('numberEntry_5.rt', numberEntry_5.rt)
thisExp.nextEntry()
# the Routine "FinalScore" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()






















# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
