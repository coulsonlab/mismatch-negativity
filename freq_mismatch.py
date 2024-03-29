#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on April 19, 2021, at 16:23
If you publish work using this script the most relevant publication is:
    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
from freq_sequence_generation import generate_pattern_mismatch


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'pattern_mismatch'  # from the Builder filename that created this script
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
    originPath='D:\\Code\\mismatch_negativity\\pattern_mismatch.py',
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

if expInfo['participant'] == 'higher':
    title_text = 'TEST\n\nPattern mismatch experiment\n\nHigher/Louder'
elif expInfo['participant'] == 'lower':
    title_text = 'TEST\n\nPattern mismatch experiment\n\nLower/Louder'
else:
    title_text = 'TEST\n\nPattern mismatch experiment\n\nNo mode specified'

# Initialize components for Routine "title"
titleClock = core.Clock()
textbox = visual.TextBox2(
     win, text=title_text, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)

# Initialize components for Routine "sound_event"
sound_eventClock = core.Clock()
sound_1 = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_1', sampleRate=44100)
sound_1.setVolume(1.0)
test_A = visual.TextStim(win=win, name='test_A',
    text='100ms A\n\n400ms N/A',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "title"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
titleComponents = [textbox]
for thisComponent in titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    if textbox.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textbox.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            textbox.tStop = t  # not accounting for scr refresh
            textbox.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textbox, 'tStopRefresh')  # time at next scr refresh
            textbox.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "title"-------
for thisComponent in titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox.text',textbox.text)
textbox.reset()
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)

# Generate random ordering of sound events
# Freq mismatch for 60 db tones
Condition_A_sixty = [(60, 2000), (60, 2000), (60, 2000), (60, 2000)]
Condition_A_sixty_deviant = (60, 1000)
Condition_A_prime_sixty = [(60, 1000), (60, 1000), (60, 1000), (60, 1000)]
Condition_A_prime_sixty_deviant = (60, 2000)
Condition_B_sixty = [(60, 3000), (60, 3000), (60, 3000), (60, 3000)]
Condition_B_sixty_deviant = (60, 1000)
Condition_B_prime_sixty = [(60, 1000), (60, 1000), (60, 1000), (60, 1000)]
Condition_B_prime_sixty_deviant = (60, 3000)
Condition_C_sixty = [(60, 4000), (60, 4000), (60, 4000), (60, 4000)]
Condition_C_sixty_deviant = (60, 1000)
Condition_C_prime_sixty = [(60, 1000), (60, 1000), (60, 1000), (60, 1000)]
Condition_C_prime_sixty_deviant = (60, 4000)
Condition_D_sixty = [(60, 5000), (60, 5000), (60, 5000), (60, 5000)]
Condition_D_sixty_deviant = (60, 1000)
Condition_D_prime_sixty = [(60, 1000), (60, 1000), (60, 1000), (60, 1000)]
Condition_D_prime_sixty_deviant = (60, 5000)
Condition_E_sixty = [(60, 2000), (60, 2000), (60, 2000), (60, 2000)]
Condition_E_sixty_deviant = (60, 5000)
Condition_E_prime_sixty = [(60, 5000), (60, 5000), (60, 5000), (60, 5000)]
Condition_E_prime_sixty_deviant = (60, 2000)
Condition_F_sixty = [(60, 3000), (60, 3000), (60, 3000), (60, 3000)]
Condition_F_sixty_deviant = (60, 5000)
Condition_F_prime_sixty = [(60, 5000), (60, 5000), (60, 5000), (60, 5000)]
Condition_F_prime_sixty_deviant = (60, 3000)
Condition_G_sixty = [(60, 4000), (60, 4000), (60, 4000), (60, 4000)]
Condition_G_sixty_deviant = (60, 5000)
Condition_G_prime_sixty = [(60, 5000), (60, 5000), (60, 5000), (60, 5000)]
Condition_G_prime_sixty_deviant = (60, 4000)
# Freq mismatch for 40 db tones
Condition_A_forty = [(40, 2000), (40, 2000), (40, 2000), (40, 2000)]
Condition_A_forty_deviant = (40, 1000)
Condition_A_prime_forty = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]
Condition_A_prime_forty_deviant = (40, 2000)
Condition_B_forty = [(40, 3000), (40, 3000), (40, 3000), (40, 3000)]
Condition_B_forty_deviant = (40, 1000)
Condition_B_prime_forty = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]
Condition_B_prime_forty_deviant = (40, 3000)
Condition_C_forty = [(40, 4000), (40, 4000), (40, 4000), (40, 4000)]
Condition_C_forty_deviant = (40, 1000)
Condition_C_prime_forty = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]
Condition_C_prime_forty_deviant = (40, 4000)
Condition_D_forty = [(40, 5000), (40, 5000), (40, 5000), (40, 5000)]
Condition_D_forty_deviant = (40, 1000)
Condition_D_prime_forty = [(40, 1000), (40, 1000), (40, 1000), (40, 1000)]
Condition_D_prime_forty_deviant = (40, 5000)
Condition_E_forty = [(40, 2000), (40, 2000), (40, 2000), (40, 2000)]
Condition_E_forty_deviant = (40, 5000)
Condition_E_prime_forty = [(40, 5000), (40, 5000), (40, 5000), (40, 5000)]
Condition_E_prime_forty_deviant = (40, 2000)
Condition_F_forty = [(40, 3000), (40, 3000), (40, 3000), (40, 3000)]
Condition_F_forty_deviant = (40, 5000)
Condition_F_prime_forty = [(40, 5000), (40, 5000), (40, 5000), (40, 5000)]
Condition_F_prime_forty_deviant = (40, 3000)
Condition_G_forty = [(40, 4000), (40, 4000), (40, 4000), (40, 4000)]
Condition_G_forty_deviant = (40, 5000)
Condition_G_prime_forty = [(40, 5000), (40, 5000), (40, 5000), (40, 5000)]
Condition_G_prime_forty_deviant = (40, 4000)
num_events = 50

