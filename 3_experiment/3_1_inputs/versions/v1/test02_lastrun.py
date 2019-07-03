#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on March 13, 2017, at 13:36
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
expName = 'test02'  # from the Builder filename that created this script
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
    originPath=u'C:\\Users\\labadmin\\Dropbox\\LabSharedFolder\\DJW_PilotData\\20170130\\test02.psyexp',
    savePickle=True, saveWideText=True,
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
    image='images/morphs/faceMorph1.jpg', mask=None,
    ori=0, pos=(0, 0), size=[360,360],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='If you see this face that means you will win $1.00.',
    font='Helvetica',
    pos=(0, .80), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
continueKey = visual.TextStim(win=win, name='continueKey',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "var_01_Instr_02"
var_01_Instr_02Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='images/morphs/faceMorph100.jpg', mask=None,
    ori=0, pos=(0, 0), size=[360,360],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='If you see this face that means you will lose $1.00.',
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
    image='images/morphs/faceMorph100.jpg', mask=None,
    ori=0, pos=(300, 0), size=[250,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='Blends of the two faces will give corresponding values.',
    font='Helvetica',
    pos=(0, .7), height=0.1, wrapWidth=None, ori=0, 
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
    image='images/morphs/faceMorph1.jpg', mask=None,
    ori=0, pos=(-300, 0), size=(250,250),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
man_morph50 = visual.ImageStim(
    win=win, name='man_morph50',units='pix', 
    image='images/morphs/faceMorph50.jpg', mask=None,
    ori=0, pos=(0, 0), size=(250,250),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='$1.00',
    font='Helvetica',
    pos=(-0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
minus5 = visual.TextStim(win=win, name='minus5',
    text='-$1.00',
    font='Helvetica',
    pos=(0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
zeroDollar = visual.TextStim(win=win, name='zeroDollar',
    text='$0.00',
    font='Helvetica',
    pos=(0, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Initialize components for Routine "houseLearnInstr"
houseLearnInstrClock = core.Clock()
House01 = visual.ImageStim(
    win=win, name='House01',units='pix', 
    image='images/morphs/houseMorph100.jpg', mask=None,
    ori=0, pos=(300, 0), size=[250,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Similarly, blends of houses are also valued depending on the amount of each house in the blend.',
    font='Helvetica',
    pos=(0, .70), height=0.1, wrapWidth=None, ori=0, 
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
    image='images/morphs/houseMorph1.jpg', mask=None,
    ori=0, pos=(-300, 0), size=[250,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
man_morph50_2 = visual.ImageStim(
    win=win, name='man_morph50_2',units='pix', 
    image='images/morphs/houseMorph49.jpg', mask=None,
    ori=0, pos=(0, 0), size=[250,250],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='$1.00',
    font='Helvetica',
    pos=(-0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
minus5_2 = visual.TextStim(win=win, name='minus5_2',
    text='-$1.00',
    font='Helvetica',
    pos=(0.5, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
zeroDollar_2 = visual.TextStim(win=win, name='zeroDollar_2',
    text='$0.00',
    font='Helvetica',
    pos=(0, -0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);

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
    text='You will now guess the value of images of houses and faces that have been combined to varying degrees.\n\nYou need to acheive an average answer that is within $0.20 of the actual value over the course of 20 trials.\n\nDo not worry - if you do not succeed your will simply repeat the test (you have 5 chances).\n',
    font='Arial',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Test"
TestClock = core.Clock()
import random

inputText = ""

testNumber = 0
totalError = 0
avgError = 0
actualValue = 0
error = 0
roundNumber = 1

randFace = random.randint(1,100)
trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"

randHouse = 0


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
    text='Use the format X.XX (e.g. 0.50)',
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
RoundNumber = visual.TextStim(win=win, name='RoundNumber',
    text='default text',
    font='helvetica',
    pos=(-0.75, 0.85), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-9.0);

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
    text='Actual value was:',
    font='Helvetica',
    pos=(0, .2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
youSaid = visual.TextStim(win=win, name='youSaid',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
AvgError = visual.TextStim(win=win, name='AvgError',
    text='default text',
    font='Helvetica',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0);
RoundNumber_b = visual.TextStim(win=win, name='RoundNumber_b',
    text='default text',
    font='Helvetica',
    pos=(-0.75, 0.85), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0);

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
    ori=0, pos=(0, 0), size=(480, 480),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
useFormat_2 = visual.TextStim(win=win, name='useFormat_2',
    text='Use the format X.XX (e.g. 0.50)',
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
RoundNumber_c = visual.TextStim(win=win, name='RoundNumber_c',
    text='default text',
    font='Helvetica',
    pos=(-0.75, 0.85), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-9.0);

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
avgError2 = visual.TextStim(win=win, name='avgError2',
    text='default text',
    font='Helvetica',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0);

roundNumber_d = visual.TextStim(win=win, name='roundNumber_d',
    text='default text',
    font='Arial',
    pos=(-0.75, 0.85), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0);

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

# Initialize components for Routine "Part1Complete"
Part1CompleteClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Please let the RA or experimenter know\nthat you have completed Part 1.\n\nThey will start Part 2 for you.',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part2 = visual.TextStim(win=win, name='Part2',
    text='Part 2: Test',
    font='Arial',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
routine_01_Instr01Components = [image, text_2, key_resp_4, continueKey]
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
    
    # *continueKey* updates
    if t >= 0.0 and continueKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        continueKey.tStart = t
        continueKey.frameNStart = frameN  # exact frame index
        continueKey.setAutoDraw(True)
    
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
    if t >= 2.5 and key_resp_7.status == NOT_STARTED:
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
    if t >= 2.5 and text_7.status == NOT_STARTED:
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
    if t >= 2 and man_morph50.status == NOT_STARTED:
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
    if t >= 2 and zeroDollar.status == NOT_STARTED:
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
    if t >= 2.5 and key_resp_11.status == NOT_STARTED:
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
    if t >= 2.5 and continue9.status == NOT_STARTED:
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
    if t >= 2 and man_morph50_2.status == NOT_STARTED:
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
    if t >= 2 and zeroDollar_2.status == NOT_STARTED:
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
    if t >= 0.5 and to_continue_2.status == NOT_STARTED:
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
    if t >= 0.5 and key_resp_8.status == NOT_STARTED:
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
    
    testNumber+=1
    
    randFace = random.randint(1,100)
    randHouse = random.randint(1,100)
    
    trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"
    trialHouse = "images/morphs/houseMorph" + str(randHouse) + ".jpg"
    
    actFaceVal = 1.00 - (2*randFace/100) 
    actHouseVal = 1.00 - (2*randHouse/100) 
    numberEntry = event.BuilderKeyResponse()
    square_entry.setOpacity(1)
    square_entry.setPos((0, -.75))
    square_entry.setLineWidth(1)
    square_entry.setOri(0)
    square_entry.setSize((0.25, 0.15))
    faces.setImage(trialFace)
    RoundNumber.setText(("Round %i" % roundNumber))
    # keep track of which components have finished
    TestComponents = [numberEntry, square_entry, EnterValue, nextTrialTest, inputTextValue, faces, useFormat, Fixation, RoundNumber]
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
        
        # *RoundNumber* updates
        if t >= 0.5 and RoundNumber.status == NOT_STARTED:
            # keep track of start time/frame for later
            RoundNumber.tStart = t
            RoundNumber.frameNStart = frameN  # exact frame index
            RoundNumber.setAutoDraw(True)
        
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
    
    error = abs(float(inputText) - actFaceVal)
    totalError = totalError+error
    avgError = totalError/testNumber
    
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
    ActVal.setColor('white', colorSpace='rgb')
    ActVal.setText(("$%0.2f" % actFaceVal)
)
    ActVal.setPos((0, 0))
    ActVal.setFont('Helvetica')
    ActVal.setHeight(0.15)
    key_resp_10 = event.BuilderKeyResponse()
    youSaid.setText(inputText)
    AvgError.setText(("Average error: $%0.2f" % avgError))
    RoundNumber_b.setText(("Round %i" % roundNumber))
    # keep track of which components have finished
    ActualValueComponents = [ActVal, key_resp_10, continue3, ActualValueText, youSaid, AvgError, RoundNumber_b]
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
        
        # *AvgError* updates
        if t >= 0.2 and AvgError.status == NOT_STARTED:
            # keep track of start time/frame for later
            AvgError.tStart = t
            AvgError.frameNStart = frameN  # exact frame index
            AvgError.setAutoDraw(True)
        
        # *RoundNumber_b* updates
        if t >= 0.2 and RoundNumber_b.status == NOT_STARTED:
            # keep track of start time/frame for later
            RoundNumber_b.tStart = t
            RoundNumber_b.frameNStart = frameN  # exact frame index
            RoundNumber_b.setAutoDraw(True)
        
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
    
    testNumber+=1
    actualValue = houseValue
    
    numberEntry_2 = event.BuilderKeyResponse()
    square_entry_2.setOpacity(1)
    square_entry_2.setPos((0, -.75))
    square_entry_2.setLineWidth(1)
    square_entry_2.setOri(0)
    square_entry_2.setSize((0.25, 0.15))
    houses.setImage(trialHouse)
    RoundNumber_c.setText(("Round %i" % roundNumber))
    # keep track of which components have finished
    testHouseComponents = [numberEntry_2, square_entry_2, EnterValue_2, nextTrialTest_2, inputTextValue_2, houses, useFormat_2, Fixation_2, RoundNumber_c]
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
        
        # *RoundNumber_c* updates
        if t >= 0.5 and RoundNumber_c.status == NOT_STARTED:
            # keep track of start time/frame for later
            RoundNumber_c.tStart = t
            RoundNumber_c.frameNStart = frameN  # exact frame index
            RoundNumber_c.setAutoDraw(True)
        
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
    
    error = abs(float(inputText) - actHouseVal)
    totalError = totalError+error
    avgError = totalError/testNumber
    
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
    ActVal_2.setText(("$%0.2f" % actHouseVal)
)
    ActVal_2.setPos((0, 0))
    ActVal_2.setFont('Helvetica')
    ActVal_2.setHeight(0.15)
    key_resp_14 = event.BuilderKeyResponse()
    youSaid_2.setText(inputText)
    avgError2.setText(("Average error: $%0.2f" % avgError))
    
    roundNumber_d.setText(("Round %i" % roundNumber))
    # keep track of which components have finished
    ActValueHouseComponents = [ActVal_2, key_resp_14, continue3_2, ActualValueText_2, youSaid_2, avgError2, roundNumber_d]
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
        
        # *avgError2* updates
        if t >= 0.0 and avgError2.status == NOT_STARTED:
            # keep track of start time/frame for later
            avgError2.tStart = t
            avgError2.frameNStart = frameN  # exact frame index
            avgError2.setAutoDraw(True)
        
        
        # *roundNumber_d* updates
        if t >= 0.2 and roundNumber_d.status == NOT_STARTED:
            # keep track of start time/frame for later
            roundNumber_d.tStart = t
            roundNumber_d.frameNStart = frameN  # exact frame index
            roundNumber_d.setAutoDraw(True)
        
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
    if testNumber>=20 and avgError<=0.20:
        test_faceValue.finished=1
    elif testNumber>=20 and avgError>0.20:
        testNumber = 0
        avgError = 0
        totalError = 0
        roundNumber +=1
    
    
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

# ------Prepare to start Routine "Part1Complete"-------
t = 0
Part1CompleteClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Part1CompleteComponents = [instructions, Part2]
for thisComponent in Part1CompleteComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Part1Complete"-------
while continueRoutine:
    # get current time
    t = Part1CompleteClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
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
    for thisComponent in Part1CompleteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Part1Complete"-------
for thisComponent in Part1CompleteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Part1Complete" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
