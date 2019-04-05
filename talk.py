from transitions import Machine

from chatterbot import ChatBot

import argparse

import sys

from time import sleep

import pyperclip as cp

import webbrowser

import subprocess

import os

from selenium import webdriver
# Global driver 
DRIVER = None

from dictionary import *
d = dictionary()

from ScrapProfesssor import *

from ScrapGroups import *

from ScrapSchedule import *

# Last sentence
LAST_SENTENCE = 'First input'

# First input is not heard
FIRTS = True

import platform
if platform.system() == 'windows':
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
else:
    startupinfo = None

def refresh(slide):
    p = subprocess.Popen(['hovercraft', os.path.join('slides', slide), 'build'],
                         startupinfo=startupinfo)
    sleep(1)
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, 'build/index.html')
    if DRIVER is not None:
        DRIVER.get("file://" + filename)
        DRIVER.refresh()

class FiniteStateMachine:

    refresh('professor.rst')
    
    states = ['listen', 'yes', 'foi_generally', 'which_classroom', 'classroom', 'which_professor',
              'professor', 'which_kind_of_study', 'which_year_of_study', 'which_group', 'schedule']

    def __init__(self):

        # Initialize the state machine
        self.machine = Machine(model=self, states=FiniteStateMachine.states,
                               initial='listen')
        
        # Add transitions (trigger, source_state, destination_state)
        self.machine.add_transition('barice_input', 'listen', 'yes')
        
        self.machine.add_transition('foi_input', 'yes', 'foi_generally',
                                    after='foi_generally_output')
        
        self.machine.add_transition('classroom_input', 'yes', 'which_classroom')
        self.machine.add_transition('classroomN_input', 'which_classroom', 'classroom',
                                    after='classroom_output')
        
        self.machine.add_transition('professor_input', 'yes', 'which_professor')
        self.machine.add_transition('professorN_input', 'which_professor', 'professor',
                                    after='professor_output')
        
        self.machine.add_transition('schedule_input', 'yes', 'which_kind_of_study',
                                    after='kind_of_study_output')
        self.machine.add_transition('kind_of_study_input', 'which_kind_of_study',
                                    'which_year_of_study', after='year_of_study_output')
        self.machine.add_transition('year_of_study_input', 'which_year_of_study',
                                    'which_group', after='groupN_output')
        self.machine.add_transition('groupN_input', 'which_group', 'schedule',
                                    after='schedule_output')

        self.machine.add_transition('listen_input', '*', 'listen')

    def foi_generally_output(self):
        refresh('foi_generally.rst')
        print(d['FOI'][self.CMD])
        self.listen_input()

    def classroom_output(self):
        self.listen_input()

    def professor_output(self):
        p = subprocess.Popen(['hovercraft', os.path.join('slides', 'professor.rst'), 'build'],
                         startupinfo=startupinfo)
        sleep(1)
        scrapProfessors(self.professor)
        dirname = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(dirname, 'build/index.html')
        DRIVER.get(filename)
        DRIVER.refresh()
        print(d['Profesori'][self.CMD])
        self.listen_input()

    def kind_of_study_output(self):
        refresh('kind_of_study.rst')
        print(d['Raspored'][self.CMD])

    def year_of_study_output(self):
        refresh('year_of_study.rst')
        print(d['Vrsta_studija'][self.CMD])

    def groupN_output(self):
        there_is_schedule = scrapGroups(str(self.kind_of_study), str(self.year_of_study))
        if there_is_schedule:
            refresh('groupN.rst')
            print(d['Godina_studija'][self.CMD])
        else:
            refresh('no_schedule.rst')
            print('Raspored nedostupan')
            self.listen_input()

    def schedule_output(self):
        scrapSchedule(str(self.kind_of_study), str(self.year_of_study), str(self.group))
        refresh('schedule.rst')
        print(d['Grupa'][self.CMD])
        self.listen_input()
    
