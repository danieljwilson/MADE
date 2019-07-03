#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.1),
    on Thu Oct 27 14:18:49 2016
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
expName = 'test01'  # from the Builder filename that created this script
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
    originPath=u'/Users/danieljwilson/Dropbox/PHD/CENDRI/Project/Code/Test01/test01.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "FullTest_01"
FullTest_01Clock = core.Clock()
#earnings = -100
#newValue = 0
inputText = ""
earnings = 0
earningsUpdate = 0
square_entry_3 = visual.Rect(
    win=win, name='square_entry_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
Accept_Reject = visual.TextStim(win=win, name='Accept_Reject',
    text=u'Do you accept or reject this combination?',
    font=u'Helvetica',
    pos=(0, 0.75), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
nextTrialTest_3 = visual.TextStim(win=win, name='nextTrialTest_3',
    text=u"enter 'f' for accept, and 'j' for reject",
    font=u'Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);
earnings_ = visual.TextStim(win=win, name='earnings_',
    text='default text',
    font=u'Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0);
Fixation_3 = visual.TextStim(win=win, name='Fixation_3',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
face_test = visual.ImageStim(
    win=win, name='face_test',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(250, 0), size=(360, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
houses_2 = visual.ImageStim(
    win=win, name='houses_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-250, 0), size=(480, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
EarningsLabel = visual.TextStim(win=win, name='EarningsLabel',
    text=u'earnings',
    font=u'Helvetica',
    pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-10.0);

# Initialize components for Routine "TestInstr"
TestInstrClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='For the test you will be presented with one house image and one face image that you can either accept or reject.\n\nIf you ACCEPT and the combined value is GREATER than zero, you will earn that amount of money.\n\nIf the ACCEPT and the combined value is LESS than zero you will lose that amount of money.\n\nIf you REJECT you will neither earn nor lose money.',
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
    image='images/morphs/05.png', mask=None,
    ori=0, pos=(-250, 0), size=(300,300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
houseMorph07_2 = visual.ImageStim(
    win=win, name='houseMorph07_2',units='pix', 
    image='images/morphs/House07.png', mask=None,
    ori=0, pos=(250, 0), size=[400,300],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='In this case the combined value of the two images is: 2.90 -1.95 = 0.95.',
    font='Helvetica',
    pos=(0, .6), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
faceValueText_2 = visual.TextStim(win=win, name='faceValueText_2',
    text='2.90 dollars',
    font='Helvetica',
    pos=(-0.4, -0.44), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
houseValue_2 = visual.TextStim(win=win, name='houseValue_2',
    text='-1.95 dollars',
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

# Initialize components for Routine "TestInstr_3"
TestInstr_3Clock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='The test will now begin.\n\nTry to accumulate as much money as possible.\n\n\nThere will be 20 trials.',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
press_key = visual.TextStim(win=win, name='press_key',
    text='default text',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Part_1"
Part_1Clock = core.Clock()
to_continue = visual.TextStim(win=win, name='to_continue',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text='Part 1: Learning',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "routine_01_Instr01"
routine_01_Instr01Clock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='images/man01.png', mask=None,
    ori=0, pos=(0, 0), size=[500,500],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='This face is worth 5.00 dollars',
    font='Helvetica',
    pos=(0, .80), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "var_01_Instr_02"
var_01_Instr_02Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='images/man02.png', mask=None,
    ori=0, pos=(0, 0), size=[500,500],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='This face is worth -5.00 dollars',
    font='Helvetica',
    pos=(0, .80), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "var_01_Instr_03"
var_01_Instr_03Clock = core.Clock()
man02 = visual.ImageStim(
    win=win, name='man02',units='pix', 
    image='images/man02.png', mask=None,
    ori=0, pos=(300, 0), size=[250,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='Combination of the two faces will give different "values".',
    font='Helvetica',
    pos=(0, .80), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
man01 = visual.ImageStim(
    win=win, name='man01',units='pix', 
    image='images/man01.png', mask=None,
    ori=0, pos=(-300, 0), size=(250,250),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
man_morph50 = visual.ImageStim(
    win=win, name='man_morph50',units='pix', 
    image='images/morphs/09.png', mask=None,
    ori=0, pos=(0, 0), size=(250,250),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='5.00 dollars',
    font='Helvetica',
    pos=(-0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
minus5 = visual.TextStim(win=win, name='minus5',
    text='-5.00 dollars',
    font='Helvetica',
    pos=(0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
zeroDollar = visual.TextStim(win=win, name='zeroDollar',
    text='0.00 dollars',
    font='Helvetica',
    pos=(0, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Initialize components for Routine "PreLearnScreen"
PreLearnScreenClock = core.Clock()
to_continue_3 = visual.TextStim(win=win, name='to_continue_3',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part1Learn = visual.TextStim(win=win, name='Part1Learn',
    text='Part 1: Faces',
    font='Helvetica',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
minScore_2 = visual.TextStim(win=win, name='minScore_2',
    text='You will be shown a face: try to guess the value in your head.\n\nAfter a couple of seconds you will be shown the actual value.\n\nSee how close to the actual value you can get.\n\nThere are 10 trials.\n',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Part_1_Faces"
Part_1_FacesClock = core.Clock()
face_morphs = visual.ImageStim(
    win=win, name='face_morphs',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
TopText = visual.TextStim(win=win, name='TopText',
    text='The value of this face is:',
    font='Helvetica',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
Value = visual.TextStim(win=win, name='Value',
    text='default text',
    font=u'Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
continueOn = visual.TextStim(win=win, name='continueOn',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);

# Initialize components for Routine "houseLearnInstr"
houseLearnInstrClock = core.Clock()
House01 = visual.ImageStim(
    win=win, name='House01',units='pix', 
    image='images/morphs/House10.png', mask=None,
    ori=0, pos=(300, 0), size=[240,180],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Also, houses and "combinations" of two houses will give different values.',
    font='Helvetica',
    pos=(0, .80), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continue9 = visual.TextStim(win=win, name='continue9',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
man01_2 = visual.ImageStim(
    win=win, name='man01_2',units='pix', 
    image='images/morphs/House01.png', mask=None,
    ori=0, pos=(-300, 0), size=(240,180),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
man_morph50_2 = visual.ImageStim(
    win=win, name='man_morph50_2',units='pix', 
    image='images/morphs/House05.png', mask=None,
    ori=0, pos=(0, 0), size=(240,180),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='5.00 dollars',
    font='Helvetica',
    pos=(-0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
minus5_2 = visual.TextStim(win=win, name='minus5_2',
    text='-5.00 dollars',
    font='Helvetica',
    pos=(0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
zeroDollar_2 = visual.TextStim(win=win, name='zeroDollar_2',
    text='0.00 dollars',
    font='Helvetica',
    pos=(0, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Initialize components for Routine "PreLearnScreen2"
PreLearnScreen2Clock = core.Clock()
to_continue_4 = visual.TextStim(win=win, name='to_continue_4',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part1Learn_2 = visual.TextStim(win=win, name='Part1Learn_2',
    text='Part 1: Houses',
    font='Helvetica',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
minScore_3 = visual.TextStim(win=win, name='minScore_3',
    text='You will be shown a house: try to guess the value in your head.\n\nAfter a couple of seconds you will be shown the actual value.\n\nSee how close to the actual value you can get.\n\nThere are 10 trials.\n',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Part1_Houses"
Part1_HousesClock = core.Clock()
House_morphs = visual.ImageStim(
    win=win, name='House_morphs',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(480, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
TopText_2 = visual.TextStim(win=win, name='TopText_2',
    text='The value of this house is:',
    font='Helvetica',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
Value_2 = visual.TextStim(win=win, name='Value_2',
    text='default text',
    font=u'Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
continueOn_2 = visual.TextStim(win=win, name='continueOn_2',
    text=u'press any key to continue',
    font=u'Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);

# Initialize components for Routine "PreTestScreen"
PreTestScreenClock = core.Clock()
to_continue_2 = visual.TextStim(win=win, name='to_continue_2',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part1Test = visual.TextStim(win=win, name='Part1Test',
    text='Part 1: Test',
    font='Helvetica',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
minScore = visual.TextStim(win=win, name='minScore',
    text='You need to acheive an average answer that is within 0.50 dollars of the actual value.\n\nIf you do not succeed you will need to go back to training and then take the test again.\n\nThere are 20 trials.\n',
    font='Arial',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Test"
TestClock = core.Clock()
inputText = ""
square_entry = visual.Rect(
    win=win, name='square_entry',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
EnterValue = visual.TextStim(win=win, name='EnterValue',
    text='Enter the value for this face',
    font='Helvetica',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
nextTrialTest = visual.TextStim(win=win, name='nextTrialTest',
    text="after you enter a value press 'return'",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
inputTextValue = visual.TextStim(win=win, name='inputTextValue',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
faces = visual.ImageStim(
    win=win, name='faces',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
useFormat = visual.TextStim(win=win, name='useFormat',
    text='Use the format X.XX (e.g. 2.50)',
    font='Helvetica',
    pos=(0, 0.75), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Initialize components for Routine "ActualValue"
ActualValueClock = core.Clock()
ActVal = visual.TextStim(win=win, name='ActVal',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
continue3 = visual.TextStim(win=win, name='continue3',
    text='press any key to contine',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
ActualValueText = visual.TextStim(win=win, name='ActualValueText',
    text=u'Actual value was:',
    font=u'Helvetica',
    pos=(0, .2), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0);
youSaid = visual.TextStim(win=win, name='youSaid',
    text='default text',
    font=u'Helvetica',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "testHouse"
testHouseClock = core.Clock()
inputText = ""
square_entry_2 = visual.Rect(
    win=win, name='square_entry_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=1.0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
EnterValue_2 = visual.TextStim(win=win, name='EnterValue_2',
    text='Enter the value for this house',
    font='Helvetica',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
nextTrialTest_2 = visual.TextStim(win=win, name='nextTrialTest_2',
    text="after you enter a value press 'return'",
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
inputTextValue_2 = visual.TextStim(win=win, name='inputTextValue_2',
    text='default text',
    font='Helvetica',
    pos=(0, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
houses = visual.ImageStim(
    win=win, name='houses',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(480, 360),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
useFormat_2 = visual.TextStim(win=win, name='useFormat_2',
    text='Use the format X.XX (e.g. 2.50)',
    font='Helvetica',
    pos=(0, 0.75), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
Fixation_2 = visual.TextStim(win=win, name='Fixation_2',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Initialize components for Routine "ActValueHouse"
ActValueHouseClock = core.Clock()
ActVal_2 = visual.TextStim(win=win, name='ActVal_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
continue3_2 = visual.TextStim(win=win, name='continue3_2',
    text='press any key to contine',
    font='Helvetica',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
ActualValueText_2 = visual.TextStim(win=win, name='ActualValueText_2',
    text='Actual value was:',
    font='Helvetica',
    pos=(0, .2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
youSaid_2 = visual.TextStim(win=win, name='youSaid_2',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "Congrats"
CongratsClock = core.Clock()
to_continue_5 = visual.TextStim(win=win, name='to_continue_5',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part1Learn_3 = visual.TextStim(win=win, name='Part1Learn_3',
    text='Congratulations',
    font='Helvetica',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
minScore_4 = visual.TextStim(win=win, name='minScore_4',
    text='You have accurately stated the values of the faces and houses.\n\nNow we will move on to Part 2.\n',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "TestInstr"
TestInstrClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='For the test you will be presented with one house image and one face image that you can either accept or reject.\n\nIf you ACCEPT and the combined value is GREATER than zero, you will earn that amount of money.\n\nIf the ACCEPT and the combined value is LESS than zero you will lose that amount of money.\n\nIf you REJECT you will neither earn nor lose money.',
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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=1, method='random', 
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
    inputTextValue.alignHoriz = 'center'
    numberEntry_3 = event.BuilderKeyResponse()
    square_entry_3.setOpacity(1)
    square_entry_3.setPos((0, -.75))
    square_entry_3.setLineWidth(1)
    square_entry_3.setOri(0)
    square_entry_3.setSize((0.25, 0.15))
    face_test.setImage(faceImage)
    houses_2.setImage(houseImage)
    # keep track of which components have finished
    FullTest_01Components = [numberEntry_3, square_entry_3, Accept_Reject, nextTrialTest_3, earnings_, Fixation_3, face_test, houses_2, EarningsLabel]
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
        
        # *numberEntry_3* updates
        if t >= 0.7 and numberEntry_3.status == NOT_STARTED:
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
        if t >= 0.5 and square_entry_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry_3.tStart = t
            square_entry_3.frameNStart = frameN  # exact frame index
            square_entry_3.setAutoDraw(True)
        
        # *Accept_Reject* updates
        if t >= 0.5 and Accept_Reject.status == NOT_STARTED:
            # keep track of start time/frame for later
            Accept_Reject.tStart = t
            Accept_Reject.frameNStart = frameN  # exact frame index
            Accept_Reject.setAutoDraw(True)
        
        # *nextTrialTest_3* updates
        if t >= 0.5 and nextTrialTest_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest_3.tStart = t
            nextTrialTest_3.frameNStart = frameN  # exact frame index
            nextTrialTest_3.setAutoDraw(True)
        
        # *earnings_* updates
        if t >= 0.5 and earnings_.status == NOT_STARTED:
            # keep track of start time/frame for later
            earnings_.tStart = t
            earnings_.frameNStart = frameN  # exact frame index
            earnings_.setAutoDraw(True)
        if earnings_.status == STARTED:  # only update if drawing
            earnings_.setText(('%0.2f' %(earnings)), log=False)
        
        # *Fixation_3* updates
        if t >= 0.0 and Fixation_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_3.tStart = t
            Fixation_3.frameNStart = frameN  # exact frame index
            Fixation_3.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation_3.status == STARTED and t >= frameRemains:
            Fixation_3.setAutoDraw(False)
        
        # *face_test* updates
        if t >= 0.5 and face_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            face_test.tStart = t
            face_test.frameNStart = frameN  # exact frame index
            face_test.setAutoDraw(True)
        
        # *houses_2* updates
        if t >= 0.5 and houses_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            houses_2.tStart = t
            houses_2.frameNStart = frameN  # exact frame index
            houses_2.setAutoDraw(True)
        
        # *EarningsLabel* updates
        if t >= 0.5 and EarningsLabel.status == NOT_STARTED:
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
    thisExp.addData('earnings', earnings)
    inputText=""
    
    # check responses
    if numberEntry_3.keys in ['', [], None]:  # No response was made
        numberEntry_3.keys=None
    test.addData('numberEntry_3.keys',numberEntry_3.keys)
    if numberEntry_3.keys != None:  # we had a response
        test.addData('numberEntry_3.rt', numberEntry_3.rt)
    # the Routine "FullTest_01" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'test'


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

# ------Prepare to start Routine "TestInstr_3"-------
t = 0
TestInstr_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exitKeys_3 = event.BuilderKeyResponse()
# keep track of which components have finished
TestInstr_3Components = [exitKeys_3, instructions_3, continue9_4]
for thisComponent in TestInstr_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "TestInstr_3"-------
while continueRoutine:
    # get current time
    t = TestInstr_3Clock.getTime()
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
# check responses
if exitKeys_3.keys in ['', [], None]:  # No response was made
    exitKeys_3.keys=None
thisExp.addData('exitKeys_3.keys',exitKeys_3.keys)
if exitKeys_3.keys != None:  # we had a response
    thisExp.addData('exitKeys_3.rt', exitKeys_3.rt)
thisExp.nextEntry()
# the Routine "TestInstr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Instructions.xlsx'),
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
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Instructions.setText(instr)
    key_resp_2 = event.BuilderKeyResponse()
    press_key.setText('press any key to continue')
    # keep track of which components have finished
    trialComponents = [Instructions, key_resp_2, press_key]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions* updates
        if t >= 0.3 and Instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            Instructions.tStart = t
            Instructions.frameNStart = frameN  # exact frame index
            Instructions.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.5 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *press_key* updates
        if t >= 0.3 and press_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_key.tStart = t
            press_key.frameNStart = frameN  # exact frame index
            press_key.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Part_1"-------
t = 0
Part_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Part_1Components = [to_continue, text, key_resp_3]
for thisComponent in Part_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part_1"-------
while continueRoutine:
    # get current time
    t = Part_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *to_continue* updates
    if t >= 0.2 and to_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        to_continue.tStart = t
        to_continue.frameNStart = frameN  # exact frame index
        to_continue.setAutoDraw(True)
    
    # *text* updates
    if t >= 0.2 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.2 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part_1"-------
for thisComponent in Part_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Part_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_01_Instr01"-------
t = 0
routine_01_Instr01Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
routine_01_Instr01Components = [image, text_2, key_resp_4, text_3]
for thisComponent in routine_01_Instr01Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "routine_01_Instr01"-------
while continueRoutine:
    # get current time
    t = routine_01_Instr01Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_01_Instr01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_01_Instr01"-------
for thisComponent in routine_01_Instr01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "routine_01_Instr01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "var_01_Instr_02"-------
t = 0
var_01_Instr_02Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
var_01_Instr_02Components = [image_2, text_4, key_resp_5, text_5]
for thisComponent in var_01_Instr_02Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "var_01_Instr_02"-------
while continueRoutine:
    # get current time
    t = var_01_Instr_02Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if t >= 0.0 and image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_2.tStart = t
        image_2.frameNStart = frameN  # exact frame index
        image_2.setAutoDraw(True)
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in var_01_Instr_02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "var_01_Instr_02"-------
for thisComponent in var_01_Instr_02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "var_01_Instr_02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "var_01_Instr_03"-------
t = 0
var_01_Instr_03Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
var_01_Instr_03Components = [man02, text_6, key_resp_7, text_7, man01, man_morph50, text_8, minus5, zeroDollar]
for thisComponent in var_01_Instr_03Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "var_01_Instr_03"-------
while continueRoutine:
    # get current time
    t = var_01_Instr_03Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *man02* updates
    if t >= 0.0 and man02.status == NOT_STARTED:
        # keep track of start time/frame for later
        man02.tStart = t
        man02.frameNStart = frameN  # exact frame index
        man02.setAutoDraw(True)
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *man01* updates
    if t >= 0.0 and man01.status == NOT_STARTED:
        # keep track of start time/frame for later
        man01.tStart = t
        man01.frameNStart = frameN  # exact frame index
        man01.setAutoDraw(True)
    
    # *man_morph50* updates
    if t >= 3 and man_morph50.status == NOT_STARTED:
        # keep track of start time/frame for later
        man_morph50.tStart = t
        man_morph50.frameNStart = frameN  # exact frame index
        man_morph50.setAutoDraw(True)
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    
    # *minus5* updates
    if t >= 0.0 and minus5.status == NOT_STARTED:
        # keep track of start time/frame for later
        minus5.tStart = t
        minus5.frameNStart = frameN  # exact frame index
        minus5.setAutoDraw(True)
    
    # *zeroDollar* updates
    if t >= 3.0 and zeroDollar.status == NOT_STARTED:
        # keep track of start time/frame for later
        zeroDollar.tStart = t
        zeroDollar.frameNStart = frameN  # exact frame index
        zeroDollar.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in var_01_Instr_03Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "var_01_Instr_03"-------
for thisComponent in var_01_Instr_03Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "var_01_Instr_03" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PreLearnScreen"-------
t = 0
PreLearnScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
PreLearnScreenComponents = [to_continue_3, Part1Learn, key_resp_9, minScore_2]
for thisComponent in PreLearnScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PreLearnScreen"-------
while continueRoutine:
    # get current time
    t = PreLearnScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *to_continue_3* updates
    if t >= 0.2 and to_continue_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        to_continue_3.tStart = t
        to_continue_3.frameNStart = frameN  # exact frame index
        to_continue_3.setAutoDraw(True)
    
    # *Part1Learn* updates
    if t >= 0.2 and Part1Learn.status == NOT_STARTED:
        # keep track of start time/frame for later
        Part1Learn.tStart = t
        Part1Learn.frameNStart = frameN  # exact frame index
        Part1Learn.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.2 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *minScore_2* updates
    if t >= 0.5 and minScore_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        minScore_2.tStart = t
        minScore_2.frameNStart = frameN  # exact frame index
        minScore_2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreLearnScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreLearnScreen"-------
for thisComponent in PreLearnScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "PreLearnScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
learn_faceValue = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part1.xlsx'),
    seed=None, name='learn_faceValue')
thisExp.addLoop(learn_faceValue)  # add the loop to the experiment
thisLearn_faceValue = learn_faceValue.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearn_faceValue.rgb)
if thisLearn_faceValue != None:
    for paramName in thisLearn_faceValue.keys():
        exec(paramName + '= thisLearn_faceValue.' + paramName)

for thisLearn_faceValue in learn_faceValue:
    currentLoop = learn_faceValue
    # abbreviate parameter names if possible (e.g. rgb = thisLearn_faceValue.rgb)
    if thisLearn_faceValue != None:
        for paramName in thisLearn_faceValue.keys():
            exec(paramName + '= thisLearn_faceValue.' + paramName)
    
    # ------Prepare to start Routine "Part_1_Faces"-------
    t = 0
    Part_1_FacesClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    face_morphs.setImage(faceImage)
    key_resp_6 = event.BuilderKeyResponse()
    Value.setText(('%0.2f' %(faceValue)))
    # keep track of which components have finished
    Part_1_FacesComponents = [face_morphs, fixation, key_resp_6, TopText, Value, continueOn]
    for thisComponent in Part_1_FacesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Part_1_Faces"-------
    while continueRoutine:
        # get current time
        t = Part_1_FacesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face_morphs* updates
        if t >= 0.5 and face_morphs.status == NOT_STARTED:
            # keep track of start time/frame for later
            face_morphs.tStart = t
            face_morphs.frameNStart = frameN  # exact frame index
            face_morphs.setAutoDraw(True)
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.5 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *TopText* updates
        if t >= 0.5 and TopText.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopText.tStart = t
            TopText.frameNStart = frameN  # exact frame index
            TopText.setAutoDraw(True)
        
        # *Value* updates
        if t >= 3 and Value.status == NOT_STARTED:
            # keep track of start time/frame for later
            Value.tStart = t
            Value.frameNStart = frameN  # exact frame index
            Value.setAutoDraw(True)
        
        # *continueOn* updates
        if t >= 3.5 and continueOn.status == NOT_STARTED:
            # keep track of start time/frame for later
            continueOn.tStart = t
            continueOn.frameNStart = frameN  # exact frame index
            continueOn.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part_1_FacesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Part_1_Faces"-------
    for thisComponent in Part_1_FacesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    learn_faceValue.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        learn_faceValue.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "Part_1_Faces" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'learn_faceValue'


# ------Prepare to start Routine "houseLearnInstr"-------
t = 0
houseLearnInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
houseLearnInstrComponents = [House01, text_9, key_resp_11, continue9, man01_2, man_morph50_2, text_11, minus5_2, zeroDollar_2]
for thisComponent in houseLearnInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "houseLearnInstr"-------
while continueRoutine:
    # get current time
    t = houseLearnInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *House01* updates
    if t >= 0.0 and House01.status == NOT_STARTED:
        # keep track of start time/frame for later
        House01.tStart = t
        House01.frameNStart = frameN  # exact frame index
        House01.setAutoDraw(True)
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *continue9* updates
    if t >= 0.0 and continue9.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue9.tStart = t
        continue9.frameNStart = frameN  # exact frame index
        continue9.setAutoDraw(True)
    
    # *man01_2* updates
    if t >= 0.0 and man01_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        man01_2.tStart = t
        man01_2.frameNStart = frameN  # exact frame index
        man01_2.setAutoDraw(True)
    
    # *man_morph50_2* updates
    if t >= 3 and man_morph50_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        man_morph50_2.tStart = t
        man_morph50_2.frameNStart = frameN  # exact frame index
        man_morph50_2.setAutoDraw(True)
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    
    # *minus5_2* updates
    if t >= 0.0 and minus5_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        minus5_2.tStart = t
        minus5_2.frameNStart = frameN  # exact frame index
        minus5_2.setAutoDraw(True)
    
    # *zeroDollar_2* updates
    if t >= 3.0 and zeroDollar_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        zeroDollar_2.tStart = t
        zeroDollar_2.frameNStart = frameN  # exact frame index
        zeroDollar_2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in houseLearnInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "houseLearnInstr"-------
for thisComponent in houseLearnInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys=None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "houseLearnInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PreLearnScreen2"-------
t = 0
PreLearnScreen2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()
# keep track of which components have finished
PreLearnScreen2Components = [to_continue_4, Part1Learn_2, key_resp_13, minScore_3]
for thisComponent in PreLearnScreen2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PreLearnScreen2"-------
while continueRoutine:
    # get current time
    t = PreLearnScreen2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *to_continue_4* updates
    if t >= 0.2 and to_continue_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        to_continue_4.tStart = t
        to_continue_4.frameNStart = frameN  # exact frame index
        to_continue_4.setAutoDraw(True)
    
    # *Part1Learn_2* updates
    if t >= 0.2 and Part1Learn_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Part1Learn_2.tStart = t
        Part1Learn_2.frameNStart = frameN  # exact frame index
        Part1Learn_2.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.2 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_13.keys = theseKeys[-1]  # just the last key pressed
            key_resp_13.rt = key_resp_13.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *minScore_3* updates
    if t >= 0.5 and minScore_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        minScore_3.tStart = t
        minScore_3.frameNStart = frameN  # exact frame index
        minScore_3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreLearnScreen2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreLearnScreen2"-------
for thisComponent in PreLearnScreen2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys=None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
# the Routine "PreLearnScreen2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
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
    
    # ------Prepare to start Routine "Part1_Houses"-------
    t = 0
    Part1_HousesClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    House_morphs.setImage(houseImage)
    key_resp_12 = event.BuilderKeyResponse()
    Value_2.setText(('%0.2f' %(houseValue)))
    # keep track of which components have finished
    Part1_HousesComponents = [House_morphs, fixation_2, key_resp_12, TopText_2, Value_2, continueOn_2]
    for thisComponent in Part1_HousesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Part1_Houses"-------
    while continueRoutine:
        # get current time
        t = Part1_HousesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *House_morphs* updates
        if t >= 0.5 and House_morphs.status == NOT_STARTED:
            # keep track of start time/frame for later
            House_morphs.tStart = t
            House_morphs.frameNStart = frameN  # exact frame index
            House_morphs.setAutoDraw(True)
        
        # *fixation_2* updates
        if t >= 0.0 and fixation_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_2.tStart = t
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_2.status == STARTED and t >= frameRemains:
            fixation_2.setAutoDraw(False)
        
        # *key_resp_12* updates
        if t >= 0.5 and key_resp_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_12.tStart = t
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_12.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_12.keys = theseKeys[-1]  # just the last key pressed
                key_resp_12.rt = key_resp_12.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *TopText_2* updates
        if t >= 0.5 and TopText_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopText_2.tStart = t
            TopText_2.frameNStart = frameN  # exact frame index
            TopText_2.setAutoDraw(True)
        
        # *Value_2* updates
        if t >= 3 and Value_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Value_2.tStart = t
            Value_2.frameNStart = frameN  # exact frame index
            Value_2.setAutoDraw(True)
        
        # *continueOn_2* updates
        if t >= 3.5 and continueOn_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            continueOn_2.tStart = t
            continueOn_2.frameNStart = frameN  # exact frame index
            continueOn_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Part1_HousesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Part1_Houses"-------
    for thisComponent in Part1_HousesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys=None
    trials_2.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        trials_2.addData('key_resp_12.rt', key_resp_12.rt)
    # the Routine "Part1_Houses" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "PreTestScreen"-------
t = 0
PreTestScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
PreTestScreenComponents = [to_continue_2, Part1Test, key_resp_8, minScore]
for thisComponent in PreTestScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PreTestScreen"-------
while continueRoutine:
    # get current time
    t = PreTestScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *to_continue_2* updates
    if t >= 0.2 and to_continue_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        to_continue_2.tStart = t
        to_continue_2.frameNStart = frameN  # exact frame index
        to_continue_2.setAutoDraw(True)
    
    # *Part1Test* updates
    if t >= 0.2 and Part1Test.status == NOT_STARTED:
        # keep track of start time/frame for later
        Part1Test.tStart = t
        Part1Test.frameNStart = frameN  # exact frame index
        Part1Test.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.2 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *minScore* updates
    if t >= 0.5 and minScore.status == NOT_STARTED:
        # keep track of start time/frame for later
        minScore.tStart = t
        minScore.frameNStart = frameN  # exact frame index
        minScore.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreTestScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreTestScreen"-------
for thisComponent in PreTestScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "PreTestScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_faceValue = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part1.xlsx'),
    seed=None, name='test_faceValue')
thisExp.addLoop(test_faceValue)  # add the loop to the experiment
thisTest_faceValue = test_faceValue.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_faceValue.rgb)
if thisTest_faceValue != None:
    for paramName in thisTest_faceValue.keys():
        exec(paramName + '= thisTest_faceValue.' + paramName)

for thisTest_faceValue in test_faceValue:
    currentLoop = test_faceValue
    # abbreviate parameter names if possible (e.g. rgb = thisTest_faceValue.rgb)
    if thisTest_faceValue != None:
        for paramName in thisTest_faceValue.keys():
            exec(paramName + '= thisTest_faceValue.' + paramName)
    
    # ------Prepare to start Routine "Test"-------
    t = 0
    TestClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    theseKeys=""
    shift_flag = False
    inputTextValue.alignHoriz = 'center'
    numberEntry = event.BuilderKeyResponse()
    square_entry.setOpacity(1)
    square_entry.setPos((0, -.75))
    square_entry.setLineWidth(1)
    square_entry.setOri(0)
    square_entry.setSize((0.25, 0.15))
    faces.setImage(faceImage)
    # keep track of which components have finished
    TestComponents = [numberEntry, square_entry, EnterValue, nextTrialTest, inputTextValue, faces, useFormat, Fixation]
    for thisComponent in TestComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Test"-------
    while continueRoutine:
        # get current time
        t = TestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n = len(theseKeys)
        i = 0
        while i < n:
            if theseKeys[i] == 'return' and len(inputText) > 3:
                # pressing RETURN means time to stop
                continueRoutine = False
                break
        
            elif theseKeys[i] == 'backspace':
                inputText = inputText[:-1] #lose the final character
                i = i + 1
            
            elif theseKeys[i] == 'period':
                inputText  = inputText + "."
                i = i+1
        
            elif theseKeys[i] == 'minus':
                inputText  = inputText + "-"
                i = i+1
        
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
        if t >= 0.7 and numberEntry.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry.tStart = t
            numberEntry.frameNStart = frameN  # exact frame index
            numberEntry.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numberEntry.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numberEntry.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', 'backspace', 'period', 'return', '-', 'minus'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numberEntry.keys.extend(theseKeys)  # storing all keys
                numberEntry.rt.append(numberEntry.clock.getTime())
        
        # *square_entry* updates
        if t >= 0.5 and square_entry.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry.tStart = t
            square_entry.frameNStart = frameN  # exact frame index
            square_entry.setAutoDraw(True)
        
        # *EnterValue* updates
        if t >= 0.5 and EnterValue.status == NOT_STARTED:
            # keep track of start time/frame for later
            EnterValue.tStart = t
            EnterValue.frameNStart = frameN  # exact frame index
            EnterValue.setAutoDraw(True)
        
        # *nextTrialTest* updates
        if t >= 0.5 and nextTrialTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest.tStart = t
            nextTrialTest.frameNStart = frameN  # exact frame index
            nextTrialTest.setAutoDraw(True)
        
        # *inputTextValue* updates
        if t >= 0.5 and inputTextValue.status == NOT_STARTED:
            # keep track of start time/frame for later
            inputTextValue.tStart = t
            inputTextValue.frameNStart = frameN  # exact frame index
            inputTextValue.setAutoDraw(True)
        if inputTextValue.status == STARTED:  # only update if drawing
            inputTextValue.setText(inputText, log=False)
        
        # *faces* updates
        if t >= 0.5 and faces.status == NOT_STARTED:
            # keep track of start time/frame for later
            faces.tStart = t
            faces.frameNStart = frameN  # exact frame index
            faces.setAutoDraw(True)
        
        # *useFormat* updates
        if t >= 0.5 and useFormat.status == NOT_STARTED:
            # keep track of start time/frame for later
            useFormat.tStart = t
            useFormat.frameNStart = frameN  # exact frame index
            useFormat.setAutoDraw(True)
        
        # *Fixation* updates
        if t >= 0.0 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation.status == STARTED and t >= frameRemains:
            Fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test"-------
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #let's store the final text string into the results final...
    thisExp.addData('inputText', inputText)
    inputText=""
    # check responses
    if numberEntry.keys in ['', [], None]:  # No response was made
        numberEntry.keys=None
    test_faceValue.addData('numberEntry.keys',numberEntry.keys)
    if numberEntry.keys != None:  # we had a response
        test_faceValue.addData('numberEntry.rt', numberEntry.rt)
    # the Routine "Test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ActualValue"-------
    t = 0
    ActualValueClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ActVal.setColor(u'white', colorSpace='rgb')
    ActVal.setText(('0.2f' %(faceValue)))
    ActVal.setPos((0, 0))
    ActVal.setFont(u'Helvetica')
    ActVal.setHeight(0.15)
    key_resp_10 = event.BuilderKeyResponse()
    youSaid.setText(('%0.2f' %(inputText)))
    # keep track of which components have finished
    ActualValueComponents = [ActVal, key_resp_10, continue3, ActualValueText, youSaid]
    for thisComponent in ActualValueComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ActualValue"-------
    while continueRoutine:
        # get current time
        t = ActualValueClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ActVal* updates
        if t >= 0.2 and ActVal.status == NOT_STARTED:
            # keep track of start time/frame for later
            ActVal.tStart = t
            ActVal.frameNStart = frameN  # exact frame index
            ActVal.setAutoDraw(True)
        
        # *key_resp_10* updates
        if t >= 0.5 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                key_resp_10.rt = key_resp_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *continue3* updates
        if t >= 0.5 and continue3.status == NOT_STARTED:
            # keep track of start time/frame for later
            continue3.tStart = t
            continue3.frameNStart = frameN  # exact frame index
            continue3.setAutoDraw(True)
        
        # *ActualValueText* updates
        if t >= 0.2 and ActualValueText.status == NOT_STARTED:
            # keep track of start time/frame for later
            ActualValueText.tStart = t
            ActualValueText.frameNStart = frameN  # exact frame index
            ActualValueText.setAutoDraw(True)
        
        # *youSaid* updates
        if t >= 1 and youSaid.status == NOT_STARTED:
            # keep track of start time/frame for later
            youSaid.tStart = t
            youSaid.frameNStart = frameN  # exact frame index
            youSaid.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ActualValueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ActualValue"-------
    for thisComponent in ActualValueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys=None
    test_faceValue.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        test_faceValue.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "ActualValue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "testHouse"-------
    t = 0
    testHouseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    theseKeys=""
    shift_flag = False
    inputTextValue.alignHoriz = 'center'
    numberEntry_2 = event.BuilderKeyResponse()
    square_entry_2.setOpacity(1)
    square_entry_2.setPos((0, -.75))
    square_entry_2.setLineWidth(1)
    square_entry_2.setOri(0)
    square_entry_2.setSize((0.25, 0.15))
    houses.setImage(houseImage)
    # keep track of which components have finished
    testHouseComponents = [numberEntry_2, square_entry_2, EnterValue_2, nextTrialTest_2, inputTextValue_2, houses, useFormat_2, Fixation_2]
    for thisComponent in testHouseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "testHouse"-------
    while continueRoutine:
        # get current time
        t = testHouseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n = len(theseKeys)
        i = 0
        while i < n:
            if theseKeys[i] == 'return' and len(inputText) > 3:
                # pressing RETURN means time to stop
                continueRoutine = False
                break
        
            elif theseKeys[i] == 'backspace':
                inputText = inputText[:-1] #lose the final character
                i = i + 1
            
            elif theseKeys[i] == 'period':
                inputText  = inputText + "."
                i = i+1
        
            elif theseKeys[i] == 'minus':
                inputText  = inputText + "-"
                i = i+1
        
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
        
        # *numberEntry_2* updates
        if t >= 0.7 and numberEntry_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            numberEntry_2.tStart = t
            numberEntry_2.frameNStart = frameN  # exact frame index
            numberEntry_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(numberEntry_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if numberEntry_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', 'backspace', 'period', 'return', '-', 'minus'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                numberEntry_2.keys.extend(theseKeys)  # storing all keys
                numberEntry_2.rt.append(numberEntry_2.clock.getTime())
        
        # *square_entry_2* updates
        if t >= 0.5 and square_entry_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_entry_2.tStart = t
            square_entry_2.frameNStart = frameN  # exact frame index
            square_entry_2.setAutoDraw(True)
        
        # *EnterValue_2* updates
        if t >= 0.5 and EnterValue_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            EnterValue_2.tStart = t
            EnterValue_2.frameNStart = frameN  # exact frame index
            EnterValue_2.setAutoDraw(True)
        
        # *nextTrialTest_2* updates
        if t >= 0.5 and nextTrialTest_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            nextTrialTest_2.tStart = t
            nextTrialTest_2.frameNStart = frameN  # exact frame index
            nextTrialTest_2.setAutoDraw(True)
        
        # *inputTextValue_2* updates
        if t >= 0.5 and inputTextValue_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            inputTextValue_2.tStart = t
            inputTextValue_2.frameNStart = frameN  # exact frame index
            inputTextValue_2.setAutoDraw(True)
        if inputTextValue_2.status == STARTED:  # only update if drawing
            inputTextValue_2.setText(inputText, log=False)
        
        # *houses* updates
        if t >= 0.5 and houses.status == NOT_STARTED:
            # keep track of start time/frame for later
            houses.tStart = t
            houses.frameNStart = frameN  # exact frame index
            houses.setAutoDraw(True)
        
        # *useFormat_2* updates
        if t >= 0.5 and useFormat_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            useFormat_2.tStart = t
            useFormat_2.frameNStart = frameN  # exact frame index
            useFormat_2.setAutoDraw(True)
        
        # *Fixation_2* updates
        if t >= 0.0 and Fixation_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation_2.tStart = t
            Fixation_2.frameNStart = frameN  # exact frame index
            Fixation_2.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Fixation_2.status == STARTED and t >= frameRemains:
            Fixation_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testHouseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testHouse"-------
    for thisComponent in testHouseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #let's store the final text string into the results final...
    thisExp.addData('inputText', inputText)
    inputText=""
    # check responses
    if numberEntry_2.keys in ['', [], None]:  # No response was made
        numberEntry_2.keys=None
    test_faceValue.addData('numberEntry_2.keys',numberEntry_2.keys)
    if numberEntry_2.keys != None:  # we had a response
        test_faceValue.addData('numberEntry_2.rt', numberEntry_2.rt)
    # the Routine "testHouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ActValueHouse"-------
    t = 0
    ActValueHouseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ActVal_2.setColor('white', colorSpace='rgb')
    ActVal_2.setText(houseValue
)
    ActVal_2.setPos((0, 0))
    ActVal_2.setFont('Helvetica')
    ActVal_2.setHeight(0.15)
    key_resp_14 = event.BuilderKeyResponse()
    youSaid_2.setText(inputText)
    # keep track of which components have finished
    ActValueHouseComponents = [ActVal_2, key_resp_14, continue3_2, ActualValueText_2, youSaid_2]
    for thisComponent in ActValueHouseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ActValueHouse"-------
    while continueRoutine:
        # get current time
        t = ActValueHouseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ActVal_2* updates
        if t >= 0.2 and ActVal_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ActVal_2.tStart = t
            ActVal_2.frameNStart = frameN  # exact frame index
            ActVal_2.setAutoDraw(True)
        
        # *key_resp_14* updates
        if t >= 0.5 and key_resp_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_14.tStart = t
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_14.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_14.keys = theseKeys[-1]  # just the last key pressed
                key_resp_14.rt = key_resp_14.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *continue3_2* updates
        if t >= 0.5 and continue3_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            continue3_2.tStart = t
            continue3_2.frameNStart = frameN  # exact frame index
            continue3_2.setAutoDraw(True)
        
        # *ActualValueText_2* updates
        if t >= 0.2 and ActualValueText_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ActualValueText_2.tStart = t
            ActualValueText_2.frameNStart = frameN  # exact frame index
            ActualValueText_2.setAutoDraw(True)
        
        # *youSaid_2* updates
        if t >= 1 and youSaid_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            youSaid_2.tStart = t
            youSaid_2.frameNStart = frameN  # exact frame index
            youSaid_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ActValueHouseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ActValueHouse"-------
    for thisComponent in ActValueHouseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys=None
    test_faceValue.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        test_faceValue.addData('key_resp_14.rt', key_resp_14.rt)
    # the Routine "ActValueHouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'test_faceValue'


# ------Prepare to start Routine "Congrats"-------
t = 0
CongratsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()
# keep track of which components have finished
CongratsComponents = [to_continue_5, Part1Learn_3, key_resp_15, minScore_4]
for thisComponent in CongratsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Congrats"-------
while continueRoutine:
    # get current time
    t = CongratsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *to_continue_5* updates
    if t >= 0.2 and to_continue_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        to_continue_5.tStart = t
        to_continue_5.frameNStart = frameN  # exact frame index
        to_continue_5.setAutoDraw(True)
    
    # *Part1Learn_3* updates
    if t >= 0.2 and Part1Learn_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Part1Learn_3.tStart = t
        Part1Learn_3.frameNStart = frameN  # exact frame index
        Part1Learn_3.setAutoDraw(True)
    
    # *key_resp_15* updates
    if t >= 0.2 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_15.keys = theseKeys[-1]  # just the last key pressed
            key_resp_15.rt = key_resp_15.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *minScore_4* updates
    if t >= 0.5 and minScore_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        minScore_4.tStart = t
        minScore_4.frameNStart = frameN  # exact frame index
        minScore_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CongratsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Congrats"-------
for thisComponent in CongratsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys=None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.nextEntry()
# the Routine "Congrats" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
