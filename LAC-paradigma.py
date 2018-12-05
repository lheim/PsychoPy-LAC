#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on Wed Dec  5 11:29:44 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.0b11'
expName = 'LAC-paradigma'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
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
    originPath='/Users/nope/ownCloud/work/uka/code/psychoPy/psychopy-LAC/LAC-paradigma.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text="Liebe(r) Proband(in),\n\nvielen Dank, dass Sie sich bereit erklärt haben, an dieser Studie teilzunehmen.\n\nAuf der nachfolgenden Seiten, möchten wir Sie zunächst über den Ablauf des Experiments informieren.\n\nDrücken Sie hierfür bitte die 'Leertaste'.",
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text="Die Studie gliedert sich in folgende Teile:\n\n1) Messung Ihrer physiologischen Daten im Ruhezustand. (~ 5 min)\n\n2) Messung Ihrer physiologischen Daten während der Wechselnden Darbietung von Gerüchen. (~ 60 min)\n\n    2.1) Darbietung des Geruches.\n\n    2.2) Bewertung des dargebotenen Geruches.\n\n3) Ende\n\nWeiter mit der 'Leertaste'.",
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "baseline_instruction"
baseline_instructionClock = core.Clock()
baseline_instruc_text = visual.TextStim(win=win, name='baseline_instruc_text',
    text="Wir starten nun mit der Messung Ihrer Physiologischen Daten im Ruhezustand.\n\nBitte betrachten Sie während der Aufzeichnung das Kreuz, welches auf dem Bildschirm erscheint und versuchen Sie sich dabei so wenig wie möglich zu bewegen und nicht zu reden.\n\nBitte nehmen Sie nun die Schläuche wieder in die Nase und achten sie darauf, nur durch die Nase zu atmen.\n\n\nWeiter mit der 'Leertaste'.",
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
cross_1 = visual.TextStim(win=win, name='cross_1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.8, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=0.5, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "beginning"
beginningClock = core.Clock()
beginning_text = visual.TextStim(win=win, name='beginning_text',
    text="Es startet nun der zweite Teil der Studie.\n\nHierbei werden Ihnen verschiedene Gerüche während der Aufzeichnung Ihrer physiologischen Daten präsentiert.\n\nBitte versuchen Sie auch hier, sich so wenig wie möglich zu bewegen und nicht zu reden.\n\n\nWeiter mit der 'Leertaste'.",
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "example_scale"
example_scaleClock = core.Clock()
example_scale_text = visual.TextStim(win=win, name='example_scale_text',
    text="Hier sehen Sie eine beispielhafte Bewertungsskala.\n\nMit den Pfeiltasten können Sie einen Wert auswählen.\nMit der Leertaste bestätigen Sie diesen.\n\nProbieren Sie dies hier aus und fahren dann mit der 'Leertaste' fort.",
    font='Arial',
    pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
example_rating = visual.RatingScale(win=win, name='example_rating', 
marker='triangle', 
size=1.0, 
pos=[0.0, -0.4], 
low=1, high=9, 
labels=['gar nicht', ' sehr stark'], 
scale='Eigenschaft', 
markerStart='5', 
acceptKeys='space')

# Initialize components for Routine "starting_trial"
starting_trialClock = core.Clock()
starting_text = visual.TextStim(win=win, name='starting_text',
    text="Sie können das Experiment nun mit der 'Leertaste' starten.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "respiration_trigger"
respiration_triggerClock = core.Clock()

cross_2 = visual.TextStim(win=win, name='cross_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
respiration_text = visual.TextStim(win=win, name='respiration_text',
    text='Waiting for Inhale.',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
cross_3 = visual.TextStim(win=win, name='cross_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_odor_DEBUG = visual.TextStim(win=win, name='text_odor_DEBUG',
    text='default text',
    font='Arial',
    pos=(0, -0.5), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "stimuli_code"
stimuli_codeClock = core.Clock()
import serial
import time
from datetime import datetime

expClock = core.Clock()

try:
    olf = serial.Serial('COM5', 19200) # when testing WITH OLF
    print("Found COM Port, using it.")
except serial.SerialException:
    print("Couldnt find COM port. Using port = None")
    olf = None # when testing withOUT OLF

# Initialize components for Routine "intensity"
intensityClock = core.Clock()
intensity_rating = visual.RatingScale(win=win, name='intensity_rating', 
marker='triangle', 
size=1.0, 
pos=[0.0, -0.4], 
low=1, high=9, 
labels=['nicht warnehmbar', ' sehr intensiv'], 
scale='Intensivität', 
markerStart='5', 
acceptKeys='space')
intensity_text = visual.TextStim(win=win, name='intensity_text',
    text='Wie intensiv haben Sie diesen Geruch empfunden?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "pleasantness"
pleasantnessClock = core.Clock()
pleasantness_rating = visual.RatingScale(win=win, name='pleasantness_rating', 
marker='triangle', 
size=1.0, 
pos=[0.0, -0.4], 
low=1, high=9, 
labels=['sehr unangenehm', ' sehr angenehm'], 
scale='Angenehmlichkeit', 
markerStart='5', 
acceptKeys='space')
pleasantness_text = visual.TextStim(win=win, name='pleasantness_text',
    text='Wie angenehm haben Sie diesen Geruch empfunden?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "familarity"
familarityClock = core.Clock()
familarity_rating = visual.RatingScale(win=win, name='familarity_rating', 
marker='triangle', 
size=1.0, 
pos=[0.0, -0.4], 
low=1, high=9, 
labels=['überhaupt nicht vertraut', ' sehr vertraut'], 
scale='Bekanntheit', 
markerStart='5', 
acceptKeys='space')
familarity_text = visual.TextStim(win=win, name='familarity_text',
    text='Wie vertraut ist Ihnen dieser Geruch?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "arousel"
arouselClock = core.Clock()
arousel_rating = visual.RatingScale(win=win, name='arousel_rating', 
marker='triangle', 
size=1.0, 
pos=[0.0, -0.4], 
low=1, high=9, 
labels=['sehr entspannend', 'sehr aktivierend'], 
scale='Aktivierung', 
markerStart='5', 
acceptKeys='space')
arousel_text = visual.TextStim(win=win, name='arousel_text',
    text='Wie entspannend bzw. aktivierend ist dieser Duftstoff?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "interstimulus"
interstimulusClock = core.Clock()
text_interstimulus = visual.TextStim(win=win, name='text_interstimulus',
    text='Waiting for the next odor ...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

text_remaining_time = visual.TextStim(win=win, name='text_remaining_time',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "name_of_odor"
name_of_odorClock = core.Clock()
text_name_of_odor = visual.TextStim(win=win, name='text_name_of_odor',
    text='Können Sie die Ihnen vorgestellten Gerüche bennennen?',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_name_of_odor = visual.RatingScale(win=win, name='rating_name_of_odor', 
marker='triangle', 
size=1.0, 
pos=[0.0, -0.4], 
low=0, high=1, 
labels=['nein', 'ja'],  
markerStart='1', 
acceptKeys='space')

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text="Das war's!\n\nVielen Dank für Ihre Teilnahme.\n\nBeenden mit der 'Leertaste'.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
t = 0
welcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_welcome = event.BuilderKeyResponse()
# keep track of which components have finished
welcomeComponents = [welcome_text, key_welcome]
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if t >= 0.0 and welcome_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_text.tStart = t
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.setAutoDraw(True)
    
    # *key_welcome* updates
    if t >= 0.0 and key_welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_welcome.tStart = t
        key_welcome.frameNStart = frameN  # exact frame index
        key_welcome.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_welcome.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_welcome.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_welcome.keys = theseKeys[-1]  # just the last key pressed
            key_welcome.rt = key_welcome.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_welcome.keys in ['', [], None]:  # No response was made
    key_welcome.keys=None
thisExp.addData('key_welcome.keys',key_welcome.keys)
if key_welcome.keys != None:  # we had a response
    thisExp.addData('key_welcome.rt', key_welcome.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_instructions = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instructions_text, key_instructions]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_text.tStart = t
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.setAutoDraw(True)
    
    # *key_instructions* updates
    if t >= 0.0 and key_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_instructions.tStart = t
        key_instructions.frameNStart = frameN  # exact frame index
        key_instructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_instructions.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_instructions.keys = theseKeys[-1]  # just the last key pressed
            key_instructions.rt = key_instructions.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_instructions.keys in ['', [], None]:  # No response was made
    key_instructions.keys=None
thisExp.addData('key_instructions.keys',key_instructions.keys)
if key_instructions.keys != None:  # we had a response
    thisExp.addData('key_instructions.rt', key_instructions.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "baseline_instruction"-------
t = 0
baseline_instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_baseline_instruction = event.BuilderKeyResponse()
# keep track of which components have finished
baseline_instructionComponents = [baseline_instruc_text, key_baseline_instruction]
for thisComponent in baseline_instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "baseline_instruction"-------
while continueRoutine:
    # get current time
    t = baseline_instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *baseline_instruc_text* updates
    if t >= 0.0 and baseline_instruc_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        baseline_instruc_text.tStart = t
        baseline_instruc_text.frameNStart = frameN  # exact frame index
        baseline_instruc_text.setAutoDraw(True)
    
    # *key_baseline_instruction* updates
    if t >= 0.0 and key_baseline_instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_baseline_instruction.tStart = t
        key_baseline_instruction.frameNStart = frameN  # exact frame index
        key_baseline_instruction.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_baseline_instruction.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_baseline_instruction.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_baseline_instruction.keys = theseKeys[-1]  # just the last key pressed
            key_baseline_instruction.rt = key_baseline_instruction.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baseline_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "baseline_instruction"-------
for thisComponent in baseline_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_baseline_instruction.keys in ['', [], None]:  # No response was made
    key_baseline_instruction.keys=None
thisExp.addData('key_baseline_instruction.keys',key_baseline_instruction.keys)
if key_baseline_instruction.keys != None:  # we had a response
    thisExp.addData('key_baseline_instruction.rt', key_baseline_instruction.rt)
thisExp.nextEntry()
# the Routine "baseline_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "baseline"-------
t = 0
baselineClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_baseline = event.BuilderKeyResponse()
# keep track of which components have finished
baselineComponents = [key_baseline, cross_1]
for thisComponent in baselineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "baseline"-------
while continueRoutine:
    # get current time
    t = baselineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_baseline* updates
    if t >= 0.0 and key_baseline.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_baseline.tStart = t
        key_baseline.frameNStart = frameN  # exact frame index
        key_baseline.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_baseline.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_baseline.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_baseline.keys = theseKeys[-1]  # just the last key pressed
            key_baseline.rt = key_baseline.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *cross_1* updates
    if t >= 0 and cross_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        cross_1.tStart = t
        cross_1.frameNStart = frameN  # exact frame index
        cross_1.setAutoDraw(True)
    frameRemains = 0 + 365- win.monitorFramePeriod * 0.75  # most of one frame period left
    if cross_1.status == STARTED and t >= frameRemains:
        cross_1.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "baseline"-------
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_baseline.keys in ['', [], None]:  # No response was made
    key_baseline.keys=None
thisExp.addData('key_baseline.keys',key_baseline.keys)
if key_baseline.keys != None:  # we had a response
    thisExp.addData('key_baseline.rt', key_baseline.rt)
thisExp.nextEntry()
# the Routine "baseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "beginning"-------
t = 0
beginningClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_beginning = event.BuilderKeyResponse()
# keep track of which components have finished
beginningComponents = [beginning_text, key_beginning]
for thisComponent in beginningComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "beginning"-------
while continueRoutine:
    # get current time
    t = beginningClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *beginning_text* updates
    if t >= 0.0 and beginning_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        beginning_text.tStart = t
        beginning_text.frameNStart = frameN  # exact frame index
        beginning_text.setAutoDraw(True)
    
    # *key_beginning* updates
    if t >= 0.0 and key_beginning.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_beginning.tStart = t
        key_beginning.frameNStart = frameN  # exact frame index
        key_beginning.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_beginning.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_beginning.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_beginning.keys = theseKeys[-1]  # just the last key pressed
            key_beginning.rt = key_beginning.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginning"-------
for thisComponent in beginningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_beginning.keys in ['', [], None]:  # No response was made
    key_beginning.keys=None
thisExp.addData('key_beginning.keys',key_beginning.keys)
if key_beginning.keys != None:  # we had a response
    thisExp.addData('key_beginning.rt', key_beginning.rt)
thisExp.nextEntry()
# the Routine "beginning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "example_scale"-------
t = 0
example_scaleClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
example_rating.reset()
# keep track of which components have finished
example_scaleComponents = [example_scale_text, example_rating]
for thisComponent in example_scaleComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "example_scale"-------
while continueRoutine:
    # get current time
    t = example_scaleClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *example_scale_text* updates
    if t >= 0.0 and example_scale_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        example_scale_text.tStart = t
        example_scale_text.frameNStart = frameN  # exact frame index
        example_scale_text.setAutoDraw(True)
    # *example_rating* updates
    if t >= 0.0 and example_rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        example_rating.tStart = t
        example_rating.frameNStart = frameN  # exact frame index
        example_rating.setAutoDraw(True)
    continueRoutine &= example_rating.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "example_scale"-------
for thisComponent in example_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('example_rating.response', example_rating.getRating())
thisExp.addData('example_rating.rt', example_rating.getRT())
thisExp.nextEntry()
# the Routine "example_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "starting_trial"-------
t = 0
starting_trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_starting = event.BuilderKeyResponse()
# keep track of which components have finished
starting_trialComponents = [starting_text, key_starting]
for thisComponent in starting_trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "starting_trial"-------
while continueRoutine:
    # get current time
    t = starting_trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *starting_text* updates
    if t >= 0.0 and starting_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        starting_text.tStart = t
        starting_text.frameNStart = frameN  # exact frame index
        starting_text.setAutoDraw(True)
    
    # *key_starting* updates
    if t >= 0.0 and key_starting.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_starting.tStart = t
        key_starting.frameNStart = frameN  # exact frame index
        key_starting.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_starting.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_starting.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_starting.keys = theseKeys[-1]  # just the last key pressed
            key_starting.rt = key_starting.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in starting_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "starting_trial"-------
for thisComponent in starting_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_starting.keys in ['', [], None]:  # No response was made
    key_starting.keys=None
thisExp.addData('key_starting.keys',key_starting.keys)
if key_starting.keys != None:  # we had a response
    thisExp.addData('key_starting.rt', key_starting.rt)
thisExp.nextEntry()
# the Routine "starting_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('odors.csv'),
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
    
    # ------Prepare to start Routine "respiration_trigger"-------
    t = 0
    respiration_triggerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # calculate moving average
    key_respiration = event.BuilderKeyResponse()
    # keep track of which components have finished
    respiration_triggerComponents = [cross_2, key_respiration, respiration_text]
    for thisComponent in respiration_triggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "respiration_trigger"-------
    while continueRoutine:
        # get current time
        t = respiration_triggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *cross_2* updates
        if t >= 0.0 and cross_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross_2.tStart = t
            cross_2.frameNStart = frameN  # exact frame index
            cross_2.setAutoDraw(True)
        
        # *key_respiration* updates
        if t >= 0.0 and key_respiration.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_respiration.tStart = t
            key_respiration.frameNStart = frameN  # exact frame index
            key_respiration.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_respiration.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_respiration.status == STARTED:
            theseKeys = event.getKeys(keyList=['i', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_respiration.keys = theseKeys[-1]  # just the last key pressed
                key_respiration.rt = key_respiration.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *respiration_text* updates
        if t >= 0.0 and respiration_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            respiration_text.tStart = t
            respiration_text.frameNStart = frameN  # exact frame index
            respiration_text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respiration_triggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "respiration_trigger"-------
    for thisComponent in respiration_triggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_respiration.keys in ['', [], None]:  # No response was made
        key_respiration.keys=None
    trials.addData('key_respiration.keys',key_respiration.keys)
    if key_respiration.keys != None:  # we had a response
        trials.addData('key_respiration.rt', key_respiration.rt)
    # the Routine "respiration_trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimuli"-------
    t = 0
    stimuliClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.100000)
    # update component parameters for each repeat
    text_odor_DEBUG.setText(f"{odor} on {channel}")
    # keep track of which components have finished
    stimuliComponents = [cross_3, text_odor_DEBUG]
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimuliClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_3* updates
        if t >= 0.0 and cross_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross_3.tStart = t
            cross_3.frameNStart = frameN  # exact frame index
            cross_3.setAutoDraw(True)
        frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross_3.status == STARTED and t >= frameRemains:
            cross_3.setAutoDraw(False)
        
        # *text_odor_DEBUG* updates
        if t >= 0.0 and text_odor_DEBUG.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_odor_DEBUG.tStart = t
            text_odor_DEBUG.frameNStart = frameN  # exact frame index
            text_odor_DEBUG.setAutoDraw(True)
        frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_odor_DEBUG.status == STARTED and t >= frameRemains:
            text_odor_DEBUG.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stimuli_code"-------
    t = 0
    stimuli_codeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    trials.addData('stimuli_unixtime', '%.3f' %time.time())
    logging.log(level=logging.EXP, msg= 'stimuli_unixtime: ' + '%.3f' %time.time())
    
    trials.addData('stimuli_time', datetime.now().strftime("%H:%M:%S.%f"))
    logging.log(level=logging.EXP, msg= 'stimuli_time: ' + datetime.now().strftime("%H:%M:%S.%f"))
    
    start_time = expClock.getTime()
    trials.addData('stimuli_clock', start_time)
    logging.log(level=logging.EXP, msg= 'stimuli_clock: %.2f' %start_time)
    
    if olf:
        olf.write(b"\nF%d\r" %channel)
        time.sleep(3)
        olf.write(b"\nF%d\r" %channel)
    else:
        time.sleep(3)
    
    time.sleep(5)
    continueRoutine = False
    # keep track of which components have finished
    stimuli_codeComponents = []
    for thisComponent in stimuli_codeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimuli_code"-------
    while continueRoutine:
        # get current time
        t = stimuli_codeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuli_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli_code"-------
    for thisComponent in stimuli_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "stimuli_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "intensity"-------
    t = 0
    intensityClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    intensity_rating.reset()
    # keep track of which components have finished
    intensityComponents = [intensity_rating, intensity_text]
    for thisComponent in intensityComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "intensity"-------
    while continueRoutine:
        # get current time
        t = intensityClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *intensity_rating* updates
        if t >= 0.0 and intensity_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            intensity_rating.tStart = t
            intensity_rating.frameNStart = frameN  # exact frame index
            intensity_rating.setAutoDraw(True)
        continueRoutine &= intensity_rating.noResponse  # a response ends the trial
        
        # *intensity_text* updates
        if t >= 0.0 and intensity_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            intensity_text.tStart = t
            intensity_text.frameNStart = frameN  # exact frame index
            intensity_text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intensityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intensity"-------
    for thisComponent in intensityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('intensity_rating.response', intensity_rating.getRating())
    trials.addData('intensity_rating.rt', intensity_rating.getRT())
    # the Routine "intensity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pleasantness"-------
    t = 0
    pleasantnessClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    pleasantness_rating.reset()
    # keep track of which components have finished
    pleasantnessComponents = [pleasantness_rating, pleasantness_text]
    for thisComponent in pleasantnessComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pleasantness"-------
    while continueRoutine:
        # get current time
        t = pleasantnessClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *pleasantness_rating* updates
        if t >= 0.0 and pleasantness_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            pleasantness_rating.tStart = t
            pleasantness_rating.frameNStart = frameN  # exact frame index
            pleasantness_rating.setAutoDraw(True)
        continueRoutine &= pleasantness_rating.noResponse  # a response ends the trial
        
        # *pleasantness_text* updates
        if t >= 0.0 and pleasantness_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            pleasantness_text.tStart = t
            pleasantness_text.frameNStart = frameN  # exact frame index
            pleasantness_text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pleasantnessComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pleasantness"-------
    for thisComponent in pleasantnessComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('pleasantness_rating.response', pleasantness_rating.getRating())
    trials.addData('pleasantness_rating.rt', pleasantness_rating.getRT())
    # the Routine "pleasantness" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "familarity"-------
    t = 0
    familarityClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    familarity_rating.reset()
    # keep track of which components have finished
    familarityComponents = [familarity_rating, familarity_text]
    for thisComponent in familarityComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "familarity"-------
    while continueRoutine:
        # get current time
        t = familarityClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *familarity_rating* updates
        if t >= 0.0 and familarity_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            familarity_rating.tStart = t
            familarity_rating.frameNStart = frameN  # exact frame index
            familarity_rating.setAutoDraw(True)
        continueRoutine &= familarity_rating.noResponse  # a response ends the trial
        
        # *familarity_text* updates
        if t >= 0.0 and familarity_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            familarity_text.tStart = t
            familarity_text.frameNStart = frameN  # exact frame index
            familarity_text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in familarityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "familarity"-------
    for thisComponent in familarityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('familarity_rating.response', familarity_rating.getRating())
    trials.addData('familarity_rating.rt', familarity_rating.getRT())
    # the Routine "familarity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "arousel"-------
    t = 0
    arouselClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    arousel_rating.reset()
    # keep track of which components have finished
    arouselComponents = [arousel_rating, arousel_text]
    for thisComponent in arouselComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "arousel"-------
    while continueRoutine:
        # get current time
        t = arouselClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *arousel_rating* updates
        if t >= 0.0 and arousel_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            arousel_rating.tStart = t
            arousel_rating.frameNStart = frameN  # exact frame index
            arousel_rating.setAutoDraw(True)
        continueRoutine &= arousel_rating.noResponse  # a response ends the trial
        
        # *arousel_text* updates
        if t >= 0.0 and arousel_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            arousel_text.tStart = t
            arousel_text.frameNStart = frameN  # exact frame index
            arousel_text.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in arouselComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "arousel"-------
    for thisComponent in arouselComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('arousel_rating.response', arousel_rating.getRating())
    trials.addData('arousel_rating.rt', arousel_rating.getRT())
    # the Routine "arousel" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "interstimulus"-------
    t = 0
    interstimulusClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    end_time = expClock.getTime()
    
    trial_time = end_time - start_time
    trials.addData('trial_duration', trial_time)
    logging.log(level=logging.EXP, msg= 'trial_duration: %.2f' %trial_time)
    
    print(f"This trial took {trial_time} seconds.")
    
    key_interstimulus = event.BuilderKeyResponse()
    # keep track of which components have finished
    interstimulusComponents = [text_interstimulus, key_interstimulus, text_remaining_time]
    for thisComponent in interstimulusComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "interstimulus"-------
    while continueRoutine:
        # get current time
        t = interstimulusClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_interstimulus* updates
        if t >= 0.0 and text_interstimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_interstimulus.tStart = t
            text_interstimulus.frameNStart = frameN  # exact frame index
            text_interstimulus.setAutoDraw(True)
        interval = 60
        
        end_time = expClock.getTime()
        trial_time = end_time - start_time
        
        remaining_time = interval - trial_time
        remaining_time = '%.1f' %remaining_time
        
        if trial_time > interval:
            print("Continuing")
            continueRoutine = False
        
        # *key_interstimulus* updates
        if t >= 0.0 and key_interstimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_interstimulus.tStart = t
            key_interstimulus.frameNStart = frameN  # exact frame index
            key_interstimulus.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_interstimulus.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_interstimulus.status == STARTED:
            theseKeys = event.getKeys(keyList=['n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_interstimulus.keys = theseKeys[-1]  # just the last key pressed
                key_interstimulus.rt = key_interstimulus.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_remaining_time* updates
        if t >= 0.0 and text_remaining_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_remaining_time.tStart = t
            text_remaining_time.frameNStart = frameN  # exact frame index
            text_remaining_time.setAutoDraw(True)
        if text_remaining_time.status == STARTED:  # only update if drawing
            text_remaining_time.setText(remaining_time, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in interstimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "interstimulus"-------
    for thisComponent in interstimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_interstimulus.keys in ['', [], None]:  # No response was made
        key_interstimulus.keys=None
    trials.addData('key_interstimulus.keys',key_interstimulus.keys)
    if key_interstimulus.keys != None:  # we had a response
        trials.addData('key_interstimulus.rt', key_interstimulus.rt)
    # the Routine "interstimulus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


# ------Prepare to start Routine "name_of_odor"-------
t = 0
name_of_odorClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_name_of_odor.reset()
# keep track of which components have finished
name_of_odorComponents = [text_name_of_odor, rating_name_of_odor]
for thisComponent in name_of_odorComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "name_of_odor"-------
while continueRoutine:
    # get current time
    t = name_of_odorClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_name_of_odor* updates
    if t >= 0.0 and text_name_of_odor.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_name_of_odor.tStart = t
        text_name_of_odor.frameNStart = frameN  # exact frame index
        text_name_of_odor.setAutoDraw(True)
    # *rating_name_of_odor* updates
    if t >= 0.0 and rating_name_of_odor.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_name_of_odor.tStart = t
        rating_name_of_odor.frameNStart = frameN  # exact frame index
        rating_name_of_odor.setAutoDraw(True)
    continueRoutine &= rating_name_of_odor.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in name_of_odorComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "name_of_odor"-------
for thisComponent in name_of_odorComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_name_of_odor.response', rating_name_of_odor.getRating())
thisExp.addData('rating_name_of_odor.rt', rating_name_of_odor.getRT())
thisExp.nextEntry()
# the Routine "name_of_odor" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_end = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [end_text, key_end]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    
    # *key_end* updates
    if t >= 0.0 and key_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_end.tStart = t
        key_end.frameNStart = frameN  # exact frame index
        key_end.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_end.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_end.keys = theseKeys[-1]  # just the last key pressed
            key_end.rt = key_end.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_end.keys in ['', [], None]:  # No response was made
    key_end.keys=None
thisExp.addData('key_end.keys',key_end.keys)
if key_end.keys != None:  # we had a response
    thisExp.addData('key_end.rt', key_end.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

if olf:
    olf.close()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
