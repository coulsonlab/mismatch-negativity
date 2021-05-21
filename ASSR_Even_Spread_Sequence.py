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

# Create a timer
timer = core.Clock()

# Create our list of sound file names and shuffle them
sequence = ['TB20hz5min.wav', 'TB30hz5min.wav', 'TB40hz5min.wav', 'TB50hz5min.wav', 'TB80hz5min.wav']
random.shuffle(sequence)
sequence_order = []
sequence_timings = []

test_info = ('The sounds will play in the following sequence: \n\n' + 
sequence[0][0:6] + ', ' + sequence[1][0:6] + ', ' + sequence[2][0:6] + ', ' + 
sequence[3][0:6] + ', ' + sequence[4][0:6] + '\n\n Press any key to begin.')

instruct = visual.TextStim(win, text = test_info, height = 0.06)
instruct.draw()
win.flip()
key_press = False
while not key_press:
    key_press = event.waitKeys()
win.flip()

for file in sequence:
    # Load the sound and set the volume
    sound_1 = sound.Sound('ASSR_Sound/' + file, stereo=True, hamming=False)
    sound_1.setVolume(1.0)
    
    # Tell the experimenter what sound is playing
    display_text = 'Sound File: ' + file + '\n\n Press any key to quit.'
    test_A = visual.TextStim(win=win,
                             text=display_text,
                             pos=(0, 0), height=0.1, 
                             color='black')
    test_A.draw()
    win.flip()
    
    # Wait 1 second before starting so no keys are accidentally pressed
    core.wait(1)
    
    wait_time = sound_1.getDuration() # Get the duration time
    now = ptb.GetSecs() # Get the onset time
    sound_1.play(when=now) # Play immediately
    sequence_timings.append(now) # Record the onset time
    sequence_order.append(file[:6]) # Record the order of sounds
    
    # Wait until the sound is done or 'Esc' is pressed
    key_press = False
    end_exp = False
    while not key_press:
        key_press = event.waitKeys(maxWait = (wait_time))
        if key_press:
            sound_1.stop()
            df = pd.DataFrame(data = {'Sequence Order': sequence_order, 'Sequence Timing': sequence_timings})
            df.to_csv(filename + '.csv')
            win.close()
            core.quit()
            
    # 2 second pause between trials
    core.wait(2)

print('All done!')
    
# Save the sequence that was played in a CSV file
df = pd.DataFrame(data = {'Sequence Order': sequence_order, 'Sequence Timing': sequence_timings})
df.to_csv(filename + '.csv')

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# make sure everything is closed down
win.close()
core.quit()