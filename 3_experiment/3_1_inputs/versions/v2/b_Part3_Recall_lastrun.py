#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on January 31, 2018, at 16:16
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
    originPath=u'C:\\Users\\lab\\Dropbox\\LabSharedFolder\\MADE01\\CODE\\v3_FractionalWeights\\b_Part3_Recall.psyexp',
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

# Initialize components for Routine "Part_1"
Part_1Clock = core.Clock()
to_continue = visual.TextStim(win=win, name='to_continue',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text='Recall Values',
    font='Helvetica',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
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
face_list = sorted(glob.glob('images/morphs/face/*.jpg'))
house_list = sorted(glob.glob('images/morphs/house/*.jpg'))


# create values to match to stimuli
values = np.arange(-1.,1.01,0.02)
# REVERSE values
values = values * -1

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

# Initialize components for Routine "PreTestScreen"
PreTestScreenClock = core.Clock()
to_continue_2 = visual.TextStim(win=win, name='to_continue_2',
    text='press any key to continue',
    font='Helvetica',
    pos=(0, -0.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part1Test = visual.TextStim(win=win, name='Part1Test',
    text='Recall Values',
    font='Helvetica',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
Fifty_estimates = visual.TextStim(win=win, name='Fifty_estimates',
    text='You will now be randomly shown a series of 50 faces and houses.\n\nPlease fill in your best estimate of the exact value of each.',
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
nRepsCorrect = 0
# randFace = random.randint(1,100)
# trialFace = "images/morphs/faceMorph" + str(randFace) + ".jpg"

# randHouse = 0


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
    text="after you enter a value press 'Enter'",
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
    text='Use the format X.XX (e.g. -0.50)',
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
    text='You have completed the main experiment.\n\nYou will now complete a few short tests and questionnaires.\n\nPlease let the RA know that you are finished.',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Part1Complete"
Part1CompleteClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Please let the RA or experimenter know\nthat you are ready to begin the next part of the study.',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part2 = visual.TextStim(win=win, name='Part2',
    text='Stop',
    font='Arial',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Fail"
FailClock = core.Clock()
instructions_4 = visual.TextStim(win=win, name='instructions_4',
    text='Your average error is above the \nbaseline for continuing in the task.\n\nPlease let the RA or experimenter\nknow that you have completed Part 1.',
    font='Helvetica',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Part2_2 = visual.TextStim(win=win, name='Part2_2',
    text='Part 1 Complete',
    font='Arial',
    pos=(0, 0.6), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
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

# the Routine "Part_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PreTestScreen"-------
t = 0
PreTestScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
PreTestScreenComponents = [to_continue_2, Part1Test, key_resp_8, Fifty_estimates]
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
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *Fifty_estimates* updates
    if t >= 0.5 and Fifty_estimates.status == NOT_STARTED:
        # keep track of start time/frame for later
        Fifty_estimates.tStart = t
        Fifty_estimates.frameNStart = frameN  # exact frame index
        Fifty_estimates.setAutoDraw(True)
    
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
# the Routine "PreTestScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_faceValue = data.TrialHandler(nReps=25, method='random', 
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
    
    trialFace = face_df.exemplar[randFace]
    trialHouse = house_df.exemplar[randHouse]
    
    actFaceVal = face_df.value[randFace]
    actHouseVal = house_df.value[randHouse]
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
    error = abs(float(inputText) - actFaceVal)
    totalError = totalError+error
    avgError = totalError/testNumber
    
    #let's store the final text string into the results final...
    thisExp.addData('inputText', inputText)
    thisExp.addData('face_value', actFaceVal)
    thisExp.addData('error', error)
    
    
    inputText=""
    
    # check responses
    if numberEntry.keys in ['', [], None]:  # No response was made
        numberEntry.keys=None
    test_faceValue.addData('numberEntry.keys',numberEntry.keys)
    if numberEntry.keys != None:  # we had a response
        test_faceValue.addData('numberEntry.rt', numberEntry.rt)
    # the Routine "Test" was not non-slip safe, so reset the non-slip timer
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
    error = abs(float(inputText) - actHouseVal)
    totalError = totalError+error
    avgError = totalError/testNumber
    
    #let's store the final text string into the results final...
    thisExp.addData('inputText', inputText)
    thisExp.addData('house_value', actHouseVal)
    thisExp.addData('error', error)
    
    inputText=""
    
    if testNumber>=50:
        nRepsCorrect = 1
        test_faceValue.finished=1
    # check responses
    if numberEntry_2.keys in ['', [], None]:  # No response was made
        numberEntry_2.keys=None
    test_faceValue.addData('numberEntry_2.keys',numberEntry_2.keys)
    if numberEntry_2.keys != None:  # we had a response
        test_faceValue.addData('numberEntry_2.rt', numberEntry_2.rt)
    # the Routine "testHouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 25 repeats of 'test_faceValue'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=nRepsCorrect, method='random', 
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
    trials_2.addData('key_resp_15.keys',key_resp_15.keys)
    if key_resp_15.keys != None:  # we had a response
        trials_2.addData('key_resp_15.rt', key_resp_15.rt)
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
    thisExp.nextEntry()
    
# completed nRepsCorrect repeats of 'trials_2'


# ------Prepare to start Routine "Fail"-------
t = 0
FailClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
FailComponents = [instructions_4, Part2_2]
for thisComponent in FailComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fail"-------
while continueRoutine:
    # get current time
    t = FailClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_4* updates
    if t >= 0.0 and instructions_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_4.tStart = t
        instructions_4.frameNStart = frameN  # exact frame index
        instructions_4.setAutoDraw(True)
    
    # *Part2_2* updates
    if t >= 0.0 and Part2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Part2_2.tStart = t
        Part2_2.frameNStart = frameN  # exact frame index
        Part2_2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FailComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fail"-------
for thisComponent in FailComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Fail" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
