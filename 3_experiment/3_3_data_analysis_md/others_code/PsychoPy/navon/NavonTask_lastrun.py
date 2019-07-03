#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00),
    on Mon Oct 24 20:00:18 2016
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
expName = 'NavonTask'  # from the Builder filename that created this script
expInfo = {'participant':'', 'gender (m/f)':'', 'age':'', 'session':03}
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
    originPath=u'/Users/danieljwilson/Dropbox/PHD/CENDRI/Project/Code/PsychoPy/navon/NavonTask.psyexp',
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
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instrPractice"
instrPracticeClock = core.Clock()
instruct1 = visual.TextStim(win=win, name='instruct1',
    text="In this experiment you will be presented with a large letter made up of smaller letters. Your task is to\n\nRespond by pressing;\n - 'S' if the SMALL letters are S\n - 'H' if the SMALL letters are H\n\nTry to respond as quickly and as accurately as possible.\n\nThere will be a number of practice trials in which you will be given feedback. \n\nPress any key when you are ready to proceed.",
    font='Arial',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixate = visual.TextStim(win=win, name='fixate',
    text='+',
    font='Arial',
    units='cm', pos=[0, 0], height=2, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);
stimulus = visual.ImageStim(
    win=win, name='stimulus',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[200,200],
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mask = visual.ImageStim(
    win=win, name='mask',units='pix', 
    image='mask.png', mask=None,
    ori=0, pos=[0,0], size=[200,200],
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instrMain"
instrMainClock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text="OK, ready to start the main experiment?\n\nRemember, press;\n - 'S' if the SMALL letters are S\n - 'H' if the SMALL letters are H\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.",
    font='Arial',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixate = visual.TextStim(win=win, name='fixate',
    text='+',
    font='Arial',
    units='cm', pos=[0, 0], height=2, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);
stimulus = visual.ImageStim(
    win=win, name='stimulus',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[200,200],
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mask = visual.ImageStim(
    win=win, name='mask',units='pix', 
    image='mask.png', mask=None,
    ori=0, pos=[0,0], size=[200,200],
    color='white', colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksMsg = visual.TextStim(win=win, name='thanksMsg',
    text="You're done! Fun, wasn't it!? ;-)",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instrPractice"-------
t = 0
instrPracticeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ok1 = event.BuilderKeyResponse()
# keep track of which components have finished
instrPracticeComponents = [instruct1, ok1]
for thisComponent in instrPracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instrPractice"-------
while continueRoutine:
    # get current time
    t = instrPracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct1* updates
    if t >= 0.0 and instruct1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct1.tStart = t
        instruct1.frameNStart = frameN  # exact frame index
        instruct1.setAutoDraw(True)
    
    # *ok1* updates
    if t >= 0.0 and ok1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ok1.tStart = t
        ok1.frameNStart = frameN  # exact frame index
        ok1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ok1.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ok1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ok1.keys = theseKeys[-1]  # just the last key pressed
            ok1.rt = ok1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrPractice"-------
for thisComponent in instrPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ok1.keys in ['', [], None]:  # No response was made
    ok1.keys=None
thisExp.addData('ok1.keys',ok1.keys)
if ok1.keys != None:  # we had a response
    thisExp.addData('ok1.rt', ok1.rt)
thisExp.nextEntry()
# the Routine "instrPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='practiceTrials')
thisExp.addLoop(practiceTrials)  # add the loop to the experiment
thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial.keys():
        exec(paramName + '= thisPracticeTrial.' + paramName)

for thisPracticeTrial in practiceTrials:
    currentLoop = practiceTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial.keys():
            exec(paramName + '= thisPracticeTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    stimulus.setPos([xPos, yPos])
    stimulus.setImage(stimFile)
    mask.setPos([xPos, yPos])
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [fixate, stimulus, mask, resp]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixate* updates
        if t >= 1.0 and fixate.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixate.tStart = t
            fixate.frameNStart = frameN  # exact frame index
            fixate.setAutoDraw(True)
        frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixate.status == STARTED and t >= frameRemains:
            fixate.setAutoDraw(False)
        
        # *stimulus* updates
        if t >= 2.0 and stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulus.tStart = t
            stimulus.frameNStart = frameN  # exact frame index
            stimulus.setAutoDraw(True)
        frameRemains = 2.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stimulus.status == STARTED and t >= frameRemains:
            stimulus.setAutoDraw(False)
        
        # *mask* updates
        if t >= 2.2 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t
            mask.frameNStart = frameN  # exact frame index
            mask.setAutoDraw(True)
        frameRemains = 2.2 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if mask.status == STARTED and t >= frameRemains:
            mask.setAutoDraw(False)
        
        # *resp* updates
        if t >= 2.0 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.0 + 7.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'h'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    # store data for practiceTrials (TrialHandler)
    practiceTrials.addData('resp.keys',resp.keys)
    practiceTrials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        practiceTrials.addData('resp.rt', resp.rt)
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! That was wrong"
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_2* updates
        if t >= 0.0 and feedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_2.tStart = t
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_2.status == STARTED and t >= frameRemains:
            feedback_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practiceTrials'

# get names of stimulus parameters
if practiceTrials.trialList in ([], [None], None):
    params = []
else:
    params = practiceTrials.trialList[0].keys()
# save data for this loop
practiceTrials.saveAsExcel(filename + '.xlsx', sheetName='practiceTrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instrMain"-------
t = 0
instrMainClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ok2 = event.BuilderKeyResponse()
# keep track of which components have finished
instrMainComponents = [instr2, ok2]
for thisComponent in instrMainComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instrMain"-------
while continueRoutine:
    # get current time
    t = instrMainClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if t >= 0.0 and instr2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2.tStart = t
        instr2.frameNStart = frameN  # exact frame index
        instr2.setAutoDraw(True)
    
    # *ok2* updates
    if t >= 0.0 and ok2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ok2.tStart = t
        ok2.frameNStart = frameN  # exact frame index
        ok2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ok2.status == STARTED:
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
    for thisComponent in instrMainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrMain"-------
for thisComponent in instrMainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instrMain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
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
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    stimulus.setPos([xPos, yPos])
    stimulus.setImage(stimFile)
    mask.setPos([xPos, yPos])
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [fixate, stimulus, mask, resp]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixate* updates
        if t >= 1.0 and fixate.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixate.tStart = t
            fixate.frameNStart = frameN  # exact frame index
            fixate.setAutoDraw(True)
        frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixate.status == STARTED and t >= frameRemains:
            fixate.setAutoDraw(False)
        
        # *stimulus* updates
        if t >= 2.0 and stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimulus.tStart = t
            stimulus.frameNStart = frameN  # exact frame index
            stimulus.setAutoDraw(True)
        frameRemains = 2.0 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stimulus.status == STARTED and t >= frameRemains:
            stimulus.setAutoDraw(False)
        
        # *mask* updates
        if t >= 2.2 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t
            mask.frameNStart = frameN  # exact frame index
            mask.setAutoDraw(True)
        frameRemains = 2.2 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if mask.status == STARTED and t >= frameRemains:
            mask.setAutoDraw(False)
        
        # *resp* updates
        if t >= 2.0 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.0 + 7.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'h'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksMsg]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksMsg* updates
    if t >= 0.0 and thanksMsg.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksMsg.tStart = t
        thanksMsg.frameNStart = frameN  # exact frame index
        thanksMsg.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksMsg.status == STARTED and t >= frameRemains:
        thanksMsg.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