#60
if expInfo['participant'] == 'A 60':
    sequence = generate_frequency_mismatch(Condition_A_sixty, Condition_A_sixty_deviant, num_events)
elif expInfo['participant'] == 'A prime 60':
    sequence = generate_frequency_mismatch(Condition_A_prime_sixty, Condition_A_prime_sixty_deviant, num_events)
elif expInfo['participant'] == 'B 60':
    sequence = generate_frequency_mismatch(Condition_B_sixty, Condition_B_sixty_deviant, num_events)
elif expInfo['participant'] == 'B prime 60':
    sequence = generate_frequency_mismatch(Condition_B_prime_sixty, Condition_B_prime_sixty_deviant, num_events)
elif expInfo['participant'] == 'C 60':
    sequence = generate_frequency_mismatch(Condition_C_sixty, Condition_C_sixty_deviant, num_events)
elif expInfo['participant'] == 'C prime 60':
    sequence = generate_frequency_mismatch(Condition_C_prime_sixty, Condition_C_prime_sixty_deviant, num_events)
elif expInfo['participant'] == 'D 60':
    sequence = generate_frequency_mismatch(Condition_D_sixty, Condition_D_sixty_deviant, num_events)
elif expInfo['participant'] == 'D prime 60':
    sequence = generate_frequency_mismatch(Condition_D_prime_sixty, Condition_D_prime_sixty_deviant, num_events)
elif expInfo['participant'] == 'E 60':
    sequence = generate_frequency_mismatch(Condition_E_sixty, Condition_E_sixty_deviant, num_events)
elif expInfo['participant'] == 'E prime 60':
    sequence = generate_frequency_mismatch(Condition_E_prime_sixty, Condition_E_prime_sixty_deviant, num_events)
elif expInfo['participant'] == 'F 60':
    sequence = generate_frequency_mismatch(Condition_F_sixty, Condition_F_sixty_deviant, num_events)
elif expInfo['participant'] == 'F prime 60':
    sequence = generate_frequency_mismatch(Condition_F_prime_sixty, Condition_F_prime_sixty_deviant, num_events)
elif expInfo['participant'] == 'G 60':
    sequence = generate_frequency_mismatch(Condition_G_sixty, Condition_G_sixty_deviant, num_events)
