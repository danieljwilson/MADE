#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.71.01),
    on Mon Oct 24 19:59:59 2016
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
expName = u'branching'  # from the Builder filename that created this script
expInfo = {'participant':'ID01', 'session':001}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/danieljwilson/Dropbox/PHD/CENDRI/Project/Code/PsychoPy/branchedExp/branching.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
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

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text="If you press 'a' you'll get 3 trials of Routine A\n\nIf you press 'b' you'll get 3 trials of Routine B",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "A"
AClock = core.Clock()
msgA = visual.TextStim(win=win, name='msgA',
    text='You chose A (the blue pill?)',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "B"
BClock = core.Clock()
msgB = visual.TextStim(win=win, name='msgB',
    text='You chose B (the red pill?)',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp = event.BuilderKeyResponse()

# keep track of which components have finished
instrComponents = [instrText, resp]
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *resp* updates
    if t >= 0.0 and resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp.tStart = t
        resp.frameNStart = frameN  # exact frame index
        resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['a', 'b'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            resp.keys = theseKeys[-1]  # just the last key pressed
            resp.rt = resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp.keys in ['', [], None]:  # No response was made
    resp.keys=None
thisExp.addData('resp.keys',resp.keys)
if resp.keys != None:  # we had a response
    thisExp.addData('resp.rt', resp.rt)
thisExp.nextEntry()
if resp.keys=='a':
    nRepsA=1
    nRepsB=0
else:
    nRepsA=0
    nRepsB=1

# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repsA = data.TrialHandler(nReps=nRepsA, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='repsA')
thisExp.addLoop(repsA)  # add the loop to the experiment
thisRepsA = repsA.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepsA.rgb)
if thisRepsA != None:
    for paramName in thisRepsA.keys():
        exec(paramName + '= thisRepsA.' + paramName)

for thisRepsA in repsA:
    currentLoop = repsA
    # abbreviate parameter names if possible (e.g. rgb = thisRepsA.rgb)
    if thisRepsA != None:
        for paramName in thisRepsA.keys():
            exec(paramName + '= thisRepsA.' + paramName)
    
    # ------Prepare to start Routine "A"-------
    t = 0
    AClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    msgA.setColor(letterColor, colorSpace='rgb')
    # keep track of which components have finished
    AComponents = [msgA]
    for thisComponent in AComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "A"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *msgA* updates
        if t >= 0.0 and msgA.status == NOT_STARTED:
            # keep track of start time/frame for later
            msgA.tStart = t
            msgA.frameNStart = frameN  # exact frame index
            msgA.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if msgA.status == STARTED and t >= frameRemains:
            msgA.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "A"-------
    for thisComponent in AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed nRepsA repeats of 'repsA'

# get names of stimulus parameters
if repsA.trialList in ([], [None], None):
    params = []
else:
    params = repsA.trialList[0].keys()
# save data for this loop
repsA.saveAsExcel(filename + '.xlsx', sheetName='repsA',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
repsB = data.TrialHandler(nReps=nRepsB, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='repsB')
thisExp.addLoop(repsB)  # add the loop to the experiment
thisRepsB = repsB.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepsB.rgb)
if thisRepsB != None:
    for paramName in thisRepsB.keys():
        exec(paramName + '= thisRepsB.' + paramName)

for thisRepsB in repsB:
    currentLoop = repsB
    # abbreviate parameter names if possible (e.g. rgb = thisRepsB.rgb)
    if thisRepsB != None:
        for paramName in thisRepsB.keys():
            exec(paramName + '= thisRepsB.' + paramName)
    
    # ------Prepare to start Routine "B"-------
    t = 0
    BClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    msgB.setColor(letterColor, colorSpace='rgb')
    # keep track of which components have finished
    BComponents = [msgB]
    for thisComponent in BComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "B"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *msgB* updates
        if t >= 0.0 and msgB.status == NOT_STARTED:
            # keep track of start time/frame for later
            msgB.tStart = t
            msgB.frameNStart = frameN  # exact frame index
            msgB.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if msgB.status == STARTED and t >= frameRemains:
            msgB.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B"-------
    for thisComponent in BComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed nRepsB repeats of 'repsB'

# get names of stimulus parameters
if repsB.trialList in ([], [None], None):
    params = []
else:
    params = repsB.trialList[0].keys()
# save data for this loop
repsB.saveAsExcel(filename + '.xlsx', sheetName='repsB',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