def main_branch(SENTENCE):
    CMD = chatbot.get_response( SENTENCE )
    m.CMD = CMD
    if CMD in d['Izvoli']:
        m.barice_input()
        print(d['Izvoli'][CMD])
    elif CMD in d['FOI']:
        m.foi_input()
    elif CMD in d['Dvorana']:
        m.classroom_input()
        print(d['Dvorana'][CMD])
    elif CMD in d['Profesor']:
        m.professor_input()
        print(d['Profesor'][CMD])
    elif CMD in d['Raspored']:
        m.schedule_input()       
    else: print(CMD)

def classroom_branch(SENTENCE):
    CMD = chatbotClassroom.get_response( SENTENCE )
    if CMD in d['Dvorane']:
        m.classroomN_input()
        print(d['Dvorane'][CMD])
    else: print(CMD)
    
def professor_branch(SENTENCE):
    CMD = chatbotProfessor.get_response( SENTENCE )
    m.CMD = CMD
    if CMD in d['Profesori']:
        m.professor = CMD
        m.professorN_input()
    else: print(CMD)

def schedule_branch(SENTENCE):
    CMD = chatbotSchedule.get_response( SENTENCE )
    m.CMD = CMD
    if CMD in d['Vrsta_studija']:
        m.kind_of_study = CMD
        m.kind_of_study_input()
    elif CMD in d['Godina_studija']:
        m.year_of_study = CMD
        m.year_of_study_input()
    elif CMD in d['Grupa']:
        m.group = CMD
        m.groupN_input()
    else: print(CMD)

def processing_input():
    global LAST_SENTENCE
    SENTENCE = LAST_SENTENCE
    
    if SENTENCE == 'exit':
        DRIVER.close()
        sys.exit()
        
    if m.state == 'listen' or  m.state == 'yes': main_branch(SENTENCE)
        
    elif m.state == 'which_classroom': classroom_branch(SENTENCE)

    elif m.state == 'which_professor': professor_branch(SENTENCE)                          

    elif m.state == 'which_kind_of_study' or m.state == 'which_year_of_study' or m.state == 'which_group':
        schedule_branch(SENTENCE)

def listen():
    global LAST_SENTENCE
    sleep( 0.5 )
    l = cp.paste().lower()
    if l != LAST_SENTENCE:
            x = LAST_SENTENCE
            LAST_SENTENCE = l            
            if x is not 'First input':
                print( 'Heard:', l )
                processing_input()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( "--train", const=True, nargs='?', type=bool, help="Specify if the agent shoud be trained. If not specified agent will be started in default (listening) mode.")
    args = parser.parse_args()

    TRAIN = bool( args.train )

    la = [
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'Ponovi unos molim.'
        }
    ]

    chatbot = ChatBot(
        'BARICA_HR',
        read_only=not TRAIN,
        logic_adapters=la,
        database='db.sqlite3' )
    chatbotClassroom = ChatBot(
        'BARICA_HR_CLASSROOM',
        read_only=not TRAIN,
        logic_adapters=la,
        database='dbC.sqlite3')
    chatbotProfessor = ChatBot(
        'BARICA_HR_PROFESSOR',
        read_only=not TRAIN,
        logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.75,
            'default_response': 'Ponovi unos molim.'
        }
    ],
        database='dbP.sqlite3' )
    chatbotSchedule= ChatBot(
        'BARICA_HR_SCHEDULE',
        read_only=not TRAIN,
        logic_adapters=la,
        database='dbS.sqlite3' )

    if TRAIN:
            from train import *
            from trainClassroom import *
            from trainProfessor import *
            from trainSchedule import *
            train( chatbot )
            trainClassroom( chatbotClassroom )
            trainProfessor( chatbotProfessor )
            trainSchedule ( chatbotSchedule ) 
            sys.exit()
    
    m = FiniteStateMachine()

    # Change to execute in the another browser
    DRIVER = webdriver.Chrome()
    refresh('listen.rst')
    
    while True:
        
        '''try:'''        
        listen()
        '''except Exception:
            pass
            print('Ponovi unos')'''
