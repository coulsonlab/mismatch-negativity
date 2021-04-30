#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on April 23, 2021, at 00:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
from generate_intensity_mismatch import generate_intensity_mismatch
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'MMN_test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Winnie Xu\\Desktop\\Coulson Lab\\MMN_test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# Generate random ordering of sound events (varaition of intensity levels)
stand40_5000 = [(40, 5000), (40, 5000), (40, 5000), (40, 5000)]
dev40_5000 = (40, 5000)
stand45_5000 = [(45, 5000), (45, 5000), (45, 5000), (45, 5000)]
dev45_5000 = (45, 5000)
stand50_5000 = [(50, 5000), (50, 5000), (50, 5000), (50, 5000)]
dev50_5000 = (50, 5000)
stand55_5000 = [(55, 5000), (55, 5000), (55, 5000), (55, 5000)]
dev55_5000 = (55, 5000)
stand60_5000 = [(60, 5000), (60, 5000), (60, 5000), (60, 5000)]
dev60_5000 = (60, 5000)

stand40_10000 = [(40, 10000), (40, 10000), (40, 10000), (40, 10000)]
dev40_10000 = (40, 10000)
stand45_10000 = [(45, 10000), (45, 10000), (45, 10000), (45, 10000)]
dev45_10000 = (45, 10000)
stand50_10000 = [(50, 10000), (50, 10000), (50, 10000), (50, 10000)]
dev50_5000 = (50, 10000)
stand55_5000 = [(55, 10000), (55, 10000), (55, 10000), (55, 10000)]
dev55_5000 = (55, 10000)
stand60_5000 = [(60, 10000), (60, 10000), (60, 10000), (60, 10000)]
dev60_5000 = (60, 10000)

num_events = 50

#Tentative, may change depending on the actual design of the experiment
if expInfo['participant'] == '5000Hz':
    #sequence = generate_frequency_mismatch([stand40_5000, stand45_5000, stand50_5000, stand55_5000, stand60_5000], [dev40_5000, dev45_5000, dev50_5000, dev55_5000, dev60_5000], num_events)
    sequence = generate_intensity_mismatch(stand40_5000, dev40_5000, num_events)
elif expInfo['participant'] == '10000Hz':
    sequence = generate_intensity_mismatch([stand40_10000, stand45_10000, stand50_10000, stand55_10000, stand60_10000], [dev40_10000, dev45_10000, dev50_10000, dev55_10000, dev60_10000], num_events)
else:
    sequence = None

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=250.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=sequence,
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    sound_1.setSound(freq, secs=0.1, hamming=True)
    sound_1.setVolume(1.0, log=False)
    # keep track of which components have finished
    trialComponents = [image, sound_1]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStart)
    trials.addData('sound_1.stopped', sound_1.tStop)
    thisExp.nextEntry()
    
# completed 250.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
