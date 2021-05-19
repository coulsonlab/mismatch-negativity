@@ -0,0 +1,109 @@
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
prefs.hardware['audioLib'] = ['pyo']
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
import pandas as pd
import random
import os  # handy system and path functions
import sys  # to get file system encoding
from psychopy.hardware import keyboard
import psychtoolbox as ptb # for GetSecs

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'even_spread_sequence'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

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

# Create our list of sound file names and shuffle them
sequence = ['TB20hz5min.wav', 'TB30hz5min.wav', 'TB40hz5min.wav', 'TB50hz5min.wav', 'TB80hz5min.wav']
random.shuffle(sequence)

for file in sequence:
    sound_file_name = 'ASSR_Sound/' + file
    counter = 0
    sound_1 = sound.Sound(sound_file_name, stereo=True, hamming=False)
    sound_1.setVolume(1.0)
    
    display_text = 'Sound File: ' + file
    test_A = visual.TextStim(win=win,
                             text=display_text,
                             pos=(0, 0), height=0.1, 
                             color='black')
    test_A.draw()
    win.flip()
    wait_time = sound_1.getDuration()
    
    now = ptb.GetSecs()
    sound_1.play(when=now)
    
    core.wait(wait_time) # Allows the sound to play, then waits 2 seconds before looping
    core.wait(2)

print('All done!')
    
# Save the sequence that was played in a CSV file
df = pd.DataFrame(data = {'Sequence Order': sequence})
df.to_csv(filename + '.csv')

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
logging.flush()
# make sure everything is closed down
win.close()
core.quit()