elif expInfo['participant'] == 'G prime 60':
    sequence = generate_frequency_mismatch(Condition_G_prime_sixty, Condition_G_prime_sixty_deviant, num_events)
# 40
elif expInfo['participant'] == 'A 40':
    sequence = generate_frequency_mismatch(Condition_A_forty, Condition_A_forty_deviant, num_events)
elif expInfo['participant'] == 'A prime 40':
    sequence = generate_frequency_mismatch(Condition_A_prime_forty, Condition_A_prime_forty_deviant, num_events)
elif expInfo['participant'] == 'B 40':
    sequence = generate_frequency_mismatch(Condition_B_forty, Condition_B_forty_deviant, num_events)
elif expInfo['participant'] == 'B prime 40':
    sequence = generate_frequency_mismatch(Condition_B_prime_forty, Condition_B_prime_forty_deviant, num_events)
elif expInfo['participant'] == 'C 40':
    sequence = generate_frequency_mismatch(Condition_C_forty, Condition_C_forty_deviant, num_events)
elif expInfo['participant'] == 'C prime 40':
    sequence = generate_frequency_mismatch(Condition_C_prime_forty, Condition_C_prime_forty_deviant, num_events)
elif expInfo['participant'] == 'D 40':
    sequence = generate_frequency_mismatch(Condition_D_forty, Condition_D_forty_deviant, num_events)
elif expInfo['participant'] == 'D prime 40':
    sequence = generate_frequency_mismatch(Condition_D_prime_forty, Condition_D_prime_forty_deviant, num_events)
elif expInfo['participant'] == 'E 40':
    sequence = generate_frequency_mismatch(Condition_E_forty, Condition_E_forty_deviant, num_events)
elif expInfo['participant'] == 'E prime 40':
    sequence = generate_frequency_mismatch(Condition_E_prime_forty, Condition_E_prime_forty_deviant, num_events)
elif expInfo['participant'] == 'F 40':
    sequence = generate_frequency_mismatch(Condition_F_forty, Condition_F_forty_deviant, num_events)
elif expInfo['participant'] == 'F prime 40':
    sequence = generate_frequency_mismatch(Condition_F_prime_forty, Condition_F_prime_forty_deviant, num_events)
elif expInfo['participant'] == 'G 40':
    sequence = generate_frequency_mismatch(Condition_G_forty, Condition_G_forty_deviant, num_events)
elif expInfo['participant'] == 'G prime 40':
    sequence = generate_frequency_mismatch(Condition_G_prime_forty, Condition_G_prime_forty_deviant, num_events)
else:
    sequence = None

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=sequence,
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

trial_count = 0
for thisTrial in trials:
    trial_count += 1
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sound_event"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    sound_1.setSound(freq, secs=0.1, hamming=True)
    # source: https://discourse.psychopy.org/t/generating-sound/2325/2
    # we may need to change this formula depending on output hardware
    # not even sure if this converts properly tbh
    volume=((0.34/0.1)/(10**(111.8/20)))*(10**(vol/20))
    sound_1.setVolume(volume)
    
    # update test_A label
    text = 'event #%d\n\n%s\n\n100ms %ddB %dHz' % (trial_count, label, vol, freq)
    test_A.setText(text)
    
    # keep track of which components have finished
    sound_eventComponents = [sound_1, test_A]
    for thisComponent in sound_eventComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sound_eventClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sound_event"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sound_eventClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sound_eventClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # *test_A* updates
        if test_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_A.frameNStart = frameN  # exact frame index
            test_A.tStart = t  # local t and not account for scr refresh
            test_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_A, 'tStartRefresh')  # time at next scr refresh
            test_A.setAutoDraw(True)
        if test_A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_A.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                test_A.tStop = t  # not accounting for scr refresh
                test_A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test_A, 'tStopRefresh')  # time at next scr refresh
                test_A.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_eventComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sound_event"-------
    for thisComponent in sound_eventComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStartRefresh)
    trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    trials.addData('test_A.started', test_A.tStartRefresh)
    trials.addData('test_A.stopped', test_A.tStopRefresh)
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